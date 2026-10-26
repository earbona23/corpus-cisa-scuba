#!/usr/bin/env python3
"""Split the CISA SCuBA M365 Secure Configuration Baselines into one Markdown
file per policy, for the XERJ Corpus Hub. Reads the baseline .md files from
./src and writes ./policies/MS.<ID>.md. Pure stdlib; see README for regeneration."""
import os, re, sys, glob

SRC = sys.argv[1] if len(sys.argv) > 1 else "src"
OUT = sys.argv[2] if len(sys.argv) > 2 else "policies"
POLICY_RE = re.compile(r'^#### (MS\.[A-Z0-9]+\.\d+\.\d+v\d+)\s*$')
INSTR_RE  = re.compile(r'^####\s+(MS\.[A-Z0-9]+\.\d+\.\d+v\d+)\s+Instructions\s*$')
CRIT_RE   = re.compile(r'<!--\s*Policy:\s*MS\.[A-Z0-9]+\.\d+\.\d+v\d+;\s*Criticality:\s*([A-Z/ ]+?)\s*-->')
BADGE_RE  = re.compile(r'^\s*\[!\[.*\]\(https://img\.shields\.io/.*\)\]\(.*\)\s*$')

def product_of(text, fname):
    m = re.search(r'^# CISA M365 Secure Configuration Baseline for (.+)$', text, re.M)
    return m.group(1).strip() if m else os.path.splitext(os.path.basename(fname))[0]

def sections(lines, level):
    """Yield (heading, body_lines) for headings of exactly `level` (#*level)."""
    hdr = re.compile(r'^#{%d} (?!#)(.*)$' % level)
    cur, body, out = None, [], []
    for ln in lines:
        m = hdr.match(ln)
        if m:
            if cur is not None: out.append((cur, body))
            cur, body = m.group(1).strip(), []
        elif cur is not None:
            body.append(ln)
    if cur is not None: out.append((cur, body))
    return out

def split_by_h4(body):
    """Split a block into {h4_title: body_lines} by '#### ' headers."""
    out, cur, buf = {}, None, []
    for ln in body:
        m = re.match(r'^#### (.*)$', ln)
        if m:
            if cur is not None: out[cur] = buf
            cur, buf = m.group(1).strip(), []
        elif cur is not None:
            buf.append(ln)
    if cur is not None: out[cur] = buf
    return out

def clean(body):
    out = [ln for ln in body if not BADGE_RE.match(ln)]
    txt = "\n".join(out)
    txt = re.sub(r'<!--.*?-->', '', txt, flags=re.S)        # drop HTML comments
    txt = re.sub(r'\n{3,}', '\n\n', txt).strip()
    return txt

os.makedirs(OUT, exist_ok=True)
total, sizes = 0, []
for f in sorted(glob.glob(os.path.join(SRC, "*.md"))):
    text = open(f, encoding="utf-8").read()
    if "# Baseline Policies" not in text: continue
    product = product_of(text, f)
    base = os.path.splitext(os.path.basename(f))[0]
    bp = text.split("# Baseline Policies", 1)[1]
    for group, gbody in sections(bp.splitlines(), 2):           # ## N. Group
        sub = {h: b for h, b in sections(gbody, 3)}             # ### Policies / Resources / etc.
        policies = split_by_h4(sub.get("Policies", []))
        instr    = split_by_h4(sub.get("Implementation", []))
        resources = clean(sub.get("Resources", []))
        licreq    = clean(sub.get("License Requirements", []))
        for ptitle, pbody in policies.items():
            pid = ptitle.split()[0]
            if not pid.startswith("MS."): continue
            raw = "\n".join(pbody)
            cm = CRIT_RE.search(raw)
            crit = cm.group(1).strip() if cm else "—"
            # statement = first non-empty, non-badge line
            stmt = ""
            for ln in pbody:
                s = ln.strip()
                if s and not BADGE_RE.match(ln): stmt = s; break
            ins = instr.get(pid + " Instructions") or instr.get(ptitle + " Instructions") or []
            ins_txt = clean(ins) if ins else "_See the baseline; no separate implementation steps._"
            doc = []
            doc.append(f"# {pid}: {stmt}")
            doc.append(f"Product: {product} · Baseline: {base} · Group: {group} · Criticality: {crit}")
            doc.append("\n## Policy\n" + clean(pbody))
            if resources: doc.append("\n## Resources\n" + resources)
            doc.append("\n## License Requirements\n" + (licreq or "- N/A"))
            doc.append("\n## Implementation\n" + ins_txt)
            out_md = "\n".join(doc).rstrip() + "\n"
            path = os.path.join(OUT, pid + ".md")
            open(path, "w", encoding="utf-8").write(out_md)
            total += 1; sizes.append((len(out_md.encode()), pid))

sizes.sort(reverse=True)
print(f"policies written: {total}")
print(f"largest: {sizes[0][1]}.md ({sizes[0][0]:,} bytes); 150 KB cap {'never hit' if sizes[0][0] < 150*1024 else 'HIT'}")
