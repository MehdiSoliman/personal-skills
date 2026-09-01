---
name: quittance-loyer
description: "Generate a French rent receipt (quittance de loyer) PDF."
version: 1.1.0
author: Mehdi Soliman
license: MIT
---

# Quittance de loyer (template générique)

## When to Use
Generate a monthly French rent receipt (**quittance de loyer**) + a payment notice (**avis d'échéance**), in a clean single-A4 layout (two sections). Use when asked to generate a rent receipt, or the quittance/landlord/rent/TEOM workflow.

## À personnaliser (avant première utilisation)
Edit the top of `scripts/make_quittance.py`:
- **Bailleur** : nom, adresse, téléphone, email
- **Locataire** : nom + adresse
- **Logement** : nom de la résidence, adresse, lot / étage / surface / parking
- **Montants** : loyer, provision charges, aide CAF, TEOM annuelle

## Points légaux (ne pas oublier)
- La quittance **doit** détailler loyer ET charges **séparément** + le total + la **mention légale complète** (« annule tous les reçus… » + « n'emporte pas présomption de paiement des termes antérieurs »).
- « Débit / Crédit » n'est **PAS** obligatoire (convention de logiciel de gestion).
- La **taxe foncière** reste à la charge du **bailleur** — ne JAMAIS la refacturer au locataire. Seule la **TEOM** (ordures ménagères) est récupérable (décret 87-713).

## Workflow
1. **Personnaliser** `scripts/make_quittance.py` (constantes en tête de fichier).
2. **Générer le PDF** : `python scripts/make_quittance.py`.
3. **Sauvegarder sur Drive** (optionnel) : via le skill `google-workspace`.

## Dépendances
- `weasyprint` (génération PDF).

## Piège
- Le script est calé pour tenir sur **1 page A4**. Si on ajoute des lignes (TEOM, etc.), resserrer le padding de `table.amounts td` ou les marges de `h2.sec` pour rester sur une page.
