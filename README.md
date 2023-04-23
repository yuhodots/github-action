# github-action
> Simple examples of github actions and git hooks

- [개인 블로그](https://yuhodots.github.io/cheatsheet/22-08-26/)에도 내용이 정리되어있습니다.

## GitHub Actions

> 공식 문서: [GitHub Actions에 대한 워크플로 구문](https://docs.github.com/ko/actions/using-workflows/workflow-syntax-for-github-actions)

- Workflows: 한 개 혹은 여러 개의 Job으로 구성되고, event나 스케줄 등에 의해 트리거될 수 있음
- Events: Workflow run을 트리거할 수 있는 activity
- Jobs: Same runner에 존재하는 workflow 내의 여러 단계들. 여러 jobs이 의존성을 가질 수 있고 병렬적 실행되는 것도 가능
- Actions: individual tasks that you can combine to create jobs and customize your workflow
- Runners: Workflow가 수행될 인스턴스. 일반적으로는 GitHub에서 호스팅해주는 runner를 사용하나 self-hosted runners도 가능

1. Workflows 생성: github의 workflow template 활용하거나, `.github/workflows` 폴더 직접 생성
2. `.yml` 파일 생성하고 내용 작성
   - `name`:  The name of the workflow as it will appear in the "Actions" tab of the GitHub
   - `run-name`: The name for workflow runs generated from the workflow, which will appear in the list of workflow runs on your repository's "Actions" tab
   - `on`: Trigger for this workflow. 즉, event를 의미하며 array로 작성시 여러 event 활용 가능
   - `jobs`: Groups together all the jobs that run in the workflow. 여러 Job에 대해 기본적으로는 병렬 수행
   - `jobs/${job_name}/runs-on`: 사용할 OS를 명시
   - `jobs/${job_name}/steps/uses`: 이미 만들어진 action이 있는 경우 어떤 action을 사용할지 명시
   - `jobs/${job_name}/steps/run`: runner 내에서 수행할 커맨드를 명시
3. 그 외: 조직과 workflow 공유, secret key 저장, dependecy caching, artifact 저장 등의 기능도 수행 가능하니 공식 문서 참고하기

## Git Hooks

> 공식 문서: [Git맞춤 - Git Hooks](https://git-scm.com/book/ko/v2/Git맞춤-Git-Hooks)

- GitHub Action은 remote에서 트리거에 따른 작업을 수행하지만, 로컬에서도 git hooks를 통해 특정 액션에 대한 특정 스크립트를 자동으로 실행할 수 있음. 또한 **husky**라는 Git Hooks를 보다 쉽게 적용할 수 있는 모듈 또한 존재함
- `.git/hooks/{hook_name}`의 경로에 스크립트를 작성하면 끝
- Commit workflow hooks
  - `pre-commit`: 커밋할 때 가장 먼저 호출되는 훅으로 커밋 메시지를 작성하기 전에 호출됨
  - `prepare-commit-msg`: Git이 커밋 메시지를 생성하고 나서 편집기를 실행하기 전에 실행됨. 사람이 커밋 메시지를 수정하기 전에 먼저 프로그램으로 손보고 싶을 때 사용
  - `commit-msg`: 커밋 메시지가 들어 있는 임시 파일의 경로를 아규먼트로 받는 훅. 그리고 이 스크립트가 0이 아닌 값을 반환하면 커밋되지 않음. 이 훅에서 최종적으로 커밋이 완료되기 전에 프로젝트 상태나 커밋 메시지를 검증 가능
  - `post-commit`: 커밋이 완료된 후에 실행되는 훅으로, 넘겨받는 아규먼트가 하나도 없지만 커밋 해시정보는 `git log -1 HEAD` 명령으로 가져올 수 있음. 일반적으로 커밋된 것을 누군가 혹은 다른 프로그램에게 알릴 때 사용

- 이 외에도 `pre-rebase`, `post-rewrite`, `post-merge`, `pre-push` 등의 hook과, server hooks인 `pre-receive`, `post-receive`, `update` 등도 존재함

## Husky

> 공식 문서: [Husky](https://typicode.github.io/husky/#/)

1. `npm install --save-dev husky`: Install
2. `npx husky install`: Enable Git hooks
3. `npm pkg set scripts.prepare="husky install"`: Modify package.json for handling git hooks automatically
4. `npx husky add .husky/pre-commit "{do_something}"`: Git hooks 생성
5. `git add .husky/pre-commit`

### pre-commit

> 공식 문서: https://pre-commit.com

- 사용 가능한 pre-commit hooks 들은 [이곳](https://pre-commit.com/hooks.html)에서 확인 가능함

1. `brew install pre-commit`: Install
2. `pre-commit sample-config > .pre-commit-config.yaml`: Create a config file
3. `pre-commit run`: 수동으로 pre-commit 실행하기
4. **`pre-commit install`**: commit 할 때 자동으로 pre-commit가 실행되도록 git hook에 등록
