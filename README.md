# Social Media Top 50 Datasets

Top 50 rankings scraped from SocialBlade across 5 platforms, plus a simulated student performance dataset. All published on Kaggle.

## Datasets

| Dataset | Platform | Records | Key Metric |
|---------|----------|---------|------------|
| [YouTube Top 50](https://www.kaggle.com/datasets/mubashirsidiki/top-50-youtube-channels-by-subscribers) | YouTube | 50 | Subscribers |
| [TikTok Top 50](https://www.kaggle.com/datasets/mubashirsidiki/top-50-tiktok-accounts-by-followers) | TikTok | 50 | Followers |
| [Twitch Top 50](https://www.kaggle.com/datasets/mubashirsidiki/top-50-twitch-channels-by-followers) | Twitch | 50 | Followers |
| [Facebook Top 50](https://www.kaggle.com/datasets/mubashirsidiki/top-50-facebook-pages-by-likes) | Facebook | 50 | Likes |
| [Instagram Top 50](https://www.kaggle.com/datasets/mubashirsidiki/top-50-instagram-accounts-by-followers) | Instagram | 50 | Followers |
| [Student Performance](https://www.kaggle.com/datasets/mubashirsidiki/student-academic-performance-500-students) | — | 500 | Final Score |

## Structure

```
datasets/
├── youtube-top-50/        # CSV + Kaggle notebook
├── tiktok-top-50/         # CSV + Kaggle notebook
├── twitch-top-50/         # CSV + Kaggle notebook
├── facebook-top-50/       # CSV + Kaggle notebook
├── instagram-top-50/      # CSV + Kaggle notebook
└── student-performance/   # CSV + Kaggle notebook (ML pipeline)
```

Each dataset folder contains the CSV, a Kaggle notebook (`.ipynb`), and `dataset-metadata.json` for the Kaggle API.

## Notebooks

- **Social media datasets** — Dark-themed visual exploration (bar charts, scatter plots)
- **Student Performance** — Full ML pipeline: classification (pass/fail) and regression (final score) with 5+ models, ROC curves, confusion matrix, feature importance

## Tools

- `kaggle_utils.py` — CLI helper for Kaggle API (create, upload, list datasets)
- `social-blade-dataset/` — Raw scraped data (source)

## License

MIT
