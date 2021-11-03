import sqlite3

con = sqlite3.connect('data.sqlite', isolation_level=None)

def init_sql():
  con.execute('''CREATE TABLE IF NOT EXISTS data (
      id               integer primary key
    , name             text    null
    , rarity           text    null
    , Type             text    null
    , Level            integer null
    , Attack           integer null
    , Defense          integer null
    , Armor            integer null
    , Damage           integer null
    , HP               integer null
    , XPGain           integer null
    , Stamina          integer null
    , StaminaGain      integer null
    , GoldGain         integer null
    , Banishment       integer null
    , BeastSlayer      integer null
    , Breaker          integer null
    , CriticalHit      integer null
    , Disarm           integer null
    , Dodge            integer null
    , Duelist          integer null
    , EliteHunter      integer null
    , FirstStrike      integer null
    , FuryCaster       integer null
    , GlorySeeker      integer null
    , GreenskinSlayer  integer null
    , Holy             integer null
    , Hypnotize        integer null
    , MasterBlacksmith integer null
    , MasterCrafter    integer null
    , MasterInventor   integer null
    , MasterThief      integer null
    , Nullify          integer null
    , Oceanic          integer null
    , PiercingStrike   integer null
    , ProtectGold      integer null
    , Protection       integer null
    , ReinforcedArmor  integer null
    , Sustain          integer null
    , TemporalShift    integer null
    , Thievery         integer null
    , craftAttack      integer null
    , craftDefense     integer null
    , craftArmor       integer null
    , craftDamage      integer null
    , craftHP          integer null
    , craftXPGain      integer null
    , craftStamina     integer null
    , craftGoldGain    integer null
    , setName          text    null
    , setAttack        integer null
    , setDefense       integer null
    , setArmor         integer null
    , setDamage        integer null
    , setHP            integer null
    , setXPGain        integer null
    , setStamina       integer null
    , setStaminaGain   integer null
    , setGoldGain      integer null
  )''')

def close_sql():
  con.close()

def sql_writer(list):
  colNames = ', '.join([a for (a, b) in list])
  placeholders = ', '.join(['?' for (a, b) in list])
  values = tuple(b for (a, b) in list)
  con.execute(f'REPLACE INTO data ({colNames}) values({placeholders})', values)