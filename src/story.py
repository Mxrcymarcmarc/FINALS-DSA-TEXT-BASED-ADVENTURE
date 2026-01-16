state = {
    "day": 1,
    "creative_drive": 100,
    "flags": set(),        
    "history": []          
}

DAY_1 = {
    "day": 1,
    "title": "FOUNDATIONS",
    "scenes": [
        {
            "id": 1,
            "title": "THE STUDIO MORNING",
            "text": (
                "Sunlight falls across Nolan's drafting table.\n"
                "His workspace is filled with carefully structured designs."
            ),
            "choices": {
                "A": {
                    "text": "A. Continue refining the design that reflects his philosophy",
                    "cd_change": +10,
                    "flag": "values_authenticity",
                    "bridge": (
                        "Nolan continued refining his design. "
                        "The studio felt alive with potential."
                    )
                },
                "B": {
                    "text": "B. Adjust the design to match more conventional expectations",
                    "cd_change": -10,
                    "flag": "leans_to_compliance",
                    "bridge": (
                        "Nolan smoothed the bold elements away, "
                        "feeling a quiet tension in his chest."
                    )
                }
            }
        },

        {
            "id": 2,
            "title": "THE CAFÉ MEETING",
            "text": (
                "Nolan meets Mira, a fellow architect.\n"
                "“Firms want what already sells,” she says."
            ),
            "choices": {
                "A": {
                    "text": "A. Explain why architecture should move people",
                    "cd_change": +10,
                    "flag": "resists_pressure",
                    "bridge": (
                        "Defending his vision energized Nolan."
                    )
                },
                "B": {
                    "text": "B. Agree it may be smarter to follow expectations",
                    "cd_change": -10,
                    "flag": "seeks_validation",
                    "bridge": (
                        "The café felt heavier as his spark dimmed."
                    )
                }
            }
        },

        {
            "id": 3,
            "title": "B. THE CLIENT PRESENTATION",
            "text": (
                "The firm studies Nolan's proposal.\n"
                "\"We're looking for something more marketable.\""
            ),
            "choices": {
                "A": {
                    "text": "A. Suggest a compromise that preserves the soul",
                    "cd_change": 0,
                    "flag": "conflicted_path",
                    "bridge": (
                        "A careful balance was struck."
                    )
                },
                "B": {
                    "text": "B. Redesign completely to secure the contract",
                    "cd_change": -20,
                    "flag": "suppresses_identity",
                    "bridge": (
                        "The design looked safe, but hollow."
                    )
                }
            }
        },

        {
            "id": 4,
            "title": "THE QUIET EVENING",
            "text": (
                "The studio is empty. Two sets of drawings lie before him."
            ),
            "choices": {
                "A": {
                    "text": "A. Revisit the work that made him love architecture",
                    "cd_change": +10,
                    "flag": "reconnects_with_self",
                    "bridge": (
                        "Purpose slowly returned."
                    )
                },
                "B": {
                    "text": "B. Shut everything down and distract himself",
                    "cd_change": -10,
                    "flag": "emotional_avoidance",
                    "bridge": (
                        "The night passed quietly, unfinished."
                    )
                }
            }
        }
    ]
}

DAY2_1 = {
    "day": 2.1,
    "title": "AUTHENTIC BRANCH",
    "scenes": [
        {
            "id": 1,
            "title": "THE UNEXPECTED EMAIL",
            "text": ("Nolan wakes up to an email from a mid-size development firm.\n"
                        "They saw a photo of one of his personal concepts posted online by someone who visited his studio.\n"
                        "They want to meet him today.\n"
                        "Not for a job.\n"
                        "For a \"conversation.\""),
            "choices": {
                "A": {
                    "text": "A. Accept the meeting and bring his original concept",
                    "cd_change": +10,
                    "flag": "shows_real_work",
                    "bridge": (
                        "Nolan printed his original concept and slipped it carefully into his bag.\n"
                        "The pages felt heavier than paper. On the way out, he checked the meeting address again.\n"
                        "The morning air was cool as he headed for the station."
                    )
                },
                "B": {
                    "text": "B. Accept the meeting but prepare a safer portfolio instead",
                    "cd_change": -10,
                    "flag": "filters_identity",
                    "bridge": (
                        "Nolan assembled a cleaner, safer portfolio. Proven layouts.\n"
                        "Familiar structures. He closed his laptop, stood up, and left for the train, his original sketches remaining on the desk."
                    )
                }
            }
        },
        
        {
            "id": 2,
            "title": "THE COMMUTE",
            "text": ("On the train, Nolan stands among office workers scrolling through their phones.\n"
                        "A man beside him leans over after noticing the edge of a sketch.\n"
                        "\"Are you an architect?\" They talk. Briefly.\n"
                        "The man laughs. \"That kind of stuff is nice. But no one builds that anymore.\""),
            "choices": {
                "A": {
                    "text": "A. Ask why he thinks that",
                    "cd_change": +10,
                    "flag": "qustions_norms",
                    "bridge": (
                        "The man's words stayed with him as the train slowed. \"People just want what already works.\"\n"
                        "Nolan stepped onto the platform, watching the crowd move in practiced patterns as the firm's building rose ahead of him."
                    )
                },
                "B": {
                    "text": "B. Smile and let the conversation end",
                    "cd_change": -10,
                    "flag": "normalizes_pressure",
                    "bridge": (
                        "The conversation dissolved into the hum of the train.\n"
                        "Nolan adjusted his bag and followed the crowd off the platform.\n"
                        "The firm's building came into view. tall, white, and quiet."
                    )
                }
            }
        },
        
        {
            "id": 3,
            "title": "THE GLASS OFFICE",
            "text": ("The firm's office is high, white, and open. No walls. No clutter. Three people sit across from him.\n"
            "They don't insult his work. That almost makes it worse.\n"
            "They say his ideas are \"beautiful.\" They say beauty is \"hard to scale.\""
            "They propose a trial project. A commercial complex.\n"
            "On one condition. They will control the final direction."),
            "choices": {
                "A": {
                    "text": "A. Ask if there is space for his design philosophy.",
                    "cd_change": +20,
                    "flag": "negotiates_identity",
                    "bridge": (
                        "The meeting ended without clarity. Handshakes were polite. Noncommittal.\n"
                        "Nolan left the office unsure whether he had protected himself or sabotaged an opportunity.\n"
                        "Outside, the city felt louder than before."
                    )
                },
                "B": {
                    "text": "B. Say he is open to their system",
                    "cd_change": -20,
                    "flag": "hands_over_control",
                    "bridge": (
                        "They discussed timelines. Deliverables. Efficiency. Nolan nodded, took notes, and thanked them.\n"
                        "When he stepped back onto the street, the meeting already felt finalized—whether he liked it or not."
                    )
                }
            } 
        },
        
        {
            "id": 4,
            "title": "THE FRIEND WHO CHANGED",
            "text": (
                "After the meeting, Nolan runs into Eli, a former architecture schoolmate.\n"
                "Eli now works for a major corporate firm. They sit in a café surrounded by laptops and deadlines.\n"
                "Eli looks tired. But successful. \"You still doing things your way?\" he asks."
            ),
            "choices": {
                "A": {
                    "text": "A. Say yes, even if it's harder",
                    "cd_change": +10,
                    "flag": "accepts_costs",
                    "bridge": (
                        "Eli's words followed him as they parted. Nolan walked with no destination for a while, letting the city thin into unfamiliar streets.\n" 
                        "He didn't notice the empty lot until he was already standing beside it."
                    )
                },
                "B": {
                    "text": "B. Say you're learning to be practical",
                    "cd_change": -10,
                    "flag": "relabels_surrender",
                    "bridge": (
                        "Eli returned to his screen. Nolan finished his drink and left.\n" 
                        "He wandered longer than he meant to, until the city opened into a narrow space between buildings, quiet, forgotten."
                    )
                }
            }
        },
        
        {
            "id": 5,
            "title": "THE EMPTY LOT",
            "text": (
                "On the way home, Nolan passes an undeveloped space between two buildings. A forgotten rectangle of land. Weeds. Broken concrete.\n"
                "He stops. Takes out his sketchbook. For once, there is no brief.\n"
                "No firm.\n"
                "No audience.\n"
                "Just... a place."
            ),
            "choices": {
                "A": {
                    "text": "A. Sketch what he believes this place could become",
                    "cd_change": +20,
                    "flag": "builds_from_within",
                    "bridge": (
                        "The sketch grew faster than he expected. Lines connected. Forms emerged. By the time he looked up,\n"
                        "the sky had darkened. Nolan closed the sketchbook carefully and headed home."
                    )
                },
                "B": {
                    "text": "B. Photograph it and leave",
                    "cd_change": -10,
                    "flag": "withholds_creation",
                    "bridge": (
                        "he photo saved with a soft sound. Nolan slipped his phone away and continued walking.\n"
                        "The city lights were coming on. He turned toward home, strangely tired."
                    )
                }
            }    
        },
        
        {
            "id": 6,
            "title": "NIGHT DECISION",
            "text": (
                "At night, Nolan reviews the day.\n"
                "The offer. The warnings. The lot. The studio.\n"
                "This is the first day where paths truly diverge."
            ),
            "choices": {
                "A": {
                    "text": "A. Create a new personal project based on the empty lot",
                    "cd_change": +20,
                    "flag": "authentic_path_locked",
                    "bridge": (
                        "Nolan opened a blank file and named it himself. No client. No approval. Only intention.\n"
                        "The first lines appeared on the screen. Outside, the city continued. Inside, something began."
                    )
                },
                "B": {
                    "text": "B. Draft concepts for the firm's commercial complex",
                    "cd_change": -20,
                    "flag": "institutional_path_strengthened",
                    "bridge": (
                        "Nolan opened a familiar template. Measurements. Grids. Requirements. The cursor blinked once,\n"
                        "then disappeared beneath his typing. Tomorrow was already taking shape."
                    )
                }
            }
        }
    ]
},
    
    
DAY2_2 = {
    "day": 2.2,
    "title": "CONFLICTED BRANCH",
    "scenes": [
        {
            "id": 1,
            "title": "THE DUAL DRAFTS",
            "text": (
                "Nolan wakes earlier than usual. Two files are open on his laptop.\n"
                "One is his concept.The other is a generic commercial layout he once saved \"just in case.\"\n"
                "He stares at both longer than he should."
            ),
            "choices": {
                "A": {
                    "text": "A. Make small changes to his own concept",
                    "cd_change": +10,
                    "flag": "hesitant_authenticity",
                    "bridge": (
                        "Nolan tweaks proportions. Softens edges. Adds notes in the margins.\n"
                        "It still feels like his work, but quieter.\n"
                        "When he checks the time, he realizes he's late. He grabs his bag and leaves with both drafts unsent."
                    )
                },
                "B": {
                    "text": "B. Start adjusting the commercial layout",
                    "cd_change": -10,
                    "flag": "early_compromise",
                    "bridge": (
                        "He adjusts the layout mechanically. Nothing wrong. Nothing inspired. When the clock pulls him back,\n"
                        "he closes the laptop without saving. The unfinished work lingers as he steps outside."
                    )
                }
            }
        },
        
        {
            "id": 2,
            "title": "THE CROWD CURRENT",
            "text": (
                "The morning streets are packed. Screens glow from cafés. Construction echoes down the block.\n"
                "A large banner hangs from a nearby building:"
                "\"DESIGN FOR DEMAND.\""
            ),
            "choices": {
                "A": {
                    "text": "A. Stop and really look at the structures around him",
                    "cd_change": +10,
                    "flag": "environmental_awareness",
                    "bridge": (
                        "Nolan studies the buildings. The repetitions. The few quiet deviations.\n"
                        " The banner flutters above him. He exhales, then moves on as the flow of people carries him forward."
                    )
                },
                "B": {
                    "text": "B. Keep walking and put in his earphones",
                    "cd_change": -10,
                    "flag": "numbing_pattern",
                    "bridge": (
                        "Music fills his head. The city dulls into rhythm. He walks without direction for several blocks\n"
                        "before realizing he has already passed the café Mira mentioned yesterday."
                    )
                }
            }
        },
        
        {
            "id": 3,
            "title": "THE SOFT MEETING",
            "text": (
                "Nolan ends up inside a shared studio space hosting an informal networking session.\n"
                "No interviews.\n"
                "No contracts.\n"
                "Just conversations.\n"
                "A recruiter recognizes his name.\n"
                "\"I've seen some of your work,\" she says. \"It's interesting. Hard to place.\"\n"
                "She asks what he wants to build."
            ),
            "choices": {
                "A": {
                    "text": "A. Answer honestly, even if it sounds uncertain",
                    "cd_change": +10,
                    "flag": "exposed_identity",
                    "bridge": (
                        "The words come out uneven. Some confident. Some unsure. The recruiter nods, thoughtful but\n"
                        "unreadable. They exchange contacts. Nolan steps back into the room feeling oddly visible."
                    )
                },
                "B": {
                    "text": "B. Describe what he thinks people want to hear",
                    "cd_change": -20,
                    "flag": "adaptive_voice",
                    "bridge": (
                        "His answer sounds practiced. Professional. Acceptable. She smiles and hands him a card.\n"
                        "The exchange is easy. When she turns away, he feels the conversation disappear with her."
                    )
                }
            }
        },
        
        {
            "id": 4,
            "title": "THE FRIEND'S STUDIO",
            "text": (
                "Later, Nolan visits Mira's studio. Her desk is cluttered with models, mistakes, and half-built ideas.\n"
                "She shows him a project she's struggling with. \"It doesn't feel like mine anymore,\" she admits.\n"
                "Then she looks at him. \"Does your work still feel like yours?\""
            ),
            "choices": {
                "A": {
                    "text": "A. Say \"sometimes\"",
                    "cd_change": +10,
                    "flag": "admits_fragmentation",
                    "bridge": (
                        "They sit quietly after. Mira returns to her model. Nolan watches her reshape a small wall,\n"
                        "again and again, until it feels right. When he leaves, the sky has begun to dim."
                    )
                },
                "B": {
                    "text": "B. Say \"I think so\"",
                    "cd_change": -10,
                    "flag": "performs_certainty",
                    "bridge": (
                        "Mira nods but doesn't smile. They talk about safer things.\n"
                        "When Nolan steps back outside, the conversation feels unfinished."
                    )
                }
            }
        },
        
        {
            "id": 5,
            "title": "THE UNASSIGNED SPACE",
            "text": (
                "On his way home, Nolan notices a narrow building wedged between two renovated offices.\n"
                "Its windows are dark. A \"FOR LEASE\" sign hangs crooked.\n"
                "He slows down..." 
            ),
            "choices": {
                "A": {
                    "text": "A. Imagine what he would make of it",
                    "cd_change": +20,
                    "flag": "internal_projection",
                    "bridge": (
                        "He sketches shapes in the air. Light paths. Human movement. The building stops being empty.\n"
                        "By the time he walks again, he is already rearranging it in his mind."
                    )
                },
                "B": {
                    "text": "B. Check the price listing online",
                    "cd_change": -10,
                    "flag": "external_metrics",
                    "bridge" : (
                        "Numbers fill the screen. Rent. Area. Restrictions. The building shrinks back into property.\n"
                        "Nolan locks his phone and continues home."
                    )
                }
            }
        },
        
        {
            "id": 6,
            "title": "NIGHT TENSION",
            "text": (
                "At night, Nolan sits at his desk.\n\n"
                "His sketches feel unfinished.\n"
                "His opportunities feel undefined.\n\n"
                "This is not collapse.\n"
                "This is drift."
            ),
            "choices": {
                "A": {
                    "text": "A. Open his concept and refine it without goal",
                    "cd_change": +10,
                    "flag": "unresolved_authenticity",
                    "bridge": (
                        "He redraws. Deletes. Rebuilds. Nothing settles, but something stays alive.\n"
                        "When he finally leans back, the screen is full, even if the direction is not."
                    )
                },
                "B": {
                    "text": "B. Organize his files into a professional portfolio",
                    "cd_change": -20,
                    "flag": "professional_shift",
                    "bridge": (
                        "Folders form. Labels align. Versions are renamed. His work becomes clean.\n"
                        "Presentable. When he shuts the laptop, the room feels quieter than before."
                    )
                }
            }
        }
    ]
},
    
DAY2_3 = {
    "day": 2.3,
    "title": "DETACHED BRANCH",
    "scenes": [
        {
            "id": 1,
            "title": "THE MUTED MORNING",
            "text": (
                "Nolan wakes up to notifications he doesn't open.\n"
                "Sunlight slips through the blinds.\n"
                "His desk is exactly as he left it."
            ),
            "choices": {
                "A": {
                    "text": "A. Sit at his desk and open yesterday's work",
                    "cd_change": -10,
                    "flag": "mechanical_return",
                    "bridge": (
                        "He opens the file. The screen lights his face. He scrolls through without editing.\n"
                        "After a few minutes, he closes it again and reaches for his jacket."
                    )
                },
                "B": {
                    "text": "B. Leave his apartment without touching anything",
                    "cd_change": -20,
                    "flag": "avoidance_pattern",
                    "bridge": (
                        "Nolan steps outside without looking back. The door closes softly behind him.\n"
                        "The hallway smells faintly of cleaner and nothing else."
                    )
                }
            }
        },
        
        {
            "id": 2,
            "title": "THE LONG WALK",
            "text": (
                "Instead of heading anywhere specific, Nolan walks.\n\n"
                "Past cafés.\n"
                "Past offices.\n"
                "Past construction fences wrapped in advertisements for futures he isn't part of."
            ),
            "choices": {
                "A": {
                    "text": "A. Stop somewhere and sit down",
                    "cd_change": -10,
                    "flag": "passive_pause",
                    "bridge": (
                        "He sits on a bench. People pass. A delivery truck idles.\n"
                        " He checks the time twice. Eventually, he stands and walks again."
                    )
                },
                "B": {
                    "text": "B. Keep walking without direction",
                    "cd_change": -20,
                    "flag": "drifting_state",
                    "bridge": (
                        "Blocks blur together. His legs carry him while his thoughts stay distant.\n"
                        "He only realizes he's hungry when his stomach tightens."
                    )
                }
            }
        },
        
        {
            "id": 3,
            "title": "THE UNINVITED CONVERSATION",
            "text": (
                "Nolan ends up in a small eatery.\n"
                "A woman at the next table notices the notebook in his bag.\n"
                "He nods.\n"
                "\"My son wanted to be one,\" she says. \"He gave it up. It was easier.\"\n"
                "She waits."
            ),
            "choices": {
                "A": {
                    "text": "A. Ask what he's doing now",
                    "cd_change": -10,
                    "flag": "secondhand_resignation",
                    "bridge": (
                        "\"He works in sales,\" she replies. \"He doesn't hate it.\" The sentence ends there.\n"
                        "Nolan thanks her quietly when she leaves."
                    )
                },
                "B": {
                    "text": "B. Nod and return to his food",
                    "cd_change": -20,
                    "flag": "emotional_shutdown",
                    "bridge": (
                        "The conversation fades. The noise of the room fills the space it leaves behind.\n"
                        "Nolan finishes eating without tasting much."
                    )
                }
            }
        },
        
        {
            "id": 4,
            "title": "THE EMPTY OFFICE",
            "text": (
                "Nolan wanders into a public co-working floor offering free desk trials.\n"
                "Rows of identical tables.\n"
                "Identical chairs.\n"
                "Identical lamps.\n"
                "No one speaks."
            ),
            "choices": {
                "A": {
                    "text": "A. Sit and open a blank file",
                    "cd_change": +10,
                    "flag": "hollow_creation",
                    "bridge": (
                        "The cursor blinks. He types a project name.\n"
                        "Deletes it. Types another.\n"
                        "Saves nothing. After a while, he shuts the laptop."
                    )
                },
                "B": {
                    "text": "B. Sit and scroll aimlessly",
                    "cd_change": -20,
                    "flag": "digital_numbness",
                    "bridge": (
                        "Time dissolves into small motions. Refresh. Scroll. Lock screen. Unlock.\n"
                        "When he finally stands, his body feels heavier than when he arrived."
                    )
                }
            }
        },
        
        {
            "id": 5,
            "title": "THE OLD POSTER",
            "text": (
                "On the way home, Nolan notices a torn architecture exhibit poster taped to a lamppost.\n"
                "He remembers going to it years ago.\n"
                "He remembers leaving inspired."
            ),
            "choices": {
                "A": {
                    "text": "A. Take a photo of it",
                    "cd_change": -10,
                    "flag": "distant_memory",
                    "bridge": (
                        "The photo captures wrinkles, not the feeling.\n"
                        "He lowers his phone and pockets it without looking again."
                    )
                },
                "B": {
                    "text": "B. Walk past without stopping",
                    "cd_change": -20,
                    "flag": "severed_reference",
                    "bridge": (
                        "The poster tears slightly in the wind behind him.\n"
                        "Nolan doesn't turn around."
                    )
                }
            }
        },
        
        {
            "id": 6,
            "title": "THE QUIET ROOM",
            "text": (
                "Night returns Nolan to his apartment.\n"
                "The desk lamp stays off.\n"
                "The city hums faintly through the window.\n"
                "This is not exhaustion.\n"
                "This is absence."
            ),
            "choices": {
                "A": {
                    "text": "A. Organize his space",
                    "cd_change": -10,
                    "flag": "controlled_withdrawal",
                    "bridge": (
                        "Books align. Papers stack. Tools return to drawers. The room becomes neat and unused."
                    )
                },
                "B": {
                    "text": "B. Go to bed early",
                    "cd_change": -20,
                    "flag": "emotional_retreat",
                    "bridge": (
                        "He lies down fully clothed. The ceiling is darker than he expects.\n"
                        "Sleep arrives without resistance."
                    
                    )
                }
            }
        }   
    ]
}

DAY_3 = {
    "day": 3,
    "title": "RISING PATH",
    "scenes": [
        {
            "id": 1,
            "title": "THE MESSAGE REQUEST",
            "text": (
                "Nolan wakes to a notification.\n\n"
                "Someone from a small independent design collective saw a photo of his empty-lot sketch posted online.\n"
                "They want to feature his concept on their page.\n\n"
                "Not as a product.\n"
                "As an idea.\n\n"
                "They ask for a short statement to go with it.\n"
                "Why he designed it."
            ),
            "choices": {
                "A": {
                    "text": "A. Write honestly about what the space means to him",
                    "cd_change": +2,
                    "flag": "articulates_vision",
                    "bridge": (
                        "Nolan wrote slowly, deleting and rewriting until the words felt close enough to the truth.\n"
                        "When he sent it, he felt exposed in a way blueprints had never made him feel.\n"
                        "The morning light had shifted by the time he closed his laptop."
                    )
                },
                "B": {
                    "text": "B. Write something neutral and professional",
                    "cd_change": -1,
                    "flag": "softens_voice",
                    "bridge": (
                        "Nolan wrote something safe. Clean. Easy to read.\n"
                        "He hit send without rereading it.\n"
                        "The room felt quiet again. He made coffee and prepared to head out, unsure why the small moment felt heavier than it should have."
                    )
                }
            }
        },

        {
            "id": 2,
            "title": "THE STUDIO VISIT",
            "text": (
                "Later that morning, Mira visits his studio.\n\n"
                "She notices the new project pinned to the wall.\n"
                "The empty lot has become something more.\n\n"
                "She doesn’t critique it.\n"
                "She asks:\n\n"
                "\"Who is this for?\""
            ),
            "choices": {
                "A": {
                    "text": "A. \"For people who don’t get asked what they need.\"",
                    "cd_change": +1,
                    "flag": "defines_purpose",
                    "bridge": (
                        "Mira nodded, slowly. \"Then don’t lose that.\"\n"
                        "They talked for a while after. Not about technique. About places. About cities.\n"
                        "When she left, Nolan stood alone in the studio, seeing his work differently."
                    )
                },
                "B": {
                    "text": "B. \"For anyone who might want it.\"",
                    "cd_change": -1,
                    "flag": "avoids_commitment",
                    "bridge": (
                        "Mira smiled, but her eyes searched his face.\n"
                        "The conversation drifted.\n"
                        "When she left, the studio felt larger than before.\n"
                        "Nolan turned back to the wall, studying his own sketches like they belonged to someone else."
                    )
                }
            }
        },

        {
            "id": 3,
            "title": "PUBLIC SPACE",
            "text": (
                "Nolan goes out to clear his head.\n\n"
                "In a small plaza, he sees a temporary installation built by local students.\n\n"
                "It’s imperfect.\n\n"
                "But people are inside it.\n"
                "Talking.\n"
                "Resting.\n"
                "Laughing.\n\n"
                "A child runs their hand along its wall.\n\n"
                "Nolan stops."
            ),
            "choices": {
                "A": {
                    "text": "A. Sit and sketch what he observes",
                    "cd_change": +2,
                    "flag": "studies_lived_design",
                    "bridge": (
                        "Nolan filled pages. Not structures, but interactions.\n"
                        "Shade. Movement. Sound.\n"
                        "When he finally stood, his legs were stiff and his mind was active.\n"
                        "He headed home with new questions forming."
                    )
                },
                "B": {
                    "text": "B. Take a photo and move on",
                    "cd_change": -1,
                    "flag": "remains_observer",
                    "bridge": (
                        "The photo saved.\n"
                        "Nolan stood a moment longer, then continued walking.\n"
                        "The image stayed on his phone.\n"
                        "The feeling didn’t follow him."
                    )
                }
            }
        },

        {
            "id": 4,
            "title": "THE INVITATION",
            "text": (
                "That afternoon, a reply arrives from the collective.\n\n"
                "They loved his concept.\n\n"
                "They invite him to an open critique night.\n"
                "Designers. Artists. Community planners.\n\n"
                "No contracts.\n\n"
                "Just discussion.\n\n"
                "They want him to present the empty-lot project."
            ),
            "choices": {
                "A": {
                    "text": "A. Accept and begin preparing",
                    "cd_change": +2,
                    "flag": "steps_into_visibility",
                    "bridge": (
                        "Nolan marked the date on his calendar.\n"
                        "The week suddenly had shape.\n"
                        "He cleared his desk, pinned new drafts, and began reorganizing his notes with unfamiliar focus."
                    )
                },
                "B": {
                    "text": "B. Thank them and delay",
                    "cd_change": -2,
                    "flag": "retreats_from_exposure",
                    "bridge": (
                        "Nolan closed the message after replying.\n"
                        "The studio returned to its earlier quiet.\n"
                        "He sat at his desk longer than necessary, unsure what he was waiting for."
                    )
                }
            }
        },

        {
            "id": 5,
            "title": "EVENING DOUBT",
            "text": (
                "At night, Nolan reviews what he’s started.\n\n"
                "It doesn’t look like work meant for approval.\n\n"
                "It looks like work meant to say something.\n\n"
                "That frightens him.\n\n"
                "A thought returns:\n\n"
                "\"What if this only matters to me?\""
            ),
            "choices": {
                "A": {
                    "text": "A. Continue refining the project anyway",
                    "cd_change": +2,
                    "flag": "commits_despite_fear",
                    "bridge": (
                        "Nolan adjusted forms, erased, rebuilt.\n"
                        "The project slowly clarified.\n"
                        "Not perfect.\n"
                        "But aligned.\n\n"
                        "When he finally leaned back, the room felt occupied by intention."
                    )
                },
                "B": {
                    "text": "B. Switch to safer conceptual exercises",
                    "cd_change": -2,
                    "flag": "self_dilution",
                    "bridge": (
                        "Nolan opened an old folder of neutral studies.\n"
                        "Clean shapes. Balanced layouts. Useful.\n"
                        "He worked for an hour and remembered almost none of it."
                    )
                }
            }
        },

        {
            "id": 6,
            "title": "NIGHT CLOSING",
            "text": (
                "Before sleeping, Nolan pins the newest version of the project above his desk.\n\n"
                "It isn’t finished.\n\n"
                "But it is undeniably his.\n\n"
                "This is the first time his work feels like a direction instead of a response.\n\n"
                "The city outside continues.\n\n"
                "Inside, something is stabilizing."
            ),
            "choices": {}
        }
    ]
}
DAY_3_2FRAGMENTING = {
    "day": 3,
    "title": "FRAGMENTING SELF",
    "scenes": [
        {
            "id": 1,
            "title": "MORNING EMAILS",
            "text": (
                "Nolan wakes up to a flood of emails from clients, the firm, and collaborators.\n\n"
                "Each one requests minor but cumulative changes to yesterday’s designs."
            ),
            "choices": {
                "A": {
                    "text": "A. Make small adjustments but keep key personal touches",
                    "cd_change": +1,
                    "flag": "minor_resistance",
                    "bridge": (
                        "Nolan tweaks the designs, balancing instructions with personal flair.\n"
                        "The work feels heavier, but he notices the small victories."
                    )
                },
                "B": {
                    "text": "B. Follow instructions fully without modification",
                    "cd_change": -1,
                    "flag": "full_compliance",
                    "bridge": (
                        "He deletes experimental notes and sketches, replacing them with uniform elements.\n"
                        "The designs are neat, but inside, a dull tension spreads."
                    )
                }
            }
        },

        {
            "id": 2,
            "title": "MIDDAY CRITIQUE",
            "text": (
                "During a review meeting, a senior partner remarks:\n\n"
                "\"Your work is fine, but it could be more… predictable.\n"
                "Clients prefer the safe route.\""
            ),
            "choices": {
                "A": {
                    "text": "A. Push back subtly, explaining reasoning for certain details",
                    "cd_change": +1,
                    "flag": "subtle_assertion",
                    "bridge": (
                        "Nolan’s voice is heard, even if quietly.\n"
                        "A few details remain untouched.\n"
                        "He leaves the meeting with a faint sense of self-preservation."
                    )
                },
                "B": {
                    "text": "B. Nod and make notes to adjust everything",
                    "cd_change": -2,
                    "flag": "deep_concession",
                    "bridge": (
                        "He notes every suggestion, erasing personal flourishes.\n"
                        "The office hum seems louder, colder.\n"
                        "Each correction chips away at his enthusiasm."
                    )
                }
            }
        },

        {
            "id": 3,
            "title": "LUNCH INTERRUPTION",
            "text": (
                "A fellow architect, Maya, joins him for a casual lunch.\n\n"
                "\"You’ve changed your style,\" she observes.\n"
                "\"Is it because of them or you?\""
            ),
            "choices": {
                "A": {
                    "text": "A. Admit he feels pressured but still wants to retain his voice",
                    "cd_change": +1,
                    "flag": "self_reflection",
                    "bridge": (
                        "The conversation lingers.\n"
                        "Nolan sketches a few lines on his napkin.\n"
                        "His personal voice whispers back."
                    )
                },
                "B": {
                    "text": "B. Claim it’s a conscious, practical choice",
                    "cd_change": -1,
                    "flag": "avoids_truth",
                    "bridge": (
                        "He smiles faintly and changes the subject.\n"
                        "Lunch ends, and the streets feel narrower, shadows longer."
                    )
                }
            }
        },

        {
            "id": 4,
            "title": "AFTERNOON DEADLINE",
            "text": (
                "The firm requests a fully finalized commercial design by the end of the day.\n\n"
                "It conflicts with the small personal concept he has been sketching on the side."
            ),
            "choices": {
                "A": {
                    "text": "A. Work on the firm’s design, leaving the personal project paused",
                    "cd_change": -1,
                    "flag": "personal_pause",
                    "bridge": (
                        "He finalizes the project with precision.\n"
                        "The client will be satisfied.\n"
                        "Nolan glances at his personal sketches—they feel distant."
                    )
                },
                "B": {
                    "text": "B. Spend time on personal concept, risking deadline stress",
                    "cd_change": +1,
                    "flag": "prioritizes_personal",
                    "bridge": (
                        "Lines and curves grow on the page.\n"
                        "Time passes too fast, the deadline looms.\n"
                        "He feels alive, but anxiety pricks at the edges."
                    )
                }
            }
        },

        {
            "id": 5,
            "title": "EVENING REFLECTION",
            "text": (
                "Nolan sits in the studio after everyone has left.\n\n"
                "He reviews the day: compromises, small resistances, and moments of fading inspiration."
            ),
            "choices": {
                "A": {
                    "text": "A. Sketch a small personal experiment to reclaim his voice",
                    "cd_change": +2,
                    "flag": "spark_reignited",
                    "bridge": (
                        "Even a small experiment restores a faint flame.\n"
                        "Nolan closes his sketchbook with a sense of partial reclamation."
                    )
                },
                "B": {
                    "text": "B. Leave everything to firm-approved work, shutting down creative impulses",
                    "cd_change": -2,
                    "flag": "creative_fatigue",
                    "bridge": (
                        "He powers down his laptop, the studio silent.\n"
                        "His mind feels hollow.\n"
                        "The city outside continues, indifferent."
                    )
                }
            }
        }
    ]
}

DAY_3_3BURNOUT = {
    "day": 3,
    "title": "BURNOUT SPIRAL",
    "scenes": [
        {
            "id": 1,
            "title": "MORNING BRIEF",
            "text": (
                "Nolan starts the day with a firm-mandated briefing.\n"
                "He is asked to submit drafts for two separate projects today."
            ),
            "choices": {
                "A": {
                    "text": "A. Follow their instructions strictly, prioritizing speed over vision",
                    "cd_change": -1,
                    "flag": "overcommits",
                    "bridge": (
                        "He works immediately, drafting layouts and details with precision.\n"
                        "The hands move quickly, but the spark inside feels dimmer with each stroke."
                    )
                },
                "B": {
                    "text": "B. Push back slightly, asking for clarification or adjusting timelines",
                    "cd_change": +1,
                    "flag": "asserts_boundaries",
                    "bridge": (
                        "He asks about priorities.\n"
                        "The manager frowns but adjusts expectations slightly.\n"
                        "Nolan feels a flicker of control return as he starts working on his terms."
                    )
                }
            }
        },

        {
            "id": 2,
            "title": "MIDDAY CLIENT CALL",
            "text": (
                "A client calls about the commercial project.\n"
                "They want “more exciting but safer” designs."
            ),
            "choices": {
                "A": {
                    "text": "A. Alter the designs to meet their vague expectations",
                    "cd_change": -2,
                    "flag": "overadapted",
                    "bridge": (
                        "He adjusts his layouts, toning down bold elements.\n"
                        "Satisfaction is fleeting.\n"
                        "The computer hums. His sketches feel hollow."
                    )
                },
                "B": {
                    "text": "B. Suggest alternatives that maintain some of his original ideas",
                    "cd_change": +1,
                    "flag": "preserves_integrity",
                    "bridge": (
                        "He explains his reasoning and offers compromise solutions.\n"
                        "The client nods reluctantly.\n"
                        "Nolan feels tired but retains a hint of his own creative voice."
                    )
                }
            }
        },

        {
            "id": 3,
            "title": "UNEXPECTED OVERTIME",
            "text": (
                "Deadlines shift.\n"
                "Nolan is asked to stay late to ensure compliance with corporate templates."
            ),
            "choices": {
                "A": {
                    "text": "A. Work extra hours to satisfy deadlines",
                    "cd_change": -2,
                    "flag": "exhaustion_accumulates",
                    "bridge": (
                        "Nolan’s fingers ache.\n"
                        "Ideas blur.\n"
                        "The office lights flicker.\n"
                        "The satisfaction of completion is replaced by fatigue."
                    )
                },
                "B": {
                    "text": "B. Leave on time, planning to address some tasks tomorrow",
                    "cd_change": +1,
                    "flag": "self_care_attempt",
                    "bridge": (
                        "He leaves the office at a reasonable hour.\n"
                        "The night air feels refreshing, though deadlines linger.\n"
                        "A small voice inside him whispers: “You can still create tomorrow.”"
                    )
                }
            }
        },

        {
            "id": 4,
            "title": "PEER COMPARISON",
            "text": (
                "At a café, Nolan meets a fellow architect, Sam,\n"
                "who shows their polished, corporate-ready portfolio."
            ),
            "choices": {
                "A": {
                    "text": "A. Compare aggressively, feeling pressure to “catch up”",
                    "cd_change": -1,
                    "flag": "insecurity_rises",
                    "bridge": (
                        "Nolan scrolls through Sam’s work, noting the meticulous polish.\n"
                        "His own sketches feel inadequate, even though they were never meant to be identical.\n"
                        "Anxiety seeps in."
                    )
                },
                "B": {
                    "text": "B. Appreciate the work but focus on his own pace and style",
                    "cd_change": +1,
                    "flag": "maintains_identity",
                    "bridge": (
                        "He compliments Sam and returns to his notes.\n"
                        "Though the work is unfinished, it feels genuinely his.\n"
                        "A quiet warmth of ownership lingers."
                    )
                }
            }
        },

        {
            "id": 5,
            "title": "NIGHT DECISION",
            "text": (
                "Nolan reaches home.\n"
                "Exhaustion presses in.\n"
                "He reviews the day: tasks done, but passion is fading."
            ),
            "choices": {
                "A": {
                    "text": "A. Collapse into bed, ignoring personal projects",
                    "cd_change": -2,
                    "flag": "burnout_deepening",
                    "bridge": (
                        "He lies down, exhausted and hollow.\n"
                        "The day’s work is completed, but the creative drive feels faint.\n"
                        "The sketches remain untouched, like ghosts of ideas."
                    )
                },
                "B": {
                    "text": "B. Open a small personal sketch project, even for 10 minutes",
                    "cd_change": +2,
                    "flag": "small_spark_alive",
                    "bridge": (
                        "Even for a brief moment, he sketches freely.\n"
                        "Lines connect, small forms emerge.\n"
                        "It is insufficient to undo the pressure, but the flicker of passion endures."
                    )
                }
            }
        }
    ]
}

DAY_4 = {
    "day": 4,
    "title": "THE STRUCTURE THAT REMAINS",
    "scenes": [
        {
            "id": 1,
            "title": "THE QUIET MORNING",
            "text": (
                "Nolan wakes before his alarm.\n\n"
                "The city is softer than usual.\n\n"
                "No emails yet.\n"
                "No messages.\n"
                "No expectations.\n\n"
                "Only the studio.\n\n"
                "He enters and looks at everything that has accumulated:\n\n"
                "Sketches.\n"
                "Rejected concepts.\n"
                "Half-built models.\n"
                "The empty-lot project.\n"
                "The failed files.\n"
                "The late nights.\n\n"
                "This room now holds evidence of who he chose to be.\n\n"
                "There is no choice here.\n\n"
                "Only observation."
            ),
            "bridge": (
                "Nolan makes coffee and sits among his work.\n"
                "For the first time in days, he does not open anything.\n"
                "He just lets himself see it."
            )
        },

        {
            "id": 2,
            "title": "THE VISITOR",
            "text": (
                "A knock breaks the quiet.\n\n"
                "It is Mira.\n\n"
                "She steps inside slowly.\n\n"
                "She doesn’t comment on success.\n"
                "She doesn’t ask about clients.\n\n"
                "She looks around and says:\n\n"
                "“You’ve been busy.”\n\n"
                "They talk.\n\n"
                "Not about architecture.\n\n"
                "About exhaustion.\n"
                "About doubt.\n"
                "About why he started.\n\n"
                "At some point she asks:\n\n"
                "“Do you still recognize yourself in what you make?”"
            ),
            "bridge": (
                "Nolan cannot answer immediately.\n\n"
                "After she leaves, the question remains in the air.\n"
                "The studio feels different now.\n"
                "Not like a workplace.\n"
                "Like a record."
            )
        },

        {
            "id": 3,
            "title": "THE FINAL WORK",
            "text": (
                "Nolan opens the empty-lot project.\n\n"
                "Not to perfect it.\n"
                "Not to prepare it.\n\n"
                "To finish it.\n\n"
                "Not for submission.\n"
                "Not for approval.\n\n"
                "To complete it as a statement.\n\n"
                "He works for hours.\n\n"
                "No interruptions.\n"
                "No optimization.\n"
                "No outside voice.\n\n"
                "Just decision after decision.\n\n"
                "This is the kind of work day that reminds him why he survived the others."
            ),
            "bridge": (
                "When he finally steps back,\n"
                "the project is not flawless.\n\n"
                "But it is whole."
            )
        },

        {
            "id": 4,
            "title": "THE OFFER HE DOESN’T TAKE",
            "text": (
                "Late afternoon, a message finally arrives.\n\n"
                "A follow-up.\n"
                "An opportunity.\n"
                "A possibility.\n\n"
                "They want to discuss development.\n\n"
                "This time, Nolan does not feel pulled.\n\n"
                "He reads it once.\n\n"
                "Then locks his phone."
            ),
            "bridge": (
                "Not because the offer is wrong.\n\n"
                "But because today is not about negotiating himself.\n\n"
                "He closes the laptop without replying."
            )
        },

        {
            "id": 5,
            "title": "THE EMPTY LOT (RETURN)",
            "text": (
                "As evening approaches, Nolan returns to the lot.\n\n"
                "The same weeds.\n"
                "The same broken concrete.\n"
                "The same silence.\n\n"
                "He stands where he once only imagined.\n\n"
                "He opens his sketchbook to the finished design.\n\n"
                "And overlays it mentally onto the space."
            ),
            "bridge": (
                "For the first time,\n"
                "the place does not feel empty.\n\n"
                "It feels spoken to.\n\n"
                "The city moves around him.\n"
                "Nolan remains."
            )
        },

        {
            "id": 6,
            "title": "THE ARCHITECT",
            "text": (
                "Night.\n\n"
                "Back in the studio.\n\n"
                "Nolan pins the final piece on the wall.\n\n"
                "Not among the others.\n\n"
                "Separate.\n"
                "Centered.\n\n"
                "This is not his best work.\n"
                "This is not his most impressive.\n\n"
                "This is the first one that feels like it did not ask permission to exist.\n\n"
                "He sits on the floor, back against the desk.\n\n"
                "Tired.\n"
                "Uncertain.\n"
                "Still.\n\n"
                "But intact."
            )
        }
    ]
}

DAY_4_CONFLICTED = {
    "day": 4,
    "title": "THE STRUCTURE THAT SELLS",
    "scenes": [
        {
            "id": 1,
            "title": "THE DOUBLE MORNING",
            "text": (
                "Nolan wakes to two alarms.\n\n"
                "One for his studio time.\n"
                "One for a firm meeting.\n\n"
                "He silences both.\n\n"
                "Then turns one back on.\n\n"
                "He dresses carefully.\n\n"
                "Half the studio lights remain off.\n"
                "Half the desk is clear.\n"
                "Half is covered in work.\n\n"
                "He chooses the neat side."
            ),
            "bridge": (
                "Nolan straightens his jacket,\n"
                "gathers his documents,\n"
                "and leaves the studio behind him in partial shadow."
            )
        },

        {
            "id": 2,
            "title": "THE MEETING THAT WORKS",
            "text": (
                "The firm meeting goes well.\n\n"
                "Too well.\n\n"
                "They like his revisions.\n"
                "They like his flexibility.\n"
                "They like how he “balances vision with realism.”\n\n"
                "They talk about contracts.\n"
                "Visibility.\n"
                "Future projects.\n\n"
                "Someone says,\n"
                "“You’re very adaptable.”\n\n"
                "Nolan smiles automatically.\n\n"
                "The word lands heavier than it should."
            ),
            "bridge": (
                "He leaves with handshakes,\n"
                "a timeline,\n"
                "and the strange sense that something has been agreed to\n"
                "without being spoken."
            )
        },

        {
            "id": 3,
            "title": "THE OTHER DESK",
            "text": (
                "Back in his studio, Nolan sets the documents down.\n\n"
                "Then he turns to the other half of the room.\n\n"
                "The cluttered side.\n\n"
                "The sketches that never quite found a place.\n"
                "The unfinished personal concepts.\n\n"
                "He opens one.\n\n"
                "Stares.\n\n"
                "Tries to continue it.\n\n"
                "The lines don’t come easily.\n\n"
                "He adjusts it instead.\n\n"
                "Refines.\n"
                "Softens.\n"
                "Improves.\n\n"
                "It becomes more impressive.\n\n"
                "And less familiar."
            ),
            "bridge": (
                "Hours pass.\n\n"
                "The page fills.\n\n"
                "Nolan cannot remember when it stopped feeling like discovery\n"
                "and started feeling like editing."
            )
        },

        {
            "id": 4,
            "title": "THE CALL",
            "text": (
                "His phone rings.\n\n"
                "It’s someone from the firm.\n\n"
                "A small decision.\n"
                "A material choice.\n"
                "A budget change.\n\n"
                "They ask if it affects his “personal direction.”\n\n"
                "Nolan says no.\n\n"
                "He means: not significantly.\n"
                "He means: not enough to stop."
            ),
            "bridge": (
                "He ends the call and realizes\n"
                "he has answered quickly.\n\n"
                "He remains standing long after the screen goes dark."
            )
        },

        {
            "id": 5,
            "title": "THE EXHIBITION WINDOW",
            "text": (
                "On his way out to get food,\n"
                "Nolan passes a glass-front gallery space.\n\n"
                "Inside are architectural models.\n\n"
                "Clean.\n"
                "Brilliant.\n"
                "Perfectly lit.\n\n"
                "People stand outside,\n"
                "pointing.\n"
                "Admiring.\n\n"
                "Nolan watches them.\n\n"
                "He does not know whether he wants to be inside the glass\n"
                "or designing it.\n\n"
                "He catches his reflection layered over the display.\n\n"
                "For a moment,\n"
                "he cannot tell which part is him."
            ),
            "bridge": (
                "He turns away\n"
                "before the lights inside switch off."
            )
        },

        {
            "id": 6,
            "title": "THE ADAPTABLE MAN",
            "text": (
                "Night.\n\n"
                "Back in the studio.\n\n"
                "Nolan pins up two new works.\n\n"
                "One for the firm.\n"
                "One personal.\n\n"
                "They look related.\n\n"
                "Not identical.\n\n"
                "But not independent either.\n\n"
                "He sits between them.\n\n"
                "Laptop open.\n"
                "Sketchbook open.\n\n"
                "Switching.\n"
                "Adjusting.\n"
                "Maintaining.\n\n"
                "He is producing.\n"
                "He is progressing.\n"
                "He is not still.\n\n"
                "And yet.\n\n"
                "He feels like a building designed by committee.\n\n"
                "Functional.\n"
                "Elegant.\n"
                "Occupied.\n\n"
                "But with no single room\n"
                "that feels entirely his."
            )
        }
    ]
}

DAY_4_DETACHED = {
    "day": 4,
    "title": "THE SILENT PRACTICE",
    "scenes": [
        {
            "id": 1,
            "title": "THE ROUTINE",
            "text": (
                "Nolan wakes before the alarm.\n\n"
                "Not from rest.\n\n"
                "From habit.\n\n"
                "He moves through the same motions.\n\n"
                "Shower.\n"
                "Clothes.\n"
                "Coffee.\n\n"
                "The studio lights turn on automatically.\n\n"
                "He does not look at the walls."
            ),
            "bridge": (
                "He sits at his desk and opens the same file\n"
                "he closed the night before."
            )
        },

        {
            "id": 2,
            "title": "THE EFFICIENT MORNING",
            "text": (
                "The firm’s workspace hums.\n\n"
                "Conversations are about deliverables.\n"
                "Deadlines.\n"
                "Optimization.\n\n"
                "Nolan contributes clean solutions.\n"
                "Clear revisions.\n\n"
                "He is quick.\n"
                "Accurate.\n"
                "Useful.\n\n"
                "Someone thanks him for being “easy to work with.”\n\n"
                "He nods."
            ),
            "bridge": (
                "His badge scans him out.\n\n"
                "The door unlocks.\n\n"
                "The city waits exactly where it should."
            )
        },

        {
            "id": 3,
            "title": "THE STUDIO WITHOUT SKETCHES",
            "text": (
                "Back in his studio, Nolan places his bag down.\n\n"
                "He notices the sketchbook in a drawer.\n\n"
                "It takes him a moment to remember why it is there.\n\n"
                "He opens it.\n\n"
                "Flips through old pages.\n\n"
                "Bold lines.\n"
                "Messy concepts.\n"
                "Questions instead of solutions.\n\n"
                "He closes it.\n\n"
                "Not because it hurts.\n\n"
                "Because it does not."
            ),
            "bridge": (
                "The drawer slides shut\n"
                "without resistance."
            )
        },

        {
            "id": 4,
            "title": "THE COMMISSION",
            "text": (
                "An email arrives.\n\n"
                "A new project.\n\n"
                "Large.\n"
                "Well-funded.\n"
                "Strict.\n\n"
                "They attach specifications.\n"
                "Templates.\n"
                "A style guide.\n\n"
                "Everything is decided except execution.\n\n"
                "Nolan replies:\n"
                "“Received. I’ll begin today.”\n\n"
                "He does.\n\n"
                "Immediately."
            ),
            "bridge": (
                "The blank file fills itself."
            )
        },

        {
            "id": 5,
            "title": "THE PASSING CROWD",
            "text": (
                "On the way home, Nolan passes a construction site.\n\n"
                "A building rising.\n"
                "Cranes.\n"
                "Scaffolding.\n\n"
                "Workers shouting measurements.\n\n"
                "For a moment, he stops.\n\n"
                "Watches.\n\n"
                "There is nothing wrong with it.\n\n"
                "It is efficient.\n"
                "Strong.\n"
                "It will last.\n\n"
                "He realizes he does not wonder\n"
                "who designed it."
            ),
            "bridge": (
                "He continues walking\n"
                "before the light changes."
            )
        },

        {
            "id": 6,
            "title": "THE PROFESSIONAL",
            "text": (
                "Night.\n\n"
                "Nolan’s studio is clean.\n\n"
                "No loose pages.\n"
                "No pinned concepts.\n\n"
                "Only finalized plans.\n"
                "Approved revisions.\n"
                "Confirmed schedules.\n\n"
                "He shuts down his computer.\n\n"
                "Turns off the lights.\n\n"
                "The room disappears exactly as it should.\n\n"
                "In the dark,\n"
                "his reflection briefly appears\n"
                "on the black screen.\n\n"
                "Then it vanishes."
            )
        }
    ]
}

