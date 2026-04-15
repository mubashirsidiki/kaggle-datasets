# Kaggle Dataset Workspace

Curated dataset packages for Kaggle, including social media rankings and a student performance dataset.

## What is here

- YouTube channel rankings (global, US, India) and global top videos by views
- TikTok, Instagram, Twitch, Facebook rankings
- GitHub top repositories by stars
- Student performance dataset with EDA + ML notebook

## Repo structure

```text
datasets/
  <platform>/<region-or-scope>/<metric>/<tier>/
    data/
    notebooks/
    metadata/
    assets/   # optional
    docs/     # optional

scripts/
  kaggle_utils.py

docs/
  kaggle-manual-steps.md
```

## Notes

- Each dataset package is self-contained for Kaggle publishing.
- `metadata/dataset_metadata.json` is the Kaggle metadata file.
- Notebooks are personalized per dataset and kept compact.

## License

Apache-2.0
