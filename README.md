# 🏆 THE MOSTLY AI PRIZE 🏆

The official repository for the MOSTLY AI PRIZE, a 2x $50,000 synthetic data competition running from May until July 2025.

| Challenge                   | Dataset Details                                                                                          | Stage 1                                                                                                   | Stage 2                                                                                                   |
|----------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| **The FLAT DATA Challenge** | - 100,000 records<br> - 80 data columns<br> - 60 numeric, 20 categorical                                        | - [Training Data](flat/stage1/flat-training.csv.gz)<br> - [Holdout Data](flat/stage1/flat-holdout.csv.gz)<br>.             | - [Training Data](flat/stage2/flat-training.csv.gz)<br> - [Holdout Data](flat/stage2/flat-holdout.csv.gz)<br> - [Evaluation Runs](flat/stage2/submissions/)  |
| **The SEQUENTIAL DATA Challenge** | - 20,000 groups, 5–10 records each<br> - 10 data columns<br> - 7 numeric, 3 categorical                        | - [Training Data](sequential/stage1/sequential-training.csv.gz)<br> - [Holdout Data](sequential/stage1/sequential-holdout.csv.gz)<br>. | - [Training Data](sequential/stage2/sequential-training.csv.gz)<br> - [Holdout Data](sequential/stage2/sequential-holdout.csv.gz)<br> - [Evaluation Runs](sequential/stage2/submissions/)              |

## Stage 1

During stage 1 anyone with a GitHub account was invited to participate. All submissions were automatically evaluated via the [Synthetic Data Quality Assurance](https://github.com/mostly-ai/mostlyai-qa) toolkit. All results can be found here: [stage1-results.csv](./stage1-results.csv).

| FLAT                   |  SEQUENTIAL    |
|------------------------|----------------|
| ![Stage 1 Flat Leaderboard](./stage1-flat.png) | ![Stage 1 Sequential Leaderboard](./stage1-sequential.png) |

## Stage 2

During stage 2 the top 5 leaders of stage 1 were invited to submit their code submissions, which were then evaluated on a slightly modified version of the stage 1 datasets.

With the support of a fantastic jury board of renowned synthetic data experts (@suhaskowshik @adivekar-utexas @shree-gade @mplatzer @scriminaci @psitronic), these code submissions were then run on dedicated GPU instances a total of 6 times each. The generated synthetic data was captured, and then again evaluated with the same metrics as for Stage 1.

| FLAT                   |  SEQUENTIAL    |
|------------------------|----------------|
| ![Stage 2 Flat](./stage2-flat.png) | ![Stage 2 Sequential](./stage2-sequential.png) |

And these were the corresponding open-sourced code submissions:

- FLAT Challenge
  1. [Gandagorn / mostlyai_flat](https://github.com/Gandagorn/mostlyai_flat)
  2. [Tecnarca / mostlyai-engine-prize](https://github.com/Tecnarca/mostlyai-engine-prize)
  3. [muellermarkus / mostly_ai_prize](https://github.com/muellermarkus/mostly_ai_prize)
  4. [EugenioTL / mostlyai-engine-custom](https://github.com/EugenioTL/mostlyai-engine-custom)
  5. [Benels / MostlyAI-challenge-submission-Benels](https://github.com/Benels/MostlyAI-challenge-submission-Benels)

- SEQUENTIAL Challenge
  1. [Gandagorn / mostlyai_seq](https://github.com/Gandagorn/mostlyai_seq)
  2. [Benels / MostlyAI-challenge-submission-Benels](https://github.com/Benels/MostlyAI-challenge-submission-Benels)
  3. [EugenioTL / mostlyai-engine-custom](https://github.com/EugenioTL/mostlyai-engine-custom)
  4. [Tecnarca / mostlyai-engine-prize](https://github.com/Tecnarca/mostlyai-engine-prize)
  5. [filomba01 / mostly-ai-competition](https://github.com/filomba01/mostly-ai-competition)
