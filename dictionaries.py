import pandas as pd
from helpers import remove_punctuation


# World War 1 dictionary

ww1_dict = ['world war i', 'world war 1', 'ww1', 'wwi', '1914', '1916', '1917', '1918', 'the great war', 'verdun', 'somme', 'mustard gas', 'no man\'s land', 'armistice', 'trenches', 'trench', 'treaty of versailles', 'colonial troops', 'franz ferdinand', 'wilson', 'lusitania', 'central powers', 'league of nations', '1915', 'spanish flu', 'spanish influenza', 'first world war']


# World War 2 dictionary 

ww2_dict = ['world war ii', 'world war 2', 'ww2', 'wwii', '1939', '1940', '1941', '1942', '1943', '1944', '1945', 'axis powers', 'allied powers', 'hitler', 'churchill', 'roosevelt', 'stalin', 'holocaust', 'pearl harbor', 'hiroshima', 'nagasaki', 'nazis', 'nazi', 'concentration camps', 'fascism', 'fascist', 'dunkirk', 'atomic bomb', 'nuclear', 'united nations', 'enigma code', 'd-day', 'reich', 'marshall plan', 'gestapo', 'deportation', 'auschwitz', 'swastika', 'ss', 'blitzkrieg', 'stalingrad', 'internment camps', 'manhattan project', 'nuremberg trials', 'luftwaffe', 'the big three']


# Space Exploration dictionary 

space_dict = ['moon landing', '1969', 'apollo 11', 'apollo', 'space race', 'neil armstrong', 'buzz aldrin', 'michael collins', 'lunar module', 'command module', 'lunar surface', 'moon mission', 'lunar landing', 'astronauts', 'astronaut', 'flag planting', 'apollo program', 'spaceflight', 'saturn 5', 'saturn v', 'laika', 'moonwalk', 'moon rover', 'spacecraft', 'nasa', 'solar system', 'mars', 'satellite', 'satellites', 'international space station', 'iss', 'yuri gagarin', 'gagarin', 'sputnik', 'mercury program', 'vostok program', 'luna program', 'space shuttle program', 'mir space station']


# Cold War dictionary

cold_war_dict = ['nuclear arms race', 'iron curtain', 'berlin airlift', 'proxy wars', 'proxy war', 'proxy states',  'cuban missile', 'cuban revolution', 'berlin wall', 'mccarthyism', 'mutual assured destruction', 'warsaw pact', 'north atlantic treaty organization', 'sputnik', 'perestroika', 'glasnost', 'helsinki accords', 'truman doctrine', 'huac', 'house un-american activities committee', 'korean war', 'gorbachev', 'khrushchev', 'kennedy', 'stalin', 'nixon', 'truman', 'johnson', 'saigon', 'agent blue', 'agent orange', 'paris peace accords', 'napalm', 'mutually assured destruction', 'mutually-assured destruction', 'mi5', 'soviet union', 'ussr', 'mutual defense assistante act', 'nuclear deterrence', 'olympic boycott', 'olympic boycotts', ' ostpolitik', 'brandt', 'reagan', 'red scare', 'russification', 'south-east asia treaty organisation', 'seato', 'sovietisation', 'stasi', 'tet', 'checkpoint charlie', 'cold war', 'east germany', 'west germany', 'iron curtain', 'gdr', 'frg', 'ddr', 'brd', 'reunification', 'space race', 'apollo program', 'apollo 11','atomic testing', 'arms race']


# Vietnam War dictionary

vietnam_war_dict = ['vietnam war', 'viet cong', 'viet', 'viets', 'agent orange', 'napalm', 'tet offensive', 'my lai massacre', 'hanoi', 'saigon', 'tonkin', 'paris peace accords', 'rolling thunder', 'agent blue', '1954', '1974', 'nixon']


# Women Emancipation dictionary 

women_emancipation_dict = ['feminism', 'suffrage', 'equal rights', 'gender equality', "women's liberation", 'female empowerment', 'female emancipation', 'gender roles', "women's rights", 'glass ceiling', 'patriarchy', 'sexism', 'feminist', 'abortion', 'women in the workplace', 'equal pay', 'maternity leave', 'body positivity', 'sexual harassment', 'sexist', 'gender wage gap', 'gender discrimination', 'domestic violence', "women's march", 'gender stereotypes', 'gender bias', 'empowering', "women's health", 'contraceptive pill', 'birth-control', 'gender inequality', 'contraception', 'wage gap', 'gender pay gap', 'seneca falls', 'suffragist', 'suffragists', 'feminists', 'reproductive rights', 'international women’s day', 'roe v. wade', 'birth control', 'gender gap', "women’s abilities", 'female engineer', 'female mathematician', 'first woman', 'first female', 'gender inequality', 'macho', 'veil']


# Black History dictionary

black_history_dict = ['black history', 'slavery', 'emancipation proclamation', 'underground railroad', 'jim crow laws', 'segregation', 'montgomery bus boycott', 'martin luther king jr.', 'rosa parks', 'malcolm x', 'black panthers', 'frederick douglass', 'harriet tubman', 'sojourner truth', 'booker t. washington', 'w.e.b. du bois', 'civil rights act', 'voting rights act', 'black power', 'african american culture', 'harlem renaissance', 'great migration', 'tuskegee airmen', 'buffalo soldiers', 'negro league baseball', 'black lives matter', 'kwanzaa', 'haitian revolution', 'madam cj walker', 'tuskegee experiment', 'zora neale hurston', 'shirley chisholm', 'octavius catto', 'black wall street', 'black liberation', 'slave rebellion', 'freedom riders', 'hip-hop', 'african diaspora', 'american civil war', 'kkk', 'ku klux klan', 'racism', 'racist', 'discrimination', 'segregate', 'segregated', 'colored facilities', 'first black', 'first african american', 'civil rights movement', 'martin luther king', 'juneteenth', 'slave', 'slaves', 'racists', 'apartheid', 'nelson mandela', 'mlk', 'black harlem', 'new negro movement']


# Digitalisation dictionary

digitalisation_dict = ['internet', 'drones', 'computer', 'mobile phone', 'web', 'robots', 'artificial intelligence', 'social media', 'hackers', 'laptop', 'screen', 'facebook', 'software', 'instagram', 'twitter', 'smartphone', 'computers', 'mobile phones', 'darkweb', 'google', 'microsoft', 'hacking', 'cybersecurity', 'cyber-attack', 'cyber attack', 'cybercrime', 'hacker']


# Sexuality dictionary

sexuality_dict = ['sexuality', 'gender expression', 'bdsm', 'safe sex', 'sexual health', 'sex education', 'reproductive rights', 'sex-worker', 'sexual empowerment', 'stripper', 'strip-club', 'strip club', 'sexual stigma', 'kink', 'fetish', 'polyamory', 'polygamy', 'monogamy', 'sexuality exploration', 'sexuality education', 'sexual liberation', 'pleasure activism', 'prostitute', 'sadism', 'condom', 'contraception', 'orgasm', 'masturbation', 'masturbating', 'jerking off', 'get laid', 'pornography', 'porno', 'porn', 'pornstar', 'anal', 'sextoy', 'dildo', 'libido', 'vulva', 'vagina', 'penis']


# STDs dictionary

STDs_dict = ['aids', 'hiv', 'human immunodeficiency virus', 'acquired immunodeficiency syndrome', 'antiretroviral therapy', 'hiv transmission', 'hiv testing', 'aids symptoms', 'hiv prevention', 'aids awareness', 'world aids day', 'aids activism', 'freddie mercury', 'hiv-positive', 'hiv-negative', 'sexually transmissible disease', 'std', 'syphilis', 'chlamydia', 'herpes', 'sexual health', 'gonorrhea', 'papillomavirus', 'cervical cancer', 'pelvic inflammatory disease', 'mycoplasma genitalium', 'uti', 'trichomoniasis', 'infertility', 'stds']


# Opioid crisis dictionary

opioid_crisis_dict = ['drug', 'opioid crisis', 'opioids', 'opioid', 'prescription painkillers', 'heroin', 'fentanyl', 'overdose', 'naloxone', 'substance abuse', 'pain management', 'methadone', 'morphine', 'buprenorphine', 'narcotic analgesics', 'overdosed', 'morphium', 'pain reliever', 'pain relievers', 'pain killer', 'pain killers', 'pain relief', 'syringe', 'syringes']


# Mental Health dictionary

mental_health_dict = ['psychoses', 'psychose', 'psychosis', 'schizophrene', 'schizophrenia', 'schizophrenic', 'psychiatrist', 'psychiatrists', 'psychiatric hospital', 'ptsd', 'post traumatic stress disorder', 'anxiety', 'shell shock', 'anti-depressants', 'depression', 'depressed', 'antidepressant', 'anti-depressant', 'antidepressants', 'bipolar disorder', 'bipolar', 'mental disorder', 'eating disorder', 'eating disorders', 'mental health', 'anorexia', 'burnout', 'burn-out', 'self harm', 'selfharm', 'self-harm', 'obsessive disorder', 'compulsive disorder', 'ocd', 'panic attack']


# Atomic Bomb dictionary

atomic_bomb_dict = ['manhattan project', 'oppenheimer', 'hiroshima', 'nagasaki', 'enola gay', 'trinity test', 'nuclear explosion', 'atomic testing', 'radiation effects', 'arms race', 'atomic bombings', 'fat man', 'nuclear chain reaction', 'nuclear', 'atomic']


# Genetic Engineering dictionary

genetic_engineering_dict = ['genetic', 'gene', 'genes', 'dna', 'genome', 'biotechnology', 'cloning', 'clone', 'clones', 'crispr-cas9', 'crispr', 'genetically modified', 'gmo', 'mutation', 'designer babies', 'gene therapy', 'stem cells', 'in vitro fertilization', 'ivf', 'in vitro', 'epigenetics', 'regenerative medicine', 'biohacking', 'in vivo']


# LGBTQIA+ dictionary

lgbtq_dict = ['gay', 'lesbian', 'lgbt pride', 'bisexual', 'drag queen', 'transexual', 'marriage equality', 'homosexual', 'coming out', 'homosexual rights', 'aids stigma', 'non binary', 'queer', 'freddie mercury', 'lgbtq+', 'two-spirit', 'transphobia', 'gender identity', 'lgbtqia+', 'transgender', 'gender fluid', 'asexual', 'pansexual', 'same-sex marriage', 'transsexual', 'non-binary', 'bisexuality', 'homosexuality', 'transsexuality', 'homophobia', 'homophobic', 'gender dysphoria', 'stonewall', 'lgbt', 'lgbtq', 'sexual orientation', 'drag show', 'drag performance', 'sex change', 'gender affirming surgery']


# Terrorism dictionary

terrorism_dict = ['terrorism', 'terrorist', 'terrorist attack', 'suicide bombing', 'suicide bomb', 'suicide bomber', '9-11', 'twin towers', 'hostage crisis', 'jihad', 'al-qaeda', 'bin laden', 'boeing 767', 'pentagon', 'flight 11', 'flight 175', 'flight 77', 'flight 93', 'hijacking', 'hijackers', 'hijacker', 'hijacked', 'isis', 'islamic state', 'explosive belt', 'counterterrorism', 'counter-terrorism', 'terrorists', 'nine eleven', 'september 11', 'homeland security', 'world trade center', 'north tower', 'south tower']


# List of events/movements and list of associated dictionaries

events = ['WW1', 'WW2', 'Space', 'Cold War', 'Vietnam War', 'Women emancipation', 'Black History', 'Digitalisation', 'Sexuality', 'STDs', 'Opioid Crisis', 'Mental Health', 'Atomic Bomb', 'Genetic Engineering', 'LGBTQ', 'Terrorism' ]
dictionaries = [ww1_dict, ww2_dict, space_dict, cold_war_dict, vietnam_war_dict, women_emancipation_dict, black_history_dict, digitalisation_dict, sexuality_dict, STDs_dict, opioid_crisis_dict, mental_health_dict, atomic_bomb_dict, genetic_engineering_dict, lgbtq_dict, terrorism_dict]
new_dictionaries = []


# Change the layout of the dictionaries to prepare for word search (replace `', '` with ` | `)

for el in dictionaries:
    for word in el:
        word = remove_punctuation(word) 
    new_dictionaries.append(' | '.join(el))


# Create a DataFrame for 'events' dictionaries

dictionaries_df = pd.DataFrame(list(zip(events, new_dictionaries)), columns=['events', 'dictionaries'])
dictionaries_df = dictionaries_df.set_index('events')


# Create a .csv file containing the dictionaries dataframe

dictionaries_df.to_csv('data/AdditionalDatasets/dictionaries.csv', index = True)