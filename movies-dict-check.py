import pandas as pd


# Creating the test sets : dataframes of movies with known associated event or movement

# Test subset for WW1

ww1_test_set = pd.DataFrame({
    'id_wiki': [354122, 4592959, 1198629, 6361585, 5403512, 5501736, 7133888, 73368, 62097, 23255, 27754718, 8368715, 1205027, 3092405],
    'id_freebase': ['/m/01znj1', '/m/0cbl95', '/m/04gm93', '/m/0g2h97', '/m/0dk937', '/m/0dpq1q', '/m/0h5ys_', '/m/0jq1x', '/m/0gsx1', '/m/05sjq', '/m/0cc5qkt', '/m/0270_nb', '/m/04h4c9', '/m/08qwy4'],
    'name': ['Gallipoli', 'All Quiet on the Western Front', 'Aces High', 'The Red Baron', 'Flyboys', 'Darling Lili', 'The Lost Patrol', 'The Big Parade', 'Grand Illusion', 'Paths of Glory', 'War Horse', 'Johnny Got His Gun', 'A Very Long Engagement', 'Merry Christmas'],
    'date': ['1981', '1930-04-21', '1976', '2008-03-31', '2006-09-22', '1970-06-24', '1934-02-16', '1925', '1937', '1957', '2011.0', '1971.0', '2004.0', '2005.0']
})
ww1_test_set['true_event'] = [['WW1'] for el in range(len(ww1_test_set))]


# Test subset for WW2

ww2_test_set = pd.DataFrame({
    'id_wiki': [57585, 4492505, 8994, 182164, 633052, 14725310, 28269, 65834, 42159, 42856, 142465, 181229, 99454],
    'id_freebase': ['/m/0ft18', '/m/0c5d5j', '/m/02h22', '/m/018wsw', '/m/02yvct', '/m/0gy0l_', '/m/07024', '/m/0hfzr', '/m/0bl5c', '/m/0bs4r', '/m/011ysn', '/m/018rvr', '/m/0pd4f'],
    'name': ['Casablanca', 'Come and See', 'Das Boot', 'Grave of the Fireflies', 'Inglourious Basterds', 'Letters from Iwo Jima', 'Saving Private Ryan', "Schindler's List", 'The Best Years of Our Lives', 'The Bridge on the River Kwai', 'The Thin Red Line', 'The Great Escape', 'Patton'],
    'date': ['1942-11-26', '1985', '1981-09-17', '1988-04-16', '2009-05-20', '2006-12-09', '1998-07-24', '1993-11-30', '1946', '1957-10-02', '1998.0', '1963.0', '1970.0']
})
ww2_test_set['true_event'] = [['WW2'] for el in range(len(ww2_test_set))] 


# Test subset for Space Race

space_exploration_test_set = pd.DataFrame({
    'id_wiki': [142417, 113442, 1110047, 13887546, 11378430, 879000, 3146408, 103325, 1722156, 379851, 1619604, 10543866, 5541680, 878670],
    'id_freebase': ['/m/011yd2', '/m/0sxgv', '/m/046vs6', '/m/03cm7j_', '/m/02r9hx1', '/m/03l3hv', '/m/08vf0c', '/m/0q23s', '/m/05r3qc', '/m/021fvl', '/m/05h6v8', '/m/02qhcj5', '/m/0drp1s', '/m/03l29p'],
    'name': ['Apollo 13', 'The Right Stuff', 'October Sky', 'From the Earth to the Moon', 'The Mouse on the Moon', 'Destination Moon', 'G.O.R.A.', 'Royal Space Force: The Wings of Honneamise', 'Space Cowboys', 'The Dish', 'Marooned', 'In the Shadow of the Moon', 'Race to Space', 'First Men in the Moon'],
    'date': ['1995-06-22', '1983-10-21', '1999-02-19', '1958', '1963', '1950-06-27', '1968', '2004-11-12', '2000.0', '2000.0', '1969.0', '2007.0', '2002.0', '1964.0']
})
space_exploration_test_set['true_event'] = [['Space Exploration'] for el in range(len(space_exploration_test_set))] 
space_exploration_test_set['true_event'][4].append('Cold War')
space_exploration_test_set['true_event'][7].append('Cold War')


# Test subset for Cold War

cold_war_test_set = pd.DataFrame({
    'id_wiki': [464883, 1129041, 37241569, 566713, 34130, 5454803, 2663129, 58147, 8695, 9378717, 470185, 16613205, 3557540],
    'id_freebase': ['/m/02crgz', '/m/048scx', '/m/0n53wvj', '/m/02qrv7', '/m/08720', '/m/0dmn0x', '/m/07w8fz', '/m/0fy66', '/m/02dwj', '/m/0286hyp', '/m/02dcrt', '/m/03yf02f', '/m/09ldwy'],
    'name': ['Miracle', 'Thirteen Days', 'Cold War', 'The Living Daylights', 'WarGames', 'The Lives of Others', 'Good Night, and Good Luck.', 'The Manchurian Candidate', 'Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb', 'The Spy Who Came in from the Cold', 'Three Days of the Condor', 'The Tunnel', 'The Hunt for Red October'],
    'date': ['2004-02-06', '2000-12-16', '2012-11-08', '1987', '1983-06-03', '2006-03-15', '2005-09-01', '1962-10-24', '1964-01-29', '1965.0', '1975.0', '1935.0', '1990.0']
})
cold_war_test_set['true_event'] = [['Cold War'] for el in range(len(cold_war_test_set))]
cold_war_test_set['true_event'][4].append('Atomic Bomb')
cold_war_test_set['true_event'][4].append('Digital Revolution')
cold_war_test_set['true_event'][8].append('Atomic Bomb')


# Test subset for Vietnam War

vietnam_war_test_set = pd.DataFrame({
    'id_wiki': [18951054, 11701, 1011468, 3859075, 168593, 2478590, 675947, 103011, 1546168, 113460, 73425, 4457806, 226682],
    'id_freebase': ['/m/0jzw', '/m/0333t', '/m/03z106', '/m/0b3nrz', '/m/016kxf', '/m/07gv6d', '/m/0320br', '/m/0p_qr', '/m/0599rp', '/m/0sxmx', '/m/0jqj5', '/m/02p86pb', '/m/01h1cp'],
    'name': ['Apocalypse Now', 'Full Metal Jacket', 'We Were Soldiers', 'Rescue Dawn', 'Good Morning, Vietnam', 'Tigerland', 'Hamburger Hill', 'Coming Home', 'Heaven & Earth', 'Platoon', 'The Deer Hunter', 'Born on the Fourth of July', 'Casualties of War'],
    'date': ['1979-05-10', '1987-06-17', '2002-02-25', '2006-09-09', '1987-12-23', '2000-10-06', '1987-08-28', '1978-02-15', '1993-12-13', '1986-12-19', '1978.0', '1989.0', '1989.0']
})
vietnam_war_test_set['true_event'] = [['Vietnam War'] for el in range(len(vietnam_war_test_set))]
vietnam_war_test_set['true_event'][6].append('Mental Health')
vietnam_war_test_set['true_event'][7].append('Mental Health')


# Test subset for Women Emancipation

women_emancipation_test_set = pd.DataFrame({
    'id_wiki': [1164646, 390693, 25594421, 2148370, 74018, 5527808, 11347793, 176762, 444267, 249876, 106117, 3185575, 689785],
    'id_freebase': ['/m/04cq1k', '/m/022npf', '/m/09rvcvl', '/m/06qbrw', '/m/0jsxn', '/m/0dq_ss', '/m/02r8hh_', '/m/017zss', '/m/0296vv', '/m/01l2b3', '/m/026390q', '/m/08xvpn', '/m/032_br'],
    'name': ['Iron Jawed Angels', 'Born in Flames', 'Made in Dagenham', 'North Country', 'His Girl Friday', 'The Joy Luck Club', 'Persepolis', 'Whale Rider', 'Legally Blonde', 'Bend It Like Beckham', 'Thelma & Louise', 'The Color Purple', 'The Accused'],
    'date': ['2004-01-16', '1983', '2010-09-11', '2005-10-21', '1940-01-11', '1993-09-08', '2007-06-27', '2002-09-09', '2001-06-26', '2002-04-11', '1991.0', '1985.0', '1988.0']
})
women_emancipation_test_set['true_event'] = [['Women Emancipation'] for el in range(len(women_emancipation_test_set))]
women_emancipation_test_set['true_event'][6].append('Terrorism')
women_emancipation_test_set['true_event'][11].append('Black History')


# Test subset for Black History

black_history_test_set = pd.DataFrame({
    'id_wiki': [300972, 73428, 29454281, 225487, 2084045, 155997, 1073955, 19032190, 397574, 509676, 4770345, 707823, 3947481],
    'id_freebase': ['/m/01rwyq', '/m/0jqkh', '/m/0ds3t5x', '/m/01gvwd', '/m/06l2pj', '/m/014gcy', '/m/043ncp', '/m/09rsjpv', '/m/023gxx', '/m/02jxbw', '/m/0cmdm1',  '/m/034hzj',  '/m/0b83jp'],
    'name': ['Malcolm X', 'Do the Right Thing', 'The Help', 'Claudine', 'Crooklyn', 'Boyz N the Hood', 'Soul Food', 'Red Tails', 'Remember the Titans', 'Glory', 'Get on the Bus', 'Cry Freedom', 'The Great Debaters'],
    'date': ['1992-11-18', '1989-05', '2011-08-10', '1974', '1994-05-13', '1991-07-02', '1997-09-26', '2012-01-20', '2000-09-23', '1989.0', '1996.0', '1987.0', '2007.0']
})
black_history_test_set['true_event'] = [['Black History'] for el in range(len(black_history_test_set))]
black_history_test_set['true_event'][5].append('Drug Abuse')
black_history_test_set['true_event'][7].append('WW2')


# Test subset for Digitalisation

digitalization_test_set = pd.DataFrame({
    'id_wiki': [23941708, 30007, 34344124, 672934, 142224, 4273140, 1368785, 306195, 49696, 4338909, 24319139, 1438861, 264176],
    'id_freebase': ['/m/08ct6', '/m/07cz2', '/m/07gp9', '/m/031qr5', '/m/011xg5', '/m/0bth54', '/m/04x7w0', '/m/01sk1v', '/m/0d6b7', '/m/0bxy6l', '/m/07s846j', '/m/051n5m', '/m/01n4z6'],
    'name': ['2001: A Space Odyssey', 'The Matrix', 'Terminator 2: Judgment Day', 'The Lawnmower Man', 'A.I. Artificial Intelligence', 'Avatar', 'Freejack', 'The Net', 'Metropolis', 'Countdown', 'The Social Network', 'The Thirteenth Floor', 'Hackers'],
    'date': ['1968-04-06', '1999-03-31', '1991-07-01', '1992-03-06', '2001-06-26', '2009-12-10', '1992-01-17', '1995-07-28', '1927-01-10', '1987-03-14', '2010.0', '1999.0', '1995.0']
})
digitalization_test_set['true_event'] = [['Digital Revolution'] for el in range(len(digitalization_test_set))]
digitalization_test_set['true_event'][6].append('Genetic Engineering')


# Test subset for Sexuality

sexuality_test_set = pd.DataFrame({
    'id_wiki': [4838538, 44122, 1988806, 226842, 615121, 2141418, 2457326, 1897341, 28075240, 195388, 2557469, 163456, 1508787, 9979],
    'id_freebase': ['/m/0cqbfc', '/m/0c0zq', '/m/06c753', '/m/01h1zp', '/m/02wtp6', '/m/06ptw1', '/m/07fg13', '/m/064lsn', '/m/0cmc26r', '/m/01brqv', '/m/07mwp6', '/m/015qrk', '/m/056tj0',  '/m/02qcr'],
    'name': ['Summer with Monika', 'American Beauty', 'Lolita', 'Ken Park', 'The Dreamers', 'Mysterious Skin', 'Palindromes', 'The Pianist', 'A Dangerous Method', 'Y tu mamá también', 'Killing Me Softly', 'Last Tango in Paris', '9 Songs', 'Eyes Wide Shut'],
    'date': ['1953', '1999-09-08', '1997-09-27', '2002-08-31', '2003-09-01', '2004-09-03', '2005-01-21', '2002-05-24', '2011-09-02', '2001-06-08', '2002.0', '1972.0',  '2004.0', '1999.0']
})
sexuality_test_set['true_event'] = [['Sexuality'] for el in range(len(sexuality_test_set))]
sexuality_test_set['true_event'][3].append('LGBTQ')
sexuality_test_set['true_event'][6].append('Women Emancipation')
sexuality_test_set['true_event'][7].append('WW2')
sexuality_test_set['true_event'][8].append('Mental Health')


# Test subset for STDs

stds_test_set = pd.DataFrame({
    'id_wiki': [615418, 6256985, 28194808, 2046284, 11517671, 23266463, 468353, 543162, 13699003, 1367539, 171540, 593921, 1105412],
    'id_freebase': ['/m/02ww1t', '/m/0fz68f', '/m/0cnx21r', '/m/06hbq5', '/m/02rgktd', '/m/065_f26', '/m/02d49z', '/m/02nczh', '/m/03cffvv', '/m/04x4rr', '/m/0170th', '/m/02tgd2', '/m/046f3p'],
    'name': ['Kids', 'Teenage Caveman', 'Black Venus', "She's Too Young", 'Damaged Lives', 'Girl, Positive', 'Thirteen', "Boys Don't Cry", 'And the Band Played On', 'Longtime Companion', 'The People vs. Larry Flynt', 'The Pillow Book', 'Kinsey'],
    'date': ['1995-05', '2002', '2010-09', '2004-02-16', '1933', '2007-06-25', '2003-01-17', '1999-09-02', '1993-09-11', '1989-10', '1996.0', '1996.0', '2004.0']
})
stds_test_set['true_event'] = [['STDs'] for el in range(len(stds_test_set))]
stds_test_set['true_event'][0].append('Sexuality')
stds_test_set['true_event'][7].append('LGBTQ')
stds_test_set['true_event'][8].append('LGBTQ')
stds_test_set['true_event'][9].append('LGBTQ')
stds_test_set['true_event'][11].append('Sexuality')
stds_test_set['true_event'][12].append('Sexuality')


# Test subset for Drug Abuse

drug_abuse_test_set = pd.DataFrame({
    'id_wiki': [37599, 23830211, 3182907, 105434, 5842075, 1611072, 2470904, 1380618, 2244939, 6179073, 96893, 291610, 265975],
    'id_freebase': ['/m/09cr8', '/m/07k2mq', '/m/08xnxg', '/m/0qf2t', '/m/0f8j13', '/m/05gjj1', '/m/07gb81', '/m/04y2j6', '/m/06yv1n', '/m/0fvcx9', '/m/0n_hp', '/m/01qncf',  '/m/01ndgk'],
    'name': ['Traffic', 'Requiem for a Dream', 'The Basketball Diaries', 'Trainspotting', 'Fear and Loathing in Las Vegas', 'A Scanner Darkly', '28 Days', 'Permanent Midnight', 'Clean and Sober', 'Less Than Zero', 'Blow', 'Drugstore Cowboy', 'Sid and Nancy'],
    'date': ['2001-01-05', '2000-10-27', '1995-04-21', '1996-02-23', '1998-05-15', '2006-07-07', '2000-02-08', '1998-09-16', '1988', '1987-11-06', '2001.0', '1989.0', '1986.0']
})
drug_abuse_test_set['true_event'] = [['Drug Abuse'] for el in range(len(drug_abuse_test_set))]


# Test subset for Mental Health

mental_health_test_set = pd.DataFrame({
    'id_wiki': [54160, 33502433, 3383952, 7047921, 3569822, 106335, 26971354, 12685170, 9114950, 24480838, 21913863, 983692, 571311],
    'id_freebase': ['/m/0f4vx', '/m/0h95927', '/m/098s2w', '/m/0h1x5f', '/m/09m6kg', '/m/0qm98', '/m/0fpkhkz', '/m/02x0fs9', '/m/027y5ys', '/m/09k56b7', '/m/07xtqq', '/m/03wlrb', '/m/02r6sh'],
    'name': ['Leaving Las Vegas', 'The Silver Linings Playbook', 'Girl, Interrupted', 'Little Miss Sunshine', 'A Beautiful Mind', 'Ordinary People', 'Melancholia', 'Lars and the Real Girl', 'Fight Club - Members Only', 'Black Swan', "One Flew Over the Cuckoo's Nest", 'Sybil', 'An Angel at My Table'],
    'date': ['1995-09-15', '2012-11-21', '1999-12-08', '2006-01-20', '2001-12-13', '1980-09-19', '2011-05-18', '2007-09-10', '2006-02-17', '2010-09-01', '1975.0', '1976.0', '1990.0']
})
mental_health_test_set['true_event'] = [['Mental Health'] for el in range(len(mental_health_test_set))]
mental_health_test_set['true_event'][3].append('Women Emancipation')
mental_health_test_set['true_event'][4].append('Cold War')


# Test subset for Atomic Bomb

atomic_bomb_test_set = pd.DataFrame({
    'id_wiki': [123464, 993867, 936429, 242542, 37068, 8863891, 31607, 18735140, 31629, 779536, 10705512, 920062, 164365],
    'id_freebase': ['/m/0x2j1', '/m/03xj57', '/m/03rk23', '/m/01k5_t', '/m/097r7', '/m/027mh15', '/m/07s5y', '/m/04gppzp', '/m/07sc1', '/m/03bq6g', '/m/02qmrw4', '/m/03pzxn',  '/m/015wf0'],
    'name': ['Fail-Safe', "By Dawn's Early Light", 'Miracle Mile', 'Testament', 'The War Game', 'When the Wind Blows', 'The Day After', 'Barefoot Gen', 'Threads', 'Fat Man and Little Boy', 'On the Beach', 'Special Bulletin', 'The China Syndrome'],
    'date': ['1964-10-07', '1990-05-19', '1988-09-11', '1932', '1965', '1986-10', '1983-11-20', '1983', '1984', '1989.0', '1959.0', '1983.0', '1979.0']
})
atomic_bomb_test_set['true_event'] = [['Atomic Bomb'] for el in range(len(atomic_bomb_test_set))]
atomic_bomb_test_set['true_event'][0].append('Cold War')
atomic_bomb_test_set['true_event'][1].append('Cold War')
atomic_bomb_test_set['true_event'][7].append('WW2')
atomic_bomb_test_set['true_event'][8].append('Cold War')
atomic_bomb_test_set['true_event'][9].append('WW2')
atomic_bomb_test_set['true_event'][11].append('Terrorism')


# Test subset for Genetic Engineering

genetic_engineering_test_set = pd.DataFrame({
    'id_wiki': [30340901, 146947, 42886, 3746, 27098, 31893898, 50957, 14899108, 456601, 1168522, 28954658, 27279709, 28370997],
    'id_freebase': ['/m/0gwm_wy', '/m/012s1d', '/m/0bscw', '/m/017n9', '/m/06r2_', '/m/0gvrtf4', '/m/0dfw0', '/m/02qr2tx', '/m/02bqxb', '/m/04d0ng', '/m/0dgrv5m', '/m/0btyf5z', '/m/0crj7yz'],
    'name': ['Elysium', 'Spider-Man', 'Gattaca', 'Blade Runner', 'Star Trek II: The Wrath of Khan', 'The Deep Blue Sea', 'Star Wars Episode II: Attack of the Clones', 'Splice', 'The Fly', 'Mimic', 'Sharktopus', 'Rise of the Planet of the Apes', 'Hanna'],
    'date': ['2013-03-01', '2002-05-03', '1997-09-07', '1982-06-25', '1982-06-04', '2011-09-11', '2002-05-16', '2009-10-06', '1986-08-15', '1997-08-22', '2010.0', '2011.0', '2011.0']
})
genetic_engineering_test_set['true_event'] = [['Genetic Engineering'] for el in range(len(genetic_engineering_test_set))]
genetic_engineering_test_set['true_event'][3].append('Digital Revolution')
genetic_engineering_test_set['true_event'][8].append('Digital Revolution')


# Test subset for LGBTQIA+

lgbtq_test_set = pd.DataFrame({
    'id_wiki': [3146002, 61664, 1856185, 24207129, 15782460, 4752795, 33025020, 455013, 468293, 239589, 1428955, 31653535, 171555, 33025020],
    'id_freebase': ['/m/08vd2q', '/m/0gpx6', '/m/061dj0', '/m/07l50_1', '/m/03ntf1h', '/m/0clh4y', '/m/0fpmrmq', '/m/02bk82', '/m/02d41336193', '/m/01jrbv', '/m/050t99', '/m/0gf8q8p', '/m/0170xl', '/m/0fpmrmq'],
    'name': ['Sunday Bloody Sunday', 'All About My Mother', 'Jeffrey', 'A Single Man', 'Hedwig and the Angry Inch', 'Before Night Falls', 'Pariah', 'The Boys in the Band', 'Philadelphia', 'The Birdcage', 'My Beautiful Laundrette', 'Tomboy', 'Gods and Monsters', 'Pariah'],
    'date': ['1971', '1999-04-08', '1995', '2009-09-11', '2001-01-19', '2001-01-26', '2011-01-20', '1970-03-17', '1993', '1996.0', '1985.0', '2011.0', '1998.0', '2011.0']
})
lgbtq_test_set['true_event'] = [['LGBTQ'] for el in range(len(lgbtq_test_set))]
lgbtq_test_set['true_event'][1].append('STDs')
lgbtq_test_set['true_event'][2].append('STDs')
lgbtq_test_set['true_event'][3].append('Mental Health')
lgbtq_test_set['true_event'][8].append('STDs')


# Test subset for Terrorism

terrorism_test_set = pd.DataFrame({
    'id_wiki': [1891886, 34953010, 15497901, 185058, 2311219, 16733548, 33028800, 3634311, 106328, 2174599, 9551038, 5958413, 2983983],
    'id_freebase': ['/m/0645k5', '/m/0j43swk', '/m/03mc6yp', '/m/0198lt', '/m/072x7s', '/m/0404j37', '/m/0h03fhx', '/m/09r94m', '/m/0qm8b', '/m/06sfk6', '/m/02pjnwh', '/m/0fgm_l', '/m/08hppl'],
    'name': ['V for Vendetta', 'Zero Dark Thirty', 'The Baader Meinhof Complex', '9/11', 'Munich', 'The Hurt Locker', 'Argo', 'United 93', 'Black Hawk Down', 'The Siege', 'Black Sunday', 'A Mighty Heart', 'Paradise Now'],
    'date': ['2006-02-13', '2012-12-19', '2008-09-25', '2002-03-10', '2005-12-23', '2008-09-04', '2012-08-31', '2006-04-28', '2001-12-18', '1998-11-06', '1977.0', '2007.0', '2005.0']
})
terrorism_test_set['true_event'] = [['Terrorism'] for el in range(len(terrorism_test_set))]


# Concatenating all these test sets into one big dataframe

movies_test_set = pd.concat([ww1_test_set, ww2_test_set, space_exploration_test_set, cold_war_test_set, vietnam_war_test_set, women_emancipation_test_set, black_history_test_set, digitalization_test_set, sexuality_test_set, stds_test_set, drug_abuse_test_set, mental_health_test_set, atomic_bomb_test_set, genetic_engineering_test_set, lgbtq_test_set, terrorism_test_set], ignore_index = True)


# Create a .csv file containing the movies test set

movies_test_set.to_csv('data/AdditionalDatasets/movies_test_set.csv', index = False)