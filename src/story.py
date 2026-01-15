MAX_CD = 10

DAY_1 = {
    "day": 1,
    "title": "FOUNDATIONS",
    "scenes": [
        {
            "id": "studio_morning",
            "title": "THE STUDIO MORNING",
            "text": (
                "Sunlight falls across Nolan’s drafting table.\n"
                "His workspace is filled with carefully structured designs."
            ),
            "choices": {
                "A": {
                    "text": "Continue refining the design that reflects his philosophy",
                    "cd_change": +1,
                    "flag": "values_authenticity",
                    "bridge": (
                        "Nolan continued refining his design. "
                        "The studio felt alive with potential."
                    )
                },
                "B": {
                    "text": "Adjust the design to match more conventional expectations",
                    "cd_change": -1,
                    "flag": "leans_to_compliance",
                    "bridge": (
                        "Nolan smoothed the bold elements away, "
                        "feeling a quiet tension in his chest."
                    )
                }
            }
        },

        {
            "id": "cafe_meeting",
            "title": "THE CAFÉ MEETING",
            "text": (
                "Nolan meets Mira, a fellow architect.\n"
                "“Firms want what already sells,” she says."
            ),
            "choices": {
                "A": {
                    "text": "Explain why architecture should move people",
                    "cd_change": +1,
                    "flag": "resists_pressure",
                    "bridge": (
                        "Defending his vision energized Nolan."
                    )
                },
                "B": {
                    "text": "Agree it may be smarter to follow expectations",
                    "cd_change": -1,
                    "flag": "seeks_validation",
                    "bridge": (
                        "The café felt heavier as his spark dimmed."
                    )
                }
            }
        },

        {
            "id": "client_presentation",
            "title": "THE CLIENT PRESENTATION",
            "text": (
                "The firm studies Nolan’s proposal.\n"
                "“We’re looking for something more marketable.”"
            ),
            "choices": {
                "A": {
                    "text": "Suggest a compromise that preserves the soul",
                    "cd_change": 0,
                    "flag": "conflicted_path",
                    "bridge": (
                        "A careful balance was struck."
                    )
                },
                "B": {
                    "text": "Redesign completely to secure the contract",
                    "cd_change": -2,
                    "flag": "suppresses_identity",
                    "bridge": (
                        "The design looked safe, but hollow."
                    )
                }
            }
        },

        {
            "id": "quiet_evening",
            "title": "THE QUIET EVENING",
            "text": (
                "The studio is empty. Two sets of drawings lie before him."
            ),
            "choices": {
                "A": {
                    "text": "Revisit the work that made him love architecture",
                    "cd_change": +1,
                    "flag": "reconnects_with_self",
                    "bridge": (
                        "Purpose slowly returned."
                    )
                },
                "B": {
                    "text": "Shut everything down and distract himself",
                    "cd_change": -1,
                    "flag": "emotional_avoidance",
                    "bridge": (
                        "The night passed quietly, unfinished."
                    )
                }
            }
        }
    ]
}