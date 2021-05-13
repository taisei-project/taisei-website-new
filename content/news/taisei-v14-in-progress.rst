Taisei v1.4 Progress
####################
:date: 2021-05-13 14:30
:author: Taisei team
:slug: taisei-v14-progress-report

Unless you've been closely following Taisei on our Discord or GitHub, it may seem like Taisei is mostly "finished" (or perhaps "abandoned") from a development perspective. But nothing could be further from the truth.

While we've recently put out a new maintenance release of v1.3.2 which strictly covered some critical bugs that were reported, we've been busy at work for the past year and a half to bring you v1.4. Here's some of the new features we're planning for this upcoming version, which we're hoping to release by the end of the year:

* A **rewritten coroutines engine called `koishi`** which greatly enhances the ability to write and script the behaviour of player shots, enemy movement, danmaku patterns, and background rendering. With this, we have rewritten:

  - All 6 stages from the ground up.
  - All character shots.
  - All enemy movements and behaviours.
  - The dialogue system.

* A **new story and script**, including:

  - New story concept written by Alice D.
  - An Extra stage boss concept, with music composed by Jneen Collective.
  - New cutscenes and character art drawn by Afensorm.
  - New background models for stage 3, 4, 5, and 6 by Akari and laochailan.
  - New and improved fairy sprites by Akari.

* Many, many **small bugs and annoyances fixed**, including things like sluggish movement on MarisaA's lasers.
* New **automatic testing builds, releases, and publishing** through GitHub Actions for all supported platforms.
* Alpha support for Apple Silicon (M1).

Here's what's remaining until we feel like v1.4 would be ready to go:

* Finishing some boss logic remastering for stages 3, 4, 6.
* Completing the new Extra stage.
* Fixing up some remaining internals (such as the Boss Attack code) so they make more sense.
* Balancing the difficulty curve.
* Lots and lots of QA.

As the old saying goes, "it'll be ready when it's done," but at our current pace, we're pretty optimistic we'll have a beta out sometime mid-fall.

