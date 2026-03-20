# BEC vs LMS Schema Comparison

> Generated: 2026-03-18
> BEC repo: `bitcoin-educational-content` (JSON Schema + bec validate)
> LMS repo: `bitcoin-learning-management-system` (Drizzle ORM + Zod + tRPC)

## Executive Summary

The BEC content repo defines **14 content types** via JSON Schema Draft 7, validated by `bec validate`. The LMS app defines **24+ database tables** via Drizzle ORM with Zod runtime validation. While both repos cover the same core content types, there are **systematic mismatches** in required/optional field handling that could cause data integrity issues.

### Key Patterns

| Pattern | Count | Severity |
|---------|-------|----------|
| BEC requires, LMS nullable | **38** | High |
| BEC optional, LMS required | **5** | Medium |
| BEC field missing in LMS | **12** | Medium |
| LMS field missing in BEC | **~50+** | Expected (app-specific) |
| Structural differences (tags, proofreading, contributors) | **3 systemic** | Architectural |

### Systemic Architectural Differences

These affect **every content type** and are by design, not bugs:

1. **Tags**: BEC stores tags inline as arrays; LMS uses junction tables (`course_tags`, `tutorial_tags`, `resource_tags`). Both enforce the same 51-tag vocabulary. **No action needed.**
2. **Proofreading**: BEC embeds proofreading metadata in each content YAML (required for most types); LMS has a dedicated `content.proofreading` workflow table. **No action needed** (sync logic should handle the mapping).
3. **Sync metadata**: LMS adds `lastCommit`, `lastUpdated`, `lastSync`, `path`, `isArchived` to every content type. These are app-managed, not content-authored. **Expected.**
4. **Contributors**: BEC requires `contributor_names` (GitHub usernames) on many types; LMS generally handles contributors through a separate `proofreading_contributor` table or omits the field entirely. **Potential data loss during sync.**

---

## Per-Content-Type Comparison

### 1. COURSE

| Field | BEC | LMS | Mismatch |
|-------|-----|-----|----------|
| `id` | Required (UUID) | Required (varchar) | Type differs: UUID vs varchar(100) |
| `topic` | Required (enum, 8 values) | Required (text) | LMS has no enum constraint |
| `subtopic` | Required (enum, 30+ values) | Required (text) | LMS has no enum constraint |
| `level` | Required (enum: beginner/intermediate/advanced/expert/wizard) | Required (enum: Beginner/Intermediate/Advanced) | **LMS missing: expert, wizard** |
| `hours` | Required (integer, min 1) | Required (double) | Type: integer vs double |
| `professors_id` | Required (UUID array, min 1) | Not on course table | **Missing in LMS table** (likely junction table) |
| `original_language` | Required | Optional (default 'en') | **BEC required, LMS defaulted** |
| `tags` | Required (min 1) | Junction table | Structural |
| `proofreading` | Required (min 1) | Separate table | Structural |
| `name` (content) | Required (1-200 chars) | Required (localized) | Aligned |
| `goal` (content) | Required | Required (localized) | Aligned |
| `objectives` (content) | Required (1-10 items) | Required (text[], localized) | LMS has no max constraint |
| `type` | Optional (theory/practice) | Optional (Theory/Practice) | Aligned |
| `teaching_format` | Optional | Optional | Aligned |
| `format` | Optional (online/inperson/hybrid) | Optional (Online/InPerson) | **LMS missing: hybrid** |
| `published_at` | Optional | Optional (nullable) | Aligned |
| `project_id` | Optional | Optional (nullable) | Aligned |
| `license` | Optional (CC-BY-SA-V4/MIT) | Not in LMS | **Missing in LMS** |
| `videos` | Optional (complex object) | Separate `videos` table | Structural |

**LMS-only fields**: `index`, `contact`, `isArchived`, `isPlanbSchool`, `hasAssignment`, `assignmentWeight`, `assignmentStartDate`, `assignmentEndDate`, `assignmentDescription`, `passingGradeThreshold`, `areScoresCalculated`, `isAssignmentGradingPublished`, `hasLogo`, `presentationMarkdown`, `paidVideoLink`, `onlinePriceDollars`, `numberOfRating`, `sumOfAllRating`, `remainingSeats`

---

### 2. TUTORIAL

| Field | BEC | LMS | Mismatch |
|-------|-----|-----|----------|
| `id` | Required (UUID) | Required (UUID) | Aligned |
| `level` | Required (enum) | Required | Aligned |
| `category` | Required (enum, 20 values) | Required | LMS has no enum constraint |
| `professor_id` | **Required** (UUID) | **Nullable** | **BEC required, LMS optional** |
| `license` | **Required** (enum) | **Not in LMS** | **Missing in LMS** |
| `original_language` | **Required** | Optional (default 'en') | **BEC required, LMS defaulted** |
| `proofreading` | Required (min 1) | Separate table | Structural |
| `project_id` | Optional | Optional (nullable) | Aligned |
| `tags` | Optional | Junction table | Structural |
| `credit_link` | Optional (URI) | Optional (nullable) | Aligned |
| `name` (content) | Required (1-200 chars) | Required (varchar 255) | Aligned |
| `description` (content) | Required (max 1000) | **Nullable** | **BEC required, LMS optional** |

**LMS-only fields**: `subcategory`, `isArchived`, `logoUrl`, `lastUpdateContent`

---

### 3. PROFESSOR

| Field | BEC | LMS | Mismatch |
|-------|-----|-----|----------|
| `id` | Required (UUID) | Required (UUID) | Aligned |
| `name` | Required | Required (unique) | Aligned |
| `bio` (content) | **Required** | **Nullable** | **BEC required, LMS optional** |
| `short_bio` (content) | **Required** | **Nullable** | **BEC required, LMS optional** |
| `links.twitter` | Optional | Optional (nullable) | Aligned |
| `links.website` | Optional | Optional (nullable) | Aligned |
| `company` | Optional | Optional (nullable) | Aligned |
| `affiliations` | Optional (string[]) | Optional (uuid[]) | **Type: string[] vs uuid[]** |
| `tips.lightning_address` | Optional | Optional (nullable) | Aligned |
| `tips.silent_payment` | Optional | Optional (nullable) | Aligned |
| `tags` | Optional | Junction table | Structural |

**LMS-only fields**: `githubUrl`, `linkedinUrl`, `nostr`, `lnurlPay`, `paynym`, `tipsUrl`

---

### 4. EVENT

| Field | BEC | LMS | Mismatch |
|-------|-----|-----|----------|
| `id` | Required (UUID) | Required (UUID) | Aligned |
| `start_date` | Required (datetime) | Required (timestamp) | Aligned |
| `end_date` | Required (datetime) | Required (timestamp) | Aligned |
| `name` | **Required** | **Nullable** | **BEC required, LMS optional** |
| `type` | **Required** (enum: 5 types) | **Nullable** | **BEC required, LMS optional** |
| `description` | **Required** | **Nullable** | **BEC required, LMS optional** |
| `timezone` | **Required** (IANA) | **Nullable** | **BEC required, LMS optional** |
| `address_city_country` | **Required** | **No direct field** (uses addressLine1-3, all nullable) | **BEC required, LMS missing** |
| `language` | **Required** (array, min 1) | Junction table (`event_languages`) | Structural |
| `links.website` | Optional | Optional (nullable) | Aligned |
| `tags` | Required (min 1) | Junction table | Structural |
| `available_seats` | Optional | Optional (nullable) | Aligned |
| `book_online` | Optional | Optional (default false) | Aligned |
| `book_in_person` | Optional | Optional (default false) | Aligned |
| `price_dollars` | Optional | Optional (nullable) | Aligned |
| `project_id` | Optional | Optional (nullable) | Aligned |

**LMS-only fields**: `rawDescription`, `courseRelated`, `professor`, `liveUrl`, `chatUrl`, `replayUrl`, `assetUrl`, `remainingSeats`

---

### 5. QUIZ

| Field | BEC | LMS | Mismatch |
|-------|-----|-----|----------|
| `chapterId` | Required | Required | Aligned |
| `difficulty` | Required (easy/intermediate/hard/expert) | Required | LMS uses Easy/Medium/Hard (different enum values) |
| `author` | **Required** | **Nullable** | **BEC required, LMS optional** |
| `tags` | **Required** (min 1) | **Not in LMS** | **Missing in LMS** |
| `question` | Required | Required | Aligned |
| `answer` | Required | Required | Aligned |
| `wrong_answers` | **Required (exactly 3)** | Required (text[], **no count constraint**) | **BEC enforces count, LMS doesn't** |
| `explanation` | **Required** | **Nullable** | **BEC required, LMS optional** |
| `reviewed` | **Required** (boolean) | **Not in LMS** | **Missing in LMS** |

**LMS-only fields**: `duration`, `disabled`, `courseId` (FK)

---

### 6. BOOK

| Field | BEC | LMS | Mismatch |
|-------|-----|-----|----------|
| `author` | Required | Required | Aligned |
| `level` | **Required** (enum) | **Nullable** | **BEC required, LMS optional** |
| `tags` | Required (min 1) | Junction table | Structural |
| `title` (content) | Required | Required | Aligned |
| `publication_year` (content) | **Required** (integer) | **Nullable** | **BEC required, LMS optional** |
| `cover` (content) | **Required** | **Nullable** | **BEC required, LMS optional** |
| `description` (content) | **Required** | **Nullable** | **BEC required, LMS optional** |
| `original` (content) | Required (boolean) | Required (boolean) | Aligned |
| `contributors` (content) | **Required** (UUID[], min 1) | **Not in LMS** | **Missing in LMS** |
| `original_language` | Optional | Optional (default 'en') | Aligned |
| `license` | Optional | Not in LMS | Missing in LMS |

**LMS-only fields**: `publisher`, `shopUrl`, `downloadUrl`, `translator`, `summaryText`, `summaryContributorId`

---

### 7. CHANNEL (YouTube Channel)

| Field | BEC | LMS | Mismatch |
|-------|-----|-----|----------|
| `id` | Required (UUID) | Required (UUID) | Aligned |
| `name` | Required | Required | Aligned |
| `language` | Required | Required | Aligned |
| `links.channel` | Required (URI) | Required (`channel`) | Aligned |
| `description` | **Required** | **Nullable** | **BEC required, LMS optional** |
| `links.trailer` | **Optional** | **Required** | **Reversed: BEC optional, LMS required** |
| `license` | **Required** | **Not in LMS** | **Missing in LMS** |
| `contributor_names` OR `contributors` | **Required** (oneOf) | **Not in LMS** | **Missing in LMS** |
| `tags` | Required (min 1) | Junction table | Structural |
| `project_id` | Optional | Optional (nullable) | Aligned |

---

### 8. CONFERENCE

| Field | BEC | LMS | Mismatch |
|-------|-----|-----|----------|
| `name` | Required | Required | Aligned |
| `year` | Required (YYYY-MM) | Required (text) | LMS has no format constraint |
| `location` | Required | Required | Aligned |
| `builder` | **Required** | **Not in LMS** | **Missing in LMS** |
| `language` | **Required** (array, min 1) | **Nullable** (`languages`) | **BEC required, LMS optional** |
| `links.website` | **Required** | **Nullable** (`websiteUrl`) | **BEC required, LMS optional** |
| `links.twitter` | Optional | Optional (nullable) | Aligned |
| `tags` | Required (min 1) | Junction table | Structural |

**LMS-only fields**: `description`, `projectId`, conference stages + videos

---

### 9. GLOSSARY WORD

| Field | BEC | LMS | Mismatch |
|-------|-----|-----|----------|
| `id` | Required (UUID) | Required (FK) | Aligned |
| `en_word` | **Required** | **No direct equivalent** (uses `fileName`) | **Mapping unclear** |
| `original_language` | Required | Optional (default 'en') | **BEC required, LMS defaulted** |
| `license` | **Required** | **Not in LMS** | **Missing in LMS** |
| `term` (content) | Required (UPPERCASE pattern) | Required (`term`, no pattern) | **LMS missing pattern constraint** |
| `definition` (content) | Required (markdown) | Required | Aligned |
| `related_words` | Optional | Optional (nullable) | Aligned |
| `tags` | Optional | Junction table | Structural |

**LMS-only fields**: `shortDefinition`

---

### 10. MOVIE

| Field | BEC | LMS | Mismatch |
|-------|-----|-----|----------|
| `id` | Required (UUID) | Required (UUID) | Aligned |
| `title` | Required | Required | Aligned |
| `author` | Required | Required | Aligned |
| `language` | Required | Required | Aligned |
| `links.platform` | Required (URI) | Required (`platform`) | Aligned |
| `publication_year` | **Required** (1900-2100) | **Nullable** | **BEC required, LMS optional** |
| `duration` | **Required** (min 1) | **Nullable** | **BEC required, LMS optional** |
| `description` | **Required** | **Nullable** | **BEC required, LMS optional** |
| `links.trailer` | **Optional** | **Required** | **Reversed: BEC optional, LMS required** |
| `contributor_names` | **Required** (min 1) | **Not in LMS** | **Missing in LMS** |
| `license` | **Required** | **Not in LMS** | **Missing in LMS** |
| `tags` | Required (min 1) | Junction table | Structural |

---

### 11. NEWSLETTER

| Field | BEC | LMS | Mismatch |
|-------|-----|-----|----------|
| `id` | Required (UUID) | Required (FK) | Aligned |
| `title`/`name` | Required (`title`) | Required (`name`) | **Field name differs** |
| `author` | Required | Required | Aligned |
| `language` | Required | Required | Aligned |
| `level` | **Required** (enum) | **Not in LMS** | **Missing in LMS** |
| `publication_date` | **Required** (YYYY-MM-DD) | **Not in LMS** | **Missing in LMS** |
| `link` | **Required** (array, min 1) | **Nullable** (`websiteUrl`) | **BEC required, LMS optional** |
| `description` | **Required** | **Nullable** | **BEC required, LMS optional** |
| `contributor_names` | **Required** (min 1) | **Nullable** (`contributors`) | **BEC required, LMS optional** |
| `license` | **Required** | **Not in LMS** | **Missing in LMS** |
| `tags` | Required (min 1) | Junction table | Structural |
| `project_id` | Optional | Not in LMS | Missing |

---

### 12. PODCAST

| Field | BEC | LMS | Mismatch |
|-------|-----|-----|----------|
| `id` | Required (UUID) | Required (FK) | Aligned |
| `name` | Required | Required | Aligned |
| `host` | Required | Required | Aligned |
| `language` | Required | Required | Aligned |
| `links.podcast` | Required | Required (`podcastUrl`) | Aligned |
| `description` | **Required** | **Nullable** | **BEC required, LMS optional** |
| `contributor_names` | **Required** (min 1) | **Not in LMS** | **Missing in LMS** |
| `license` | **Required** | **Not in LMS** | **Missing in LMS** |
| `tags` | Required (min 1) | Junction table | Structural |
| `links.twitter` | Optional | Optional (nullable) | Aligned |
| `links.website` | Optional | Optional (nullable) | Aligned |

**LMS-only fields**: `nostr`

---

### 13. PAPER (Research Paper)

| Field | BEC | LMS | Mismatch |
|-------|-----|-----|----------|
| `id` | Required (UUID) | Required (UUID) | Aligned |
| `title` | Required (min 1) | Required | Aligned |
| `authors` | Required (array, min 1) | Required (text[]) | Aligned |
| `abstract` | Required (min 10 chars) | Required | LMS has no min constraint |
| `original_language` | Required | Required (`language`) | Aligned |
| `paper_type` | Required (enum, 7 values) | Required (`type`, text) | **LMS has no enum constraint** |
| `pdf_url` | Required (URI) | Required (`paperUrl`) | **Field name differs** |
| `topics` | **Required** (array, min 1) | **Nullable** | **BEC required, LMS optional** |
| `source` | **Optional** | **Required** | **Reversed: BEC optional, LMS required** |
| `publication_date` | Optional | Optional (nullable) | Aligned |
| `type` (SCI/SCIE/SSCI) | Optional (enum) | Not in LMS | Missing |
| `category` | Optional | Not in LMS | Missing |
| N/A | N/A | Required (`bibUrl`) | **LMS requires field not in BEC** |

---

### 14. PROJECT

| Field | BEC | LMS | Mismatch |
|-------|-----|-----|----------|
| `id` | Required (UUID) | Required (UUID) | Aligned |
| `name` | Required | Required | Aligned |
| `category` | Required (enum, 15 values) | Required (varchar) | LMS has no enum constraint |
| `links` | **Required** (object) | All URL fields nullable | **BEC requires links object, LMS all nullable** |
| `original_language` | **Required** | Optional (default 'en') | **BEC required, LMS defaulted** |
| `tags` | Required (min 1) | Junction table | Structural |
| `proofreading` | Required (min 1) | Separate table | Structural |
| `licence` | Optional | Not in LMS | Missing |
| `contributor_names` | Optional | Not in LMS | Missing |
| Addresses | Optional | Optional (all nullable) | Aligned |

---

### 15. BET (Bitcoin Education Template)

| Field | BEC | LMS | Mismatch |
|-------|-----|-----|----------|
| `id` | Required (UUID) | Required (FK) | Aligned |
| `type` | Required (enum) | Required (enum) | Aligned |
| `original_language` | Required | Optional (default 'en') | **BEC required, LMS defaulted** |
| `contributor_names` | **Required** (min 1) | **Not in LMS** | **Missing in LMS** |
| `license` | **Required** | **Not in LMS** | **Missing in LMS** |
| `tags` | Required (min 1) | Junction table | Structural |
| `proofreading` | Required (min 1) | Separate table | Structural |
| `links.download` | **Optional** | **Required** (`downloadUrl`) | **Reversed: BEC optional, LMS required** |
| `project_id` | Optional | Optional (nullable) | Aligned |
| `name` (content) | Required | Required (localized) | Aligned |
| `description` (content) | Required | Required (localized) | Aligned |

---

## LMS-Only Content Types (no BEC equivalent)

| Type | Purpose |
|------|---------|
| **Lab** | Interactive sessions with professor, sessions, student count |
| **Educator Content** | User-generated content with status workflow (Draft/Published) |
| **B-Certificate** | Exam certification with scores and timestamps |
| **Coupon** | Commerce: discount codes for courses/events |
| **Blog** | Blog posts with localized content |
| **Calendar** | Date-based events with localized titles |
| **Legal Documents** | Legal pages (ToS, Privacy) with localized content |
| **Translation Workflow** | Course translation tracking (Todo/InProgress/Done) |

---

## Summary of All Mismatches

### BEC Required, LMS Nullable/Optional (HIGH PRIORITY)

These fields pass `bec validate` but could be NULL in the LMS database:

| Content Type | Field | Risk |
|-------------|-------|------|
| Tutorial | `professor_id` | Tutorials shown without author |
| Tutorial | `description` (content) | Missing descriptions in UI |
| Professor | `bio` (content) | Empty professor profiles |
| Professor | `short_bio` (content) | Empty professor cards |
| Event | `name` | Unnamed events in UI |
| Event | `type` | Uncategorized events |
| Event | `description` | Empty event pages |
| Event | `timezone` | Time display issues |
| Event | `address_city_country` | No location shown |
| Quiz | `author` | Unattributed questions |
| Quiz | `explanation` | No explanations after quiz |
| Book | `level` | No difficulty indicator |
| Book | `publication_year` | Missing metadata |
| Book | `cover` | No cover image |
| Book | `description` | Empty book pages |
| Channel | `description` | Empty channel pages |
| Conference | `language` | No language filter |
| Conference | `links.website` | No website link |
| Movie | `publication_year` | Missing metadata |
| Movie | `duration` | No duration shown |
| Movie | `description` | Empty movie pages |
| Newsletter | `level` | No difficulty indicator |
| Newsletter | `publication_date` | No date shown |
| Newsletter | `link` | No link to newsletter |
| Newsletter | `description` | Empty descriptions |
| Newsletter | `contributor_names` | No attribution |
| Podcast | `description` | Empty podcast pages |
| Paper | `topics` | No topic categorization |
| Glossary | `en_word` | No English reference key |

### BEC Optional, LMS Required (MEDIUM PRIORITY)

These fields could be missing in BEC content but LMS expects them:

| Content Type | Field | Risk |
|-------------|-------|------|
| Channel | `trailer` | Sync fails if no trailer in BEC |
| Movie | `trailer` | Sync fails if no trailer in BEC |
| Paper | `source` | Sync fails if no source in BEC |
| Paper | `bibUrl` | Field doesn't exist in BEC at all |
| BET | `downloadUrl` | Sync fails if no download link in BEC |

### Missing in LMS (Fields BEC validates but LMS doesn't store)

| Field | Affected Types | Impact |
|-------|---------------|--------|
| `license` | Tutorial, Channel, Glossary, Movie, Newsletter, Podcast, BET | License info lost |
| `contributor_names` | Channel, Movie, Newsletter, Podcast, BET | Attribution lost |
| `reviewed` (quiz) | Quiz | Review status lost |
| `builder` | Conference | Organizer info lost |
| `en_word` | Glossary | English reference key unclear |
| `level` | Newsletter | Difficulty not stored |
| `publication_date` | Newsletter | Pub date not stored |
| `tags` (quiz) | Quiz | Quiz categorization lost |

### Enum Value Mismatches

| Content Type | Field | BEC Values | LMS Values | Missing in LMS |
|-------------|-------|-----------|------------|----------------|
| Course | `level` | beginner, intermediate, advanced, expert, wizard | Beginner, Intermediate, Advanced | **expert, wizard** |
| Course | `format` | online, inperson, hybrid | Online, InPerson | **hybrid** |
| Quiz | `difficulty` | easy, intermediate, hard, expert | Easy, Medium, Hard | **intermediate->Medium rename, expert missing** |

---

## Recommendations

### P0 - Data Integrity

1. **Add NOT NULL constraints in LMS** for fields that BEC requires: `event.name`, `event.type`, `event.description`, `tutorial.professorId`, `professor bio/short_bio`, `quiz.explanation`
2. **Add enum constraints in LMS** for `topic`, `subtopic`, `category` fields that BEC validates against fixed vocabularies
3. **Add `expert` and `wizard` to LMS course level enum** to match BEC
4. **Add `hybrid` to LMS course format enum** to match BEC

### P1 - Feature Parity

5. **Add `license` column** to tutorial, channel, glossary, movie, newsletter, podcast, and BET tables (or a shared resource field)
6. **Add `contributor_names` column** or junction table for channel, movie, newsletter, podcast, BET
7. **Add `reviewed` boolean to quiz** questions
8. **Add `builder` to conference** table
9. **Add `level` and `publication_date` to newsletter** table

### P2 - Sync Safety

10. **Make LMS `trailer` nullable** on channel and movie (BEC has it optional)
11. **Make LMS `source` nullable** on research papers (BEC has it optional)
12. **Make LMS `bibUrl` nullable** on research papers (BEC doesn't have this field)
13. **Make LMS `downloadUrl` nullable** on BET (BEC has it optional)
14. **Review sync logic** for graceful handling of these mismatches

### P3 - Constraint Alignment

15. **Add pattern validation** in LMS Zod schemas for glossary terms (uppercase pattern)
16. **Add count validation** for quiz `wrong_answers` (exactly 3)
17. **Add min/max constraints** matching BEC schemas (e.g., abstract min 10 chars, publication_year 1900-2100)
