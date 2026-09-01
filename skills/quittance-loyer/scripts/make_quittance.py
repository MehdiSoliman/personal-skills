#!/usr/bin/env python3
# Quittance de loyer — template générique (design maison)
import weasyprint

# ================= À PERSONNALISER =================
bailleur_nom = "VOTRE NOM"
bailleur_addr = "Votre adresse · code postal · ville"
bailleur_contact = "06 00 00 00 00 · vous@email.com"
logement = "Nom de la résidence\nAdresse du logement"
logement_detail = "Lot · étage · surface · parking (optionnel)"
locataire = "Nom du locataire\nAdresse du locataire"
gen_lieu = "Votre ville"

loyer = 0.00
charges = 0.00
aide_caf = 0.00
teom_annuel = 0.00
# ===================================================

gen_date = "JJ/MM/AAAA"
q_start, q_end = "01/MM/AAAA", "31/MM/AAAA"   # quittance
a_start, a_end = "01/MM/AAAA", "30/MM/AAAA"   # avis d'échéance

teom_ech = teom_annuel / 4                      # 1 échéance / 4

# Quittance : TEOM si la période en comporte une. Avis : 1re échéance (sept → déc).
teom_q = 0.0
teom_a = teom_ech

def eur(v):
    return f"{v:.2f}".replace(".", ",") + " €"

total_q = loyer + charges + teom_q
net_q   = total_q - aide_caf
total_a = loyer + charges + teom_a
net_a   = total_a - aide_caf

teom_row_q = f'<tr><td>Taxe ordures ménagères (TEOM)</td><td class="num">{eur(teom_q)}</td></tr>\n  ' if teom_q > 0 else ''
teom_row_a = f'<tr><td>Taxe ordures ménagères (TEOM) — échéance 1/4</td><td class="num">{eur(teom_a)}</td></tr>\n  ' if teom_a > 0 else ''

html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
@page {{ size: A4; margin: 17mm 19mm 16mm 19mm; }}
* {{ box-sizing: border-box; }}
body {{ font-family: 'DejaVu Sans', sans-serif; font-size: 10pt; color: #1c1c1c; line-height: 1.5; margin: 0; }}

table.head {{ width: 100%; border-collapse: collapse; }}
table.head td {{ vertical-align: top; padding: 0; }}
.bailleur .name {{ font-size: 9.5pt; font-weight: bold; color: #333; }}
.bailleur .meta {{ color: #888; font-size: 8pt; line-height: 1.5; margin-top: 2px; }}
.date {{ text-align: right; font-size: 10.5pt; color: #333; }}
.accent-rule {{ border: 0; border-top: 3px solid #e8822d; margin: 14px 0 0 0; }}

h2.sec {{ font-size: 14pt; font-weight: bold; margin: 20px 0 2px 0; color: #111; }}
.sec .tag {{ color: #e8822d; font-size: 8.5pt; font-weight: bold; letter-spacing: 1.2px; text-transform: uppercase; }}
.period {{ font-size: 10pt; color: #444; margin: 2px 0 14px 0; }}

table.info {{ width: 100%; border-collapse: collapse; margin: 4px 0 4px 0; }}
table.info td {{ width: 50%; vertical-align: top; padding: 12px 16px; background: #faf7f4; border: 1px solid #eee; }}
table.info td + td {{ border-left: 0; }}
.lbl {{ font-size: 8pt; font-weight: bold; letter-spacing: 1.2px; color: #e8822d; text-transform: uppercase; display: block; margin-bottom: 5px; }}
.info .val {{ line-height: 1.45; }}
.info .small {{ color: #888; font-size: 8.5pt; margin-top: 4px; }}

table.amounts {{ width: 100%; border-collapse: collapse; margin: 16px 0 8px 0; }}
table.amounts td {{ padding: 6px 4px; font-size: 10pt; }}
table.amounts td.num {{ text-align: right; white-space: nowrap; }}
table.amounts tr.border-top td {{ border-top: 1px solid #ddd; }}
table.amounts tr.total td {{ font-weight: bold; }}
table.amounts tr.aide td {{ color: #2e7d32; }}
table.amounts tr.net td {{ font-weight: bold; font-size: 11.5pt; background: #fdf0e4; padding: 9px 4px; }}
table.amounts tr.net td.num {{ color: #c05d12; }}

.legal {{ font-size: 7.6pt; color: #777; line-height: 1.4; margin: 8px 0 0 0; text-align: justify; }}
.dotted {{ border: 0; border-top: 1.5px dotted #bbb; margin: 16px 0 0 0; }}
.sign {{ text-align: right; margin-top: 16px; }}
.sign .who {{ font-weight: bold; }}
.sign .rule {{ border-top: 1px solid #333; width: 140px; margin-left: auto; margin-bottom: 6px; }}
.hl {{ font-weight: bold; }}
</style></head><body>

<table class="head">
  <tr>
    <td class="bailleur">
      <div class="name">{bailleur_nom}</div>
      <div class="meta">{bailleur_addr}<br>{bailleur_contact}</div>
    </td>
    <td class="date">{gen_lieu},<br>le {gen_date}</td>
  </tr>
</table>
<hr class="accent-rule">

<h2 class="sec"><span class="tag">Quittance</span><br>Quittance de loyer</h2>
<div class="period">Période du {q_start} au {q_end}</div>

<table class="info">
  <tr>
    <td>
      <span class="lbl">Logement</span>
      <div class="val">{logement}</div>
      <div class="small">{logement_detail}</div>
    </td>
    <td>
      <span class="lbl">Locataire</span>
      <div class="val">{locataire}</div>
    </td>
  </tr>
</table>

<table class="amounts">
  <tr><td>Loyer principal</td><td class="num">{eur(loyer)}</td></tr>
  <tr><td>Provision pour charges</td><td class="num">{eur(charges)}</td></tr>
  {teom_row_q}
  <tr class="border-top total"><td>Total de la période</td><td class="num">{eur(total_q)}</td></tr>
  <tr class="aide"><td>Aide au logement (CAF)</td><td class="num">− {eur(aide_caf)}</td></tr>
  <tr class="net"><td>Net à payer</td><td class="num">{eur(net_q)}</td></tr>
</table>

<div class="legal">Quittance valant reçu pour le paiement de la période ci-dessus, sans préjudice du terme en cours et sous réserve de tous suppléments pouvant être dus en vertu des lois ou conventions applicables. Cette quittance annule tous les reçus qui auraient pu être donnés pour acompte versé sur le présent terme, même si ces reçus portent une date postérieure à la date ci-dessus. Le paiement de la présente quittance n'emporte pas présomption de paiement des termes antérieurs.</div>

<hr class="dotted">

<h2 class="sec"><span class="tag">À venir</span><br>Avis d'échéance</h2>
<div class="period">Période du {a_start} au {a_end}</div>

<table class="amounts">
  <tr><td>Loyer principal</td><td class="num">{eur(loyer)}</td></tr>
  <tr><td>Provision pour charges</td><td class="num">{eur(charges)}</td></tr>
  {teom_row_a}
  <tr class="border-top total"><td>Total de la période</td><td class="num">{eur(total_a)}</td></tr>
  <tr class="aide"><td>Aide au logement (CAF)</td><td class="num">− {eur(aide_caf)}</td></tr>
  <tr class="net"><td>Net à payer</td><td class="num">{eur(net_a)}</td></tr>
</table>

<div class="legal">Nous vous invitons à régler le montant ci-dessus au plus tard le {a_start}. Cet avis est une demande de paiement et ne peut en aucun cas servir de reçu ou de quittance de loyer.</div>

<div class="sign">
  <div class="rule"></div>
  <div class="who">Le bailleur</div>
  <div>{bailleur_nom}</div>
</div>

</body></html>"""

out = "Quittance.pdf"
weasyprint.HTML(string=html).write_pdf(out)
print("PDF généré :", out)
