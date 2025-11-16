import git

# Path to a repository you have locally
REPO_PATH = "../sc-lms-portals"

base_hash = "d218122ee9fa718674f80eb3f033fcaeecc7f0fc"
head_hash = "97aa3b7aa495554910ca7113f76ee786ad5bb081"

repo = git.Repo(REPO_PATH)

print("Testing repo.merge_base() ...")

merge_bases = repo.merge_base(base_hash, head_hash)

print(merge_bases)
