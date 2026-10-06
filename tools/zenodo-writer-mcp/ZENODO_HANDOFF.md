# ZENODO_HANDOFF

Canonical handoff for the current Zenodo v0.1 deposit task.

## Main objective

Keep the project on the primary path:

Island → Bridge Object → First Network Edge → Repeated Interaction → Real Collaboration

The current infrastructure work exists only to make the first Bridge Object citable and traceable. Do not expand infrastructure beyond what is needed to finish v0.1.

## Bridge Object

**Physical Activity Adherence — Digital Intervention Micro Map v0.1**

Joint Open Research Project:
- Catherine Ge
- Starr Choi

v0.1 is frozen at PA001–PA010.

## Canonical ZIP

Use only:

`zenodo-physical-activity-adherence-micro-map-v0.1-CC-BY-4.0.zip`

Expected size: about 19,868 bytes.

Expected SHA-256:

`16319a5c24c2013457d418c88fda87454a195ca91fa423fd47f403df2a60b7fe`

Do **not** use the older:

`zenodo-physical-activity-adherence-micro-map-v0.1.zip`

Do not modify, recompress, regenerate, or replace the canonical ZIP unless explicitly instructed after DOI reservation.

## Current Zenodo task

Create and save a Zenodo **draft** only.

Metadata:

- Resource type: Dataset
- Title: Physical Activity Adherence — Digital Intervention Micro Map v0.1
- Creators, in order:
  1. Catherine Ge
  2. Starr Choi
- Version: 0.1
- License: Creative Commons Attribution 4.0 International (CC BY 4.0)
- Visibility: Public
- Publication date: current date
- DOI option: No, I need one

If Zenodo requires additional description/keywords/fields and the value is not already present in repository/project materials, stop and report the missing field instead of inventing content.

## File upload handling

The active browser is a cloud browser and cannot see the user's Mac Downloads folder.

The canonical ZIP is already available in the cloud-browser shared file area.

If clicking Zenodo's upload control does not open a usable file picker:

1. Inspect the Files-area DOM for `input[type="file"]`.
2. If present, use the browser/computer-use file-upload primitive to set the canonical ZIP directly on that input, even if hidden.
3. If no usable file input exists, use the browser-native file/dropzone upload primitive.
4. Do not synthesize a File object in page JavaScript.
5. Do not loop on GUI clicks.

Upload success is established only when the Zenodo page visibly lists:

`zenodo-physical-activity-adherence-micro-map-v0.1-CC-BY-4.0.zip`

and the upload is complete.

## Allowed actions now

- Fill the Zenodo draft form
- Upload the canonical ZIP
- Save draft
- Report validation warnings / missing fields
- Report draft URL / record ID if shown

## Publication authorization

Starr explicitly provided the exact confirmation string:

`PUBLISH_ZENODO_RECORD`

Publication is now authorized for the existing Zenodo draft **23178043** only.

Allowed publication action:
- Open the existing draft `https://zenodo.org/uploads/23178043`
- Confirm the final pre-publish audit still matches the recorded values
- Click **Publish** once
- Wait for Zenodo to confirm publication
- Stop immediately after publication and report the final record URL, DOI resolution status, file count/name/size/checksum shown, and any warnings

Still forbidden:
- Creating another draft
- Deleting any record
- Changing metadata before publication unless a new validation error requires it
- Replacing or modifying the DOI-aware ZIP
- Publishing any other record
- Expanding OAuth / Clerk / Vercel / MCP infrastructure

## After the draft is saved

Stop and report:

1. Whether draft save succeeded
2. Uploaded filename
3. Actual metadata values
4. Validation warnings / missing required fields
5. Draft URL / record ID

The next stage, only after review, is:

Reserve DOI → write real reserved DOI into CITATION.cff / README / sisfit.cn / frozen archive → regenerate DOI-aware ZIP → replace draft ZIP → pre-publish audit → wait for `PUBLISH_ZENODO_RECORD`.

After Zenodo publication, immediately return to the main network-building path:

PA010 / Fukuoka et al. 2019 → one correction request → external expert check → network-edge ledger.
