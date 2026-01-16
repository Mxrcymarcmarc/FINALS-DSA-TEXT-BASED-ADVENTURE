MAX_CD = 100

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
