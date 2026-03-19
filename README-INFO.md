# PDF Merger (PDF + Images → Single PDF)

## 1. Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 2. Usage

### Required Files

* `merge.py`
* `cv.pdf` (can have any number of pages)
* Images:

  * `transcript.jpg`
  * `ielts.jpg`

> You can add more PDFs or images later by editing the lists inside `merge.py`.

---

### Run Script

```bash
py merge.py
```

---

### Output

* `portfolio.pdf`
* Contains:

  1. All pages from `cv.pdf`
  2. Followed by each image as separate pages

---
