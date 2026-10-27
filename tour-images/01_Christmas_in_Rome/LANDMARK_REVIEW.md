# Christmas in Rome — landmark review

Every image was checked at full resolution against how each landmark is actually built and laid out. Reference photos still can't be downloaded (outbound HTTPS to Wikimedia/Vatican is blocked in this environment), so the findings below rely on architectural knowledge. Most are geometric and can be checked against any photo of the site.

The earlier QA pass said most images "require verified photo comparison" but didn't name what was wrong. This review names each defect, rates it, and gives a corrected prompt for every image that needs regenerating.

## Verdict summary

| Image | Verdict | Main issue |
|---|---|---|
| Banner | **Fix** | Dome shown in full above the facade; tree stands apart from the obelisk |
| Day 1 — coach departure | **Fix** (was marked *passed*) | Steering wheel on the right but boarding door also on the right: no real coach is built this way |
| Day 2 — St Peter's at night | Usable with caution | Full dome visible from inside the square |
| Day 3 — Christmas Day | **Fix** | Garbled fake-Latin facade and obelisk inscriptions; full dome visible |
| Day 4 — Pompeii forum | Usable | Correct orientation (Temple of Jupiter, Vesuvius behind) |
| Day 5 — Florence Duomo | **Fix** | Brunelleschi's dome placed beside the facade instead of behind it |
| Day 6 — arrival home | Usable | Generic, no landmarks |
| Highlight — St Peter's | Usable | Correct: tree beside the obelisk, colonnade from the inside |
| Highlight — Naples | Usable | Castel dell'Ovo with Vesuvius behind, Somma ridge on the correct side |
| Highlight — Pompeii | Usable | Generic street with stepping stones; no specific site claimed |
| Highlight — Capri | **Fix** | Faraglioni proportions and arch wrong; Stella shown detached from the island |
| Highlight — Sorrento | Usable | Generic marina below tufa cliffs; matches the Marina Grande character |
| Highlight — Florence | Usable with caution | Ponte Vecchio is broadly right; check the corridor windows against a photo |

**Usable now: 6 of 13. Usable after a quick check against a photo: 2 (Day 2, Florence highlight). Needs regeneration: 5.**

"Usable" means no visible factual defect was found. It is not legal or brand approval. All images remain AI illustrations, and the website should label them as such.

## Defects in detail

### Banner — `banner/Rome_Banner.png`
- **Dome over-exposed (major).** St Peter's has a long nave that Maderno added in front of Michelangelo's dome, so from ground level in the square the facade hides the drum and most of the dome. Only the upper dome and lantern show. Here the full drum and two side cupolas sit directly on top of the attic, which is the view from far down Via della Conciliazione, not from inside the square.
- **Tree placement (minor).** The Vatican Christmas tree stands next to the obelisk, with the nativity scene nearby. Here it stands alone near the south colonnade.
- Clocks at both attic corners and the Apostolic Palace on the right (north) are correct.

### Day 1 — `daily/Rome_Day01.png` (previously marked *passed*)
- **Impossible vehicle layout (major).** The passenger door is on the right, as on continental European coaches, but the steering wheel is also behind the right half of the windscreen. Continental coaches are driven from the left, and UK coaches have the door on the left. Anyone who rides coaches will notice, and service members stationed in Europe board them regularly.
- The double "rabbit-ear" mirrors are fine; they're standard on touring coaches.

### Day 2 — `daily/Rome_Day02.png`
- **Dome over-exposed (moderate).** Same issue as the banner, though less obvious at night.
- The tree and nativity beside the obelisk, the Apostolic Palace on the right and the colonnade on the left are all consistent with a viewpoint under the south colonnade.

### Day 3 — `daily/Rome_Day03.png`
- **Garbled inscriptions (major, an obvious AI tell).** The frieze reads `IN HONOREM PRINCIPIS APOST AEYLLS.CROMANVSPONT MAX K EOSN MAXAXAMA EKT KOTVH HA`. The real inscription is `IN HONOREM PRINCIPIS APOST PAVLVS V BVRGHESIVS ROMANVS PONT MAX AN MDCXII PONT VII`. The obelisk base also shows nonsense lettering. Regenerating with "inscription illegible / softly out of focus" is safer than asking the model to spell Latin.
- **Dome over-exposed (major at this distance).** From beside the obelisk you mostly see the facade. Here the dome appears complete, with its drum above the attic.
- The red drape on the central Loggia of Blessings is a good, accurate Christmas detail. Keep it.

### Day 4 — `daily/Rome_Day04.png`
- Orientation is correct: the forum looks north to the Temple of Jupiter on its podium, flanked by arches, with Vesuvius behind it and Monte Somma to the right.
- The banded brick-and-stucco columns in the left foreground are closer to the Basilica's columns than to the forum portico. A specialist might notice, but it's acceptable as illustration.

### Day 5 — `daily/Rome_Day05.png`
- **Dome in the wrong place (critical).** Santa Maria del Fiore's facade faces west, and the dome rises directly *behind* it on the same axis. Seen from the piazza, the dome should crown the facade, with Giotto's campanile at the right-hand (south) corner. Here the dome stands to the left of the facade, with a side elevation running toward the viewer, which is impossible from a frontal facade view.
- The striped building at the right edge reads as the Baptistery. The Baptistery stands opposite the facade, behind the viewer, so it should be out of frame or at the frame edge behind the camera position.
- The campanile is well proportioned.

### Capri — `highlights/Rome_Highlight04_Capri.png`
- **Stack proportions wrong (major).** The three Faraglioni are Stella (~109 m, joined to Capri by a low rocky neck), di Mezzo (~81 m) and di Fuori/Scopolo (~104 m). Here the middle stack is about half the height of the others, and the first stack is fully detached from the island.
- **Arch wrong (major).** Faraglione di Mezzo has a tunnel that runs all the way through at sea level, wide enough for boats. Here it appears as a small cave mouth.

### Highlight — Florence `highlights/Rome_Highlight06_Florence.png`
- Three arches, shopfront overhangs and the central open span are right. Check the Vasari Corridor's window rhythm on the upstream side against a photo before publishing.

## Corrected prompts

Prepend the shared style preamble already used in `prompts.json` ("Photorealistic travel photography, one continuous scene…").

**Banner (2:1).**
> Ground-level view across St Peter's Square at winter dusk, looking west at the Maderno facade of St Peter's Basilica. Because the long nave stands between facade and dome, only the upper half of Michelangelo's dome and its lantern rise above the statue-lined attic; the drum is hidden. Single Egyptian obelisk on the central axis with the tall decorated Christmas tree immediately beside it and a nativity scene at its base. Bernini colonnades curving in from both sides, Apostolic Palace on the right. Warm amber lamps, peach and lavender sky. Any inscriptions softly illegible. No text overlays.

**Day 1 (3:2).**
> Modern unbranded continental-European touring coach, left-hand drive: driver's seat and steering wheel behind the LEFT half of the windscreen, passenger door at the front RIGHT beside the kerb. Small anonymous figures with luggage boarding at winter dusk under a plain bus-terminal canopy. Warm cabin lights, blue twilight. No identifiable city.

**Day 3 (3:2).**
> Christmas morning, clear winter sun, St Peter's Square seen from just north of the obelisk. The basilica facade dominates the frame; only the top of the dome and its lantern show above the attic. Red drape on the central balcony. Tree beside the obelisk. All carved inscriptions on the facade frieze and obelisk base rendered softly and illegibly, with no readable letters. Sparse, anonymous figures.

**Day 5 (3:2).**
> Piazza del Duomo, Florence, late-afternoon golden light. Frontal three-quarter view of the west facade of Santa Maria del Fiore in white, green and pink marble, with Brunelleschi's red-tiled dome rising directly BEHIND the facade on the same axis. Giotto's campanile stands at the facade's right-hand (south) corner and is fully in frame. Baptistery not in frame. Pedestrians small and anonymous.

**Capri (3:2).**
> View from the Belvedere di Tragara, Capri, winter afternoon. Three limestone Faraglioni in a line out to sea: Stella on the left, joined to the island's shore by a low rocky neck; di Mezzo in the middle, slightly lower than the others, with a clear sea-level tunnel passing right through it; di Fuori on the right, tall and separate. Pine-covered cliffs in the left foreground, deep-blue sea, no boats in the arch.
