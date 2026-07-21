
# Northgate Badge-Access Review Dossier

Working record of the access-control review board. The containment rollup deployed during the Northgate incident is producing an unreliable responder queue; how the rollup is *meant* to behave was settled here incrementally, not in any single summary. February triage proposals were partly reversed during the March working sessions and several March positions were revised again in the May close-out, so trace each rule to its final dated decision. `/app/docs/report_spec.json` is the output contract only: it fixes file names, key sets and checksum serialization, not how any value is derived.

### Review entry 0011 — atrium lane

Door controller C4 on eastwing was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 46 camera frames against the server-hall swipe log for the night shift and found no unattributed entries.
Escort refresher for the vault contractor cohort closed with 75 attendees; facilities holds the roster.
Okonkwo confirmed the atrium anti-passback timer stayed at the 104-second vendor default across the incident window.
Badge stock at the coldroom desk reconciled after the relief shift: 133 blanks issued, none unaccounted.
Baptiste closed the dockbay follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on eastwing recalibrated in 191 minutes during the night shift with no operator intervention.
Ferrara measured 220 ms of clock drift on the server-hall visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for vault listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on atrium door C2 after the rollout and saw nothing anomalous.
Locksmith callback for coldroom door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified dockbay monitoring resumed on the night shift 336 seconds after the controller restart.
Fire-panel interlock test on eastwing passed on the swing shift; Haugen logged the 365-second release delay.
Baptiste traced 394 orphaned reader heartbeats on server-hall to a patch-panel swap, not to the rollup.
Visitor pre-registration for vault processed 23 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on atrium: the strike alignment was within spec after 52 cycles.
Access-review queue for coldroom carried 81 items into the night shift, all of them informational.
Sato archived 110 controller diagnostics from dockbay to cold storage; none bear on rollup behaviour.
Cabling survey on eastwing door B3 finished during the early shift; 139 terminations were re-dressed.
Okonkwo reconciled the server-hall muster report against 168 badge-in events and found no gap.
Door controller C4 on vault was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 226 camera frames against the atrium swipe log for the night shift and found no unattributed entries.
Escort refresher for the coldroom contractor cohort closed with 255 attendees; facilities holds the roster.
Ferrara confirmed the dockbay anti-passback timer stayed at the 284-second vendor default across the incident window.
Badge stock at the eastwing desk reconciled after the relief shift: 313 blanks issued, none unaccounted.
Sato closed the server-hall follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on vault recalibrated in 371 minutes during the night shift with no operator intervention.
Okonkwo measured 400 ms of clock drift on the atrium visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for coldroom listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on dockbay door C2 after the rollout and saw nothing anomalous.
Locksmith callback for eastwing door C4 closed without action; the mechanical override was already compliant.
Ferrara verified server-hall monitoring resumed on the night shift 116 seconds after the controller restart.
Fire-panel interlock test on vault passed on the swing shift; Lindqvist logged the 145-second release delay.
Sato traced 174 orphaned reader heartbeats on atrium to a patch-panel swap, not to the rollup.
Visitor pre-registration for coldroom processed 203 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on dockbay: the strike alignment was within spec after 232 cycles.
Access-review queue for eastwing carried 261 items into the night shift, all of them informational.
Baptiste archived 290 controller diagnostics from server-hall to cold storage; none bear on rollup behaviour.
> **Triage proposal (2026-02-09 - PAC-3208)** Okonkwo: entry timestamps are read from `granted_at`, the field the door controller stamps on unlock. *(Superseded — reversed in the May close-out; see the matching decision entry.)*
Cabling survey on vault door B3 finished during the early shift; 319 terminations were re-dressed.
Ferrara reconciled the atrium muster report against 348 badge-in events and found no gap.
Door controller C4 on coldroom was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 406 camera frames against the dockbay swipe log for the night shift and found no unattributed entries.
Escort refresher for the eastwing contractor cohort closed with 35 attendees; facilities holds the roster.
Okonkwo confirmed the server-hall anti-passback timer stayed at the 64-second vendor default across the incident window.
Badge stock at the vault desk reconciled after the relief shift: 93 blanks issued, none unaccounted.
Baptiste closed the atrium follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on coldroom recalibrated in 151 minutes during the night shift with no operator intervention.
Ferrara measured 180 ms of clock drift on the dockbay visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for eastwing listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on server-hall door C2 after the rollout and saw nothing anomalous.
Locksmith callback for vault door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified atrium monitoring resumed on the night shift 296 seconds after the controller restart.
Fire-panel interlock test on coldroom passed on the swing shift; Haugen logged the 325-second release delay.
Baptiste traced 354 orphaned reader heartbeats on dockbay to a patch-panel swap, not to the rollup.
Visitor pre-registration for eastwing processed 383 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on server-hall: the strike alignment was within spec after 412 cycles.
Access-review queue for vault carried 41 items into the night shift, all of them informational.
Sato archived 70 controller diagnostics from atrium to cold storage; none bear on rollup behaviour.
Cabling survey on coldroom door B3 finished during the early shift; 99 terminations were re-dressed.
Okonkwo reconciled the dockbay muster report against 128 badge-in events and found no gap.
Door controller C4 on eastwing was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 186 camera frames against the server-hall swipe log for the night shift and found no unattributed entries.
Escort refresher for the vault contractor cohort closed with 215 attendees; facilities holds the roster.
Ferrara confirmed the atrium anti-passback timer stayed at the 244-second vendor default across the incident window.
Badge stock at the coldroom desk reconciled after the relief shift: 273 blanks issued, none unaccounted.
Sato closed the dockbay follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on eastwing recalibrated in 331 minutes during the night shift with no operator intervention.
Okonkwo measured 360 ms of clock drift on the server-hall visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for vault listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on atrium door C2 after the rollout and saw nothing anomalous.
Locksmith callback for coldroom door C4 closed without action; the mechanical override was already compliant.
Ferrara verified dockbay monitoring resumed on the night shift 76 seconds after the controller restart.

### Review entry 0015 — coldroom lane

Fire-panel interlock test on eastwing passed on the swing shift; Lindqvist logged the 105-second release delay.
Sato traced 134 orphaned reader heartbeats on server-hall to a patch-panel swap, not to the rollup.
Visitor pre-registration for vault processed 163 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on atrium: the strike alignment was within spec after 192 cycles.
Access-review queue for coldroom carried 221 items into the night shift, all of them informational.
Baptiste archived 250 controller diagnostics from dockbay to cold storage; none bear on rollup behaviour.
Cabling survey on eastwing door B3 finished during the early shift; 279 terminations were re-dressed.
Ferrara reconciled the server-hall muster report against 308 badge-in events and found no gap.
Door controller C4 on vault was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 366 camera frames against the atrium swipe log for the night shift and found no unattributed entries.
Escort refresher for the coldroom contractor cohort closed with 395 attendees; facilities holds the roster.
Okonkwo confirmed the dockbay anti-passback timer stayed at the 24-second vendor default across the incident window.
Badge stock at the eastwing desk reconciled after the relief shift: 53 blanks issued, none unaccounted.
Baptiste closed the server-hall follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on vault recalibrated in 111 minutes during the night shift with no operator intervention.
Ferrara measured 140 ms of clock drift on the atrium visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for coldroom listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on dockbay door C2 after the rollout and saw nothing anomalous.
Locksmith callback for eastwing door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified server-hall monitoring resumed on the night shift 256 seconds after the controller restart.
Fire-panel interlock test on vault passed on the swing shift; Haugen logged the 285-second release delay.
Baptiste traced 314 orphaned reader heartbeats on atrium to a patch-panel swap, not to the rollup.
Visitor pre-registration for coldroom processed 343 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on dockbay: the strike alignment was within spec after 372 cycles.
Access-review queue for eastwing carried 401 items into the night shift, all of them informational.
Sato archived 30 controller diagnostics from server-hall to cold storage; none bear on rollup behaviour.
Cabling survey on vault door B3 finished during the early shift; 59 terminations were re-dressed.
Okonkwo reconciled the atrium muster report against 88 badge-in events and found no gap.
Door controller C4 on coldroom was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 146 camera frames against the dockbay swipe log for the night shift and found no unattributed entries.
Escort refresher for the eastwing contractor cohort closed with 175 attendees; facilities holds the roster.
Ferrara confirmed the server-hall anti-passback timer stayed at the 204-second vendor default across the incident window.
Badge stock at the vault desk reconciled after the relief shift: 233 blanks issued, none unaccounted.
Sato closed the atrium follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on coldroom recalibrated in 291 minutes during the night shift with no operator intervention.
Okonkwo measured 320 ms of clock drift on the dockbay visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for eastwing listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on server-hall door C2 after the rollout and saw nothing anomalous.
> **Triage proposal (2026-02-12 - PAC-3210)** Lindqvist: badge_class is taken as written; the controllers already emit canonical values. *(Superseded — reversed in the May close-out; see the matching decision entry.)*
Locksmith callback for vault door C4 closed without action; the mechanical override was already compliant.
Ferrara verified atrium monitoring resumed on the night shift 36 seconds after the controller restart.
Fire-panel interlock test on coldroom passed on the swing shift; Lindqvist logged the 65-second release delay.
Sato traced 94 orphaned reader heartbeats on dockbay to a patch-panel swap, not to the rollup.
Visitor pre-registration for eastwing processed 123 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on server-hall: the strike alignment was within spec after 152 cycles.
Access-review queue for vault carried 181 items into the night shift, all of them informational.
Baptiste archived 210 controller diagnostics from atrium to cold storage; none bear on rollup behaviour.
Cabling survey on coldroom door B3 finished during the early shift; 239 terminations were re-dressed.
Ferrara reconciled the dockbay muster report against 268 badge-in events and found no gap.
Door controller C4 on eastwing was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 326 camera frames against the server-hall swipe log for the night shift and found no unattributed entries.
Escort refresher for the vault contractor cohort closed with 355 attendees; facilities holds the roster.
Okonkwo confirmed the atrium anti-passback timer stayed at the 384-second vendor default across the incident window.
Badge stock at the coldroom desk reconciled after the relief shift: 413 blanks issued, none unaccounted.
Baptiste closed the dockbay follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on eastwing recalibrated in 71 minutes during the night shift with no operator intervention.
Ferrara measured 100 ms of clock drift on the server-hall visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for vault listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on atrium door C2 after the rollout and saw nothing anomalous.
Locksmith callback for coldroom door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified dockbay monitoring resumed on the night shift 216 seconds after the controller restart.
Fire-panel interlock test on eastwing passed on the swing shift; Haugen logged the 245-second release delay.
Baptiste traced 274 orphaned reader heartbeats on server-hall to a patch-panel swap, not to the rollup.
Visitor pre-registration for vault processed 303 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on atrium: the strike alignment was within spec after 332 cycles.
Access-review queue for coldroom carried 361 items into the night shift, all of them informational.
Sato archived 390 controller diagnostics from dockbay to cold storage; none bear on rollup behaviour.
Cabling survey on eastwing door B3 finished during the early shift; 19 terminations were re-dressed.
Okonkwo reconciled the server-hall muster report against 48 badge-in events and found no gap.
Door controller C4 on vault was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 106 camera frames against the atrium swipe log for the night shift and found no unattributed entries.
Escort refresher for the coldroom contractor cohort closed with 135 attendees; facilities holds the roster.
Ferrara confirmed the dockbay anti-passback timer stayed at the 164-second vendor default across the incident window.

### Review entry 0019 — dockbay lane

Badge stock at the eastwing desk reconciled after the relief shift: 193 blanks issued, none unaccounted.
Sato closed the server-hall follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on vault recalibrated in 251 minutes during the night shift with no operator intervention.
Okonkwo measured 280 ms of clock drift on the atrium visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for coldroom listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on dockbay door C2 after the rollout and saw nothing anomalous.
Locksmith callback for eastwing door C4 closed without action; the mechanical override was already compliant.
Ferrara verified server-hall monitoring resumed on the night shift 396 seconds after the controller restart.
Fire-panel interlock test on vault passed on the swing shift; Lindqvist logged the 25-second release delay.
Sato traced 54 orphaned reader heartbeats on atrium to a patch-panel swap, not to the rollup.
Visitor pre-registration for coldroom processed 83 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on dockbay: the strike alignment was within spec after 112 cycles.
Access-review queue for eastwing carried 141 items into the night shift, all of them informational.
Baptiste archived 170 controller diagnostics from server-hall to cold storage; none bear on rollup behaviour.
Cabling survey on vault door B3 finished during the early shift; 199 terminations were re-dressed.
Ferrara reconciled the atrium muster report against 228 badge-in events and found no gap.
Door controller C4 on coldroom was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 286 camera frames against the dockbay swipe log for the night shift and found no unattributed entries.
Escort refresher for the eastwing contractor cohort closed with 315 attendees; facilities holds the roster.
Okonkwo confirmed the server-hall anti-passback timer stayed at the 344-second vendor default across the incident window.
Badge stock at the vault desk reconciled after the relief shift: 373 blanks issued, none unaccounted.
Baptiste closed the atrium follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on coldroom recalibrated in 31 minutes during the night shift with no operator intervention.
Ferrara measured 60 ms of clock drift on the dockbay visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for eastwing listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on server-hall door C2 after the rollout and saw nothing anomalous.
Locksmith callback for vault door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified atrium monitoring resumed on the night shift 176 seconds after the controller restart.
Fire-panel interlock test on coldroom passed on the swing shift; Haugen logged the 205-second release delay.
Baptiste traced 234 orphaned reader heartbeats on dockbay to a patch-panel swap, not to the rollup.
Visitor pre-registration for eastwing processed 263 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on server-hall: the strike alignment was within spec after 292 cycles.
Access-review queue for vault carried 321 items into the night shift, all of them informational.
Sato archived 350 controller diagnostics from atrium to cold storage; none bear on rollup behaviour.
Cabling survey on coldroom door B3 finished during the early shift; 379 terminations were re-dressed.
Okonkwo reconciled the dockbay muster report against 408 badge-in events and found no gap.
Door controller C4 on eastwing was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 66 camera frames against the server-hall swipe log for the night shift and found no unattributed entries.
> **Triage proposal (2026-02-15 - PAC-3212)** Baptiste: on a repeated swipe_id keep the row with the HIGHER badge class, since the stronger credential is the one that opened the door. *(Superseded — reversed in the May close-out; see the matching decision entry.)*
Escort refresher for the vault contractor cohort closed with 95 attendees; facilities holds the roster.
Ferrara confirmed the atrium anti-passback timer stayed at the 124-second vendor default across the incident window.
Badge stock at the coldroom desk reconciled after the relief shift: 153 blanks issued, none unaccounted.
Sato closed the dockbay follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on eastwing recalibrated in 211 minutes during the night shift with no operator intervention.
Okonkwo measured 240 ms of clock drift on the server-hall visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for vault listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on atrium door C2 after the rollout and saw nothing anomalous.
Locksmith callback for coldroom door C4 closed without action; the mechanical override was already compliant.
Ferrara verified dockbay monitoring resumed on the night shift 356 seconds after the controller restart.
Fire-panel interlock test on eastwing passed on the swing shift; Lindqvist logged the 385-second release delay.
Sato traced 414 orphaned reader heartbeats on server-hall to a patch-panel swap, not to the rollup.
Visitor pre-registration for vault processed 43 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on atrium: the strike alignment was within spec after 72 cycles.
Access-review queue for coldroom carried 101 items into the night shift, all of them informational.
Baptiste archived 130 controller diagnostics from dockbay to cold storage; none bear on rollup behaviour.
Cabling survey on eastwing door B3 finished during the early shift; 159 terminations were re-dressed.
Ferrara reconciled the server-hall muster report against 188 badge-in events and found no gap.
Door controller C4 on vault was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 246 camera frames against the atrium swipe log for the night shift and found no unattributed entries.
Escort refresher for the coldroom contractor cohort closed with 275 attendees; facilities holds the roster.
Okonkwo confirmed the dockbay anti-passback timer stayed at the 304-second vendor default across the incident window.
Badge stock at the eastwing desk reconciled after the relief shift: 333 blanks issued, none unaccounted.
Baptiste closed the server-hall follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on vault recalibrated in 391 minutes during the night shift with no operator intervention.
Ferrara measured 20 ms of clock drift on the atrium visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for coldroom listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on dockbay door C2 after the rollout and saw nothing anomalous.
Locksmith callback for eastwing door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified server-hall monitoring resumed on the night shift 136 seconds after the controller restart.
Fire-panel interlock test on vault passed on the swing shift; Haugen logged the 165-second release delay.
Baptiste traced 194 orphaned reader heartbeats on atrium to a patch-panel swap, not to the rollup.
Visitor pre-registration for coldroom processed 223 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on dockbay: the strike alignment was within spec after 252 cycles.

### Review entry 0023 — eastwing lane

Access-review queue for eastwing carried 281 items into the night shift, all of them informational.
Sato archived 310 controller diagnostics from server-hall to cold storage; none bear on rollup behaviour.
Cabling survey on vault door B3 finished during the early shift; 339 terminations were re-dressed.
Okonkwo reconciled the atrium muster report against 368 badge-in events and found no gap.
Door controller C4 on coldroom was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 26 camera frames against the dockbay swipe log for the night shift and found no unattributed entries.
Escort refresher for the eastwing contractor cohort closed with 55 attendees; facilities holds the roster.
Ferrara confirmed the server-hall anti-passback timer stayed at the 84-second vendor default across the incident window.
Badge stock at the vault desk reconciled after the relief shift: 113 blanks issued, none unaccounted.
Sato closed the atrium follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on coldroom recalibrated in 171 minutes during the night shift with no operator intervention.
Okonkwo measured 200 ms of clock drift on the dockbay visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for eastwing listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on server-hall door C2 after the rollout and saw nothing anomalous.
Locksmith callback for vault door C4 closed without action; the mechanical override was already compliant.
Ferrara verified atrium monitoring resumed on the night shift 316 seconds after the controller restart.
Fire-panel interlock test on coldroom passed on the swing shift; Lindqvist logged the 345-second release delay.
Sato traced 374 orphaned reader heartbeats on dockbay to a patch-panel swap, not to the rollup.
Visitor pre-registration for eastwing processed 403 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on server-hall: the strike alignment was within spec after 32 cycles.
Access-review queue for vault carried 61 items into the night shift, all of them informational.
Baptiste archived 90 controller diagnostics from atrium to cold storage; none bear on rollup behaviour.
Cabling survey on coldroom door B3 finished during the early shift; 119 terminations were re-dressed.
Ferrara reconciled the dockbay muster report against 148 badge-in events and found no gap.
Door controller C4 on eastwing was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 206 camera frames against the server-hall swipe log for the night shift and found no unattributed entries.
Escort refresher for the vault contractor cohort closed with 235 attendees; facilities holds the roster.
Okonkwo confirmed the atrium anti-passback timer stayed at the 264-second vendor default across the incident window.
Badge stock at the coldroom desk reconciled after the relief shift: 293 blanks issued, none unaccounted.
Baptiste closed the dockbay follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on eastwing recalibrated in 351 minutes during the night shift with no operator intervention.
Ferrara measured 380 ms of clock drift on the server-hall visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for vault listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on atrium door C2 after the rollout and saw nothing anomalous.
Locksmith callback for coldroom door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified dockbay monitoring resumed on the night shift 96 seconds after the controller restart.
Fire-panel interlock test on eastwing passed on the swing shift; Haugen logged the 125-second release delay.
Baptiste traced 154 orphaned reader heartbeats on server-hall to a patch-panel swap, not to the rollup.
> **Working note (2026-03-04 - PAC-3244)** Moreau: sessions stitch when the next swipe lands within 60 ms of the previous exit. *(Revised — see the 2026-05 close-out.)*
Visitor pre-registration for vault processed 183 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on atrium: the strike alignment was within spec after 212 cycles.
Access-review queue for coldroom carried 241 items into the night shift, all of them informational.
Sato archived 270 controller diagnostics from dockbay to cold storage; none bear on rollup behaviour.
Cabling survey on eastwing door B3 finished during the early shift; 299 terminations were re-dressed.
Okonkwo reconciled the server-hall muster report against 328 badge-in events and found no gap.
Door controller C4 on vault was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 386 camera frames against the atrium swipe log for the night shift and found no unattributed entries.
Escort refresher for the coldroom contractor cohort closed with 415 attendees; facilities holds the roster.
Ferrara confirmed the dockbay anti-passback timer stayed at the 44-second vendor default across the incident window.
Badge stock at the eastwing desk reconciled after the relief shift: 73 blanks issued, none unaccounted.
Sato closed the server-hall follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on vault recalibrated in 131 minutes during the night shift with no operator intervention.
Okonkwo measured 160 ms of clock drift on the atrium visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for coldroom listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on dockbay door C2 after the rollout and saw nothing anomalous.
Locksmith callback for eastwing door C4 closed without action; the mechanical override was already compliant.
Ferrara verified server-hall monitoring resumed on the night shift 276 seconds after the controller restart.
Fire-panel interlock test on vault passed on the swing shift; Lindqvist logged the 305-second release delay.
Sato traced 334 orphaned reader heartbeats on atrium to a patch-panel swap, not to the rollup.
Visitor pre-registration for coldroom processed 363 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on dockbay: the strike alignment was within spec after 392 cycles.
Access-review queue for eastwing carried 21 items into the night shift, all of them informational.
Baptiste archived 50 controller diagnostics from server-hall to cold storage; none bear on rollup behaviour.
Cabling survey on vault door B3 finished during the early shift; 79 terminations were re-dressed.
Ferrara reconciled the atrium muster report against 108 badge-in events and found no gap.
Door controller C4 on coldroom was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 166 camera frames against the dockbay swipe log for the night shift and found no unattributed entries.
Escort refresher for the eastwing contractor cohort closed with 195 attendees; facilities holds the roster.
Okonkwo confirmed the server-hall anti-passback timer stayed at the 224-second vendor default across the incident window.
Badge stock at the vault desk reconciled after the relief shift: 253 blanks issued, none unaccounted.
Baptiste closed the atrium follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on coldroom recalibrated in 311 minutes during the night shift with no operator intervention.
Ferrara measured 340 ms of clock drift on the dockbay visitor kiosk, inside the tolerance the board set.

### Review entry 0027 — server-hall lane

Handover at the early boundary for eastwing listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on server-hall door C2 after the rollout and saw nothing anomalous.
Locksmith callback for vault door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified atrium monitoring resumed on the night shift 56 seconds after the controller restart.
Fire-panel interlock test on coldroom passed on the swing shift; Haugen logged the 85-second release delay.
Baptiste traced 114 orphaned reader heartbeats on dockbay to a patch-panel swap, not to the rollup.
Visitor pre-registration for eastwing processed 143 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on server-hall: the strike alignment was within spec after 172 cycles.
Access-review queue for vault carried 201 items into the night shift, all of them informational.
Sato archived 230 controller diagnostics from atrium to cold storage; none bear on rollup behaviour.
Cabling survey on coldroom door B3 finished during the early shift; 259 terminations were re-dressed.
Okonkwo reconciled the dockbay muster report against 288 badge-in events and found no gap.
Door controller C4 on eastwing was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 346 camera frames against the server-hall swipe log for the night shift and found no unattributed entries.
Escort refresher for the vault contractor cohort closed with 375 attendees; facilities holds the roster.
Ferrara confirmed the atrium anti-passback timer stayed at the 404-second vendor default across the incident window.
Badge stock at the coldroom desk reconciled after the relief shift: 33 blanks issued, none unaccounted.
Sato closed the dockbay follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on eastwing recalibrated in 91 minutes during the night shift with no operator intervention.
Okonkwo measured 120 ms of clock drift on the server-hall visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for vault listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on atrium door C2 after the rollout and saw nothing anomalous.
Locksmith callback for coldroom door C4 closed without action; the mechanical override was already compliant.
Ferrara verified dockbay monitoring resumed on the night shift 236 seconds after the controller restart.
Fire-panel interlock test on eastwing passed on the swing shift; Lindqvist logged the 265-second release delay.
Sato traced 294 orphaned reader heartbeats on server-hall to a patch-panel swap, not to the rollup.
Visitor pre-registration for vault processed 323 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on atrium: the strike alignment was within spec after 352 cycles.
Access-review queue for coldroom carried 381 items into the night shift, all of them informational.
Baptiste archived 410 controller diagnostics from dockbay to cold storage; none bear on rollup behaviour.
Cabling survey on eastwing door B3 finished during the early shift; 39 terminations were re-dressed.
Ferrara reconciled the server-hall muster report against 68 badge-in events and found no gap.
Door controller C4 on vault was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 126 camera frames against the atrium swipe log for the night shift and found no unattributed entries.
Escort refresher for the coldroom contractor cohort closed with 155 attendees; facilities holds the roster.
Okonkwo confirmed the dockbay anti-passback timer stayed at the 184-second vendor default across the incident window.
Badge stock at the eastwing desk reconciled after the relief shift: 213 blanks issued, none unaccounted.
Baptiste closed the server-hall follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
> **Working note (2026-03-07 - PAC-3246)** Ferrara: the occupancy carry-out is capped at 2000 ms, a bound that has never been reached in practice. *(Revised — see the 2026-05 close-out.)*
Turnstile A2 on vault recalibrated in 271 minutes during the night shift with no operator intervention.
Ferrara measured 300 ms of clock drift on the atrium visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for coldroom listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on dockbay door C2 after the rollout and saw nothing anomalous.
Locksmith callback for eastwing door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified server-hall monitoring resumed on the night shift 416 seconds after the controller restart.
Fire-panel interlock test on vault passed on the swing shift; Haugen logged the 45-second release delay.
Baptiste traced 74 orphaned reader heartbeats on atrium to a patch-panel swap, not to the rollup.
Visitor pre-registration for coldroom processed 103 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on dockbay: the strike alignment was within spec after 132 cycles.
Access-review queue for eastwing carried 161 items into the night shift, all of them informational.
Sato archived 190 controller diagnostics from server-hall to cold storage; none bear on rollup behaviour.
Cabling survey on vault door B3 finished during the early shift; 219 terminations were re-dressed.
Okonkwo reconciled the atrium muster report against 248 badge-in events and found no gap.
Door controller C4 on coldroom was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 306 camera frames against the dockbay swipe log for the night shift and found no unattributed entries.
Escort refresher for the eastwing contractor cohort closed with 335 attendees; facilities holds the roster.
Ferrara confirmed the server-hall anti-passback timer stayed at the 364-second vendor default across the incident window.
Badge stock at the vault desk reconciled after the relief shift: 393 blanks issued, none unaccounted.
Sato closed the atrium follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on coldroom recalibrated in 51 minutes during the night shift with no operator intervention.
Okonkwo measured 80 ms of clock drift on the dockbay visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for eastwing listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on server-hall door C2 after the rollout and saw nothing anomalous.
Locksmith callback for vault door C4 closed without action; the mechanical override was already compliant.
Ferrara verified atrium monitoring resumed on the night shift 196 seconds after the controller restart.
Fire-panel interlock test on coldroom passed on the swing shift; Lindqvist logged the 225-second release delay.
Sato traced 254 orphaned reader heartbeats on dockbay to a patch-panel swap, not to the rollup.
Visitor pre-registration for eastwing processed 283 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on server-hall: the strike alignment was within spec after 312 cycles.
Access-review queue for vault carried 341 items into the night shift, all of them informational.
Baptiste archived 370 controller diagnostics from atrium to cold storage; none bear on rollup behaviour.
Cabling survey on coldroom door B3 finished during the early shift; 399 terminations were re-dressed.
Ferrara reconciled the dockbay muster report against 28 badge-in events and found no gap.

### Review entry 0031 — vault lane

Door controller C4 on eastwing was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 86 camera frames against the server-hall swipe log for the night shift and found no unattributed entries.
Escort refresher for the vault contractor cohort closed with 115 attendees; facilities holds the roster.
Okonkwo confirmed the atrium anti-passback timer stayed at the 144-second vendor default across the incident window.
Badge stock at the coldroom desk reconciled after the relief shift: 173 blanks issued, none unaccounted.
Baptiste closed the dockbay follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on eastwing recalibrated in 231 minutes during the night shift with no operator intervention.
Ferrara measured 260 ms of clock drift on the server-hall visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for vault listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on atrium door C2 after the rollout and saw nothing anomalous.
Locksmith callback for coldroom door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified dockbay monitoring resumed on the night shift 376 seconds after the controller restart.
Fire-panel interlock test on eastwing passed on the swing shift; Haugen logged the 405-second release delay.
Baptiste traced 34 orphaned reader heartbeats on server-hall to a patch-panel swap, not to the rollup.
Visitor pre-registration for vault processed 63 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on atrium: the strike alignment was within spec after 92 cycles.
Access-review queue for coldroom carried 121 items into the night shift, all of them informational.
Sato archived 150 controller diagnostics from dockbay to cold storage; none bear on rollup behaviour.
Cabling survey on eastwing door B3 finished during the early shift; 179 terminations were re-dressed.
Okonkwo reconciled the server-hall muster report against 208 badge-in events and found no gap.
Door controller C4 on vault was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 266 camera frames against the atrium swipe log for the night shift and found no unattributed entries.
Escort refresher for the coldroom contractor cohort closed with 295 attendees; facilities holds the roster.
Ferrara confirmed the dockbay anti-passback timer stayed at the 324-second vendor default across the incident window.
Badge stock at the eastwing desk reconciled after the relief shift: 353 blanks issued, none unaccounted.
Sato closed the server-hall follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on vault recalibrated in 411 minutes during the night shift with no operator intervention.
Okonkwo measured 40 ms of clock drift on the atrium visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for coldroom listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on dockbay door C2 after the rollout and saw nothing anomalous.
Locksmith callback for eastwing door C4 closed without action; the mechanical override was already compliant.
Ferrara verified server-hall monitoring resumed on the night shift 156 seconds after the controller restart.
Fire-panel interlock test on vault passed on the swing shift; Lindqvist logged the 185-second release delay.
Sato traced 214 orphaned reader heartbeats on atrium to a patch-panel swap, not to the rollup.
Visitor pre-registration for coldroom processed 243 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on dockbay: the strike alignment was within spec after 272 cycles.
Access-review queue for eastwing carried 301 items into the night shift, all of them informational.
Baptiste archived 330 controller diagnostics from server-hall to cold storage; none bear on rollup behaviour.
> **Working note (2026-03-11 - PAC-3248)** Haugen: a class that has its own control window also inherits the `all`-scoped windows for that layer, so both apply. *(Revised — see the 2026-05 close-out.)*
Cabling survey on vault door B3 finished during the early shift; 359 terminations were re-dressed.
Ferrara reconciled the atrium muster report against 388 badge-in events and found no gap.
Door controller C4 on coldroom was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 46 camera frames against the dockbay swipe log for the night shift and found no unattributed entries.
Escort refresher for the eastwing contractor cohort closed with 75 attendees; facilities holds the roster.
Okonkwo confirmed the server-hall anti-passback timer stayed at the 104-second vendor default across the incident window.
Badge stock at the vault desk reconciled after the relief shift: 133 blanks issued, none unaccounted.
Baptiste closed the atrium follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on coldroom recalibrated in 191 minutes during the night shift with no operator intervention.
Ferrara measured 220 ms of clock drift on the dockbay visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for eastwing listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on server-hall door C2 after the rollout and saw nothing anomalous.
Locksmith callback for vault door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified atrium monitoring resumed on the night shift 336 seconds after the controller restart.
Fire-panel interlock test on coldroom passed on the swing shift; Haugen logged the 365-second release delay.
Baptiste traced 394 orphaned reader heartbeats on dockbay to a patch-panel swap, not to the rollup.
Visitor pre-registration for eastwing processed 23 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on server-hall: the strike alignment was within spec after 52 cycles.
Access-review queue for vault carried 81 items into the night shift, all of them informational.
Sato archived 110 controller diagnostics from atrium to cold storage; none bear on rollup behaviour.
Cabling survey on coldroom door B3 finished during the early shift; 139 terminations were re-dressed.
Okonkwo reconciled the dockbay muster report against 168 badge-in events and found no gap.
Door controller C4 on eastwing was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 226 camera frames against the server-hall swipe log for the night shift and found no unattributed entries.
Escort refresher for the vault contractor cohort closed with 255 attendees; facilities holds the roster.
Ferrara confirmed the atrium anti-passback timer stayed at the 284-second vendor default across the incident window.
Badge stock at the coldroom desk reconciled after the relief shift: 313 blanks issued, none unaccounted.
Sato closed the dockbay follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on eastwing recalibrated in 371 minutes during the night shift with no operator intervention.
Okonkwo measured 400 ms of clock drift on the server-hall visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for vault listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on atrium door C2 after the rollout and saw nothing anomalous.
Locksmith callback for coldroom door C4 closed without action; the mechanical override was already compliant.
Ferrara verified dockbay monitoring resumed on the night shift 116 seconds after the controller restart.

### Review entry 0035 — atrium lane

Fire-panel interlock test on eastwing passed on the swing shift; Lindqvist logged the 145-second release delay.
Sato traced 174 orphaned reader heartbeats on server-hall to a patch-panel swap, not to the rollup.
Visitor pre-registration for vault processed 203 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on atrium: the strike alignment was within spec after 232 cycles.
Access-review queue for coldroom carried 261 items into the night shift, all of them informational.
Baptiste archived 290 controller diagnostics from dockbay to cold storage; none bear on rollup behaviour.
Cabling survey on eastwing door B3 finished during the early shift; 319 terminations were re-dressed.
Ferrara reconciled the server-hall muster report against 348 badge-in events and found no gap.
Door controller C4 on vault was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 406 camera frames against the atrium swipe log for the night shift and found no unattributed entries.
Escort refresher for the coldroom contractor cohort closed with 35 attendees; facilities holds the roster.
Okonkwo confirmed the dockbay anti-passback timer stayed at the 64-second vendor default across the incident window.
Badge stock at the eastwing desk reconciled after the relief shift: 93 blanks issued, none unaccounted.
Baptiste closed the server-hall follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on vault recalibrated in 151 minutes during the night shift with no operator intervention.
Ferrara measured 180 ms of clock drift on the atrium visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for coldroom listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on dockbay door C2 after the rollout and saw nothing anomalous.
Locksmith callback for eastwing door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified server-hall monitoring resumed on the night shift 296 seconds after the controller restart.
Fire-panel interlock test on vault passed on the swing shift; Haugen logged the 325-second release delay.
Baptiste traced 354 orphaned reader heartbeats on atrium to a patch-panel swap, not to the rollup.
Visitor pre-registration for coldroom processed 383 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on dockbay: the strike alignment was within spec after 412 cycles.
Access-review queue for eastwing carried 41 items into the night shift, all of them informational.
Sato archived 70 controller diagnostics from server-hall to cold storage; none bear on rollup behaviour.
Cabling survey on vault door B3 finished during the early shift; 99 terminations were re-dressed.
Okonkwo reconciled the atrium muster report against 128 badge-in events and found no gap.
Door controller C4 on coldroom was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 186 camera frames against the dockbay swipe log for the night shift and found no unattributed entries.
Escort refresher for the eastwing contractor cohort closed with 215 attendees; facilities holds the roster.
Ferrara confirmed the server-hall anti-passback timer stayed at the 244-second vendor default across the incident window.
Badge stock at the vault desk reconciled after the relief shift: 273 blanks issued, none unaccounted.
Sato closed the atrium follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on coldroom recalibrated in 331 minutes during the night shift with no operator intervention.
Okonkwo measured 360 ms of clock drift on the dockbay visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for eastwing listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on server-hall door C2 after the rollout and saw nothing anomalous.
> **Working note (2026-03-15 - PAC-3250)** Sato: lockdown and maintenance are charged independently; an instant covered by both is charged twice. *(Revised — see the 2026-05 close-out.)*
Locksmith callback for vault door C4 closed without action; the mechanical override was already compliant.
Ferrara verified atrium monitoring resumed on the night shift 76 seconds after the controller restart.
Fire-panel interlock test on coldroom passed on the swing shift; Lindqvist logged the 105-second release delay.
Sato traced 134 orphaned reader heartbeats on dockbay to a patch-panel swap, not to the rollup.
Visitor pre-registration for eastwing processed 163 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on server-hall: the strike alignment was within spec after 192 cycles.
Access-review queue for vault carried 221 items into the night shift, all of them informational.
Baptiste archived 250 controller diagnostics from atrium to cold storage; none bear on rollup behaviour.
Cabling survey on coldroom door B3 finished during the early shift; 279 terminations were re-dressed.
Ferrara reconciled the dockbay muster report against 308 badge-in events and found no gap.
Door controller C4 on eastwing was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 366 camera frames against the server-hall swipe log for the night shift and found no unattributed entries.
Escort refresher for the vault contractor cohort closed with 395 attendees; facilities holds the roster.
Okonkwo confirmed the atrium anti-passback timer stayed at the 24-second vendor default across the incident window.
Badge stock at the coldroom desk reconciled after the relief shift: 53 blanks issued, none unaccounted.
Baptiste closed the dockbay follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on eastwing recalibrated in 111 minutes during the night shift with no operator intervention.
Ferrara measured 140 ms of clock drift on the server-hall visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for vault listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on atrium door C2 after the rollout and saw nothing anomalous.
Locksmith callback for coldroom door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified dockbay monitoring resumed on the night shift 256 seconds after the controller restart.
Fire-panel interlock test on eastwing passed on the swing shift; Haugen logged the 285-second release delay.
Baptiste traced 314 orphaned reader heartbeats on server-hall to a patch-panel swap, not to the rollup.
Visitor pre-registration for vault processed 343 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on atrium: the strike alignment was within spec after 372 cycles.
Access-review queue for coldroom carried 401 items into the night shift, all of them informational.
Sato archived 30 controller diagnostics from dockbay to cold storage; none bear on rollup behaviour.
Cabling survey on eastwing door B3 finished during the early shift; 59 terminations were re-dressed.
Okonkwo reconciled the server-hall muster report against 88 badge-in events and found no gap.
Door controller C4 on vault was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 146 camera frames against the atrium swipe log for the night shift and found no unattributed entries.
Escort refresher for the coldroom contractor cohort closed with 175 attendees; facilities holds the roster.
Ferrara confirmed the dockbay anti-passback timer stayed at the 204-second vendor default across the incident window.

### Review entry 0039 — coldroom lane

Badge stock at the eastwing desk reconciled after the relief shift: 233 blanks issued, none unaccounted.
Sato closed the server-hall follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on vault recalibrated in 291 minutes during the night shift with no operator intervention.
Okonkwo measured 320 ms of clock drift on the atrium visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for coldroom listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on dockbay door C2 after the rollout and saw nothing anomalous.
Locksmith callback for eastwing door C4 closed without action; the mechanical override was already compliant.
Ferrara verified server-hall monitoring resumed on the night shift 36 seconds after the controller restart.
Fire-panel interlock test on vault passed on the swing shift; Lindqvist logged the 65-second release delay.
Sato traced 94 orphaned reader heartbeats on atrium to a patch-panel swap, not to the rollup.
Visitor pre-registration for coldroom processed 123 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on dockbay: the strike alignment was within spec after 152 cycles.
Access-review queue for eastwing carried 181 items into the night shift, all of them informational.
Baptiste archived 210 controller diagnostics from server-hall to cold storage; none bear on rollup behaviour.
Cabling survey on vault door B3 finished during the early shift; 239 terminations were re-dressed.
Ferrara reconciled the atrium muster report against 268 badge-in events and found no gap.
Door controller C4 on coldroom was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 326 camera frames against the dockbay swipe log for the night shift and found no unattributed entries.
Escort refresher for the eastwing contractor cohort closed with 355 attendees; facilities holds the roster.
Okonkwo confirmed the server-hall anti-passback timer stayed at the 384-second vendor default across the incident window.
Badge stock at the vault desk reconciled after the relief shift: 413 blanks issued, none unaccounted.
Baptiste closed the atrium follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on coldroom recalibrated in 71 minutes during the night shift with no operator intervention.
Ferrara measured 100 ms of clock drift on the dockbay visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for eastwing listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on server-hall door C2 after the rollout and saw nothing anomalous.
Locksmith callback for vault door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified atrium monitoring resumed on the night shift 216 seconds after the controller restart.
Fire-panel interlock test on coldroom passed on the swing shift; Haugen logged the 245-second release delay.
Baptiste traced 274 orphaned reader heartbeats on dockbay to a patch-panel swap, not to the rollup.
Visitor pre-registration for eastwing processed 303 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on server-hall: the strike alignment was within spec after 332 cycles.
Access-review queue for vault carried 361 items into the night shift, all of them informational.
Sato archived 390 controller diagnostics from atrium to cold storage; none bear on rollup behaviour.
Cabling survey on coldroom door B3 finished during the early shift; 19 terminations were re-dressed.
Okonkwo reconciled the dockbay muster report against 48 badge-in events and found no gap.
Door controller C4 on eastwing was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 106 camera frames against the server-hall swipe log for the night shift and found no unattributed entries.
> **Working note (2026-03-19 - PAC-3252)** Delacroix: revoked badges are dropped from the input entirely before anything is counted. *(Revised — see the 2026-05 close-out.)*
Escort refresher for the vault contractor cohort closed with 135 attendees; facilities holds the roster.
Ferrara confirmed the atrium anti-passback timer stayed at the 164-second vendor default across the incident window.
Badge stock at the coldroom desk reconciled after the relief shift: 193 blanks issued, none unaccounted.
Sato closed the dockbay follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on eastwing recalibrated in 251 minutes during the night shift with no operator intervention.
Okonkwo measured 280 ms of clock drift on the server-hall visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for vault listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on atrium door C2 after the rollout and saw nothing anomalous.
Locksmith callback for coldroom door C4 closed without action; the mechanical override was already compliant.
Ferrara verified dockbay monitoring resumed on the night shift 396 seconds after the controller restart.
Fire-panel interlock test on eastwing passed on the swing shift; Lindqvist logged the 25-second release delay.
Sato traced 54 orphaned reader heartbeats on server-hall to a patch-panel swap, not to the rollup.
Visitor pre-registration for vault processed 83 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on atrium: the strike alignment was within spec after 112 cycles.
Access-review queue for coldroom carried 141 items into the night shift, all of them informational.
Baptiste archived 170 controller diagnostics from dockbay to cold storage; none bear on rollup behaviour.
Cabling survey on eastwing door B3 finished during the early shift; 199 terminations were re-dressed.
Ferrara reconciled the server-hall muster report against 228 badge-in events and found no gap.
Door controller C4 on vault was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 286 camera frames against the atrium swipe log for the night shift and found no unattributed entries.
Escort refresher for the coldroom contractor cohort closed with 315 attendees; facilities holds the roster.
Okonkwo confirmed the dockbay anti-passback timer stayed at the 344-second vendor default across the incident window.
Badge stock at the eastwing desk reconciled after the relief shift: 373 blanks issued, none unaccounted.
Baptiste closed the server-hall follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on vault recalibrated in 31 minutes during the night shift with no operator intervention.
Ferrara measured 60 ms of clock drift on the atrium visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for coldroom listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on dockbay door C2 after the rollout and saw nothing anomalous.
Locksmith callback for eastwing door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified server-hall monitoring resumed on the night shift 176 seconds after the controller restart.
Fire-panel interlock test on vault passed on the swing shift; Haugen logged the 205-second release delay.
Baptiste traced 234 orphaned reader heartbeats on atrium to a patch-panel swap, not to the rollup.
Visitor pre-registration for coldroom processed 263 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on dockbay: the strike alignment was within spec after 292 cycles.

### Review entry 0043 — dockbay lane

Access-review queue for eastwing carried 321 items into the night shift, all of them informational.
Sato archived 350 controller diagnostics from server-hall to cold storage; none bear on rollup behaviour.
Cabling survey on vault door B3 finished during the early shift; 379 terminations were re-dressed.
Okonkwo reconciled the atrium muster report against 408 badge-in events and found no gap.
Door controller C4 on coldroom was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 66 camera frames against the dockbay swipe log for the night shift and found no unattributed entries.
Escort refresher for the eastwing contractor cohort closed with 95 attendees; facilities holds the roster.
Ferrara confirmed the server-hall anti-passback timer stayed at the 124-second vendor default across the incident window.
Badge stock at the vault desk reconciled after the relief shift: 153 blanks issued, none unaccounted.
Sato closed the atrium follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on coldroom recalibrated in 211 minutes during the night shift with no operator intervention.
Okonkwo measured 240 ms of clock drift on the dockbay visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for eastwing listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on server-hall door C2 after the rollout and saw nothing anomalous.
Locksmith callback for vault door C4 closed without action; the mechanical override was already compliant.
Ferrara verified atrium monitoring resumed on the night shift 356 seconds after the controller restart.
Fire-panel interlock test on coldroom passed on the swing shift; Lindqvist logged the 385-second release delay.
Sato traced 414 orphaned reader heartbeats on dockbay to a patch-panel swap, not to the rollup.
Visitor pre-registration for eastwing processed 43 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on server-hall: the strike alignment was within spec after 72 cycles.
Access-review queue for vault carried 101 items into the night shift, all of them informational.
Baptiste archived 130 controller diagnostics from atrium to cold storage; none bear on rollup behaviour.
Cabling survey on coldroom door B3 finished during the early shift; 159 terminations were re-dressed.
Ferrara reconciled the dockbay muster report against 188 badge-in events and found no gap.
Door controller C4 on eastwing was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 246 camera frames against the server-hall swipe log for the night shift and found no unattributed entries.
Escort refresher for the vault contractor cohort closed with 275 attendees; facilities holds the roster.
Okonkwo confirmed the atrium anti-passback timer stayed at the 304-second vendor default across the incident window.
Badge stock at the coldroom desk reconciled after the relief shift: 333 blanks issued, none unaccounted.
Baptiste closed the dockbay follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on eastwing recalibrated in 391 minutes during the night shift with no operator intervention.
Ferrara measured 20 ms of clock drift on the server-hall visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for vault listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on atrium door C2 after the rollout and saw nothing anomalous.
Locksmith callback for coldroom door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified dockbay monitoring resumed on the night shift 136 seconds after the controller restart.
Fire-panel interlock test on eastwing passed on the swing shift; Haugen logged the 165-second release delay.
Baptiste traced 194 orphaned reader heartbeats on server-hall to a patch-panel swap, not to the rollup.
> **Board decision (2026-05-06 - PAC-3314)** Okonkwo: entry timestamps (final, reversing PAC-3208). The entry instant is the `event_ms` field and the exit instant is `exit_ms`; `granted_at` is a controller-local unlock stamp that drifts per door and is NOT used by the rollup. A session's `dwell_ms` is `max(exit_ms - event_ms, 0)` on the merged session bounds.
Visitor pre-registration for vault processed 223 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on atrium: the strike alignment was within spec after 252 cycles.
Access-review queue for coldroom carried 281 items into the night shift, all of them informational.
Sato archived 310 controller diagnostics from dockbay to cold storage; none bear on rollup behaviour.
Cabling survey on eastwing door B3 finished during the early shift; 339 terminations were re-dressed.
Okonkwo reconciled the server-hall muster report against 368 badge-in events and found no gap.
Door controller C4 on vault was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 26 camera frames against the atrium swipe log for the night shift and found no unattributed entries.
Escort refresher for the coldroom contractor cohort closed with 55 attendees; facilities holds the roster.
Ferrara confirmed the dockbay anti-passback timer stayed at the 84-second vendor default across the incident window.
Badge stock at the eastwing desk reconciled after the relief shift: 113 blanks issued, none unaccounted.
Sato closed the server-hall follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on vault recalibrated in 171 minutes during the night shift with no operator intervention.
Okonkwo measured 200 ms of clock drift on the atrium visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for coldroom listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on dockbay door C2 after the rollout and saw nothing anomalous.
Locksmith callback for eastwing door C4 closed without action; the mechanical override was already compliant.
Ferrara verified server-hall monitoring resumed on the night shift 316 seconds after the controller restart.
Fire-panel interlock test on vault passed on the swing shift; Lindqvist logged the 345-second release delay.
Sato traced 374 orphaned reader heartbeats on atrium to a patch-panel swap, not to the rollup.
Visitor pre-registration for coldroom processed 403 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on dockbay: the strike alignment was within spec after 32 cycles.
Access-review queue for eastwing carried 61 items into the night shift, all of them informational.
Baptiste archived 90 controller diagnostics from server-hall to cold storage; none bear on rollup behaviour.
Cabling survey on vault door B3 finished during the early shift; 119 terminations were re-dressed.
Ferrara reconciled the atrium muster report against 148 badge-in events and found no gap.
Door controller C4 on coldroom was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 206 camera frames against the dockbay swipe log for the night shift and found no unattributed entries.
Escort refresher for the eastwing contractor cohort closed with 235 attendees; facilities holds the roster.
Okonkwo confirmed the server-hall anti-passback timer stayed at the 264-second vendor default across the incident window.
Badge stock at the vault desk reconciled after the relief shift: 293 blanks issued, none unaccounted.
Baptiste closed the atrium follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on coldroom recalibrated in 351 minutes during the night shift with no operator intervention.
Ferrara measured 380 ms of clock drift on the dockbay visitor kiosk, inside the tolerance the board set.

### Review entry 0047 — eastwing lane

Handover at the early boundary for eastwing listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on server-hall door C2 after the rollout and saw nothing anomalous.
Locksmith callback for vault door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified atrium monitoring resumed on the night shift 96 seconds after the controller restart.
Fire-panel interlock test on coldroom passed on the swing shift; Haugen logged the 125-second release delay.
Baptiste traced 154 orphaned reader heartbeats on dockbay to a patch-panel swap, not to the rollup.
Visitor pre-registration for eastwing processed 183 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on server-hall: the strike alignment was within spec after 212 cycles.
Access-review queue for vault carried 241 items into the night shift, all of them informational.
Sato archived 270 controller diagnostics from atrium to cold storage; none bear on rollup behaviour.
Cabling survey on coldroom door B3 finished during the early shift; 299 terminations were re-dressed.
Okonkwo reconciled the dockbay muster report against 328 badge-in events and found no gap.
Door controller C4 on eastwing was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 386 camera frames against the server-hall swipe log for the night shift and found no unattributed entries.
Escort refresher for the vault contractor cohort closed with 415 attendees; facilities holds the roster.
Ferrara confirmed the atrium anti-passback timer stayed at the 44-second vendor default across the incident window.
Badge stock at the coldroom desk reconciled after the relief shift: 73 blanks issued, none unaccounted.
Sato closed the dockbay follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on eastwing recalibrated in 131 minutes during the night shift with no operator intervention.
Okonkwo measured 160 ms of clock drift on the server-hall visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for vault listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on atrium door C2 after the rollout and saw nothing anomalous.
Locksmith callback for coldroom door C4 closed without action; the mechanical override was already compliant.
Ferrara verified dockbay monitoring resumed on the night shift 276 seconds after the controller restart.
Fire-panel interlock test on eastwing passed on the swing shift; Lindqvist logged the 305-second release delay.
Sato traced 334 orphaned reader heartbeats on server-hall to a patch-panel swap, not to the rollup.
Visitor pre-registration for vault processed 363 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on atrium: the strike alignment was within spec after 392 cycles.
Access-review queue for coldroom carried 21 items into the night shift, all of them informational.
Baptiste archived 50 controller diagnostics from dockbay to cold storage; none bear on rollup behaviour.
Cabling survey on eastwing door B3 finished during the early shift; 79 terminations were re-dressed.
Ferrara reconciled the server-hall muster report against 108 badge-in events and found no gap.
Door controller C4 on vault was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 166 camera frames against the atrium swipe log for the night shift and found no unattributed entries.
Escort refresher for the coldroom contractor cohort closed with 195 attendees; facilities holds the roster.
Okonkwo confirmed the dockbay anti-passback timer stayed at the 224-second vendor default across the incident window.
Badge stock at the eastwing desk reconciled after the relief shift: 253 blanks issued, none unaccounted.
Baptiste closed the server-hall follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
> **Board decision (2026-05-07 - PAC-3316)** Lindqvist: canonicalization (final, reversing PAC-3210). `badge_class` is normalized with `str(...).strip().lower()`; a value that is not one of `privileged`, `contractor`, `staff`, `visitor` FALLS BACK to `visitor`, the lowest class — not to the nearest match and not to a separate bucket. `zone` is `str(...).strip().lower()` and empty becomes `unknown`; `door` collapses internal whitespace via `' '.join(str(...).split())`. `revoked` is parsed as booleans unchanged, the strings `true`/`1`/`yes` after `str(...).strip().lower()` as true, all other strings false, and any other value via Python `bool(value)`.
Turnstile A2 on vault recalibrated in 311 minutes during the night shift with no operator intervention.
Ferrara measured 340 ms of clock drift on the atrium visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for coldroom listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on dockbay door C2 after the rollout and saw nothing anomalous.
Locksmith callback for eastwing door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified server-hall monitoring resumed on the night shift 56 seconds after the controller restart.
Fire-panel interlock test on vault passed on the swing shift; Haugen logged the 85-second release delay.
Baptiste traced 114 orphaned reader heartbeats on atrium to a patch-panel swap, not to the rollup.
Visitor pre-registration for coldroom processed 143 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on dockbay: the strike alignment was within spec after 172 cycles.
Access-review queue for eastwing carried 201 items into the night shift, all of them informational.
Sato archived 230 controller diagnostics from server-hall to cold storage; none bear on rollup behaviour.
Cabling survey on vault door B3 finished during the early shift; 259 terminations were re-dressed.
Okonkwo reconciled the atrium muster report against 288 badge-in events and found no gap.
Door controller C4 on coldroom was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 346 camera frames against the dockbay swipe log for the night shift and found no unattributed entries.
Escort refresher for the eastwing contractor cohort closed with 375 attendees; facilities holds the roster.
Ferrara confirmed the server-hall anti-passback timer stayed at the 404-second vendor default across the incident window.
Badge stock at the vault desk reconciled after the relief shift: 33 blanks issued, none unaccounted.
Sato closed the atrium follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on coldroom recalibrated in 91 minutes during the night shift with no operator intervention.
Okonkwo measured 120 ms of clock drift on the dockbay visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for eastwing listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on server-hall door C2 after the rollout and saw nothing anomalous.
Locksmith callback for vault door C4 closed without action; the mechanical override was already compliant.
Ferrara verified atrium monitoring resumed on the night shift 236 seconds after the controller restart.
Fire-panel interlock test on coldroom passed on the swing shift; Lindqvist logged the 265-second release delay.
Sato traced 294 orphaned reader heartbeats on dockbay to a patch-panel swap, not to the rollup.
Visitor pre-registration for eastwing processed 323 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on server-hall: the strike alignment was within spec after 352 cycles.
Access-review queue for vault carried 381 items into the night shift, all of them informational.
Baptiste archived 410 controller diagnostics from atrium to cold storage; none bear on rollup behaviour.
Cabling survey on coldroom door B3 finished during the early shift; 39 terminations were re-dressed.
Ferrara reconciled the dockbay muster report against 68 badge-in events and found no gap.

### Review entry 0051 — server-hall lane

Door controller C4 on eastwing was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 126 camera frames against the server-hall swipe log for the night shift and found no unattributed entries.
Escort refresher for the vault contractor cohort closed with 155 attendees; facilities holds the roster.
Okonkwo confirmed the atrium anti-passback timer stayed at the 184-second vendor default across the incident window.
Badge stock at the coldroom desk reconciled after the relief shift: 213 blanks issued, none unaccounted.
Baptiste closed the dockbay follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on eastwing recalibrated in 271 minutes during the night shift with no operator intervention.
Ferrara measured 300 ms of clock drift on the server-hall visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for vault listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on atrium door C2 after the rollout and saw nothing anomalous.
Locksmith callback for coldroom door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified dockbay monitoring resumed on the night shift 416 seconds after the controller restart.
Fire-panel interlock test on eastwing passed on the swing shift; Haugen logged the 45-second release delay.
Baptiste traced 74 orphaned reader heartbeats on server-hall to a patch-panel swap, not to the rollup.
Visitor pre-registration for vault processed 103 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on atrium: the strike alignment was within spec after 132 cycles.
Access-review queue for coldroom carried 161 items into the night shift, all of them informational.
Sato archived 190 controller diagnostics from dockbay to cold storage; none bear on rollup behaviour.
Cabling survey on eastwing door B3 finished during the early shift; 219 terminations were re-dressed.
Okonkwo reconciled the server-hall muster report against 248 badge-in events and found no gap.
Door controller C4 on vault was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 306 camera frames against the atrium swipe log for the night shift and found no unattributed entries.
Escort refresher for the coldroom contractor cohort closed with 335 attendees; facilities holds the roster.
Ferrara confirmed the dockbay anti-passback timer stayed at the 364-second vendor default across the incident window.
Badge stock at the eastwing desk reconciled after the relief shift: 393 blanks issued, none unaccounted.
Sato closed the server-hall follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on vault recalibrated in 51 minutes during the night shift with no operator intervention.
Okonkwo measured 80 ms of clock drift on the atrium visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for coldroom listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on dockbay door C2 after the rollout and saw nothing anomalous.
Locksmith callback for eastwing door C4 closed without action; the mechanical override was already compliant.
Ferrara verified server-hall monitoring resumed on the night shift 196 seconds after the controller restart.
Fire-panel interlock test on vault passed on the swing shift; Lindqvist logged the 225-second release delay.
Sato traced 254 orphaned reader heartbeats on atrium to a patch-panel swap, not to the rollup.
Visitor pre-registration for coldroom processed 283 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on dockbay: the strike alignment was within spec after 312 cycles.
Access-review queue for eastwing carried 341 items into the night shift, all of them informational.
Baptiste archived 370 controller diagnostics from server-hall to cold storage; none bear on rollup behaviour.
> **Board decision (2026-05-08 - PAC-3318)** Baptiste: duplicate swipe rows (final, REVERSING PAC-3212). Repeated `swipe_id` values arrive when a reader retries an unlock, and the retry re-stamps the credential at the higher class before the escort has confirmed it. So on a duplicate the LOWER badge class wins, not the higher. Resolve in order: keep the greater `event_ms`; on a tie the LOWER badge class by the ranking privileged > contractor > staff > visitor; then the LONGER normalized door string; then the lexicographically greater zone. Deduplication happens BEFORE any count, aggregate or checksum.
Cabling survey on vault door B3 finished during the early shift; 399 terminations were re-dressed.
Ferrara reconciled the atrium muster report against 28 badge-in events and found no gap.
Door controller C4 on coldroom was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 86 camera frames against the dockbay swipe log for the night shift and found no unattributed entries.
Escort refresher for the eastwing contractor cohort closed with 115 attendees; facilities holds the roster.
Okonkwo confirmed the server-hall anti-passback timer stayed at the 144-second vendor default across the incident window.
Badge stock at the vault desk reconciled after the relief shift: 173 blanks issued, none unaccounted.
Baptiste closed the atrium follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on coldroom recalibrated in 231 minutes during the night shift with no operator intervention.
Ferrara measured 260 ms of clock drift on the dockbay visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for eastwing listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on server-hall door C2 after the rollout and saw nothing anomalous.
Locksmith callback for vault door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified atrium monitoring resumed on the night shift 376 seconds after the controller restart.
Fire-panel interlock test on coldroom passed on the swing shift; Haugen logged the 405-second release delay.
Baptiste traced 34 orphaned reader heartbeats on dockbay to a patch-panel swap, not to the rollup.
Visitor pre-registration for eastwing processed 63 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on server-hall: the strike alignment was within spec after 92 cycles.
Access-review queue for vault carried 121 items into the night shift, all of them informational.
Sato archived 150 controller diagnostics from atrium to cold storage; none bear on rollup behaviour.
Cabling survey on coldroom door B3 finished during the early shift; 179 terminations were re-dressed.
Okonkwo reconciled the dockbay muster report against 208 badge-in events and found no gap.
Door controller C4 on eastwing was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 266 camera frames against the server-hall swipe log for the night shift and found no unattributed entries.
Escort refresher for the vault contractor cohort closed with 295 attendees; facilities holds the roster.
Ferrara confirmed the atrium anti-passback timer stayed at the 324-second vendor default across the incident window.
Badge stock at the coldroom desk reconciled after the relief shift: 353 blanks issued, none unaccounted.
Sato closed the dockbay follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on eastwing recalibrated in 411 minutes during the night shift with no operator intervention.
Okonkwo measured 40 ms of clock drift on the server-hall visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for vault listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on atrium door C2 after the rollout and saw nothing anomalous.
Locksmith callback for coldroom door C4 closed without action; the mechanical override was already compliant.
Ferrara verified dockbay monitoring resumed on the night shift 156 seconds after the controller restart.

### Review entry 0055 — vault lane

Fire-panel interlock test on eastwing passed on the swing shift; Lindqvist logged the 185-second release delay.
Sato traced 214 orphaned reader heartbeats on server-hall to a patch-panel swap, not to the rollup.
Visitor pre-registration for vault processed 243 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on atrium: the strike alignment was within spec after 272 cycles.
Access-review queue for coldroom carried 301 items into the night shift, all of them informational.
Baptiste archived 330 controller diagnostics from dockbay to cold storage; none bear on rollup behaviour.
Cabling survey on eastwing door B3 finished during the early shift; 359 terminations were re-dressed.
Ferrara reconciled the server-hall muster report against 388 badge-in events and found no gap.
Door controller C4 on vault was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 46 camera frames against the atrium swipe log for the night shift and found no unattributed entries.
Escort refresher for the coldroom contractor cohort closed with 75 attendees; facilities holds the roster.
Okonkwo confirmed the dockbay anti-passback timer stayed at the 104-second vendor default across the incident window.
Badge stock at the eastwing desk reconciled after the relief shift: 133 blanks issued, none unaccounted.
Baptiste closed the server-hall follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on vault recalibrated in 191 minutes during the night shift with no operator intervention.
Ferrara measured 220 ms of clock drift on the atrium visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for coldroom listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on dockbay door C2 after the rollout and saw nothing anomalous.
Locksmith callback for eastwing door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified server-hall monitoring resumed on the night shift 336 seconds after the controller restart.
Fire-panel interlock test on vault passed on the swing shift; Haugen logged the 365-second release delay.
Baptiste traced 394 orphaned reader heartbeats on atrium to a patch-panel swap, not to the rollup.
Visitor pre-registration for coldroom processed 23 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on dockbay: the strike alignment was within spec after 52 cycles.
Access-review queue for eastwing carried 81 items into the night shift, all of them informational.
Sato archived 110 controller diagnostics from server-hall to cold storage; none bear on rollup behaviour.
Cabling survey on vault door B3 finished during the early shift; 139 terminations were re-dressed.
Okonkwo reconciled the atrium muster report against 168 badge-in events and found no gap.
Door controller C4 on coldroom was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 226 camera frames against the dockbay swipe log for the night shift and found no unattributed entries.
Escort refresher for the eastwing contractor cohort closed with 255 attendees; facilities holds the roster.
Ferrara confirmed the server-hall anti-passback timer stayed at the 284-second vendor default across the incident window.
Badge stock at the vault desk reconciled after the relief shift: 313 blanks issued, none unaccounted.
Sato closed the atrium follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on coldroom recalibrated in 371 minutes during the night shift with no operator intervention.
Okonkwo measured 400 ms of clock drift on the dockbay visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for eastwing listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on server-hall door C2 after the rollout and saw nothing anomalous.
> **Board decision (2026-05-11 - PAC-3320)** Moreau: session stitching (final, revising PAC-3244). The stitch gap is retuned to 140 ms: swipes merge into one occupancy session while `next.event_ms <= current.end_ms + 140`. The 60 ms allowance assumed a badge-and-walk cadence the Northgate doors do not have, and it was splitting single occupancies in two. Sessions are built per zone over canonical rows in `event_ms` order.
Locksmith callback for vault door C4 closed without action; the mechanical override was already compliant.
Ferrara verified atrium monitoring resumed on the night shift 116 seconds after the controller restart.
Fire-panel interlock test on coldroom passed on the swing shift; Lindqvist logged the 145-second release delay.
Sato traced 174 orphaned reader heartbeats on dockbay to a patch-panel swap, not to the rollup.
Visitor pre-registration for eastwing processed 203 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on server-hall: the strike alignment was within spec after 232 cycles.
Access-review queue for vault carried 261 items into the night shift, all of them informational.
Baptiste archived 290 controller diagnostics from atrium to cold storage; none bear on rollup behaviour.
Cabling survey on coldroom door B3 finished during the early shift; 319 terminations were re-dressed.
Ferrara reconciled the dockbay muster report against 348 badge-in events and found no gap.
Door controller C4 on eastwing was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 406 camera frames against the server-hall swipe log for the night shift and found no unattributed entries.
Escort refresher for the vault contractor cohort closed with 35 attendees; facilities holds the roster.
Okonkwo confirmed the atrium anti-passback timer stayed at the 64-second vendor default across the incident window.
Badge stock at the coldroom desk reconciled after the relief shift: 93 blanks issued, none unaccounted.
Baptiste closed the dockbay follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on eastwing recalibrated in 151 minutes during the night shift with no operator intervention.
Ferrara measured 180 ms of clock drift on the server-hall visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for vault listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on atrium door C2 after the rollout and saw nothing anomalous.
Locksmith callback for coldroom door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified dockbay monitoring resumed on the night shift 296 seconds after the controller restart.
Fire-panel interlock test on eastwing passed on the swing shift; Haugen logged the 325-second release delay.
Baptiste traced 354 orphaned reader heartbeats on server-hall to a patch-panel swap, not to the rollup.
Visitor pre-registration for vault processed 383 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on atrium: the strike alignment was within spec after 412 cycles.
Access-review queue for coldroom carried 41 items into the night shift, all of them informational.
Sato archived 70 controller diagnostics from dockbay to cold storage; none bear on rollup behaviour.
Cabling survey on eastwing door B3 finished during the early shift; 99 terminations were re-dressed.
Okonkwo reconciled the server-hall muster report against 128 badge-in events and found no gap.
Door controller C4 on vault was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 186 camera frames against the atrium swipe log for the night shift and found no unattributed entries.
Escort refresher for the coldroom contractor cohort closed with 215 attendees; facilities holds the roster.
Ferrara confirmed the dockbay anti-passback timer stayed at the 244-second vendor default across the incident window.

### Review entry 0059 — atrium lane

Badge stock at the eastwing desk reconciled after the relief shift: 273 blanks issued, none unaccounted.
Sato closed the server-hall follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on vault recalibrated in 331 minutes during the night shift with no operator intervention.
Okonkwo measured 360 ms of clock drift on the atrium visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for coldroom listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on dockbay door C2 after the rollout and saw nothing anomalous.
Locksmith callback for eastwing door C4 closed without action; the mechanical override was already compliant.
Ferrara verified server-hall monitoring resumed on the night shift 76 seconds after the controller restart.
Fire-panel interlock test on vault passed on the swing shift; Lindqvist logged the 105-second release delay.
Sato traced 134 orphaned reader heartbeats on atrium to a patch-panel swap, not to the rollup.
Visitor pre-registration for coldroom processed 163 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on dockbay: the strike alignment was within spec after 192 cycles.
Access-review queue for eastwing carried 221 items into the night shift, all of them informational.
Baptiste archived 250 controller diagnostics from server-hall to cold storage; none bear on rollup behaviour.
Cabling survey on vault door B3 finished during the early shift; 279 terminations were re-dressed.
Ferrara reconciled the atrium muster report against 308 badge-in events and found no gap.
Door controller C4 on coldroom was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 366 camera frames against the dockbay swipe log for the night shift and found no unattributed entries.
Escort refresher for the eastwing contractor cohort closed with 395 attendees; facilities holds the roster.
Okonkwo confirmed the server-hall anti-passback timer stayed at the 24-second vendor default across the incident window.
Badge stock at the vault desk reconciled after the relief shift: 53 blanks issued, none unaccounted.
Baptiste closed the atrium follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on coldroom recalibrated in 111 minutes during the night shift with no operator intervention.
Ferrara measured 140 ms of clock drift on the dockbay visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for eastwing listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on server-hall door C2 after the rollout and saw nothing anomalous.
Locksmith callback for vault door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified atrium monitoring resumed on the night shift 256 seconds after the controller restart.
Fire-panel interlock test on coldroom passed on the swing shift; Haugen logged the 285-second release delay.
Baptiste traced 314 orphaned reader heartbeats on dockbay to a patch-panel swap, not to the rollup.
Visitor pre-registration for eastwing processed 343 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on server-hall: the strike alignment was within spec after 372 cycles.
Access-review queue for vault carried 401 items into the night shift, all of them informational.
Sato archived 30 controller diagnostics from atrium to cold storage; none bear on rollup behaviour.
Cabling survey on coldroom door B3 finished during the early shift; 59 terminations were re-dressed.
Okonkwo reconciled the dockbay muster report against 88 badge-in events and found no gap.
Door controller C4 on eastwing was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 146 camera frames against the server-hall swipe log for the night shift and found no unattributed entries.
> **Board decision (2026-05-13 - PAC-3322)** Delacroix: revoked badges (final, revising PAC-3252). Revoked badges are NOT dropped from the input. They are excluded from session construction only — they open no occupancy and join no queue — but they are still counted in `class_counts` and reported in `revoked_excluded_count`. A rollup that filters them at load time undercounts the class distribution.
Escort refresher for the vault contractor cohort closed with 175 attendees; facilities holds the roster.
Ferrara confirmed the atrium anti-passback timer stayed at the 204-second vendor default across the incident window.
Badge stock at the coldroom desk reconciled after the relief shift: 233 blanks issued, none unaccounted.
Sato closed the dockbay follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on eastwing recalibrated in 291 minutes during the night shift with no operator intervention.
Okonkwo measured 320 ms of clock drift on the server-hall visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for vault listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on atrium door C2 after the rollout and saw nothing anomalous.
Locksmith callback for coldroom door C4 closed without action; the mechanical override was already compliant.
Ferrara verified dockbay monitoring resumed on the night shift 36 seconds after the controller restart.
Fire-panel interlock test on eastwing passed on the swing shift; Lindqvist logged the 65-second release delay.
Sato traced 94 orphaned reader heartbeats on server-hall to a patch-panel swap, not to the rollup.
Visitor pre-registration for vault processed 123 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on atrium: the strike alignment was within spec after 152 cycles.
Access-review queue for coldroom carried 181 items into the night shift, all of them informational.
Baptiste archived 210 controller diagnostics from dockbay to cold storage; none bear on rollup behaviour.
Cabling survey on eastwing door B3 finished during the early shift; 239 terminations were re-dressed.
Ferrara reconciled the server-hall muster report against 268 badge-in events and found no gap.
Door controller C4 on vault was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 326 camera frames against the atrium swipe log for the night shift and found no unattributed entries.
Escort refresher for the coldroom contractor cohort closed with 355 attendees; facilities holds the roster.
Okonkwo confirmed the dockbay anti-passback timer stayed at the 384-second vendor default across the incident window.
Badge stock at the eastwing desk reconciled after the relief shift: 413 blanks issued, none unaccounted.
Baptiste closed the server-hall follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on vault recalibrated in 71 minutes during the night shift with no operator intervention.
Ferrara measured 100 ms of clock drift on the atrium visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for coldroom listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on dockbay door C2 after the rollout and saw nothing anomalous.
Locksmith callback for eastwing door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified server-hall monitoring resumed on the night shift 216 seconds after the controller restart.
Fire-panel interlock test on vault passed on the swing shift; Haugen logged the 245-second release delay.
Baptiste traced 274 orphaned reader heartbeats on atrium to a patch-panel swap, not to the rollup.
Visitor pre-registration for coldroom processed 303 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on dockbay: the strike alignment was within spec after 332 cycles.

### Review entry 0063 — coldroom lane

Access-review queue for eastwing carried 361 items into the night shift, all of them informational.
Sato archived 390 controller diagnostics from server-hall to cold storage; none bear on rollup behaviour.
Cabling survey on vault door B3 finished during the early shift; 19 terminations were re-dressed.
Okonkwo reconciled the atrium muster report against 48 badge-in events and found no gap.
Door controller C4 on coldroom was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 106 camera frames against the dockbay swipe log for the night shift and found no unattributed entries.
Escort refresher for the eastwing contractor cohort closed with 135 attendees; facilities holds the roster.
Ferrara confirmed the server-hall anti-passback timer stayed at the 164-second vendor default across the incident window.
Badge stock at the vault desk reconciled after the relief shift: 193 blanks issued, none unaccounted.
Sato closed the atrium follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on coldroom recalibrated in 251 minutes during the night shift with no operator intervention.
Okonkwo measured 280 ms of clock drift on the dockbay visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for eastwing listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on server-hall door C2 after the rollout and saw nothing anomalous.
Locksmith callback for vault door C4 closed without action; the mechanical override was already compliant.
Ferrara verified atrium monitoring resumed on the night shift 396 seconds after the controller restart.
Fire-panel interlock test on coldroom passed on the swing shift; Lindqvist logged the 25-second release delay.
Sato traced 54 orphaned reader heartbeats on dockbay to a patch-panel swap, not to the rollup.
Visitor pre-registration for eastwing processed 83 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on server-hall: the strike alignment was within spec after 112 cycles.
Access-review queue for vault carried 141 items into the night shift, all of them informational.
Baptiste archived 170 controller diagnostics from atrium to cold storage; none bear on rollup behaviour.
Cabling survey on coldroom door B3 finished during the early shift; 199 terminations were re-dressed.
Ferrara reconciled the dockbay muster report against 228 badge-in events and found no gap.
Door controller C4 on eastwing was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 286 camera frames against the server-hall swipe log for the night shift and found no unattributed entries.
Escort refresher for the vault contractor cohort closed with 315 attendees; facilities holds the roster.
Okonkwo confirmed the atrium anti-passback timer stayed at the 344-second vendor default across the incident window.
Badge stock at the coldroom desk reconciled after the relief shift: 373 blanks issued, none unaccounted.
Baptiste closed the dockbay follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on eastwing recalibrated in 31 minutes during the night shift with no operator intervention.
Ferrara measured 60 ms of clock drift on the server-hall visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for vault listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on atrium door C2 after the rollout and saw nothing anomalous.
Locksmith callback for coldroom door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified dockbay monitoring resumed on the night shift 176 seconds after the controller restart.
Fire-panel interlock test on eastwing passed on the swing shift; Haugen logged the 205-second release delay.
Baptiste traced 234 orphaned reader heartbeats on server-hall to a patch-panel swap, not to the rollup.
> **Board decision (2026-05-14 - PAC-3324)** Ferrara: occupancy ledger (final, revising PAC-3246). Carry propagates between consecutive sessions in a zone. `idle_gap_ms` is `max(current.start_ms - previous.end_ms, 0)`; `carry_in_ms = max(previous_carry_out_ms - ceil(idle_gap_ms / 4), 0)` — the idle decay ROUNDS UP; `ledger_dwell_ms = adjusted_dwell_ms + (carry_in_ms // 5)` — the carry credit is FLOORED; `carry_out_ms = min(carry_in_ms + adjusted_dwell_ms + swipe_count * 6, 780)`. The carry-out cap is retuned to 780 ms; the 2000 ms bound recorded in PAC-3246 never bound and is superseded. ROUNDING: idle_gap_ms // 4 = CEIL. ROUNDING: carry_in_ms // 5 = FLOOR.
Visitor pre-registration for vault processed 263 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on atrium: the strike alignment was within spec after 292 cycles.
Access-review queue for coldroom carried 321 items into the night shift, all of them informational.
Sato archived 350 controller diagnostics from dockbay to cold storage; none bear on rollup behaviour.
Cabling survey on eastwing door B3 finished during the early shift; 379 terminations were re-dressed.
Okonkwo reconciled the server-hall muster report against 408 badge-in events and found no gap.
Door controller C4 on vault was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 66 camera frames against the atrium swipe log for the night shift and found no unattributed entries.
Escort refresher for the coldroom contractor cohort closed with 95 attendees; facilities holds the roster.
Ferrara confirmed the dockbay anti-passback timer stayed at the 124-second vendor default across the incident window.
Badge stock at the eastwing desk reconciled after the relief shift: 153 blanks issued, none unaccounted.
Sato closed the server-hall follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on vault recalibrated in 211 minutes during the night shift with no operator intervention.
Okonkwo measured 240 ms of clock drift on the atrium visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for coldroom listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on dockbay door C2 after the rollout and saw nothing anomalous.
Locksmith callback for eastwing door C4 closed without action; the mechanical override was already compliant.
Ferrara verified server-hall monitoring resumed on the night shift 356 seconds after the controller restart.
Fire-panel interlock test on vault passed on the swing shift; Lindqvist logged the 385-second release delay.
Sato traced 414 orphaned reader heartbeats on atrium to a patch-panel swap, not to the rollup.
Visitor pre-registration for coldroom processed 43 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on dockbay: the strike alignment was within spec after 72 cycles.
Access-review queue for eastwing carried 101 items into the night shift, all of them informational.
Baptiste archived 130 controller diagnostics from server-hall to cold storage; none bear on rollup behaviour.
Cabling survey on vault door B3 finished during the early shift; 159 terminations were re-dressed.
Ferrara reconciled the atrium muster report against 188 badge-in events and found no gap.
Door controller C4 on coldroom was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 246 camera frames against the dockbay swipe log for the night shift and found no unattributed entries.
Escort refresher for the eastwing contractor cohort closed with 275 attendees; facilities holds the roster.
Okonkwo confirmed the server-hall anti-passback timer stayed at the 304-second vendor default across the incident window.
Badge stock at the vault desk reconciled after the relief shift: 333 blanks issued, none unaccounted.
Baptiste closed the atrium follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on coldroom recalibrated in 391 minutes during the night shift with no operator intervention.
Ferrara measured 20 ms of clock drift on the dockbay visitor kiosk, inside the tolerance the board set.

### Review entry 0067 — dockbay lane

Handover at the early boundary for eastwing listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on server-hall door C2 after the rollout and saw nothing anomalous.
Locksmith callback for vault door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified atrium monitoring resumed on the night shift 136 seconds after the controller restart.
Fire-panel interlock test on coldroom passed on the swing shift; Haugen logged the 165-second release delay.
Baptiste traced 194 orphaned reader heartbeats on dockbay to a patch-panel swap, not to the rollup.
Visitor pre-registration for eastwing processed 223 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on server-hall: the strike alignment was within spec after 252 cycles.
Access-review queue for vault carried 281 items into the night shift, all of them informational.
Sato archived 310 controller diagnostics from atrium to cold storage; none bear on rollup behaviour.
Cabling survey on coldroom door B3 finished during the early shift; 339 terminations were re-dressed.
Okonkwo reconciled the dockbay muster report against 368 badge-in events and found no gap.
Door controller C4 on eastwing was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 26 camera frames against the server-hall swipe log for the night shift and found no unattributed entries.
Escort refresher for the vault contractor cohort closed with 55 attendees; facilities holds the roster.
Ferrara confirmed the atrium anti-passback timer stayed at the 84-second vendor default across the incident window.
Badge stock at the coldroom desk reconciled after the relief shift: 113 blanks issued, none unaccounted.
Sato closed the dockbay follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on eastwing recalibrated in 171 minutes during the night shift with no operator intervention.
Okonkwo measured 200 ms of clock drift on the server-hall visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for vault listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on atrium door C2 after the rollout and saw nothing anomalous.
Locksmith callback for coldroom door C4 closed without action; the mechanical override was already compliant.
Ferrara verified dockbay monitoring resumed on the night shift 316 seconds after the controller restart.
Fire-panel interlock test on eastwing passed on the swing shift; Lindqvist logged the 345-second release delay.
Sato traced 374 orphaned reader heartbeats on server-hall to a patch-panel swap, not to the rollup.
Visitor pre-registration for vault processed 403 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on atrium: the strike alignment was within spec after 32 cycles.
Access-review queue for coldroom carried 61 items into the night shift, all of them informational.
Baptiste archived 90 controller diagnostics from dockbay to cold storage; none bear on rollup behaviour.
Cabling survey on eastwing door B3 finished during the early shift; 119 terminations were re-dressed.
Ferrara reconciled the server-hall muster report against 148 badge-in events and found no gap.
Door controller C4 on vault was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 206 camera frames against the atrium swipe log for the night shift and found no unattributed entries.
Escort refresher for the coldroom contractor cohort closed with 235 attendees; facilities holds the roster.
Okonkwo confirmed the dockbay anti-passback timer stayed at the 264-second vendor default across the incident window.
Badge stock at the eastwing desk reconciled after the relief shift: 293 blanks issued, none unaccounted.
Baptiste closed the server-hall follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
> **Board decision (2026-05-18 - PAC-3326)** Haugen: control-window scope (final, revising PAC-3248). For each layer, a session uses the windows recorded for its OWN `top_class`. Only a class with NO window of its own in that layer falls back to the `all`-scoped windows; a class that has its own entry does NOT additionally inherit `all`. Windows are half-open `[start_ms, end_ms)` and each layer's spans are compacted before the overlap with the session is measured.
Turnstile A2 on vault recalibrated in 351 minutes during the night shift with no operator intervention.
Ferrara measured 380 ms of clock drift on the atrium visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for coldroom listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on dockbay door C2 after the rollout and saw nothing anomalous.
Locksmith callback for eastwing door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified server-hall monitoring resumed on the night shift 96 seconds after the controller restart.
Fire-panel interlock test on vault passed on the swing shift; Haugen logged the 125-second release delay.
Baptiste traced 154 orphaned reader heartbeats on atrium to a patch-panel swap, not to the rollup.
Visitor pre-registration for coldroom processed 183 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on dockbay: the strike alignment was within spec after 212 cycles.
Access-review queue for eastwing carried 241 items into the night shift, all of them informational.
Sato archived 270 controller diagnostics from server-hall to cold storage; none bear on rollup behaviour.
Cabling survey on vault door B3 finished during the early shift; 299 terminations were re-dressed.
Okonkwo reconciled the atrium muster report against 328 badge-in events and found no gap.
Door controller C4 on coldroom was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 386 camera frames against the dockbay swipe log for the night shift and found no unattributed entries.
Escort refresher for the eastwing contractor cohort closed with 415 attendees; facilities holds the roster.
Ferrara confirmed the server-hall anti-passback timer stayed at the 44-second vendor default across the incident window.
Badge stock at the vault desk reconciled after the relief shift: 73 blanks issued, none unaccounted.
Sato closed the atrium follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on coldroom recalibrated in 131 minutes during the night shift with no operator intervention.
Okonkwo measured 160 ms of clock drift on the dockbay visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for eastwing listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on server-hall door C2 after the rollout and saw nothing anomalous.
Locksmith callback for vault door C4 closed without action; the mechanical override was already compliant.
Ferrara verified atrium monitoring resumed on the night shift 276 seconds after the controller restart.
Fire-panel interlock test on coldroom passed on the swing shift; Lindqvist logged the 305-second release delay.
Sato traced 334 orphaned reader heartbeats on dockbay to a patch-panel swap, not to the rollup.
Visitor pre-registration for eastwing processed 363 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on server-hall: the strike alignment was within spec after 392 cycles.
Access-review queue for vault carried 21 items into the night shift, all of them informational.
Baptiste archived 50 controller diagnostics from atrium to cold storage; none bear on rollup behaviour.
Cabling survey on coldroom door B3 finished during the early shift; 79 terminations were re-dressed.
Ferrara reconciled the dockbay muster report against 108 badge-in events and found no gap.

### Review entry 0071 — eastwing lane

Door controller C4 on eastwing was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 166 camera frames against the server-hall swipe log for the night shift and found no unattributed entries.
Escort refresher for the vault contractor cohort closed with 195 attendees; facilities holds the roster.
Okonkwo confirmed the atrium anti-passback timer stayed at the 224-second vendor default across the incident window.
Badge stock at the coldroom desk reconciled after the relief shift: 253 blanks issued, none unaccounted.
Baptiste closed the dockbay follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on eastwing recalibrated in 311 minutes during the night shift with no operator intervention.
Ferrara measured 340 ms of clock drift on the server-hall visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for vault listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on atrium door C2 after the rollout and saw nothing anomalous.
Locksmith callback for coldroom door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified dockbay monitoring resumed on the night shift 56 seconds after the controller restart.
Fire-panel interlock test on eastwing passed on the swing shift; Haugen logged the 85-second release delay.
Baptiste traced 114 orphaned reader heartbeats on server-hall to a patch-panel swap, not to the rollup.
Visitor pre-registration for vault processed 143 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on atrium: the strike alignment was within spec after 172 cycles.
Access-review queue for coldroom carried 201 items into the night shift, all of them informational.
Sato archived 230 controller diagnostics from dockbay to cold storage; none bear on rollup behaviour.
Cabling survey on eastwing door B3 finished during the early shift; 259 terminations were re-dressed.
Okonkwo reconciled the server-hall muster report against 288 badge-in events and found no gap.
Door controller C4 on vault was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 346 camera frames against the atrium swipe log for the night shift and found no unattributed entries.
Escort refresher for the coldroom contractor cohort closed with 375 attendees; facilities holds the roster.
Ferrara confirmed the dockbay anti-passback timer stayed at the 404-second vendor default across the incident window.
Badge stock at the eastwing desk reconciled after the relief shift: 33 blanks issued, none unaccounted.
Sato closed the server-hall follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on vault recalibrated in 91 minutes during the night shift with no operator intervention.
Okonkwo measured 120 ms of clock drift on the atrium visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for coldroom listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on dockbay door C2 after the rollout and saw nothing anomalous.
Locksmith callback for eastwing door C4 closed without action; the mechanical override was already compliant.
Ferrara verified server-hall monitoring resumed on the night shift 236 seconds after the controller restart.
Fire-panel interlock test on vault passed on the swing shift; Lindqvist logged the 265-second release delay.
Sato traced 294 orphaned reader heartbeats on atrium to a patch-panel swap, not to the rollup.
Visitor pre-registration for coldroom processed 323 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on dockbay: the strike alignment was within spec after 352 cycles.
Access-review queue for eastwing carried 381 items into the night shift, all of them informational.
Baptiste archived 410 controller diagnostics from server-hall to cold storage; none bear on rollup behaviour.
> **Board decision (2026-05-20 - PAC-3328)** Sato: layer precedence (final, revising PAC-3250). LOCKDOWN takes precedence where both layers cover the same instant: time already charged as lockdown is not charged again as maintenance. Compute each layer's compacted overlap with the session, subtract the shared span from the maintenance side, then `adjusted_dwell_ms = max(dwell_ms - ceil(lockdown_overlap_ms / 2) - (maintenance_used_ms // 3), 0)`. The lockdown half ROUNDS UP and the maintenance half is FLOORED. Both `lockdown_overlap_ms` and `maintenance_overlap_ms` are REPORTED unadjusted, from each layer's own compacted union. ROUNDING: lockdown_overlap_ms // 2 = CEIL. ROUNDING: maintenance_used_ms // 3 = FLOOR.
Cabling survey on vault door B3 finished during the early shift; 39 terminations were re-dressed.
Ferrara reconciled the atrium muster report against 68 badge-in events and found no gap.
Door controller C4 on coldroom was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 126 camera frames against the dockbay swipe log for the night shift and found no unattributed entries.
Escort refresher for the eastwing contractor cohort closed with 155 attendees; facilities holds the roster.
Okonkwo confirmed the server-hall anti-passback timer stayed at the 184-second vendor default across the incident window.
Badge stock at the vault desk reconciled after the relief shift: 213 blanks issued, none unaccounted.
Baptiste closed the atrium follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on coldroom recalibrated in 271 minutes during the night shift with no operator intervention.
Ferrara measured 300 ms of clock drift on the dockbay visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for eastwing listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on server-hall door C2 after the rollout and saw nothing anomalous.
Locksmith callback for vault door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified atrium monitoring resumed on the night shift 416 seconds after the controller restart.
Fire-panel interlock test on coldroom passed on the swing shift; Haugen logged the 45-second release delay.
Baptiste traced 74 orphaned reader heartbeats on dockbay to a patch-panel swap, not to the rollup.
Visitor pre-registration for eastwing processed 103 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on server-hall: the strike alignment was within spec after 132 cycles.
Access-review queue for vault carried 161 items into the night shift, all of them informational.
Sato archived 190 controller diagnostics from atrium to cold storage; none bear on rollup behaviour.
Cabling survey on coldroom door B3 finished during the early shift; 219 terminations were re-dressed.
Okonkwo reconciled the dockbay muster report against 248 badge-in events and found no gap.
Door controller C4 on eastwing was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 306 camera frames against the server-hall swipe log for the night shift and found no unattributed entries.
Escort refresher for the vault contractor cohort closed with 335 attendees; facilities holds the roster.
Ferrara confirmed the atrium anti-passback timer stayed at the 364-second vendor default across the incident window.
Badge stock at the coldroom desk reconciled after the relief shift: 393 blanks issued, none unaccounted.
Sato closed the dockbay follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on eastwing recalibrated in 51 minutes during the night shift with no operator intervention.
Okonkwo measured 80 ms of clock drift on the server-hall visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for vault listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on atrium door C2 after the rollout and saw nothing anomalous.
Locksmith callback for coldroom door C4 closed without action; the mechanical override was already compliant.
Ferrara verified dockbay monitoring resumed on the night shift 196 seconds after the controller restart.

### Review entry 0075 — server-hall lane

Fire-panel interlock test on eastwing passed on the swing shift; Lindqvist logged the 225-second release delay.
Sato traced 254 orphaned reader heartbeats on server-hall to a patch-panel swap, not to the rollup.
Visitor pre-registration for vault processed 283 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on atrium: the strike alignment was within spec after 312 cycles.
Access-review queue for coldroom carried 341 items into the night shift, all of them informational.
Baptiste archived 370 controller diagnostics from dockbay to cold storage; none bear on rollup behaviour.
Cabling survey on eastwing door B3 finished during the early shift; 399 terminations were re-dressed.
Ferrara reconciled the server-hall muster report against 28 badge-in events and found no gap.
Door controller C4 on vault was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 86 camera frames against the atrium swipe log for the night shift and found no unattributed entries.
Escort refresher for the coldroom contractor cohort closed with 115 attendees; facilities holds the roster.
Okonkwo confirmed the dockbay anti-passback timer stayed at the 144-second vendor default across the incident window.
Badge stock at the eastwing desk reconciled after the relief shift: 173 blanks issued, none unaccounted.
Baptiste closed the server-hall follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on vault recalibrated in 231 minutes during the night shift with no operator intervention.
Ferrara measured 260 ms of clock drift on the atrium visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for coldroom listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on dockbay door C2 after the rollout and saw nothing anomalous.
Locksmith callback for eastwing door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified server-hall monitoring resumed on the night shift 376 seconds after the controller restart.
Fire-panel interlock test on vault passed on the swing shift; Haugen logged the 405-second release delay.
Baptiste traced 34 orphaned reader heartbeats on atrium to a patch-panel swap, not to the rollup.
Visitor pre-registration for coldroom processed 63 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on dockbay: the strike alignment was within spec after 92 cycles.
Access-review queue for eastwing carried 121 items into the night shift, all of them informational.
Sato archived 150 controller diagnostics from server-hall to cold storage; none bear on rollup behaviour.
Cabling survey on vault door B3 finished during the early shift; 179 terminations were re-dressed.
Okonkwo reconciled the atrium muster report against 208 badge-in events and found no gap.
Door controller C4 on coldroom was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 266 camera frames against the dockbay swipe log for the night shift and found no unattributed entries.
Escort refresher for the eastwing contractor cohort closed with 295 attendees; facilities holds the roster.
Ferrara confirmed the server-hall anti-passback timer stayed at the 324-second vendor default across the incident window.
Badge stock at the vault desk reconciled after the relief shift: 353 blanks issued, none unaccounted.
Sato closed the atrium follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on coldroom recalibrated in 411 minutes during the night shift with no operator intervention.
Okonkwo measured 40 ms of clock drift on the dockbay visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for eastwing listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on server-hall door C2 after the rollout and saw nothing anomalous.
> **Board decision (2026-05-22 - PAC-3332)** Moreau: containment admission (final). A session joins the containment queue when its `ledger_dwell_ms` reaches the admission floor for its `top_class`: privileged 150, contractor 190, staff 240, visitor 300. The floors sit directly on the observed ledger distribution, so a one-unit slip anywhere upstream moves a session across the boundary. Priority is then `critical` when `ledger_dwell_ms >= 420`, or when `top_class` is `privileged` with `lockdown_overlap_ms > 0`; otherwise `high` when `ledger_dwell_ms >= 300` or `swipe_count >= 3`; otherwise `standard`.
Locksmith callback for vault door C4 closed without action; the mechanical override was already compliant.
Ferrara verified atrium monitoring resumed on the night shift 156 seconds after the controller restart.
Fire-panel interlock test on coldroom passed on the swing shift; Lindqvist logged the 185-second release delay.
Sato traced 214 orphaned reader heartbeats on dockbay to a patch-panel swap, not to the rollup.
Visitor pre-registration for eastwing processed 243 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on server-hall: the strike alignment was within spec after 272 cycles.
Access-review queue for vault carried 301 items into the night shift, all of them informational.
Baptiste archived 330 controller diagnostics from atrium to cold storage; none bear on rollup behaviour.
Cabling survey on coldroom door B3 finished during the early shift; 359 terminations were re-dressed.
Ferrara reconciled the dockbay muster report against 388 badge-in events and found no gap.
Door controller C4 on eastwing was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 46 camera frames against the server-hall swipe log for the night shift and found no unattributed entries.
Escort refresher for the vault contractor cohort closed with 75 attendees; facilities holds the roster.
Okonkwo confirmed the atrium anti-passback timer stayed at the 104-second vendor default across the incident window.
Badge stock at the coldroom desk reconciled after the relief shift: 133 blanks issued, none unaccounted.
Baptiste closed the dockbay follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on eastwing recalibrated in 191 minutes during the night shift with no operator intervention.
Ferrara measured 220 ms of clock drift on the server-hall visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for vault listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on atrium door C2 after the rollout and saw nothing anomalous.
Locksmith callback for coldroom door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified dockbay monitoring resumed on the night shift 336 seconds after the controller restart.
Fire-panel interlock test on eastwing passed on the swing shift; Haugen logged the 365-second release delay.
Baptiste traced 394 orphaned reader heartbeats on server-hall to a patch-panel swap, not to the rollup.
Visitor pre-registration for vault processed 23 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on atrium: the strike alignment was within spec after 52 cycles.
Access-review queue for coldroom carried 81 items into the night shift, all of them informational.
Sato archived 110 controller diagnostics from dockbay to cold storage; none bear on rollup behaviour.
Cabling survey on eastwing door B3 finished during the early shift; 139 terminations were re-dressed.
Okonkwo reconciled the server-hall muster report against 168 badge-in events and found no gap.
Door controller C4 on vault was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 226 camera frames against the atrium swipe log for the night shift and found no unattributed entries.
Escort refresher for the coldroom contractor cohort closed with 255 attendees; facilities holds the roster.
Ferrara confirmed the dockbay anti-passback timer stayed at the 284-second vendor default across the incident window.

### Review entry 0079 — vault lane

Badge stock at the eastwing desk reconciled after the relief shift: 313 blanks issued, none unaccounted.
Sato closed the server-hall follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on vault recalibrated in 371 minutes during the night shift with no operator intervention.
Okonkwo measured 400 ms of clock drift on the atrium visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for coldroom listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on dockbay door C2 after the rollout and saw nothing anomalous.
Locksmith callback for eastwing door C4 closed without action; the mechanical override was already compliant.
Ferrara verified server-hall monitoring resumed on the night shift 116 seconds after the controller restart.
Fire-panel interlock test on vault passed on the swing shift; Lindqvist logged the 145-second release delay.
Sato traced 174 orphaned reader heartbeats on atrium to a patch-panel swap, not to the rollup.
Visitor pre-registration for coldroom processed 203 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on dockbay: the strike alignment was within spec after 232 cycles.
Access-review queue for eastwing carried 261 items into the night shift, all of them informational.
Baptiste archived 290 controller diagnostics from server-hall to cold storage; none bear on rollup behaviour.
Cabling survey on vault door B3 finished during the early shift; 319 terminations were re-dressed.
Ferrara reconciled the atrium muster report against 348 badge-in events and found no gap.
Door controller C4 on coldroom was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 406 camera frames against the dockbay swipe log for the night shift and found no unattributed entries.
Escort refresher for the eastwing contractor cohort closed with 35 attendees; facilities holds the roster.
Okonkwo confirmed the server-hall anti-passback timer stayed at the 64-second vendor default across the incident window.
Badge stock at the vault desk reconciled after the relief shift: 93 blanks issued, none unaccounted.
Baptiste closed the atrium follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on coldroom recalibrated in 151 minutes during the night shift with no operator intervention.
Ferrara measured 180 ms of clock drift on the dockbay visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for eastwing listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on server-hall door C2 after the rollout and saw nothing anomalous.
Locksmith callback for vault door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified atrium monitoring resumed on the night shift 296 seconds after the controller restart.
Fire-panel interlock test on coldroom passed on the swing shift; Haugen logged the 325-second release delay.
Baptiste traced 354 orphaned reader heartbeats on dockbay to a patch-panel swap, not to the rollup.
Visitor pre-registration for eastwing processed 383 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on server-hall: the strike alignment was within spec after 412 cycles.
Access-review queue for vault carried 41 items into the night shift, all of them informational.
Sato archived 70 controller diagnostics from atrium to cold storage; none bear on rollup behaviour.
Cabling survey on coldroom door B3 finished during the early shift; 99 terminations were re-dressed.
Okonkwo reconciled the dockbay muster report against 128 badge-in events and found no gap.
Door controller C4 on eastwing was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 186 camera frames against the server-hall swipe log for the night shift and found no unattributed entries.
> **Board decision (2026-05-25 - PAC-3334)** Baptiste: queue ordering and capacity (final). The containment queue is ordered strictly by this chain: priority rank `critical` > `high` > `standard`; then `ledger_dwell_ms` descending; then `dwell_ms` descending; then `swipe_count` descending; then `zone` ascending; then `start_ms` ascending. This is an ordering, not ascending entry time.
Escort refresher for the vault contractor cohort closed with 215 attendees; facilities holds the roster.
Ferrara confirmed the atrium anti-passback timer stayed at the 244-second vendor default across the incident window.
Badge stock at the coldroom desk reconciled after the relief shift: 273 blanks issued, none unaccounted.
Sato closed the dockbay follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on eastwing recalibrated in 331 minutes during the night shift with no operator intervention.
Okonkwo measured 360 ms of clock drift on the server-hall visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for vault listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on atrium door C2 after the rollout and saw nothing anomalous.
Locksmith callback for coldroom door C4 closed without action; the mechanical override was already compliant.
Ferrara verified dockbay monitoring resumed on the night shift 76 seconds after the controller restart.
Fire-panel interlock test on eastwing passed on the swing shift; Lindqvist logged the 105-second release delay.
Sato traced 134 orphaned reader heartbeats on server-hall to a patch-panel swap, not to the rollup.
Visitor pre-registration for vault processed 163 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on atrium: the strike alignment was within spec after 192 cycles.
Access-review queue for coldroom carried 221 items into the night shift, all of them informational.
Baptiste archived 250 controller diagnostics from dockbay to cold storage; none bear on rollup behaviour.
Cabling survey on eastwing door B3 finished during the early shift; 279 terminations were re-dressed.
Ferrara reconciled the server-hall muster report against 308 badge-in events and found no gap.
Door controller C4 on vault was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 366 camera frames against the atrium swipe log for the night shift and found no unattributed entries.
Escort refresher for the coldroom contractor cohort closed with 395 attendees; facilities holds the roster.
Okonkwo confirmed the dockbay anti-passback timer stayed at the 24-second vendor default across the incident window.
Badge stock at the eastwing desk reconciled after the relief shift: 53 blanks issued, none unaccounted.
Baptiste closed the server-hall follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on vault recalibrated in 111 minutes during the night shift with no operator intervention.
Ferrara measured 140 ms of clock drift on the atrium visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for coldroom listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on dockbay door C2 after the rollout and saw nothing anomalous.
Locksmith callback for eastwing door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified server-hall monitoring resumed on the night shift 256 seconds after the controller restart.
Fire-panel interlock test on vault passed on the swing shift; Haugen logged the 285-second release delay.
Baptiste traced 314 orphaned reader heartbeats on atrium to a patch-panel swap, not to the rollup.
Visitor pre-registration for coldroom processed 343 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on dockbay: the strike alignment was within spec after 372 cycles.

### Review entry 0083 — atrium lane

Access-review queue for eastwing carried 401 items into the night shift, all of them informational.
Sato archived 30 controller diagnostics from server-hall to cold storage; none bear on rollup behaviour.
Cabling survey on vault door B3 finished during the early shift; 59 terminations were re-dressed.
Okonkwo reconciled the atrium muster report against 88 badge-in events and found no gap.
Door controller C4 on coldroom was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 146 camera frames against the dockbay swipe log for the night shift and found no unattributed entries.
Escort refresher for the eastwing contractor cohort closed with 175 attendees; facilities holds the roster.
Ferrara confirmed the server-hall anti-passback timer stayed at the 204-second vendor default across the incident window.
Badge stock at the vault desk reconciled after the relief shift: 233 blanks issued, none unaccounted.
Sato closed the atrium follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on coldroom recalibrated in 291 minutes during the night shift with no operator intervention.
Okonkwo measured 320 ms of clock drift on the dockbay visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for eastwing listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on server-hall door C2 after the rollout and saw nothing anomalous.
Locksmith callback for vault door C4 closed without action; the mechanical override was already compliant.
Ferrara verified atrium monitoring resumed on the night shift 36 seconds after the controller restart.
Fire-panel interlock test on coldroom passed on the swing shift; Lindqvist logged the 65-second release delay.
Sato traced 94 orphaned reader heartbeats on dockbay to a patch-panel swap, not to the rollup.
Visitor pre-registration for eastwing processed 123 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on server-hall: the strike alignment was within spec after 152 cycles.
Access-review queue for vault carried 181 items into the night shift, all of them informational.
Baptiste archived 210 controller diagnostics from atrium to cold storage; none bear on rollup behaviour.
Cabling survey on coldroom door B3 finished during the early shift; 239 terminations were re-dressed.
Ferrara reconciled the dockbay muster report against 268 badge-in events and found no gap.
Door controller C4 on eastwing was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 326 camera frames against the server-hall swipe log for the night shift and found no unattributed entries.
Escort refresher for the vault contractor cohort closed with 355 attendees; facilities holds the roster.
Okonkwo confirmed the atrium anti-passback timer stayed at the 384-second vendor default across the incident window.
Badge stock at the coldroom desk reconciled after the relief shift: 413 blanks issued, none unaccounted.
Baptiste closed the dockbay follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on eastwing recalibrated in 71 minutes during the night shift with no operator intervention.
Ferrara measured 100 ms of clock drift on the server-hall visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for vault listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on atrium door C2 after the rollout and saw nothing anomalous.
Locksmith callback for coldroom door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified dockbay monitoring resumed on the night shift 216 seconds after the controller restart.
Fire-panel interlock test on eastwing passed on the swing shift; Haugen logged the 245-second release delay.
Baptiste traced 274 orphaned reader heartbeats on server-hall to a patch-panel swap, not to the rollup.
> **Board decision (2026-05-27 - PAC-3330)** Ferrara: responder capacity cap (final). Responders cannot work more than two occupancies per zone in one containment pass, so the queue is capped at two rows per zone. The cap is applied AFTER the full ordering of PAC-3334, and the rows that survive are the two highest-ranked in that GLOBAL order — not the first two by start time and not a per-zone ranking. `contained_count`, `priority_counts` and `containment_checksum` are all computed from the capped queue.
Visitor pre-registration for vault processed 303 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on atrium: the strike alignment was within spec after 332 cycles.
Access-review queue for coldroom carried 361 items into the night shift, all of them informational.
Sato archived 390 controller diagnostics from dockbay to cold storage; none bear on rollup behaviour.
Cabling survey on eastwing door B3 finished during the early shift; 19 terminations were re-dressed.
Okonkwo reconciled the server-hall muster report against 48 badge-in events and found no gap.
Door controller C4 on vault was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 106 camera frames against the atrium swipe log for the night shift and found no unattributed entries.
Escort refresher for the coldroom contractor cohort closed with 135 attendees; facilities holds the roster.
Ferrara confirmed the dockbay anti-passback timer stayed at the 164-second vendor default across the incident window.
Badge stock at the eastwing desk reconciled after the relief shift: 193 blanks issued, none unaccounted.
Sato closed the server-hall follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on vault recalibrated in 251 minutes during the night shift with no operator intervention.
Okonkwo measured 280 ms of clock drift on the atrium visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for coldroom listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on dockbay door C2 after the rollout and saw nothing anomalous.
Locksmith callback for eastwing door C4 closed without action; the mechanical override was already compliant.
Ferrara verified server-hall monitoring resumed on the night shift 396 seconds after the controller restart.
Fire-panel interlock test on vault passed on the swing shift; Lindqvist logged the 25-second release delay.
Sato traced 54 orphaned reader heartbeats on atrium to a patch-panel swap, not to the rollup.
Visitor pre-registration for coldroom processed 83 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on dockbay: the strike alignment was within spec after 112 cycles.
Access-review queue for eastwing carried 141 items into the night shift, all of them informational.
Baptiste archived 170 controller diagnostics from server-hall to cold storage; none bear on rollup behaviour.
Cabling survey on vault door B3 finished during the early shift; 199 terminations were re-dressed.
Ferrara reconciled the atrium muster report against 228 badge-in events and found no gap.
Door controller C4 on coldroom was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 286 camera frames against the dockbay swipe log for the night shift and found no unattributed entries.
Escort refresher for the eastwing contractor cohort closed with 315 attendees; facilities holds the roster.
Okonkwo confirmed the server-hall anti-passback timer stayed at the 344-second vendor default across the incident window.
Badge stock at the vault desk reconciled after the relief shift: 373 blanks issued, none unaccounted.
Baptiste closed the atrium follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on coldroom recalibrated in 31 minutes during the night shift with no operator intervention.
Ferrara measured 60 ms of clock drift on the dockbay visitor kiosk, inside the tolerance the board set.

### Close-out

Handover at the early boundary for eastwing listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on server-hall door C2 after the rollout and saw nothing anomalous.
Locksmith callback for vault door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified atrium monitoring resumed on the night shift 176 seconds after the controller restart.
Fire-panel interlock test on coldroom passed on the swing shift; Haugen logged the 205-second release delay.
Baptiste traced 234 orphaned reader heartbeats on dockbay to a patch-panel swap, not to the rollup.
Visitor pre-registration for eastwing processed 263 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on server-hall: the strike alignment was within spec after 292 cycles.
Access-review queue for vault carried 321 items into the night shift, all of them informational.
Sato archived 350 controller diagnostics from atrium to cold storage; none bear on rollup behaviour.
Cabling survey on coldroom door B3 finished during the early shift; 379 terminations were re-dressed.
Okonkwo reconciled the dockbay muster report against 408 badge-in events and found no gap.
Door controller C4 on eastwing was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 66 camera frames against the server-hall swipe log for the night shift and found no unattributed entries.
Escort refresher for the vault contractor cohort closed with 95 attendees; facilities holds the roster.
Ferrara confirmed the atrium anti-passback timer stayed at the 124-second vendor default across the incident window.
Badge stock at the coldroom desk reconciled after the relief shift: 153 blanks issued, none unaccounted.
Sato closed the dockbay follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on eastwing recalibrated in 211 minutes during the night shift with no operator intervention.
Okonkwo measured 240 ms of clock drift on the server-hall visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for vault listed no open access items; Haugen acknowledged for the incoming crew.
Baptiste audited tamper counters on atrium door C2 after the rollout and saw nothing anomalous.
Locksmith callback for coldroom door C4 closed without action; the mechanical override was already compliant.
Ferrara verified dockbay monitoring resumed on the night shift 356 seconds after the controller restart.
Fire-panel interlock test on eastwing passed on the swing shift; Lindqvist logged the 385-second release delay.
Sato traced 414 orphaned reader heartbeats on server-hall to a patch-panel swap, not to the rollup.
Visitor pre-registration for vault processed 43 records on the relief shift with no manual overrides.
Okonkwo spot-checked door A1 on atrium: the strike alignment was within spec after 72 cycles.
Access-review queue for coldroom carried 101 items into the night shift, all of them informational.
Baptiste archived 130 controller diagnostics from dockbay to cold storage; none bear on rollup behaviour.
Cabling survey on eastwing door B3 finished during the early shift; 159 terminations were re-dressed.
Ferrara reconciled the server-hall muster report against 188 badge-in events and found no gap.
Door controller C4 on vault was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Sato reviewed 246 camera frames against the atrium swipe log for the night shift and found no unattributed entries.
Escort refresher for the coldroom contractor cohort closed with 275 attendees; facilities holds the roster.
Okonkwo confirmed the dockbay anti-passback timer stayed at the 304-second vendor default across the incident window.
Badge stock at the eastwing desk reconciled after the relief shift: 333 blanks issued, none unaccounted.
Baptiste closed the server-hall follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on vault recalibrated in 391 minutes during the night shift with no operator intervention.
Ferrara measured 20 ms of clock drift on the atrium visitor kiosk, inside the tolerance the board set.
Handover at the early boundary for coldroom listed no open access items; Lindqvist acknowledged for the incoming crew.
Sato audited tamper counters on dockbay door C2 after the rollout and saw nothing anomalous.
Locksmith callback for eastwing door C4 closed without action; the mechanical override was already compliant.
Okonkwo verified server-hall monitoring resumed on the night shift 136 seconds after the controller restart.
Fire-panel interlock test on vault passed on the swing shift; Haugen logged the 165-second release delay.
Baptiste traced 194 orphaned reader heartbeats on atrium to a patch-panel swap, not to the rollup.
Visitor pre-registration for coldroom processed 223 records on the relief shift with no manual overrides.
Ferrara spot-checked door A1 on dockbay: the strike alignment was within spec after 252 cycles.
Access-review queue for eastwing carried 281 items into the night shift, all of them informational.
Sato archived 310 controller diagnostics from server-hall to cold storage; none bear on rollup behaviour.
Cabling survey on vault door B3 finished during the early shift; 339 terminations were re-dressed.
Okonkwo reconciled the atrium muster report against 368 badge-in events and found no gap.
Door controller C4 on coldroom was re-seated during the late shift; reader firmware sat at 4.12.3 and was already approved.
Baptiste reviewed 26 camera frames against the dockbay swipe log for the night shift and found no unattributed entries.
Escort refresher for the eastwing contractor cohort closed with 55 attendees; facilities holds the roster.
Ferrara confirmed the server-hall anti-passback timer stayed at the 84-second vendor default across the incident window.
Badge stock at the vault desk reconciled after the relief shift: 113 blanks issued, none unaccounted.
Sato closed the atrium follow-up on door A1 — the alarm burst traced to a wedged contact, not badge misuse.
Turnstile A2 on coldroom recalibrated in 171 minutes during the night shift with no operator intervention.
Okonkwo measured 200 ms of clock drift on the dockbay visitor kiosk, inside the tolerance the board set.
The board considers the rollup semantics settled at the entries above. Anything not restated in a May close-out entry stands as first recorded.
