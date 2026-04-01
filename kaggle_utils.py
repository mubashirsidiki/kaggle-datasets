from dotenv import load_dotenv
load_dotenv()

from kaggle.api.kaggle_api_extended import KaggleApi
import sys
import os

api = KaggleApi()
api.authenticate()


def list_my_datasets():
    datasets = api.dataset_list(mine=True)
    for d in datasets:
        print(f"  {d.ref}  |  {d.title}")


def upload(folder, notes="updated"):
    folder = os.path.abspath(folder)
    os.chdir(folder)
    api.dataset_create_version(folder, version_notes=notes, quiet=False)
    print("\nUpload done!")


def create(folder):
    folder = os.path.abspath(folder)
    os.chdir(folder)
    api.dataset_create_new(folder, public=True, quiet=False)
    print("\nDataset created!")


def delete(owner, slug):
    api.dataset_delete(owner, slug)
    print("Deleted!")


def info(slug):
    owner, ds = slug.split("/")
    datasets = api.dataset_list(search=ds, user=owner)
    for d in datasets:
        if d.ref == slug:
            print(f"Title:     {d.title}")
            print(f"Ref:       {d.ref}")
            print(f"Score:     {d.usability_rating}")
            print(f"Downloads: {d.download_count}")
            print(f"Votes:     {d.vote_count}")
            break


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python kaggle_utils.py list              - list your datasets")
        print("  python kaggle_utils.py info <slug>       - view dataset info")
        print("  python kaggle_utils.py create <folder>   - create new dataset")
        print("  python kaggle_utils.py upload <folder> [notes] - update dataset")
        print("  python kaggle_utils.py delete <owner> <slug>   - delete dataset")
        sys.exit()

    cmd = sys.argv[1]

    if cmd == "list":
        list_my_datasets()
    elif cmd == "info":
        info(sys.argv[2])
    elif cmd == "create":
        create(sys.argv[2])
    elif cmd == "upload":
        notes = sys.argv[3] if len(sys.argv) > 3 else "updated"
        upload(sys.argv[2], notes)
    elif cmd == "delete":
        delete(sys.argv[2], sys.argv[3])
    else:
        print(f"Unknown command: {cmd}")
