# GitHub Consultation Administration Checklist

This checklist contains the small set of GitHub settings that cannot be encoded
fully in repository files. It is intended for the sole Schema Maintainer and
Consultation Chair.

## 1. Merge the setup pull request

Open:

`https://github.com/KBOB-admin/KBOB-data-dictionary-schema/pull/new/consultation-2026-setup`

Confirm that the `Validate vocabulary` check passes, review the rendered Markdown
and issue form, then squash-merge the branch into `main`.

## 2. Create labels

Create the following labels. Colours are suggestions only.

| Label | Suggested colour |
|---|---|
| `status: new` | `D4C5F9` |
| `status: triaged` | `BFDADC` |
| `status: discussion` | `FBCA04` |
| `status: decision-ready` | `F9D0C4` |
| `status: closed` | `C5DEF5` |
| `decision: accepted` | `0E8A16` |
| `decision: accepted-modified` | `2EA44F` |
| `decision: rejected` | `D73A4A` |
| `decision: deferred` | `FEF2C0` |
| `decision: duplicate` | `CFD3D7` |
| `decision: out-of-scope` | `E4E669` |
| `type: semantic` | `1D76DB` |
| `type: technical` | `0052CC` |
| `type: editorial` | `C2E0C6` |
| `type: governance` | `5319E7` |
| `breaking-change` | `B60205` |

The issue form references `status: new`; create at least that label before
public launch.

## 3. Create milestones

- `2026-10 consolidation`
- `2026-11 consolidation`
- `2026-12 preliminary consolidation`
- `2027-01 final disposition`

Add exact workshop dates to the milestone descriptions once calendar invitations
have been agreed.

## 4. Protect `main`

Create a repository ruleset targeting the default branch `main`:

- require a pull request before merging;
- required approvals: `0` (single-maintainer model);
- require all conversations to be resolved;
- require the `validate` status check;
- require the branch to be up to date before merging;
- block force pushes;
- restrict deletions;
- allow only squash merging in the repository merge settings;
- keep bypass rights limited to the repository administrator for emergencies.

Do not require signed commits or external reviewer approval during this
consultation. Either would add friction or deadlock the single-maintainer model.

## 5. Publish the consultation baseline

After the setup PR is merged and `main` is clean:

```bash
git switch main
git pull --ff-only origin main
git tag -a v0.2.0-consultation-2026 -m "NatDD public consultation baseline 2026"
git push origin v0.2.0-consultation-2026
```

Verify that the tag contains `CONSULTATION.md`, `GOVERNANCE.md`, the issue form,
and the approved ontology state.

## 6. Launch checks

- Open a test consultation issue and confirm the form renders correctly.
- Confirm the accountability and CC0 checkboxes are mandatory.
- Open a test pull request from a temporary branch and confirm validation runs.
- Confirm direct pushes to `main` are blocked.
- Confirm public users can open issues and fork the repository.
- Replace or supplement the invitation text with calendar access details.
- Send the German/English invitation to the selected experts.

## 7. Monthly maintenance

- Assign every valid issue to the appropriate milestone.
- Move each issue through the `status:` labels.
- Apply exactly one `decision:` label when disposition is complete.
- Copy the disposition and rationale into
  `docs/consultation-disposition-register.csv` through a pull request.
- Link every accepted issue to its implementing pull request and commit.
- Publish concise workshop minutes without unnecessary personal data.
