from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=150, verbose_name="Jméno")
    description = models.TextField(blank=True, null=True, verbose_name="Popis")

    LOCATION_TYPE_CHOICES = (
        ("kontinent", "Kontinent"),
        ("království", "Království"),
        ("region", "Region"),
        ("město", "Město"),
        ("specifická lokace", "Specifická lokace"),
    )
    type = models.CharField(max_length=100, verbose_name="Typ", choices=LOCATION_TYPE_CHOICES)

    continent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="Kontinent", blank=True, null=True, related_name="continent_locations")
    kingdom = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="Království", blank=True, null=True, related_name="kingdom_locations")
    region = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="Region", blank=True, null=True, related_name="region_locations")
    city = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="Město", blank=True, null=True, related_name="city_locations")
    specific_location = models.CharField(max_length=150, verbose_name="Specifická lokace", blank=True, null=True)
    
    class Meta:
        verbose_name = "Lokace"
        verbose_name_plural = "Lokace"

    def __str__(self):
        return self.name

class NPC(models.Model):

    name = models.CharField(max_length=150, verbose_name="Jméno")
    description = models.TextField(blank=True, null=True, verbose_name="Popis")
    npc_location_id = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name="Lokace", blank=True, null=True, related_name="npc_locations")
    npc_location_name = models.CharField(max_length=150, verbose_name="Jméno lokace", blank=True, null=True)
    
    class Meta:
        verbose_name = "NPC"
        verbose_name_plural = "NPC"

    def save(self, *args, **kwargs):
        if self.npc_location_id:
            self.npc_location_name = self.npc_location_id.name
        super().save(*args, **kwargs)

    def __str__(self):

        return self.name

from django.db import models

class Player(models.Model):

    RACE_CHOICES = (
        ("člověk", "Člověk"),
        ("elf", "Elf"),
        ("hobit", "Hobit"),
        ("trpaslík", "Trpaslík"),
        ("drakorozený", "Drakorozený"),
        ("gnóm", "Gnóm"),
        ("půlelf", "Půlelf"),
        ("půlork", "Půlork"),
        ("tiefling", "Tiefling"),
    )

    CLASS_CHOICES = (
        ("barbar", "Barbar"),
        ("bard", "Bard"),
        ("bojovník", "Bojovník"),
        ("čaroděj", "Čaroděj"),
        ("černokněžník", "Černokněžník"),
        ("druid", "Druid"),
        ("hraničář", "Hraničář"),
        ("klerik", "Klerik"),
        ("kouzelník", "Kouzelník"),
        ("mnich", "Mnich"),
        ("paladin", "Paladin"),
        ("tulák", "Tulák"),
    )

    PRESVEDCENI_CHOICES = (
        ("zakonné dobro", "Zákonné DOBRO"),
        ("neutrální dobro", "Neutrální DOBRO"),
        ("chaotické dobro", "Chaotické DOBRO"),
        ("zákonně neutrální", "Zákonně NEUTRÁLNÍ"),
        ("neutrální", "NEUTRÁLNÍ"),
        ("chaoticky neutrální", "Chaoticky NEUTRÁLNÍ"),
        ("neutrální zlo", "Neutrální ZLO"),
        ("chaotické zlo", "Chaotické ZLO"),
        ("zakonné zlo", "Zákonné ZLO"),
    )

    # IDENTIFIKACE POSTAVY
    player_id = models.AutoField(primary_key=True, verbose_name="ID")
    real_name = models.CharField(max_length=150, verbose_name="Jméno hráče", blank=True, null=True)
    nick_name = models.CharField(max_length=150, verbose_name="Jméno postavy", blank=True, null=True)
    
    # ZÁKLADNÍ ÚDAJE
    lvl = models.IntegerField(default=1, verbose_name="Úroveň", blank=True, null=True)
    xp = models.IntegerField(default=0, verbose_name="Zkušenosti (XP)", blank=True, null=True)
    gender = models.CharField(max_length=10, verbose_name="Pohlaví", choices=[("M", "Muž"), ("F", "Žena"),("O", "Obojí"), ("Jiné", "Jiné")], blank=True, null=True)
    vyska = models.FloatField(default=0, verbose_name="Výška", blank=True, null=True)
    vaha = models.FloatField(default=0, verbose_name="Váha", blank=True, null=True)
    vek = models.IntegerField(default=0, verbose_name="Věk", blank=True, null=True)

    rasa = models.CharField(max_length=100, verbose_name="Rasa", choices=RACE_CHOICES, blank=True, null=True)
    povolani = models.CharField(max_length=100, verbose_name="Povolání", choices=CLASS_CHOICES, blank=True, null=True)
    presvedceni = models.CharField(max_length=100, verbose_name="Přesvědčení", choices=PRESVEDCENI_CHOICES, blank=True, null=True)

    popis_global = models.TextField(max_length=2000, verbose_name="Celkový popis postavy", blank=True, null=True)
    backstory = models.TextField(max_length=2000, verbose_name="Pozadí", blank=True, null=True)
    
    # OSOBNOST A PŘÍBĚH (Důležité pro roleplay)
    rysy = models.TextField(max_length=500, verbose_name="Osobnostní rysy", blank=True, null=True)
    idealy = models.TextField(max_length=500, verbose_name="Ideály", blank=True, null=True)
    pouta = models.TextField(max_length=500, verbose_name="Pouta", blank=True, null=True)
    vady = models.TextField(max_length=500, verbose_name="Vady", blank=True, null=True)

    # HLAVNÍ VLASTNOSTI
    sila = models.IntegerField(default=10, verbose_name="Síla", blank=True, null=True)
    obratnost = models.IntegerField(default=10, verbose_name="Obratnost", blank=True, null=True)
    odolnost = models.IntegerField(default=10, verbose_name="Odolnost", blank=True, null=True)
    inteligence = models.IntegerField(default=10, verbose_name="Inteligence", blank=True, null=True)
    moudrost = models.IntegerField(default=10, verbose_name="Moudrost", blank=True, null=True)
    charisma = models.IntegerField(default=10, verbose_name="Charisma", blank=True, null=True)

    # ODVOZENÉ STATISTIKY (Boj a základ)
    hp_max = models.IntegerField(default=10, verbose_name="Maximální životy", blank=True, null=True)
    hp_aktualni = models.IntegerField(default=10, verbose_name="Aktuální životy", blank=True, null=True)
    hp_docasne = models.IntegerField(default=0, verbose_name="Dočasné životy", blank=True, null=True)
    
    ac = models.IntegerField(default=10, verbose_name="Třída zbroje (AC)", blank=True, null=True)
    iniciativa = models.IntegerField(default=0, verbose_name="Iniciativa (Bonus)", blank=True, null=True)
    rychlost = models.IntegerField(default=30, verbose_name="Rychlost (stopy)", blank=True, null=True)
    
    hit_dice_typ = models.CharField(max_length=10, verbose_name="Typ kostky životů (např. k8)", blank=True, null=True)
    hit_dice_pocet = models.IntegerField(default=1, verbose_name="Aktuální počet kostek životů", blank=True, null=True)
    
    prof_bonus = models.IntegerField(default=2, verbose_name="Bonus za zdatnost", blank=True, null=True)
    pasivni_vnimani = models.IntegerField(default=10, verbose_name="Pasivní vnímavost", blank=True, null=True)

    # ZÁCHRANNÉ HODY (Označení, v čem je postava zdatná)
    save_str = models.BooleanField(default=False, verbose_name="Záchranný hod: Síla")
    save_dex = models.BooleanField(default=False, verbose_name="Záchranný hod: Obratnost")
    save_con = models.BooleanField(default=False, verbose_name="Záchranný hod: Odolnost")
    save_int = models.BooleanField(default=False, verbose_name="Záchranný hod: Inteligence")
    save_wis = models.BooleanField(default=False, verbose_name="Záchranný hod: Moudrost")
    save_cha = models.BooleanField(default=False, verbose_name="Záchranný hod: Charisma")

    # DOVEDNOSTI (Označení zdatností - Proficiencies)
    sk_akrobacie = models.BooleanField(default=False, verbose_name="Akrobacie (Obr)")
    sk_atletika = models.BooleanField(default=False, verbose_name="Atletika (Síl)")
    sk_cachry = models.BooleanField(default=False, verbose_name="Čachry (Obr)")
    sk_historie = models.BooleanField(default=False, verbose_name="Historie (Int)")
    sk_klamani = models.BooleanField(default=False, verbose_name="Klamání (Cha)")
    sk_lekarstvi = models.BooleanField(default=False, verbose_name="Lékařství (Mdr)")
    sk_mystika = models.BooleanField(default=False, verbose_name="Mystika (Int)")
    sk_nabozenstvi = models.BooleanField(default=False, verbose_name="Náboženství (Int)")
    sk_nenapadnost = models.BooleanField(default=False, verbose_name="Nenápadnost (Obr)")
    sk_priroda = models.BooleanField(default=False, verbose_name="Příroda (Int)")
    sk_presvedcovani = models.BooleanField(default=False, verbose_name="Přesvědčování (Cha)")
    sk_preziti = models.BooleanField(default=False, verbose_name="Přežití (Mdr)")
    sk_vhled = models.BooleanField(default=False, verbose_name="Vhled (Mdr)")
    sk_vnimani = models.BooleanField(default=False, verbose_name="Vnímání (Mdr)")
    sk_vystupovani = models.BooleanField(default=False, verbose_name="Vystupování (Cha)")
    sk_vysetrovani = models.BooleanField(default=False, verbose_name="Vyšetřování (Int)")
    sk_zachazeni_zviraty = models.BooleanField(default=False, verbose_name="Zacházení se zvířaty (Mdr)")
    sk_zastrasovani = models.BooleanField(default=False, verbose_name="Zastrašování (Cha)")

    # VYBAVENÍ A SOUBOJ
    # (Zbraně a útoky by v čistě relační databázi měly svůj vlastní model přes ForeignKey,
    # ale pro jednoduchost v jednom modelu je lze zapsat jako text)
    zbrane_a_utoky = models.TextField(verbose_name="Zbraně a Útoky (Název, Bonus, Poškození)", blank=True, null=True)
    vybaveni = models.TextField(verbose_name="Nesené vybavení", blank=True, null=True)
    zlataky = models.IntegerField(default=0, verbose_name="Zlaté mince (Zlaťáky)") 

    # MAGIE A SCHOPNOSTI
    schopnosti_rasy_a_povolani = models.TextField(verbose_name="Schopnosti a Rysy", blank=True, null=True)
    
    spellcasting_ability = models.CharField(max_length=20, verbose_name="Vlastnost pro sesílání", blank=True, null=True)
    spell_save_dc = models.IntegerField(default=0, verbose_name="SO Záchrany kouzla", blank=True, null=True)
    spell_atk_bonus = models.IntegerField(default=0, verbose_name="Útočný bonus kouzla", blank=True, null=True)
    
    kouzla_triky = models.TextField(verbose_name="Triky (Cantrips)", blank=True, null=True)
    kouzla_seznam = models.TextField(verbose_name="Seznam známých kouzel", blank=True, null=True)
    spell_slots = models.JSONField(verbose_name="Pozice kouzel (JSON formát: úroveň a počet)", blank=True, null=True)

    def __str__(self):
        return f"{self.nick_name} ({self.povolani} lvl {self.lvl})"
    
    
    
    