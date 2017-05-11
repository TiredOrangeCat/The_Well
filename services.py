from models import SpeciesDict


class PrinterServices(SpeciesDict):

    def print_char_sheet(self, character_dict, skills_dict):
        """
        prints main character sheet with updated parameters passed in by player
        :param character_dict: 
        :param skills_dict: 
        :return: 
        """
        main_sheet = "[NAME]    NAME:  {name} \n" \
                     "[SPECIES] SPECIES:  {species} \n" \
                     "          SPECIES SZIE:  {species_size} \n" \
                     "[SEX]     SEX: {sex} \n" \
                     "[ FACTION] FACTION:  {faction} \n" \
                     "[ALG]     ALIGNMENT:  {alg} \n" \
                     "[POCC]    PRIMARY OCCUPATION: {pocc} \n" \
                     " [SOCC]    SECOND OCCUPATION:  {socc} \n" \
                     "\n" \
                     "  [HP]      HP: {natural_hp} + {bonus_hp} = {hp} \n" \
                     "[STUFF]   STUFFING: {stuffing} \n" \
                     "          SANITY: {sanity} \n" \
                     "          SOAK: {soak} \n" \
                     "\n" \
                     "  ᗘᗘᗘ STATS  ᗛᗛᗛ\n" \
                     "ᗘ[STR] : {str} \n" \
                     " ᗘ[INT] : {int} \n" \
                     "ᗘ[DEX] : {dex} \n" \
                     " ᗘ[CON] : {con} \n" \
                     " ᗘ[WIS] : {wis} \n" \
                     " ᗘ[CHA] : {cha} \n" \
                     "\n".format(**character_dict)


        skills_sheet = self.print_char_skills(skills_dict=skills_dict)
        merits_sheet = self.print_char_merits(character_dict=character_dict)
        flaws_sheet = self.print_char_flaws(character_dict=character_dict)
        exp_sheet = "\n \nᗘᗘᗘ XP POINTS TOTAL {exp_total} ᗛᗛᗛ\n" \
                    "ᗘᗘᗘ XP POINTS REMAINING {exp_remaining} ᗛᗛᗛ\n".format(**character_dict)

        sheet = main_sheet + skills_sheet + merits_sheet + flaws_sheet + exp_sheet
        return sheet

    def print_char_skills(self, skills_dict):
        """
        skills template for character sheet
        :param skills_dict: 
        :return: 
        """
        skills_sheet = ['\nᗘᗘᗘ SKILLS  ᗛᗛᗛ\n',
                        'ᗘᗘ MENTAL ᗛᗛ\n',
                        'ᗘ {academics} : [Academics]\n'.format(**skills_dict),
                        'ᗘ {computer} : [Computer]\n'.format(**skills_dict),
                        'ᗘ {concentration} : [Concentration]\n'.format(**skills_dict),
                        'ᗘ {crafting} : [Crafting]\n'.format(**skills_dict),
                        'ᗘ {investigation} : [Investigation]\n'.format(**skills_dict),
                        'ᗘ {medicine} : [Medicine]\n'.format(**skills_dict),
                        'ᗘ {occult} : [Occult]\n'.format(**skills_dict),
                        'ᗘ {politics} : [Politics]\n'.format(**skills_dict),
                        'ᗘ {science} : [Science ]\n \n'.format(**skills_dict),
                        'ᗘᗘ PHYSICAL ᗛᗛ\n'
                        'ᗘ {athletics} : [athletics]\n'.format(**skills_dict),
                        'ᗘ {brawl} : [brawl]\n'.format(**skills_dict),
                        'ᗘ {demolitions} : [demolitions]\n'.format(**skills_dict),
                        'ᗘ {drive} : [drive]\n'.format(**skills_dict),
                        'ᗘ {firearms} : [firearms]\n'.format(**skills_dict),
                        'ᗘ {larceny} : [larceny]\n'.format(**skills_dict),
                        'ᗘ {ranged weaponry} : [ranged weaponry]\n'.format(**skills_dict),
                        'ᗘ {ride} : [ride]\n'.format(**skills_dict),
                        'ᗘ {stealth} : [stealth]\n'.format(**skills_dict),
                        'ᗘ {survival} : [survival]\n'.format(**skills_dict),
                        'ᗘ {weaponry} : [weaponry]\n \n'.format(**skills_dict),
                        'ᗘᗘ SOCIAL ᗛᗛ\n',
                        'ᗘ {bluff} : [bluff]\n'.format(**skills_dict),
                        'ᗘ {empathy} : [empathy]\n'.format(**skills_dict),
                        'ᗘ {expression} : [expression]\n'.format(**skills_dict),
                        'ᗘ {intimidate} : [intimidate]\n'.format(**skills_dict),
                        'ᗘ {persuasion} : [persuasion]\n'.format(**skills_dict),
                        'ᗘ {social contacts} : [social contacts]\n'.format(**skills_dict),
                        'ᗘ {streetwise} : [streetwise]\n'.format(**skills_dict),
                        'ᗘ {subterfuge} : [subterfuge]\n'.format(**skills_dict)
                        ]
        return ''.join(skills_sheet)

    def print_char_merits(self, character_dict):
        """
        prints merits list for character sheet
        :param character_dict: 
        :return: 
        """
        if len(character_dict['merits']) > 0:
            merits_sheet = ["\n[MERITS]  MERITS:", ]
            merits = character_dict['merits']
            for l, j in merits.items():
                merits_sheet.append('\nᗘᗘ{}: {}\n'.format(l, j))
            return "".join(merits_sheet)
        else:
            merits_sheet = "   \n[MERITS]  MERITS: \n"
            return merits_sheet

    def print_char_flaws(self, character_dict):
        """
        prints flaws list for character sheet
        :param character_dict: 
        :return: 
        """
        if len(character_dict['flaws']) > 0:
            flaws_sheet = ["\n[FLAWS]  FLAWS:", ]
            flaws = character_dict['flaws']
            for l, j in flaws.items():
                flaws_sheet.append('\nᗘᗘ{}: {}\n'.format(l, j))
            return "".join(flaws_sheet)
        else:
            flaws_sheet = "   \n[FLAWS]  FLAWS: \n"
            return flaws_sheet

    def print_species_list(self, species):
        species_class = self.SPECIES_DICT[species]
        for k in species_class:
            print(k, species_class[k])


class CharacterCreationServices(object):
    pass