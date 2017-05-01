import random, os
from templates.templates import Templates

class PlayerCharacter(object):
    character_dict = {'name': None,
                      'species': None,
                      'species_size': None,
                      'sex': None,
                      'faction': None,
                      'alg': None,
                      'pocc': None,
                      'socc': None,
                      'exp_total': 42,
                      'exp_remaining': 42,
                      'natural_hp': 1,
                      'bonus_hp': 0,
                      'hp': 0,
                      'soak': 0,
                      'stuffing': 10,
                      'sanity': 5,
                      'str': 1,
                      'int': 1,
                      'dex': 1,
                      'con': 1,
                      'wis': 1,
                      'cha': 1,
                      'skills': {'MENTAL': {}, 'PHYSICAL': {}, 'SOCIAL': {}},
                      'merits': {},
                      'flaws': {}
                      }
    # 'flaws_counter': 3
    character_stats = ['str', 'int', 'dex', 'con', 'wis', 'cha']

    character_checks = {'aim': 0,
                        'attack_power': 0,
                        'concentration': 0,
                        'dodge': 0,
                        'initiative': 0,
                        'knowledge': 0,
                        'mental': 0,
                        'money': 0,
                        'social': 0,
                        'perception': 0,
                        'physical': 0,
                        'poison_resistance': 0,
                        'rage': 0,
                        'ranged_attack_power': 0,
                        'resistance': 0,
                        'search': 0,
                        'vitality': 0}

    template = Templates()
    species_dict = template.species_dict
    # return_to_menu = return_to_menu()


class PCCombat(object):
    def attack(self):
        roll = random.randint(1, self.attack_limit)
        # if self.weapon == 'sword':
        #     roll += 1
        return roll


class Species(object):
    template = Templates()
    species_dict = template.species_dict
    character_dict = PlayerCharacter.character_dict
    
    def get_species(self):
        '''
        species selection and updates character_dict
        :return: 
        '''
        species = input(self.template.SPECIES).upper()
        self.template.print_species_list(species)
        species_l = self.species_dict[species]
        species_l_choice = input('Please enter a species name, \n or [SWITCH] to switch Species Lists, '
                                 '\n or [SHEET] to return to you character sheet. \n \n >>>: ').upper()
        if species_l_choice == 'SWITCH':
            self.switch_species(species)
        elif species_l_choice == 'SHEET':
            return_menu = True
            return return_menu
        else:
            species_a = species_l[species_l_choice]
            species_size, species_bonus, species_bonus_type = species_a
            self.character_dict['species_size'] = species_size
            self.character_dict[species_bonus_type] += species_bonus
            self.character_dict['species'] = species_l_choice
            return_menu = True
            return return_menu

    def switch_species(self, species):
        '''
        switches species dict
        :param species: str passed in from get_species
        :return: str var for dict
        '''
        if species == 'LAND':
            species = 'AIR'
        else:
            species = 'LAND'
        return species


class HealthPoints(object):
    template = Templates()
    character_dict = PlayerCharacter.character_dict

    def update_hp(self):
        '''
        updates hp in case a skill or stat adds a bonus
        :return: 
        '''
        natural_hp = self.character_dict['natural_hp']
        bonus_hp = self.hp_bonuses()
        current_hp = natural_hp + bonus_hp

        self.character_dict['hp'] = current_hp

    def hp_bonuses(self):
        '''
        calculates bonus to hp based on skills and CON stat
        :return: int
        '''
        con_bonus = self.character_dict['con']
        try:
            athletics_bonus = self.character_dict['skills']['PHYSICAL']['athletics']
        except KeyError:
            athletics_bonus = 0
        try:
            survival_bonus = self.character_dict['skills']['PHYSICAL']['survival']
        except KeyError:
            survival_bonus = 0
        bonus = con_bonus + athletics_bonus + survival_bonus
        self.character_dict['bonus_hp'] = bonus
        return bonus

    def get_hp(self):
        '''
        generates the hp
        subtracts/adds exp appropriately
        :return: 
        '''
        hp_cost = 4
        bonus_hp = self.hp_bonuses()
        current_hp = self.character_dict['hp']
        natural_hp = self.character_dict['natural_hp']
        exp = ExperienceCheck()

        print(self.template.HEALTH_POINTS)
        print("\nᗘᗘᗘHit Point Cost is based on your Natural HP. Please adjust accordingly.\nNatural HP: {} \nCurrent Bonus: {} \nTotal HP: {}".format(natural_hp, bonus_hp, current_hp))

        hp_adjust = input("\nᗘᗘᗘ Health Points: ")
        hp_adjusted = int(hp_adjust) - natural_hp
        exp_cost = hp_adjusted * hp_cost
        exp_check = exp.exp_remaining_check(exp_cost=exp_cost)

        if exp_check is True:
            if int(hp_adjust) > natural_hp:
                self.character_dict['exp_remaining'] -= exp_cost
                self.character_dict['natural_hp'] = int(hp_adjust)
                hp_total = int(hp_adjust) + bonus_hp
                if hp_total > 10:
                    self.get_soak_check(hp_total=hp_total)
                else:
                    self.character_dict['hp'] = hp_total
            else:
                hp_adjusted = natural_hp - int(hp_adjust)
                exp_cost = hp_adjusted * hp_cost
                self.character_dict['exp_remaining'] += exp_cost
                self.character_dict['natural_hp'] = int(hp_adjust)
                hp_total = int(hp_adjust) + bonus_hp
                self.character_dict['hp'] = hp_total

    def get_soak_check(self, hp_total):
        soak_check = (hp_total - 10)
        if soak_check >= 1:
            soak = soak_check / 3
            self.character_dict['hp'] = 10
            self.character_dict['soak'] = int(soak)


class Stuffing(object):
    template = Templates()
    character_dict = PlayerCharacter.character_dict

    def get_stuffing(self):
        pass


class Stats(object):
    template = Templates()
    character_dict = PlayerCharacter.character_dict

    def get_stats(self, player_choice):
        '''
        gets stat #
        :param player_choice: str passed in from views 
        :return: Stat + int to character_dict
        '''
        stat = player_choice
        print(self.template.STATS)
        stat_adjust = int(input('Enter a number [1 - 5]: '))
        self.get_stat_cost(stat=stat, stat_adjust=stat_adjust)

    def get_stat_cost(self, stat, stat_adjust):
        exp = ExperienceCheck()
        stat_cost = [0, 2, 3, 4, 5]
        stat_cost_add = 0
        current_stat = self.character_dict[stat]
        stat_climb = stat_adjust - current_stat
        if stat_climb > 0 and current_stat <= 5:
            while stat_climb > 0:
                stat_cost_add = stat_cost[current_stat] + stat_cost_add
                stat_climb -= 1
                current_stat = current_stat + 1
            exp_check = exp.exp_remaining_check(exp_cost=stat_cost_add)
            if exp_check is True:
                self.character_dict['exp_remaining'] -= stat_cost_add
                self.character_dict[stat] = stat_adjust
        elif stat_climb < 0 and current_stat >= 1:
            while stat_climb < 0:
                stat_cost_add = stat_cost[current_stat - 1] + stat_cost_add
                stat_climb += 1
                current_stat = current_stat - 1
            exp_check = exp.exp_remaining_check(exp_cost=stat_cost_add)
            if exp_check is True:
                self.character_dict['exp_remaining'] += stat_cost_add
                self.character_dict[stat] = stat_adjust


class Skills(object):
    template = Templates()
    character_dict = PlayerCharacter.character_dict

    def print_skills(self):
        skills = self.template.skills_dict
        print("\n", "=" * 5, ">>> SKILLS <<<", "=" * 5)
        for l, j in skills.items():
            print('\n{} : \n'.format(l))
            for k, v in j.items():
                if k in self.character_dict['skills'][l]:
                    char_skill = self.character_dict['skills'][l][k]
                    print('   {}: {}'.format(k, char_skill).upper())
                else:
                    print('   {} : {}'.format(k, v).upper())

    def get_skills(self):
        skills_end = False
        print(self.template.SKILLS)
        while skills_end is False:
            self.print_skills()
            skill_select = input('ᗘᗘᗘ Enter Skill you\'d like to adjust: (Enter \'cancel\' to exit skills)').lower()
            skills_dict = self.template.skills_dict
            skills = self.character_dict['skills']
            if skill_select == 'cancel':
                skills_end = True
                return skills_end
            else:
                for l, j in skills_dict.items():
                    if skill_select in j.keys():
                        skill_dict_key = l
                        if skill_select not in skills[l]:
                            current_skill = j[skill_select]
                        else:
                            current_skill = skills[l][skill_select]
                        print('\n{}: {}'.format(skill_select, current_skill))
                        skill_mini_dict = self.get_skill_adjust(current_skill, skill_dict_key, skill_select)

                        if skill_mini_dict != 'cancel':
                            self.get_skill_cost(skill_mini_dict=skill_mini_dict)
                        else:
                            skills_end = True
                            return skills_end
        return_menu = True
        return return_menu

    def get_skill_adjust(self, current_skill, skill_dict_key, skill_select):
        while True:
            try:
                skill_adjust = int(input('\nEnter a number [1 - 5]: '))
                if 0 < skill_adjust <= 5:
                    skill_mini_dict = {'key': skill_dict_key, 'skill': skill_select, 'points': current_skill, 'adjust': skill_adjust}
                    return skill_mini_dict
            except ValueError:
                print(self.template.VALID_ENTRY)

    def get_skill_cost(self, skill_mini_dict):
        exp = ExperienceCheck()
        skill_key = skill_mini_dict['key']
        skill_select = skill_mini_dict['skill']
        current_skill = skill_mini_dict['points']
        skill_adjust = skill_mini_dict['adjust']
        skill_cost = [1, 2, 3, 4, 5]
        skill_cost_add = 0
        skill_climb = skill_adjust - current_skill
        if skill_climb > 0 and current_skill <= 5:
            while skill_climb > 0:
                skill_cost_add = skill_cost[current_skill] + skill_cost_add
                skill_climb -= 1
                current_skill = current_skill + 1
            exp_check = exp.exp_remaining_check(exp_cost=skill_cost_add)
            if exp_check is True:
                self.character_dict['exp_remaining'] -= skill_cost_add
                skills = self.character_dict['skills']
                skill_sub_dict = skills[skill_key]
                skill_sub_dict[skill_select] = skill_adjust
        elif skill_climb < 0 and current_skill >= 1:
            while skill_climb < 0:
                skill_cost_add = skill_cost[current_skill - 1] + skill_cost_add
                skill_climb += 1
                current_skill = current_skill - 1
            exp_check = exp.exp_remaining_check(exp_cost=skill_cost_add)
            if exp_check is True:
                self.character_dict['exp_remaining'] += skill_cost_add
                skills = self.character_dict['skills']
                skill_sub_dict = skills[skill_key]
                skill_sub_dict[skill_select] = skill_adjust


class MeritsFlaws(object):
    template = Templates()
    character_dict = PlayerCharacter.character_dict

    def print_merits_flaws(self, select, mf_dict, mf):
        print('\nᗘᗘ {} :\n'.format(select))
        for keys in mf_dict[select]:
            values = mf_dict[select][keys]
            cost, check, modifier = values
            if mf == 'merits':
                pm = '-'
            else:
                pm = '+'
            print('ᗘᗘᗘ {}:   [Cost: {}{}, Attribute Affected: {}, Modifier: +{}]'.format(keys, pm, cost, check, modifier))
            
    def get_current_merits_flaws(self, mf):
        current_mf = self.character_dict[mf]
        print('Current {}: '.format(mf.upper()))
        for merit_flaw in current_mf:
            print('{}'.format(merit_flaw))

    def get_merits(self):
        exp = ExperienceCheck()
        merits_end = False
        merits_limit = 0
        mf = 'merits'
        while merits_end is False:
            if merits_limit < 3:
                self.get_current_merits_flaws(mf=mf)
                merits_list_select = input(self.template.GET_MERITS).upper()
                if merits_list_select == 'CANCEL':
                    merits_end = True
                else:
                    merits_dict = self.template.MERITS
                    self.print_merits_flaws(select=merits_list_select, mf_dict=merits_dict, mf=mf)
                    merits_select = input(self.template.SELECT_MF).lower()
                    if merits_select == 'cancel':
                        merits_end = True
                    elif merits_select == 'change list':
                        continue
                    else:
                        if merits_select in merits_dict[merits_list_select]:
                            merit_values = merits_dict[merits_list_select][merits_select]
                            exp_cost = merit_values[0]
                            exp_check = exp.exp_remaining_check(exp_cost=exp_cost)
                            if exp_check is True:
                                merits_mini_dict = {merits_select: merits_dict[merits_list_select][merits_select]}
                                merits = self.character_dict['merits']
                                merits.update(merits_mini_dict)
                                self.character_dict['exp_remaining'] -= exp_cost
                                merits_limit += 1
                        else:
                            print(self.template.VALID_ENTRY)
            else:
                merits_end = True

    def get_flaws(self):
        exp = ExperienceCheck()
        flaws_end = False
        flaws_limit = 0
        mf = 'flaws'
        while flaws_end is False:
            if flaws_limit < 3:
                self.get_current_merits_flaws(mf=mf)
                flaws_list_select = input(self.template.GET_FLAWS).upper()
                if flaws_list_select == 'CANCEL':
                    flaws_end = True
                else:
                    flaws_dict = self.template.FLAWS
                    self.print_merits_flaws(select=flaws_list_select, mf_dict=flaws_dict, mf=mf)
                    flaws_select = input(self.template.GET_FLAWS).lower()
                    if flaws_select == 'cancel':
                        flaws_end = True
                    elif flaws_select == 'change list':
                        continue
                    else:
                        if flaws_select in flaws_dict[flaws_list_select]:
                            merit_values = flaws_dict[flaws_list_select][flaws_select]
                            exp_cost = merit_values[0]
                            exp_check = exp.exp_remaining_check(exp_cost=exp_cost)
                            if exp_check is True:
                                flaws_mini_dict = {flaws_select: flaws_dict[flaws_list_select][flaws_select]}
                                flaws = self.character_dict['flaws']
                                flaws.update(flaws_mini_dict)
                                self.character_dict['exp_remaining'] += exp_cost
                                flaws_limit += 1
                        else:
                            print(self.template.VALID_ENTRY)
            else:
                flaws_end = True


class POCC(object):
    template = Templates()
    character_dict = PlayerCharacter.character_dict

    def print_pocc(self):
        print(self.template.POCC)

    def get_pocc(self):
        pocc_end = False
        while pocc_end is False:
            self.print_pocc()
            select_pocc = input(self.template.SELECT_POCC).lower()
            selected_pocc = self.template.PRIMARY_OCC.keys()
            if select_pocc in selected_pocc:
                pocc = self.template.POCC[select_pocc]
                self.character_dict['pocc'] = pocc
                bonus_adjust_sk1 = pocc[0]
                bonus_attribute_sk1 = pocc[1]
                bonus_adjust_sk2 = pocc[2]
                bonus_attribute_sk2 = pocc[3]
                self.character_dict['skills'][bonus_attribute_sk1] = bonus_adjust_sk1
                self.character_dict['skills'][bonus_attribute_sk2] = bonus_adjust_sk2

                pocc_end = True


class SOCC(object):
    template = Templates()
    character_dict = PlayerCharacter.character_dict

    def print_socc(self, socc_req):
        socc = self.template.SECONDARY_OCC[socc_req]
        for entry in socc:
            print(self.template.SECONDARY_OCC)

    def get_socc(self):
        socc_req = self.character_dict['pocc']
        socc_end = False
        while socc_end is False:
            self.print_socc(socc_req=socc_req)
            select_socc = input(self.template.SELECT_SOCC).lower()
            if select_socc in self.template.SECONDARY_OCC:
                socc = self.template.SECONDARY_OCC[select_socc]
                bonus_attributes = socc[1]
                bonus_adjust = int(socc[0])
                self.character_dict['skills'][bonus_attributes] += bonus_adjust



class BonusChecks(object):
    def get_bonuses(self):
        pass
    

class ExperienceCheck(object):
    template = Templates()
    character_dict = PlayerCharacter.character_dict
    
    def exp_remaining_check(self, exp_cost):
        is_valid = True
        exp_cost_total = self.character_dict['exp_remaining'] - exp_cost
        if exp_cost_total <= 0:
            input(self.template.NO_EXP_MSG)
            is_valid = False
            return is_valid
        else:
            return is_valid

    # def __str__(self):
    #     return '{}, HP: {}, XP: {}'.format(self.name, self.hp, self.exp)
    #
    # def rest(self):
    #     if self.hp < self.base_hp:
    #         self.hp += 1
    #
    # def leveled_up(self):
    #     self.exp += self.monster.exp
    #     if self.exp == '5':
    #         self.level += 1
    #     elif self.exp == '10':
    #         if self.level != 2:
    #             self.level += 2
    #         self.level += 1
    #     elif self.exp == '15':
    #         self.level += 1
    #     print('Level {}! You\'ve leveled up!! Power courses through you'.format(self.level))
