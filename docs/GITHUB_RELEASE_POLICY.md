# GitHub Release Policy

## Two independent repositories

| | `radreport-ai` (public) | `radreport-platform-private` (private) |
|---|---|---|
| Purpose | Transparent science, reusable tools | Product engineering |
| Contains | Docs, data catalog, generic preprocessing, baseline experiments, evaluation tools, research diagrams | Application backend, orchestration, advanced engine, integrations, deployment config, business logic, private weights |
| Licence | Apache-2.0 code, CC BY 4.0 docs | Proprietary |

No mirroring, submodules or shared automated sync. Anything crossing from private to public goes through the checklist below.

## Conflict to resolve: public science vs private code

**PhysioNet requires code for publications using credentialed data to be placed in a repository open to the research community** [L13]. So:

- Code behind a MIMIC or VinDr paper must live in the public repo.
- A private reporting engine cannot be the undisclosed basis of a paper using those datasets.
- Design the paper code as a clean, public research implementation, separate from product code.

## Never commit

Patient data; identifying clinical stories; images from restricted datasets, even thumbnails; radiology reports from restricted datasets; credentials, tokens or keys; IP addresses, hostnames or server details; `.env` files; restricted model weights; audit output; named hospital partners without a signed agreement.

## Clinical story rule

The master project directive holds details of a real patient encounter. **It stays out of both repositories.** Only the generalised account in [Clinical motivation](CLINICAL_MOTIVATION.md) is published.

## Publication checklist

Before any release:

- [ ] Data provenance checked.
- [ ] Licences of dependencies and weights checked.
- [ ] No restricted data, no secrets: run `gitleaks` or similar.
- [ ] IP decision made by the project lead.
- [ ] Hospital or partner agreements allow it.
- [ ] Clinical claims checked against evidence.
- [ ] Status banner present: research prototype.
- [ ] Citation file updated.

## If something leaks

Removing a file in a new commit does not erase it from history.

1. Make the repository private at once, if it is public.
2. Revoke any credentials.
3. Tell the project lead and data owner. For PhysioNet data, follow its reporting route. For Kenyan data, follow breach duties.
4. Rewrite history, and ask GitHub to purge cached views.
5. Record the incident.

## Versioning

Tag releases, `v0.1.0`. Mint a Zenodo DOI for releases cited in papers.

## Decisions awaiting the project lead

- Confirm Apache-2.0 and CC BY 4.0. Apache includes a patent grant. A more protective licence is possible, but limits reuse.
- Consider who owns the IP: you, an employer, a training institution or a future company? Check any internship or employment terms. This matters before a product exists.
