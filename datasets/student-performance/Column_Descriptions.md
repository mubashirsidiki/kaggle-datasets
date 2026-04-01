# Column Descriptions

## student_performance.csv

| Column | What it means |
|--------|---------------|
| student_id | Unique ID for each student, like STU0001 |
| gender | Male or Female |
| age | Student age, ranges from 15 to 19 |
| study_hours_per_week | How many hours they study per week (2-30) |
| attendance_rate | Their class attendance % (50-100) |
| parent_education | Parents' highest education: None, High School, Bachelor, Master, or PhD |
| internet_access | Do they have internet at home? Yes/No |
| extracurricular | Do they do any extracurriculars? Yes/No |
| previous_score | Their score on the last exam (0-100) |
| final_score | Their final exam score (0-100) |
| passed | Yes if final_score >= 50, otherwise No |

## Notes

- `final_score` is what you'd predict in a regression task
- `passed` is what you'd predict in a classification task
- Scores are loosely based on study hours + attendance + previous performance (with some randomness thrown in)
