# Kaggle Manual Steps

Do these for each dataset on the Kaggle website. Copy-paste the content below directly.

---

## 1. YouTube - Top 50 Channels by Subscribers

**URL:** https://www.kaggle.com/datasets/mubashirsidiki/top-50-youtube-channels-by-subscribers

### File Description

Top 50 YouTube channels ranked by total subscribers as of April 2026. Includes subscriber count, total video views, and upload count for each channel.

### Column Descriptors

| Column | Description |
|--------|-------------|
| rank | Ranking position (1-50) based on subscriber count |
| channel | Channel display name |
| subscribers | Total subscriber count (e.g. 474M = 474 million) |
| video_view | Cumulative video view count (e.g. 116.11B = 116.11 billion) |
| uploads | Total number of videos uploaded (e.g. 25.76K = 25,760) |

### Tags

`youtube` `social media` `influencers` `subscribers` `content creators` `streaming` `entertainment` `eda` `data visualization`

### Provenance

- **Source:** Publicly available YouTube channel statistics
- **Collection method:** Compiled from publicly accessible platform ranking page
- **Temporal coverage:** April 2026
- **Geographic coverage:** Global

---

## 2. TikTok - Top 50 Accounts by Followers

**URL:** https://www.kaggle.com/datasets/mubashirsidiki/top-50-tiktok-accounts-by-followers

### File Description

Top 50 TikTok accounts ranked by total followers as of April 2026. Includes follower count, following count, total likes, and upload count for each account.

### Column Descriptors

| Column | Description |
|--------|-------------|
| rank | Ranking position (1-50) based on follower count |
| account | Display name |
| followers | Total follower count (e.g. 165.5M = 165.5 million) |
| following | Number of accounts this user follows |
| likes | Total likes across all videos |
| uploads | Total number of videos posted |

### Tags

`tiktok` `social media` `influencers` `followers` `short form video` `content creators` `trending` `eda` `data visualization`

### Provenance

- **Source:** Publicly available TikTok account statistics
- **Collection method:** Compiled from publicly accessible platform ranking page
- **Temporal coverage:** April 2026
- **Geographic coverage:** Global

---

## 3. Twitch - Top 50 Channels by Followers

**URL:** https://www.kaggle.com/datasets/mubashirsidiki/top-50-twitch-channels-by-followers

### File Description

Top 50 Twitch channels ranked by total followers as of April 2026. Includes follower count for each channel.

### Column Descriptors

| Column | Description |
|--------|-------------|
| rank | Ranking position (1-50) based on follower count |
| channel | Channel name |
| followers | Total follower count (e.g. 20.19M = 20.19 million) |

### Tags

`twitch` `streaming` `gaming` `live streaming` `followers` `esports` `content creators` `eda` `data visualization`

### Provenance

- **Source:** Publicly available Twitch channel statistics
- **Collection method:** Compiled from publicly accessible platform ranking page
- **Temporal coverage:** April 2026
- **Geographic coverage:** Global

---

## 4. Facebook - Top 50 Pages by Likes

**URL:** https://www.kaggle.com/datasets/mubashirsidiki/top-50-facebook-pages-by-likes

### File Description

Top 50 Facebook pages ranked by total likes as of April 2026. Includes like count and "talking about" count (current engagement) for each page.

### Column Descriptors

| Column | Description |
|--------|-------------|
| rank | Ranking position (1-50) based on like count |
| page | Page display name |
| likes | Total page like count (e.g. 188.14M = 188.14 million) |
| talking_about | Number of people currently engaging with the page |

### Tags

`facebook` `social media` `pages` `likes` `brands` `engagement` `content creators` `eda` `data visualization`

### Provenance

- **Source:** Publicly available Facebook page statistics
- **Collection method:** Compiled from publicly accessible platform ranking page
- **Temporal coverage:** April 2026
- **Geographic coverage:** Global

---

## 5. Instagram - Top 50 Accounts by Followers

**URL:** https://www.kaggle.com/datasets/mubashirsidiki/top-50-instagram-accounts-by-followers

### File Description

Top 50 Instagram accounts ranked by followers as of April 2026. Includes account display name and username. Instagram restricts public access to detailed stats, so only rank, name, and username are included.

### Column Descriptors

| Column | Description |
|--------|-------------|
| rank | Ranking position (1-50) based on follower count |
| account | Display name |
| username | Instagram handle (e.g. @instagram) |

### Tags

`instagram` `social media` `followers` `celebrities` `influencers` `content creators` `eda` `data visualization`

### Provenance

- **Source:** Publicly available Instagram account statistics
- **Collection method:** Compiled from publicly accessible platform ranking page
- **Temporal coverage:** April 2026
- **Geographic coverage:** Global

---

## 6. Student Academic Performance - 500 Students

**URL:** https://www.kaggle.com/datasets/mubashirsidiki/student-academic-performance-500-students

### File Description

Simulated dataset of 500 high school students with demographic info, study habits, and academic performance. Useful for classification (predict pass/fail), regression (predict final score), and exploring how factors like study hours and attendance relate to outcomes.

### Column Descriptors

| Column | Description |
|--------|-------------|
| student_id | Unique student identifier (STU0001-STU0500) |
| gender | Student gender (Male/Female) |
| age | Student age in years |
| study_hours_per_week | Self-reported weekly study hours |
| attendance_rate | Class attendance percentage (0-100) |
| parent_education | Highest education level of parents |
| internet_access | Whether student has internet at home (Yes/No) |
| extracurricular | Whether student participates in extracurriculars (Yes/No) |
| previous_score | Score from previous term (0-100) |
| final_score | Final exam score (0-100) |
| passed | Whether student passed (Yes/No) |

### Tags

`education` `students` `academic performance` `classification` `regression` `tabular data` `beginners` `eda` `data visualization`

### Provenance

- **Source:** Self-generated dataset for educational purposes
- **Collection method:** Generated to mirror realistic patterns in student performance data
- **Temporal coverage:** N/A (simulated)
- **Geographic coverage:** N/A (simulated)

---

## 7. Most Viewed YouTube Videos - Top 1000

**URL:** https://www.kaggle.com/datasets/mubashirsidiki/most-viewed-youtube-videos-top-1000

### File Description

Top 1000 most viewed YouTube videos of all time, ranked by total views. Includes title, view count, like count, title length, detected language, content type classification, and flags for shorts and hashtag usage.

### Column Descriptors

| Column | Description |
|--------|-------------|
| rank | Ranking position (1-1000) based on total views |
| title | Video title |
| title_length | Character count of the video title |
| detected_language | Detected language from title text (English, Hindi, Arabic, Korean, etc.) |
| content_type | Classified content type (Music Video, Kids/Educational, Short, Ad/Promo, etc.) |
| is_short | Whether the video is a YouTube Short (1=yes, 0=no) |
| has_hashtags | Whether the title contains hashtags (1=yes, 0=no) |
| views | Total view count (e.g. 16.8B = 16.8 billion) |
| likes | Total like count (e.g. 46.4M = 46.4 million) |

### Tags

`youtube` `most viewed` `videos` `top 1000` `music` `shorts` `eda` `data visualization` `content analysis` `entertainment`

### Provenance

- **Source:** Publicly available YouTube video statistics
- **Collection method:** Compiled from publicly accessible video ranking page
- **Temporal coverage:** April 2026
- **Geographic coverage:** Global

---

## Checklist (do for all 7)

- [ ] Cover image uploaded (Settings > Edit Image)
- [ ] File description added (click file > add description)
- [ ] Column descriptors added (click column header > add description)
- [ ] Provenance filled (Metadata > Provenance > Edit)
- [ ] Author name added (Metadata > Authors > Edit)
