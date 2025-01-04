# Contributing Guidelines

Contributions are welcome via GitHub Pull Requests. This document outlines the process to help get your contribution accepted.

Any type of contribution is welcome; from new features, bug fixes, [tests](#testing), documentation improvements, or even [adding charts to the repository](#adding-a-new-chart-to-the-repository) (if it's viable once evaluated the feasibility).

## How to Contribute

1. Clone this repo.
2. Create a branch with a valid prefix
3. Submit a pull request.

A valid prefix would be `bugfix/` for fixing something and `feature/` to change the feature scope.

### Technical Requirements

When submitting a PR make sure that it:

- Must pass CI jobs for linting and test the changes
- Any change to a chart requires a version bump following [semver](https://semver.org/) principles. This is the version that is going to be merged in the GitHub repository, then our CI/CD system is going to publish in the Helm registry a new patch version including your changes and the latest images and dependencies.

#### Sign Your Work

The sign-off is a simple line at the end of the explanation for a commit. All commits need to be signed. Your signature certifies that you wrote the patch or otherwise have the right to contribute the material. The rules are pretty simple, you only need to certify the guidelines from [developercertificate.org](https://developercertificate.org/).

Then you just add a line to every git commit message:

```text
Signed-off-by: Joe Smith <joe.smith@example.com>
```

Use your real name (sorry, no pseudonyms or anonymous contributions.)

If you set your `user.name` and `user.email` git configs, you can sign your commit automatically with `git commit -s`.

Note: If your git config information is set properly then viewing the `git log` information for your commit will look something like this:

```text
Author: Joe Smith <joe.smith@example.com>
Date:   Thu Feb 2 11:41:15 2018 -0800

    Update README

    Signed-off-by: Joe Smith <joe.smith@example.com>
```

Notice the `Author` and `Signed-off-by` lines match. If they don't your PR will be rejected by the automated DCO check.

### Documentation / Styleguide / Requirements

- The title of the PR starts with chart name (e.g. `[Zitronenhain/space-shooter-py]`)
- All pull requests SHOULD adhere to the [Conventional Commits specification](https://conventionalcommits.org/)

### PR Approval and Release Process

1. Changes are manually reviewed by Zitronenhain team members.
2. Once the changes are accepted, the PR is verified with an automatic test, that includes the lint and the vulnerability checks. If that passes, the Zitronenhain team wil review the changes and trigger the verification and functional tests.
3. When the PR passes all tests, the PR is merged by the reviewer(s) in the GitHub `main` branch.

### Testing

1. To Be Done, sorry at this point.

> [!NOTE]
> Please note that, this is a free time project. Mistakes are not done on purpose and it can take up to 72h for a member to react.