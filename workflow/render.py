"""Create inspectable local reports from actual run data, never canned answers."""

from __future__ import annotations

import html
from pathlib import Path


def _refs(sentence: dict) -> str:
    return ", ".join(sentence["finding_ids"] + sentence["criterion_ids"])


def render_reports(out_dir: Path, integration: dict, extractions: list,
                   references: list, flags: list) -> None:
    status = "REVIEW REQUIRED" if flags else "DRAFT — human review required"
    lines = ["# Integrated reporting: synthetic teaching draft", "",
             f"**{status}. Not for clinical use.**", "",
             f"Framework: {integration['framework']}",
             f"Classification assessment: {integration['classification_status']}", ""]
    for section in integration["sections"]:
        lines.extend([f"## {section['title']}", ""])
        for sentence in section["sentences"]:
            lines.extend([f"{sentence['text']} [{sentence['id']}; {_refs(sentence)}]", ""])
        if not section["sentences"]:
            lines.extend(["No supported statement generated for this section.", ""])
    lines.extend(["## Criteria and evidence", ""])
    for criterion in integration["criteria_assessment"]:
        lines.extend([f"### {criterion['id']}: {criterion['assessment']}", "",
                      criterion["criterion"], "", criterion["explanation"], "",
                      f"Case findings: {', '.join(criterion['finding_ids']) or 'None'}",
                      f"Guideline: {criterion['source_id']} / {criterion['passage_id']}",
                      "", f"> {criterion['quote']}", ""])
    lines.extend(["## Unresolved issues", ""])
    lines.extend([f"- {issue}" for issue in integration["unresolved_issues"]] or ["None reported by the model."])
    lines.extend(["", "## QA findings", ""])
    lines.extend([f"- {f['severity'].upper()}: {f['concern']} ({f['reference']})" for f in flags]
                 or ["No automated flags. This does not establish clinical correctness."])
    lines.extend(["", "## Guideline evidence used", ""])
    for ref in references:
        lines.extend([f"- {ref['title']}. {ref['edition']}. {ref['canonical_url']}",
                      f"  Source method: {ref.get('acquisition_method', 'unspecified')}; acquired: {ref['retrieved_at']}",
                      f"  Retrieved URL: {ref.get('retrieved_url') or 'Local original article import'}",
                      f"  Scope: {ref.get('scope', 'See reference snapshot')}",
                      f"  SHA-256: {ref['sha256']}"])
    (out_dir / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    esc = lambda value: html.escape(str(value), quote=True)
    body = [f'<p class="label">AC3 · SYNTHETIC TEACHING WORKFLOW</p><h1>Integrated report</h1>',
            f'<p class="status">{esc(status)} · Not for clinical use</p>',
            f'<p>{esc(integration["framework"])} · {esc(integration["classification_status"])}</p>',
            '<nav><a href="#report">Report</a><a href="#criteria">Criteria</a><a href="#findings">Source evidence</a><a href="#qa">QA</a><a href="#sources">Guidelines</a></nav>',
            '<section id="report">']
    for section in integration["sections"]:
        body.append(f'<h2>{esc(section["title"])}</h2>')
        for sentence in section["sentences"]:
            links = " ".join(f'<a href="#{esc(fid)}">{esc(fid)}</a>' for fid in sentence["finding_ids"] + sentence["criterion_ids"])
            body.append(f'<p id="{esc(sentence["id"])}">{esc(sentence["text"])}<span class="refs">{links}</span></p>')
        if not section["sentences"]:
            body.append('<p class="muted">No supported statement generated.</p>')
    body.append('</section><section id="criteria"><h2>Criteria and evidence</h2>')
    for criterion in integration["criteria_assessment"]:
        evidence = " ".join(f'<a href="#{esc(fid)}">{esc(fid)}</a>' for fid in criterion["finding_ids"])
        body.append(f'<article id="{esc(criterion["id"])}"><h3>{esc(criterion["id"])} · {esc(criterion["assessment"])}</h3>'
                    f'<p>{esc(criterion["criterion"])}</p><blockquote>{esc(criterion["quote"])}</blockquote>'
                    f'<p><a href="#{esc(criterion["source_id"])}--{esc(criterion["passage_id"])}">{esc(criterion["source_id"])} / {esc(criterion["passage_id"])}</a></p>'
                    f'<p>{esc(criterion["explanation"])}</p><p>Case evidence: {evidence or "None"}</p></article>')
    body.append('</section><section id="findings"><h2>Source evidence</h2>')
    for extraction in extractions:
        body.append(f'<details open><summary>{esc(extraction["source_id"])} · {esc(extraction["document_name"])}</summary>')
        for finding in extraction["findings"]:
            body.append(f'<article id="{esc(finding["id"])}"><h3>{esc(finding["id"])} · {esc(finding["field"])}</h3>'
                        f'<p><strong>{esc(finding["value"])}</strong> · {esc(finding["status"])}</p>'
                        f'<p>Units: {esc(finding["units"])} · Method: {esc(finding["method"])} · Denominator: {esc(finding["denominator"])}</p>'
                        f'<blockquote>{esc(finding["quote"])}</blockquote><p>Page: {esc(finding["page"])}</p></article>')
        body.append('</details>')
    body.append('</section><section id="qa"><h2>QA and unresolved issues</h2>')
    for issue in integration["unresolved_issues"]:
        body.append(f'<p class="status">{esc(issue)}</p>')
    for item in flags:
        body.append(f'<p><strong>{esc(item["severity"].upper())}</strong> {esc(item["concern"])} <span class="muted">{esc(item["reference"])}</span></p>')
    if not flags:
        body.append('<p>No automated flags. This does not establish clinical correctness.</p>')
    body.append('</section><section id="sources"><h2>Guideline evidence used</h2>')
    for ref in references:
        body.append(f'<article><h3>{esc(ref["title"])}</h3><p>{esc(ref["edition"])}</p>'
                    f'<p><a href="{esc(ref["canonical_url"])}" rel="noreferrer">Original source</a></p>'
                    f'<p>Source method: {esc(ref.get("acquisition_method", "unspecified"))} · Acquired: {esc(ref["retrieved_at"])}</p>'
                    f'<p class="hash">Retrieved URL: {esc(ref.get("retrieved_url") or "Local original article import")}</p>'
                    f'<p>{esc(ref.get("scope", "See reference snapshot"))}</p>'
                    f'<p class="hash">SHA-256 {esc(ref["sha256"])}</p>')
        for passage in ref["passages"]:
            body.append(f'<details id="{esc(ref["source_id"])}--{esc(passage["id"])}"><summary>{esc(passage["section"])} · {esc(passage["id"])}</summary>'
                        f'<blockquote>{esc(passage["text"])}</blockquote></details>')
        body.append('</article>')
    body.append('</section>')
    style = """body{font:17px/1.6 system-ui,sans-serif;color:#203346;background:#f5f7fa;margin:0}main{max-width:1050px;margin:auto;padding:36px 24px}h1{font-size:40px;line-height:1.15}h2{margin-top:34px}h3{font-size:17px}a{color:#075b99}nav{display:flex;gap:20px;flex-wrap:wrap;padding:20px 0}section{background:white;padding:8px 24px 24px;margin:22px 0;border:1px solid #dce4ed;border-radius:12px}article{border-top:1px solid #e3e8ef;padding:12px 0;scroll-margin-top:20px}blockquote{border-left:4px solid #4096ad;padding:8px 16px;margin:10px 0;background:#f0f7fa;white-space:pre-wrap}.label,.refs,.muted,.hash{font-size:13px;color:#526779}.label{letter-spacing:.1em}.refs{display:block;margin-top:6px}.refs a{margin-right:8px}.status{background:#fff3d9;border-left:4px solid #d09b2c;padding:12px 16px}.hash{overflow-wrap:anywhere}summary{cursor:pointer;font-weight:700;padding:14px 0}@media print{nav{display:none}body{background:white}main{padding:0}section{border:0;padding:0}article{break-inside:avoid}}"""
    output = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Source-grounded integrated reporting</title><style>' + style + '</style></head><body><main>' + "\n".join(body) + '</main></body></html>'
    (out_dir / "report.html").write_text(output, encoding="utf-8")
