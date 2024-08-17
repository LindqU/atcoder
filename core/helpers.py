import os
import subprocess
from .logger import log
from .config import extensions


class AtcoderCli:
    @staticmethod
    def run_command(command):
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
        )
        stdout, stderr = process.communicate()
        return stdout.decode(), stderr.decode(), process.returncode

    @staticmethod
    def fetch_contest_info(contest_id=os.getenv("CONTEST_ID")):
        log.info("Fetching contest information", contest_id=contest_id)
        contest_dir = "/workspaces/atcoder/contests/"
        os.makedirs(contest_dir, exist_ok=True)
        os.chdir(contest_dir)

        # Fetch contest information and download problems using AtCoder CLI
        stdout, stderr, return_code = AtcoderCli.run_command(
            f"acc new {contest_id} --choice all"
        )
        if return_code != 0:
            log.error("Failed to fetch contest information", error=stderr)
        else:
            log.info(
                "Contest information and problems downloaded", contest_id=contest_id
            )

    @staticmethod
    def submit_solution(contest_id, problem_id, filename):
        langage = os.environ["LANGAGE"]
        extension = extensions[langage]["extension"]
        log.info(
            "Submitting solution",
            contest_id=contest_id,
            problem_id=problem_id,
            filename=filename,
        )
        stdout, stderr, returncode = AtcoderCli.run_command(
            f"acc submit {problem_id}.{extension}"
        )
        log.info(stdout)
        if returncode != 0:
            log.error("Error submitting solution", error=stderr)

    @staticmethod
    def download_problem(contest_id, problem_id):
        log.info("Downloading problem", contest_id=contest_id, problem_id=problem_id)
        AtcoderCli.run_command(f"acc add {contest_id}_{problem_id}")


class AtcoderContest:
    """ToDo: Atcoder のコンテスト環境を整えるための関数群"""

    @staticmethod
    def copy_template(contest_id=os.getenv("CONTEST_ID")):
        """ToDo: テンプレートの作成"""

        def get_directories(path):
            # pathの一覧取得
            return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

        langage = os.getenv("LANGAGE", "python")

        # mainのテンプレートを取得
        main_file_name = extensions[langage]["main_file_name"]
        log.info("Copying main template", langage=langage, filename=main_file_name)
        main_template_path = (
            f"/workspaces/atcoder/core/templates/{langage}/main/{main_file_name}"
        )
        print(main_template_path)
        with open(main_template_path, "r", encoding="utf-8") as f:
            main_template = f.read()
        main_file_name = extensions[langage]["main_file_name"]

        # testのテンプレートを取得
        test_file_name = extensions[langage]["test_file_name"]
        log.info("Copying test template", langage=langage, filename=test_file_name)
        test_template_path = f"/workspaces/atcoder/core/templates/{langage}/test/{test_file_name}"
        with open(test_template_path, "r", encoding="utf-8") as f:
            test_template = f.read()

        task_dir_path = f"/workspaces/atcoder/contests/{contest_id}"
        dir_list = get_directories(task_dir_path)

        with open(os.path.join(task_dir_path, '__init__.py'), 'w', encoding='utf-8') as f:
            pass

        for task_dir in dir_list:
            # initの生成
            with open(
                os.path.join(task_dir_path, task_dir, "__init__.py"),
                "w",
                encoding="utf-8",
            ) as f:
                pass
            log.info(
                "Gen Template File",
                langage=langage,
                filename=os.path.join(task_dir_path, task_dir, "__init__.py"),
            )
            # main.pyの生成
            with open(
                os.path.join(task_dir_path, task_dir, main_file_name),
                "w",
                encoding="utf-8",
            ) as f:
                f.write(main_template)
            log.info(
                "Gen Template File",
                langage=langage,
                filename=os.path.join(task_dir_path, task_dir, main_file_name),
            )
            # test.pyの生成
            with open(
                os.path.join(task_dir_path, task_dir, test_file_name),
                "w",
                encoding="utf-8",
            ) as f:
                f.write(test_template)
            log.info(
                "Gen Template File",
                langage=langage,
                filename=os.path.join(task_dir_path, task_dir, test_file_name),
            )
