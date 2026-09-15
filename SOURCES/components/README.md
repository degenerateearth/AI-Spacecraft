# Component evidence archive

Retrieval date: 2026-09-15

This directory preserves the identity of the exact primary documents used by
the Phase 1 component audit. `LOCAL_ARCHIVE_MANIFEST.csv` records the local file
name, byte count, SHA-256, official URL, document identity and evidence class.
The `.url` files open the authoritative manufacturer copy.

Current manufacturer HTML captures are also retained locally when the page
contains critical availability or configuration evidence. They are hashed in the
same manifest and ignored by Git because redistribution permission was not found.

Vendor PDFs are locally retained on `D:\Degen-1` for project audit only and are
excluded from Git because no redistribution license was established. A hash is
not a technical claim; it only lets a reviewer verify that the same bytes were
used. If a manufacturer replaces a file at the same URL, save the new revision
separately and preserve the old hash.

An archived datasheet does not pass the component gate by itself. Consult
`Components/Phase1_Component_Property_Matrix.csv` for whether its actual content
covers each mission-relevant property.
