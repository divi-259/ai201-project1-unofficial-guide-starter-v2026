# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

I picked the default corpus - "campus_life", which has 88 documents in total. 
Each document has 4-5 lines talking about a topic related to campus life - courses, grading, library, transit etc.
We can ask the system the questions a student is likely to ask their peers or seniors in the campus.

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

## Chunking Strategy

- **Chunk size:** 1000 characters
- **Overlap:** 0

Chunks are built from paragraphs. When consecutive paragraphs fit together within the 1000-character limit, they are combined into a single chunk.

The effect differs across the corpus:

- **campus_life**: These documents are short and made up of small paragraphs, so each document typically becomes a single chunk.
- **city_guides**: These documents have long paragraphs, so each paragraph typically becomes its own chunk.

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `admin_add_drop_deadline.txt#0` — produced by: `chunker.py::split_documents`

```
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

**Chunk 2** — source: `course_biol_160.txt#0` — produced by: `chunker.py::split_documents`

```
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.
```

**Chunk 3** — source: `course_hist_118_workload.txt#0` — produced by: `chunker.py::split_documents`

```
Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 4** — source: `dining_pellew_dining_hall_followup.txt#0` — produced by: `chunker.py::split_documents`

```
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.
```

**Chunk 5** — source: `housing_innisfree_hall.txt#0` — produced by: `chunker.py::split_documents`

```
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
"What it is like to study abroad?"
**Answer:**

```
(best distance 0.538, cutoff 0.6)

Based on the provided documents, the single most misunderstood fact about the study abroad programme is that your financial aid package travels with you, which leads most students to mistakenly assume it does not and rule themselves out. Applications open in October for the following academic year.

Source: admin_study_abroad.txt

Sources retrieved: admin_graduation_requirements.txt, admin_study_abroad.txt, course_engl_205.txt, course_hist_118.txt, money_jobs.txt

1 model calls this session, 632 tokens (570 in, 62 out)
```

**My relevance cutoff:**

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

┌─────────────────────────────────────────────────────────────┬────────────┬───────────────┐
│                          Question                           │ In corpus? │ Best distance │
├─────────────────────────────────────────────────────────────┼────────────┼───────────────┤
│ How do I book a study room?                                 │ Yes        │ 0.337         │
├─────────────────────────────────────────────────────────────┼────────────┼───────────────┤
│ What is the assessment criteria for BIOL160?                │ Yes        │ 0.401         │
├─────────────────────────────────────────────────────────────┼────────────┼───────────────┤
│ What are the graduation requirements?                       │ Yes        │ 0.327         │
├─────────────────────────────────────────────────────────────┼────────────┼───────────────┤
│ What are the hours for the health center?                   │ Yes        │ 0.318         │
├─────────────────────────────────────────────────────────────┼────────────┼───────────────┤
│ What are the walking times across campus?                   │ Yes        │ 0.331         │
├─────────────────────────────────────────────────────────────┼────────────┼───────────────┤
│ What is the capital of Mongolia?                            │ No         │ 0.825         │
├─────────────────────────────────────────────────────────────┼────────────┼───────────────┤
│ How do I change the oil in a diesel engine?                 │ No         │ 0.934         │
├─────────────────────────────────────────────────────────────┼────────────┼───────────────┤
│ Who won the 1994 World Cup?                                 │ No         │ 0.886         │
├─────────────────────────────────────────────────────────────┼────────────┼───────────────┤
│ What is the recommended dosage of ibuprofen for a headache? │ No         │ 0.844         │
├─────────────────────────────────────────────────────────────┼────────────┼───────────────┤
│ How do I write a for loop in Rust?                          │ No         │ 0.896         │
└─────────────────────────────────────────────────────────────┴────────────┴─────────-------
In corpus questions have max best distance 0.4 and out of corpus questions have best distance greater than 0.8

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**
I asked claude to help me understand the chunking function, and suggest me a better alternative. It came up with a very complex structure-aware chunking algorithm. I am still very new to this and understanding things slowly, so I asked claude to suggest me a little better alternative to fixed chunking, it came up with paragraph level chunking by keeping chunk size to an upper limit. I was able to understand the code and make sense of it in all the corpus.

**2.**
I used claude to build structured table for the run_eval.py output. Also for the criteria.md - I ran my ideas through claude and asked to find out the issues in the current criteria. It helped me in identifyling that I should have a stronger why for each criteria.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 4 of 5 | 3 of 5 | 4 of 5 | MISS |
| 2. Every answer names a source | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 4. Chunks start and end on a sentence boundary | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 5. Every factual claim traces to a retrieved chunk | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

**Criterion 1 evidence**

```
Question: How do I book a study room?
Run 1 answer: "You can book a group study room through the library site up
to two weeks ahead in two-hour blocks, with a maximum of two blocks per
person per week (study_group_rooms.txt)."
expects: "two hour blocks" → not found (answer says "two-hour blocks") → fail
```

**Criterion 2 evidence** 

```
Question: What are the graduation requirements? — run 1
"Based on the provided documents, the graduation requirements are 120
credit hours, a completed major, general education requirements, and two
writing-intensive courses taken in different departments.

Source: admin_graduation_requirements.txt"
```

**Criterion 3 evidence** 

```
What is the capital of Mongolia? — best distance 0.825 — refused
How do I change the oil in a diesel engine? — best distance 0.934 — refused
```

**Criterion 4 evidence** 

```
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.
```

Chunk opens on the document's first line and closes on a period - no sentence is split.

**Criterion 5 evidence** 

```
Question: What are the walking times across campus? — run 1
Answer: "Aldridge Hall to the science quad: 4 minutes. Fenwick Court to
central campus: 18 minutes. Morrow House to Kestrel Commons: 7 minutes.
Library to Ridgeway Café: 3 minutes. Additionally, you should add four
minutes in winter because the path past the pond ices over."

transit_walking.txt: "Aldridge Hall to the science quad: 4 minutes. Fenwick
Court to central campus: 18 minutes. Morrow House to Kestrel Commons: 7
minutes. Library to Ridgeway Café: 3 minutes. Add four minutes in winter.
The path past the pond genuinely ices over..."

Every number and claim in the answer matches the source document — nothing
fabricated.
```

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MISS | Runs came out 4 of 5, 3 of 5, 4 of 5 — target is 4 of 5 every time, and Run 2 dropped below it, so the target doesn't hold. |
| 2 | Every answer names a source | MET | 5 of 5 in all three runs — all 15 generated answers (5 questions × 3 runs) named at least one source file. |
| 3 | Gate stops out-of-corpus questions | MET | 5 of 5, deterministic — the gate refused every out-of-scope question, above the 4 of 5 target with no run-to-run variation to worry about. |
| 4 | Chunks start and end on a sentence boundary | MET | 5 of 5 sampled chunks open on a heading and close on a period, verified against the source documents in `corpora/campus_life/documents/` — deterministic since chunking doesn't change between runs. |
| 5 | Every factual claim traces to a retrieved chunk | MET | 5 of 5 in all three runs — every claim in each answer matched text found verbatim in its cited source document. |


## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->
**Criterion 1 — Retrieved chunk contains the answer (MISS: 4 of 5, 3 of 5, 4 of 5)**

Both failing questions trace to the same mechanism, and it isn't any of the five pipeline stages — loading, chunking, embedding, retrieval, and generation all did their job correctly in every run.

- *How do I book a study room?* fails in all 3 runs. The answer consistently says "two-hour blocks" (hyphenated); `questions.py` expects "two hour blocks" (no hyphen). The right chunk was retrieved from `study_group_rooms.txt` and the answer is factually correct — the model just doesn't spell it the way the judge is looking for.
- *What are the hours for the health center?* fails only in Run 2, where the answer says "8:00 am to 11:00 am" instead of "8am to 11am." Same content, different formatting, and again `scorer.py::judge`'s exact substring match doesn't tolerate it.

So the miss is in the eval harness, not the RAG pipeline: `judge()` does a literal substring check, and it breaks whenever the model paraphrases a number or unit in a way that's still correct. Run 2 dips to 3 of 5 instead of Run 1/3's 4 of 5 simply because the model happened to reformat two things instead of one that time, a scoring artifact, not a worse run.

## The Improvement

Better Judge function for better eval harness.
**What I changed:**

`scorer.py::judge` still checks for an exact substring match first, but if that fails it now falls back to `rapidfuzz`'s `partial_ratio`, scoring the best alignment of `expects` against any window of `answer` and passing if that score is 85 or above.

**Why I picked it:**

Both Criterion 1 misses were the model giving a factually correct answer in a differently formatted way ("two-hour blocks" vs "two hour blocks", "8:00 am" vs "8am") — fuzzy matching tolerates exactly that kind of formatting drift without loosening the check enough to pass a wrong answer.

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 4 of 5 | 5 of 5 | 5 of 5 | MET |
| 2. Every answer names a source | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 4. Chunks start and end on a sentence boundary | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 5. Every factual claim traces to a retrieved chunk | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |

Source: `results/run_2026-09-24_2213.md`, produced by `run_eval.py::main`. Criterion 1 comes straight from the run's pass/fail column (`scorer.py::judge`); criterion 3 from the out-of-scope gate table (5 of 5 refused, deterministic, same number in all three columns per the Unit 1 convention); criteria 2, 4, and 5 aren't scored by the script, so they're my read of the 15 generated answers in that file — every answer cites a source file, chunking is unchanged from Unit 1 so chunk boundaries are unaffected, and every factual claim matches its cited source document verbatim or in substance.

**Did it help?**

Yes. Criterion 1 was a repeatable MISS before (4, 3, 4 of 5) because `judge()` did an exact substring match and the model's paraphrasing of numbers/units ("two-hour" vs "two hour", "8:00 am" vs "8am") never matched literally. After adding the `rapidfuzz` fallback, it's now 4, 5, 5 of 5 — a consistent MET. Run 1 still has one fail: the health center answer said "8:00 am to 11:00 am" against an expected "8am to 11am," and the colons/padding pushed `partial_ratio` just under the 85 threshold. So the fix closed most of the gap but not all of it.

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
