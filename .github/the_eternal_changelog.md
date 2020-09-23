# The Eternal Changelog

This file is not for the faint of heart. It details every single change ever made to the mod. It's likely full of typos and mistakes.

***

HPM v0.4.5.2 - 05/06/2019

A quick tweak for the ghost cleanup system: it makes the AI see ghost units in the player's country, so the player doesn't need to wait years for the fix.

**The checksum for this release is EANV.**

***

HPM v0.4.5.1 - 05/06/2019

Small hotfix that should be save game compatible with 0.4.5 versions. **The checksum for this release is ZJGO.**

### Changelog

* Fixed HTY (Turkmenli) being released during Ottoman dismantlement.
* Fixed the Corrientes rebellion giving infamy and not properly warning Argentina.
* Fixed a few potential cases of undue infamy during event wars.
* Fixed the coffee rust event not happening because of a missing flag.
* Changed a few RGOs in China from Tea to Fish, Grain and Silk to try and deal with the great tea depression of the 1840's.
* Added an option to unlock crisis when Revolution and Counterrevolution is researched, as it was in previous versions.
* Made so the constitutional crisis system can now "see" the starting ruling party of player countries.
* Fixed the 2 "buy cuba" decisions giving the provinces to US instead of the FROM country. Fixed the decisions being usable if another new world nations already owns Cuba.
* Reduced infamy given by the "Directive No 1" decision. It still gives infamy, but most of it should come when the events actually fire. Reworked MTTH slowdown modifiers a little bit to take into account different situations.

***

HPM v0.4.5 - 02/06/2019

First Github release, but far from the first ever HPM release. **The checksum for this release is IEOI.**

### Changelog

* Electric Arc Furnace will unlock in 1905.
* Congo Conference decision population requirement reduced from 1M to 800k.
* Made the Neutrality modifier for Switzerland not reduce militancy as much as it did.
* (Mostly AI Behaviour): Reduced AI Aggression Base back to vanilla levels (Aggression vs uncivs is still slightly higher than vanilla). Increased AI priority for bureaucrats and the chance of them investing in pop projects. Base Tax, Tariff and Admin efficiency also move back to the vanilla (20%) level. Reduced the FACTORY_UPGRADE_EMPLOYEE_FACTOR from 75% of 70%. IMMIGRATION_SCALE changed to 0.005 (from 0.008) and PROMOTION_SCALE changed to 0.003 (from 0.004). The problem here was that the AI simply didn't have the money nor knew how to deal with the increased pop promotion speed. They bled pops because they couldn't deal with it. So now this happens more slowly and countries will have more money to deal with it. Reducing aggression is also something necessary - the AI goes crazy near the end of the game, where wars were slowing down, but increasing in scale.
* Increased the amount of money factories save from 1500 to 3000.
* Only AI non-democracies will use the "state of emergency" decision from now on. Players can still use the decision as they wish.
* Changed Limited-Access Roads to unlocked in 1915 instead of 1919, to stop it coinciding with a lot of the Army inventions.
* Faroe Island cores will go away in the late 19th century.
* Added 13 inventions to the Metallurgy tree. Reworked RGO bonuses in the tree so a good part of the bonus come from the inventions. The inventions won't fire if there's unemployment in their respective RGOs. Overall, the bonus to Coal and Iron production the tree gives was increased from 250% to 300% for Iron and 330% to 400% for coal. Most of the inventions and the bulk of the bonus to output are for late-game inventions.
* Added a decision for Canada to accept the Metis, which will also remove Maritime Union, Columbia, Metis and Rupert's Land cores from Canada. Removed the Metis from the generic "native integration" decisions.
* Khiva will not start with Nukus anymore. Slight reshape of Khiva. I need to find better sources on the region and decide on a final set up for the central Asian nations, there's conflicting information to the extent of the khanates.
* Fixed requiring impossible things to build the Suez canal.
* Moved 895 - Mersin to the Adana state so the state is not conquered as a colonial state from Egypt.
* Korea will start the war for independence during the Tonghak rebellion with a CB to get their cores back, if anyone took them. They should also fight the Chinese properly and be released properly if the aggressor are the Chinese.
* Added a decision for fore Korea to claim Tsushima (2589). It can also be used again to rename the island.
* Fixed a bug when organizing the Congo that mistakenly made the organizer also the true owner of the Congo Free State.
* Reduced Muhammad Ali modifier mobilization size by 4%.
* Fixed potential split states in the Middle East and Africa because of (potential) different colonial levels.
* Russia up to the Urals will now be full states instead of colonies, with the exception of the Kazakh territories and the Caucasus.
* The end of the initial caucasian war will now move a few pops to Jordan.
* Merged Mosul and Baghdad states into one, moved a few provinces of the later to the Basra state. Made Damascus the capital of the Eastern Syria state, moved the province to that state.
* Fixed an AI check who would make the AI research iron/coal output techs despite unemployment.
* Pacifism party policy now slightly reduces infamy.
* Restored Aristocrat voting support back to vanilla levels.
* Stopped communists supporting the roll-back of political reforms unless they are in power. They will still support social reforms.
* Monarchies should no longer be able to set the Upper House to "ruling party only". That is reserved for ideological, one-party regimes.
* Changed Moldavia's ruling party at the start to liberal. Change Wallachia's ashkenazi pops there to sephardic. Based on https://www.jstor.org/stable/25104807
* Line of Advantage decision can't be used by a vassal country or if a competing japanese power (Japan for the Shogunate, Shogunate for the Japan) exists.
* Absolute monarchies (with the appointed upper house) now have an option to dissolve the upper house and fill it with either Reactionaries, Liberal or Socialists (if unlocked). These will have consequences, however, and cost prestige, plurality and some stability.
* Fixes to the Brazilian OOB: added a Brazilian navy with 2 man'o'war, 10 frigates, 2 commerce raiders and 2 clipper transports (based on https://en.wikipedia.org/wiki/Imperial_Brazilian_Navy ). Added a starting admiral, changed one admiral that should be a general and removed generals that were too old and left the service soon after the game start, or were too young and likely not in a position of power.
* The "Avanti Italia" decision can't be used without owning the Lombardian cores.
* Fixed a NNM bug where Neutral Countries were dragged into wars through the Shadow of War event.
* The Gadsden Purchase decision/event chain will spread CSA cores to the new provinces if neighbouring provinces on the same state have CSA cores.
* Refusing a good peace deal (the ones that give you militancy and war exhaustion will now give 10 WE instead of 5.
* Increased the requirement to add an wargoal during a war back to the vanilla 7% from the current 5.5%. That is balanced with the new "propaganda" decision.
* Added a "Propaganda Campaign" decision. A country can, at the cost of plurality and money, try to tip the country in favour of its government in the UH or increase the population's jingoism. 
* Slight reshape of Franche-Comté to better follow the Meuse river. Renamed the state to Ardennes and moved Besancon to the Champagne state.
* Canada will start with Immigration Quotas instead of Open Borders.
* Zanzibar should keep its slave states after its freed from Oman.
* Changed the slave pops in Iran from the old african_minor replacement to Kilombero. based on https://en.wikipedia.org/wiki/Afro-Iranians
* Changed Mashriqi pops from Nasaf to Kabala, renamed the province to Samawah.
* Made a strait connecting Sado and Niigata.
* Fixed a missing flag that made the EIC not be integrated at all.
* Removed Turkmenli and Assyrian cores from Raqqah. Assyrian pops were moved north to Hasakah. Converted a good part of the Mashriqi pops to bedouin pops in Raqqah. As-Suwayada in Syria also got 2700 Druze mashriqi pops converted to Bedouin,and a few mashriqi pops in Ma'an in Jordan converted to bedouin.
* Changed the pops in the Caucasus group from using Russian units/leader portraits to arab units/portraits.
* Fixing low pension level being 10% instead of 100%.
* Added Fish to the list of RGOs that can get the local_tractors modifier. Renamed the modifier to "Tractors and Trawlers". Made the aristocrats be the ones who need the money when deciding if the event will fire faster or not.
* Pop issues:
  * Fixed a vanilla bug that made impossible for pops that were not getting their everyday needs to care about the pension reforms, when it should be the contrary.
  * Fixed unrealistic unemployment levels (50% of a state unemployed, with the minimum starting at 10%) needed for pops to care more about unemployment subsides.
* Removed Tea RGO from Corrientes and Misiones, changed the production in the state to Cattle, Tobacco and Tropical wood. Changed Xolotas and Formosa to Cotton. Based on (EL COMERCIO DE LA PROVINCIA DE CORRIENTES DURANTE LA PRIMERA MITAD DEL SIGLO XIX. UN PANORAMA DE SU EVOLUCIÓN http://revistas.unne.edu.ar/index.php/fhn/article/download/3452/3099 and https://www.elterritorio.com.ar/la-economia-misionera-al-inicio-del-territorio-6193972785638980-et
* Added a new fish-rgo output invention.
* Fixed two immigration modifiers having the same name, potentially screwing up a few events/decisions.
* Removed the Zulu cores from random neighbouring provinces and left only one in Thaba Bosiu, where there are Zulu pops. They still won't be able to conquer just that province if Basotho has the rest of the state, but once they are reduced to that province only by the Boers they can take it. Normalized Matabele cores in the region to stop Nguni from assimilating.
* Renaming of a few culture groups.
* Changed the MTTH for the Doctrine of Lapse events back to NNM levels.
* Ha'il should now correctly get cores in Nejd's arab gulf state.
* Hawaii changes: Literacy and pop changes. They got an event representing the declining Hawaiian population, as well as the reformation in a constitutional monarchy and a increase in the yankee population. Hawaii will start with a minimal yankee population representing missionaries and their families, and they will start with Yankee as accepted that they lose (like the Ionian islands lose) as soon as Polynesian is not a majority or they own non-cored provinces. They will also start in the US's sphere of influence, and I fixed a decision that the US could take to buy Hawaii which would never work under previous conditions. Finally, if another power annexes Hawaii and there are still Yankee pops there, the US gets a core on the island. This is mostly based on https://digitalcommons.unl.edu/cgi/viewcontent.cgi?referer=https://www.google.com/&httpsredir=1&article=1035&context=historydiss especially data about literacy and pop distribution (as only 50% were catholics in 1837, the literacy changes were made to reflect that).
* Made the constitutional crisis distribute militancy and consciousness according to who can vote, instead of a generic for-all effect.
* Fixed the vanilla Olympics events so the AI doesn't bankrupt itself with them. Made prestige gain, costs for hosting and relations given/lost even instead of varying because of the year. The events will also give a relation boost to any GP that participates in the Olympics, not just neighbour Olympic countries. The AI will no longer choose to host it or not or to participate or not in 50/50 basis, they will be much more inclined to host/join (except if they hate the host, that gives them a chance of not participating). Fixed a wrong flag that could repeat an event until the country choose to take another option. Changed so countries can join the IOC even during war and made the event more likely for Greece. Took steps to guarantee the first Olympic games is likely to happen.
* Fixed a few nations with the Liberty NV being able to get a NV event not meant for them.
* Fixed a decision for a puppet with a sphere owner that is not their overlord and tries to break free still being applicable to substates in a few situations.
* Increased the MTTH in the Socialism_Fascism events to try and make them less spammy. Made so communism events check pop support for communism instead of socialism.
* Stopped the NNM Oriental Crisis events removing Turkish cores from Adana, except for Antakya, if Turkey lost the crisis.
* The "Drums of War" event should no longer give a CB for countries that already have a CB on the unciv getting the event.
* Changed Qing's starting reform from Land to Bureaucratic. Swapped 1547 - Jian from Tea to Grain. Changed 1283 - Hydebarad from Grain to Silk. Changed 1482 - Fuzhou and 1486 - Tingzhou from Tea to Fish and Grain, respectively. Later they will flip back to tea.
* Slightly increase coffee demand in the middle-class and "urban" pops. Added the "housing" goods as needs for Intellectuals.
* Changed the PDM/NNM RGO change events for provinces with high unemployment to try and check that the new RGO won't end up creating a mass of unemployed (before firing an event to change a high-unemployment RGO to cotton, it will try to check if Cotton isn't a high unemployment good).
* Converted the "Break the Tea Monopoly" decision in an event that will progressively turn provinces to tea in India (if there isn't Tea overproduction). The decision created a huge "punch" in the tea market, knocking out several provinces out of business and creating massive unemployment. A more gradual change is more realistic and should avoid that problem.
* Blockades should now slightly affect province output.
* During the Pacific War, the GP that spheres either Chile or its adversaries can choose to remain neutral and lose its spherelings/influence or join the war.
* Changed Cheap Factories to use Steel rather than Iron to be built. Now only Basic Factories use iron.
* Changed the scale of a few vanilla disease modifiers.
* Fixed a rogue decision for Thailand that changed some RGOs in Vietnam.
* There's a vanilla bug that happens when a country that is mobilizing is annexed, which results in the country having "ghost units" - units in exile that belong to a country that doesn't exist. This creates problems with pops and screws with unit visibility, so HPM has a fix: when the AI detects the problem, they will give a few new and small island provinces in the pacific to the country that has the ghost units until it de-mobilize. This happens usually less than 10 times during a game and the country that demobilizes exists for around 10 days, then it's reabsorbed like nothing happened. This shouldn't cause any problems during a normal game, but if for some reason you'd rather not have the bugfix, there's a starting option to disable it.
* Unciv Rebel pushing back economic reforms should be more random now.
* To avoid abuse, the event that gives infamy for a country that permanently occupies another (or carry on a war they already won) will take longer to fire if players are involved in both sides of the conflict and it will need more strict requirements before firing if the one being occupied is a player.
* Forming Arabia no longer requires unoccupied provinces.
* Building any ships now require a naval base. This is made to represent the different levels of naval tech countries are - not all countries can build ocean-worthy ships at the game start. For uncivs, the closer you are to Europe, the more likely you are to have the necessary ports to build these ships.
* The rest of the Tahiti region islands will go to France with the event to get Tahiti, except for the Pitcairn islands, which will go to the UK (if they exist). Removed the free port that came with the event. Fixed pops in Pitcairn.
* The Hellenic Parliament decision will now give 5 prestige.
* Made a decision to make French Canadian primary in Canada and flip the government to reflect the french government if France owns all Canadian cores or if Canada is a puppet of France.
* Sweden will get an event to support the Danish during the Schleswig-Holstein War. If they choose not to, they lose relations with them and some prestige.
* If France goes to war during the Ems Dispatch event chain, they won't call their allies.
* Changed a few NVs in the americas from Order to Liberty/Equality, to better reflect these nations rejection of their former colonial masters.
* Crisis will now be unlocked from 1886 rather than 1870 - to try and avoid early crisis during the scramble for Africa. Currently considering moving this further.
* Fixed the Burmese OOB.
* To avoid elections being dominated by a single issue (a problem brought forward when update 3.04 changed election events to be nation wide without changing their effects), the nation-wide events were changed to affect random states according to the number of states the nation has. The option that has the least impact on moving the issue (usually the last option) is still applicable nation wide.
* Reduced the immigration bonus Secondary Powers get to avoid an oligopoly of counties that can attract immigrants.
* Minor changes to the RGO Spread events so tractors, explosives and electricity so spam is reduced in high-literacy countries. Might rework this to somehow cut down spam to the player entirely while preserving the gradual spread.
* Tweaked the Tewodros event chain to give a bit more of an advantage to the country that gets it.
* Fixed the OOB for the Ha'il, Nejd, Hedjaz and the Yemeni states. Added a general for each and adjusted starting relations.
* Fixed bad requirements for the events in the integrated HPM misc minimod that made the South Tirol compromise fire even if Italy didn't border the required provinces and resulted in an exclave being created. Changed the decision in an event chain, which the AI will only take if they are a "Benefactor" AI. The player can still use the compromise if they own South Tirol and it can end in different ways - from population transfers to unresolved.
* Changed Newcastle to Iron. Newcastle flips to coal later in the century. Plymouth, Holyhead and Isle of Man change to Iron later on in the game.
* Added a decision for Austria to reclaim Eisenstadt from a puppet Hungary, getting the province, eliminating the Hungarian core and getting a core there. This was done because they lose their cores there if they free Hungary.
* Added a system that attributes a personality to the AI, so they can use decisions which don't make sense to be used always. This system is in its infancy and only applies to the South Tirol Compromise decision, but in the future it will apply to much more. Right now there's two types of AI: Benefactor and Malevolent.
* Reworked the system that dealt with mass killings. The main points are:
	* When the decision (Named "Directive No 1") is taken, you get a modifier. This modifier is the main thing that will give infamy. It will start giving a low amount of infamy but as more killings are done, there's a chance of more infamy coming.
	* Political and Social reforms will be blocked. This is made to represent the state focusing its whole bureaucracy in the task at hand.
	* Population loss will not be done at once in a national event. It will happen over time with state-events. Every time one of these events fire there's a chance that the evidence for the ongoing massacre is going to tick up.
	- These events have a somewhat high MTTH but will happen faster in states that:
		* Have a majority of primary/accepted pops.
		* Are your cores.
		* Where your primary/accepted pops AND the ruling party ideology are the majority
		* Have soldiers in it.
		* Have good infrastructure.
		*Among other things.
		
	- Nation-wide policies/triggers that will affect the speed of these events are:
		* High/low admin and military spending.
		* Certain techs can speed it up (e. g. machine guns, gas attacks).
		* Totalitarian state modifier will greatly speed it up.
	
	- These events will not happen in a state:
		* Where there isn't a single pop of the primary/accepted culture (and there isn't any brigades in the province).
		* Occupied provinces or being occupied by rebels or other countries forces.
	* For it to happen on states without any primary/accepted pops, you need at least one military unit in the state. It will take longer to happen and be less effective.
	* The more the "evidence clock" has ticked, the bigger the faster the events fire. The higher the chance of a scandal erupting. 
	* The player can choose to end the policy at any time, but there's a cooldown to dismantle the apparatus before it can be re-done again. The time the player will wait will depend on how long the thing has has been going - with bigger cooldowns when the events have been running for longer.
	* Losing a war, a change in the type of government or having the "national confusion" modifier will interrupt the process. 
	
***

### Old Versions, Unformated and likely full of bugs

V0.4.4 - 17/05/2019
-Event 90057 - Look to $COUNTRYNAME$ should no longer fire for vassal states, since these can't be taken from sphere.
-Fixed province 2103 - Philippolis being in the rows for RGO change for coal and iron, making it constantly flip between both. It will stop on Coal now.
-Fixed the "Living Space" event to make sure it gives a proper CB, even when bordering colonial nations. The event wont target neighbouring fascist countries anymore (or fire if your country is dismantled), to help these countries end up more or less aligned rather than quarrelling all the time. To avoid it giving several CBs in different nations, the event now fires another event to a given nation, which gives the CB: if they have more than 4 states and are not a colonial nation, you get the a Demand Concession CB. If they have more than 4 states and are a colonial nation, you get a place in the sun CB. If they have less than 4 states, you get a conquest CB. So a fascist nation works through colonies before going to core territory and finally conquest with these events. The amount of infamy you get was made random from 1 to 3. Added an option to ignore the event, which will anger the jingoists and the fascists.
-Fixed several vanilla and HPM typos in inventions and events.
-Changed Dismantlement so vassals and landlocked nations can't participate in colonial dismantlement. Changed the old NNM dismantlement (that still lives on, based on states rather than countries) to a quarterly OnAction event, so it only happens last (and guarantees any colony that needs to be distributed as a country will be so).
-Recognize Circassia/Chechnya/Dagestan decisions will disappear after 1840.
-Reworked the Limburg crisis to be less convoluted. Instead of keeping Limburg free throughout it, the Dutch will annex the country and the Germans will choose how to react. If they press their claim, they will get a one year core in the province (acting as a claim), and they can choose to go to war to press their claim. Regardless of the outcome, after one year and in the next quarterly pulse they will lose their core there - regardless if they own the province or not. If they do own the province though, it will be renamed to Limburg. Reworked AI logic when picking options on the chain, made infamy gain a bit random for the Germans and made it so annexing Limburg is a decision rather than an event.
-Fixed the Laos protectorate decision so you can't create a landlocked colony.
-Fixed a vanilla bug with the brigades_compare localization that could show the wrong country being the target of a fired event (inside an event).
-Added Laos, Cambodia, Burma, Vietnam and Malaysia (only the 2 states in "mainland Malaysia") to the Imperialism CB. To use it against native countries in these regions, the country needs revolution and counterrevolution and for it to be after the Berlin Conference. There are special requirements - declaring Indochina as a colony (decision) for Vietnam, Laos and Cambodia. Being crowned emperor of India for Burma. Owning Delhi, Calcutta and any Burmese core is an exception for Burma since only the UK can take the empress decision. Malaysia is only active for the owners of Singapore and any country that owns a province in Cambodia proper can go after the Cambodian state. Hopefully this will make the AI more aggressive when colonizing SE Asia. Also note that the Imperialism CB is exclusive to European powers.
-The above also means that the decision to "create" Indochina is not exclusive to France anymore (and now it has a big red warning to let players know its useful to take it and get a CB). The recurrent event that France got to conquer Vietnam/Laos/Cambodia was scrapped out and only the imperialism CB is left now. This means that conquering Indochina is not something France has an advantage for, it depends on the competing powers in Vietnam - either owning Saigon or Hanoi will let you take the decision. Made the decision inherit Vietnam if its in the sphere of the one who takes it and both have very good relations.
-Moved province 2572 - Nan from the Shan states to the Ayutthaya state. To leave the states more or less balanced moved 1353 - Ratchaburi from Ayutthaya to Pattani
-Made the decision to Annex Champasak not exclusive to France anymore. Made it appear more frequently (so the player knows what is needed) and made the requirements a bit more diverse. It does need the player to use the "create Indochina" decision, though.
-Made negotiating an unequal treaty (a decision) with Vietnam and the border treaty with Thailand not exclusive to France anymore. This mean any GP can get Saigon now, as long as they fulfil other requirements. These decisions now have a 50% chance of giving 1 Infamy.
-Changed the decision to annex Laotian minors/Cambodia require the "Indochina" decision. So to annex these minors through decisions, you need to have declared the intention to form Indochina. Made these decisions have a 50% chance of giving 1 Infamy when you take them.
-Similar to the decision to integrate the laotian minors and Cambodia, added a decision to annex Vietnam if you own a Vietnamese core, have Mass Politics and they are in your sphere.
-As a final reminder, these decisions dealing with Indochina/SE Asia as well as the use of the Imperialism CB in the region require the "$Country_ADJ$ Indochina" Decision to be taken. These and the other decisions dealing with Indochina can be taken by any European GP and Japan except Turkey and Russia. Turkey, Russia and other GPs need the "Sea power & The Merchant Marine" tech school to be able to use these decisions.
-If Russia is dismantled without the participation of Japan, Japan will still get cores on the rest of Sakhalin - but it won't remove Russian cores. 
-Fixed the recurrent event for the integration of the Malay minors being able to fire too soon instead of when leaders died.
-Made the "Freedom of Religion" act decision be applicable to the Netherlands too.
-Made the Netherlands a semi-constitutional monarchy. Changed the Party reforms to Harassment and the voting one to Weighted Wealth. Citizen (voting) Rights were restricted to Primary culture only. Based on https://en.wikipedia.org/wiki/States-Provincial and https://en.wikipedia.org/wiki/United_Kingdom_of_the_Netherlands#Constitution_and_government
-Removed Flemish as accepted from the Netherlands. They can get it back passing a decision that requires a few things and burn through some prestige. This is done to represent better the catholic/protestant divide and the reasons that led to the Belgian revolution, as well as keep the Belgians more rebellious rather than being immediately accepted by the Netherlands.
-Moved Sociology and Political Science inventions to Biologism. Removed 30% education efficiency from Darwinism and distributed it equally to Social Science and Social Alienation.
-Reduced Ottoman minority CON/MIL gain and increased the tax efficiency of the initial ottoman policy.
-Fixed a bug in the EIC minimod that would make the EIC be integrated soon after it appeared.
-Changed 805 - Salonika from Cattle to Cotton and 767 - Maribor from Wood to Coal and 768 - Ljubljana from Cotton to grain. Greece changes based on "Land Tenure and Related Sectors of the Balkan Economy, 1600-1800" and Slovenia changes based on https://www.erih.net/how-it-started/industrial-history-of-european-countries/slovenia/
-Changed picking Tech School to not depend on Party ideology but party policies, mostly mimicking the already existing issues needed. The only exception is the Avantgarde Intelligentsia, which depends on literacy, consciousness and prestige. Also made AI countries with Revanchism not pick pacifist tech schools while communist countries won't pick the more Commerce tech schools. This should make choices more dependent on current situation - an AI country with unclaimed cores will be more likely to go after military-industrial complex.
-Refusing to go through any of the Opium Wars will now reduce the prestige of Great Britain by one fourth and will also dictate monetary reparations.
-Made all events and decisions where the player will pay something with the debt system properly show a red number telling them how much it will cost, to avoid confusion over bugs not debiting the money or money disappearing. Do note that if you don't have the money, the debt system kicks in and takes the money from your country, automatically, in instalments of 10k per payment, until the debt is paid in full. You will receive no warning about this.
-Reshuffled states in Burma and Thailand so they are a bit more balanced. Removed the Shan state that straddled both countries.
-The decision to establish a protectorate over Sarawak is no longer exclusive to the UK - any country can take it as long as they own the lands surrounding it (and sphered the country).  The decision has a 50% chance of giving 1 infamy.
-Increased the MTTH of the event for communist countries that gets rid of the Rich strata from 15 days to 60 months. This should allow pops to run, stop quick revolutions from causing lasting damage and it will represent the time that it takes to organize all this. Also added an option to not touch the capitalists, which will anger communist pops.
-Players should get an event letting them know when the Imperialism CB becomes available to them.
-Reshaped provinces in Armenia, Iran and Afghanistan. Re-divided the 2 Afghan states in North Afghanistan and South Afghanistan. Repurposed province 2133 - South Georgia into Gizab, in Afghanistan. South Georgia was a small arctic island that the UK could colonize.
-Revamped Terrain in the southern Caucasus, Iran and Afghanistan. The Zagros mountain range should be in now, and these 3 regions are much more mountainous than before. Reshaped the coast of Iran to reflect the changes, changed terrain to dry versions when appropriate. Terrain work was based on https://upload.wikimedia.org/wikipedia/commons/9/91/Iran_topo.jpg & https://4.bp.blogspot.com/-63r9Xbbxqm4/U1_4zuTY6VI/AAAAAAAABTw/QNIQICkhgNY/s1600/Afganistan-Kraj-G%C3%B3rski.jpg & https://upload.wikimedia.org/wikipedia/commons/d/db/Turkey_topo.jpg
-Added events for bankrupt countries to randomly lose infrastructure: railways, forts and ports.
-Increased countries base tax and admin efficiency by 5%.
-Fixed a bug in the NNM dismantlement code where, if Germany was dismantled, it didn't check if France (that owned Western Rhineland/Palatinate) had a truce (with Germany) and it ended up releasing Rhineland as a vassal even if France wasn't involved in the war. Also fixed a bug where Easter Rhineland was considered part of Wester Rhineland, effectively meaning that, even if France controlled Western Rhineland and the Palatinate, they would still release Rhineland as a puppet.
-Made so Eupen-Malmedy only goes to the owner of Liege if the owner of Liege has a truce with Germany.
-Changed INVENTION_IMPACT_ON_DEMAND from .15 to .13. Reverted mechanized_fishing_vessels bonus from 40% to vanilla 50%.
-Fixed a bug on the changes to vanilla that made it easier for accepted pops to migrate to colonies: they weren't really working, so colonial migration was working as vanilla. It is working now, so accepted pops will behave as primary pops when deciding to move to the colonies.
-Changed the Bureaucrats percentage in Michigan from 0.4% to 0.6% and in Arkansans from 0.23% to 0.8%. This should enable them to become states sooner.
-Egypt should correctly lose cores on Adana when they lose the Oriental crisis.
-Added Somalia to the "Colonial Claim" system during the Scramble for Africa.
-Deactivated the Imperialism CB in Mozambique after the Scramble starts.
-The event that changed the party_appointed reform for non-dictatorships will now fire if there's voting, not only if the government is controlled by liberal or by socialists. It will also move the UH reform to "population equal weight" in democracies, instead of making it "appointed".
-Stopped the "Trade for Heligoland?" event giving Kenya AND two Tanzanian provinces to the UK. Now it will only give Kenya or - if Germany doesn't own Kenya - make Germany pay 100k£.
-Venice should move their capital to Venice if they own it and it's not the capital.
-Separated the modifier for Substate nations in 2 - one for the AI and one for the player. The player is not forced to set minimum tariffs or taxes. Reduced the tax efficiency effect of both and the minimum tax for the AI.
-Moved Corfu to the Thessaly state.
-Made an event for Boer minors where an overlord that doesn't own Cape Town or for Indian Minors that A) are neighboured by a GP but not neighboured by their overlords or B) were recently released as the result of the dismantlement of their former masters to choose to: 1) become a puppet of the neighbouring GP, 2) declare independence, 3) join a neighbour of the same culture group and 4) keep the status quo.
-Yemen will be created with slavery abolished if the country that organizes it has slavery abolished.
-African colonies can now be organized with fewer states controlled. If you control half the states, you can usually organize it.
-When dismantling a nation that owns parts of another nation's colony (e. g. dismantling the UK who controls part of Mozambique and Portugal is the one who took the "organize colony" decision for Mozambique), those colonial territories will be given to the master of that colonial nation (the UK would give their Mozambique cores to Portugal) regardless if they have a truce or participated in the war. What that means is that dismantling will gravitate towards completing partial colonies, instead of perpetuating them.
-Restricted CB use during Mexican-American War/Oriental Crisis/French Expedition in Korea. What this means is that, during these scripted wars, the nations involved can only target the nation (like the US targeting Mexico) with the original CB. This is mainly done so the AI doesn't end up adding other unnecessary CBs (like the US adding acquire core CBs), but the restrictions are also applicable for the player. Made the acquire_all_cores CB cost less warscore since the AI never reached the required amount of warscore in the one instance it was used (mexican-american war) and white-peaced because of it.
-Changed event 30000 - Organizing a World Fair from taking money directly and instead made it use the debt system. This is mainly to stop the AI going bankrupt over the event, which happens not infrequently.
-Choosing to take Rhodes during the Italo-Turkish war will only give infamy if they can give you Rhodes.
-Removed the old NNM event meant to represent the Italo-Turkish war as it was obsolete. Made the option to demand Rhodes not given infamy if the turks can't give it (because they don't own it).
-Fixed the "Hegemony over the Nile" event chain not working properly.
-Slight adjustments to help the AI during the Texan Revolution.
-Moved Serbia's capital to Kragujevac at the game start. They can move it back through a decision.
-Carlist/Christino sympathies will no longer sap Spain's prestige.
-Reduced the amount of prestige you get from annexing core countries/states.
-Made a few modifiers such as Caudillos and "the_big_army" have a prestige downside. During the fight with the PBC Chile and Argentina will now get the "Caudillos" modifier.
-Made Ottoman starting prestige on par with Spain's.
-Increased all GPs starting prestige by 30, to compensate for the prestige gained in the initial wars in SPs.
-Reduced the frequency of the "A Treatise on Economics" Event.
-The End of the Liberal Revolutions event should now give 5 or 10 prestige instead of 5 or 15.
-Reduced the prestige that Denmark gets from a few vanilla flavour events. Most of their prestige spam came from these and liberal revolution events.
-Fixed the events from the Vanilla/NNM Liberal Revolutions so when they move an issue in a direction, it moves only one step over the current level. For example: If you have landed voting, the event would (previously) move pops 10% to universal voting, which is useless since no pop can support that since it's not the next reform. Now instead the event will move pops 10% to the next level (in the case of landed voting that would be "weighted wealth").
-Repurposed province 1813 - Arlit from the Sahara to be Hasakah, in Syria.
-Removed Vanilla Lakes Razzaza and Tharthar from the map, since both are artificial lakes created in the 20th century.
-Rework of terrain and provinces in the Middle East: the areas claimed by the Ottoman Empire/Saudi Arabia but not de facto under central authority were made into unoccupied provinces. These can be colonized by decision later, with cores being distributed according to current cores in neighbouring provinces. Several provinces had their terrain changed to reflect the arid conditions of the area. Kuwait will start independent but on the Ottoman sphere. Based on "Kuwait: Anglo-Ottoman Relations 1890-1914" found in https://shodhganga.inflibnet.ac.in/bitstream/10603/14230/11/11_chapter%204.pdf
-Added an event related to the history of Kuwait.
-Reworked the decision to claim the Arab Coast (as in Arab Gulf) for the Ottomans - now it doesn't require the Ottomans to be a GP, but there are other requirements. The decision will vassalize Kuwait if it's in the Ottoman's sphere of influence, with a later decision to inherit it if it's vassalized. The decisions and the decisions surrounding the Ottoman Expansion in Qatar and Bahrain have been reworked to be more dynamic and also to apply to Egypt.
-Reworked the events dealing with British intervention in the Qatar-Bahrain war. Now the UK gets a "make puppet" CB in Bahrain, to represent their protectorate there that was part of the peace deal.
-Added 1163 - Qatif and 1164 - Hufuf to the Abu Dhabi state. Renamed the state to "Arabian Gulf" - this is so any country with cores in those provinces can conquer them without needing to conquer Riyadh.
-Fixed a wrong modifier in "rebel_types" who should make non-liberal controlled but very politically liberal governments be less likely of being target to a Jacobin uprising.
-Organizing Madagascar will make the "end the merina monarchy" decision unavailable.
-Added an option to refuse independence for South Africa and not have the event repeat again.
-When using the "Claim Savoy" decision, France will fire an event to the owner of Savoy demanding the provinces. If refused, France gets lower relations and break any alliances. If accepted, cores (Italy/S-P) are removed from Savoy and the provinces are transferred to France.
-If Galicia-Lodomeria is landlocked out of Austria, Austria will release it. Bukovina will also be released not as a vassal but as an independent state.
-The decisions to integrate Bahrain/Qatar in the trucial states now require mass politics and will only show if you sphere either of these.
-Fixed a bug that was stopping Polish minors from ever using the "Unite with Poland" Decision.
-Minor rework of the Tonghak rebellion event chain: CBs given will be appropriate to country status (so no "add to sphere" for non GPs). Instead of it always ending with Korea puppet by someone, I made an option for Korea to retreat to Pyongyang, moving the capital there and starting a war with however is trying to puppet Korea. According to a random chance beforehand, representing how successful the initial invasion was, Japan might start this was already owning Inchon and Hanseong. This chance is drastically higher if the Chinese choose not to intervene. Now this intervention might lead to a 3 way war with Japan and China trying to puppet Korea (separately) and Japan and China fighting over that.
-If by 1870 Egypt is not civilized, not in anyone's sphere and is either free or their overlord is not a GP, then the #1 GP can take a decision to seize the province and build the canal.
-Fixed the event that removes party loyalty after 1845. It wasn't working like it was supposed to.
-Stopped the January Uprising event chain giving Congress Poland non-polish cores just because polish was a majority in the province.
-When NGF forms (through the normal decision), Austria gets the option of shifting their focus, abandoning their sphere in the German states and focusing in the Balkans, raising their relations with the NGF and removing their German Sphere, or they can keep everything they have and ignore this.
-Increased Egypt mobilization bonus from the Muhammad Ali reforms from 9% to 14%
-Removed all (but one) hard exclusions (based on tags) to the Liberal Revolutions events. Only exception is the United Baltic Duchies, which still have a hard ban. Reworked the time the event takes to fire to take into account unemployment, industrial score, closed borders, as well as press and meeting reforms.
-Slight reshape in 3 provinces in Sudan/South Sudan.
-Added a naval base in Galway, Port Elizabeth and Aden in 1836.
-Techs: Redistributed RGO production bonus for Coal and Iron, starting at bessemer process, so production increases earlier. Slightly boosted "cotton gin" and made the US start with it.
-Added a few more optional requirements for the Congo Conference decision: made it easier for Belgium and countries with the Naval tech school to take the decision. Changed the date that "The Dark Continent" unlocks from 1895 to 1890 if there's no conference.
-Every time a Semi-Constitutional or Constitutional Monarchy changes the ruling party outside a election - that is, the monarch uses its power to overrule the election result - a constitutional crisis event will fire that will reduce prestige, plurality and add militancy as well as a modifier. Players in democratic governments should use the party loyalty NFs to swing the elections in favour of the party they favour. 
-Non Prussian-formed Germany will not get the decisions to Appoint Bismarck, Rename Kaiser-Wilhelms land, Appoint Von Moltke, or get the Prussian tech-school. Italy can't use Cavours diplomacy if not formed by S-P.
-Made the "Academia Della Crusca" decision not bankrupt Tuscany.
-Japan is now exempt from paying tribute to the Shogun.
-The League of Three Emperors should be more likely to succeed. Germany should also break their alliances with other GPs during (and if someone accepts) the formation of the League, instead of only Austria/Russia doing it.
-Added a few more aristocrats/bureaucrats/officers to Yemen and the Gulf states.
-Made so the Ems Dispatch decision will not be taken by the AI the moment NGF forms. This is done so the Franco-Prussian war doesn't start immediately while the AI is unprepared because the AI can't contain themselves.
-Stopped the AI from using the AI-only CB "Unification Humiliate" against Austria-Hungary.
-Minor state rework in Persia. Merged Luristan and Lorestan in a single state. Moved 1134 - Dekhord from the state of Isfahan to Fars.
-Joined Olomouc and Troppau, in the Sudetes region, with Bielsko and Teschen in Austrian Silesia to make the state of Lower Silesia (based on https://en.wikipedia.org/wiki/Austrian_Silesia)
-If Krakow was integrated in Galicia-Lodomeria, they will lose their core once Austria turns into Austria-Hungary or if Austria uses the "Restore Empire" CB on them.
-Changed so Luxury, Medium and Common factories use Steel to be built rather than iron. Basic and cheap factories as well as steel works still use iron though.
-Changed Aruba to be a gold producing province from the start (based on https://www.britannica.com/place/Aruba ). Lille, in France, will start producing iron from 1860 onwards.
-Fixed pops in the Ionian islands (Greek, British, North Italians and Sephardi pops). Change RGO in both islands to fruit. Changed party names to historical names or greek party names. Added North Italian and British as accepted - something they lose if they ever acquire non-cored territory. The Ionian Islands will start as a Constitutional monarchy. Added some Sephardi pops to Athens. Based on the detailed and spectacular work of anon here https://web.archive.org/web/20190517113659/https://pastebin.com/bysiU0rm
-Removed Transylvania from the "End of the Federation - Totalitarian" Danubian Federation event. Tried to make sure it doesn't start wars with countries that doesn't exist.
-Added a decision to rename the Bourbon island to Île de la Reunion if you're a republic. It can also be renamed to Island Bonaparte if you're the Second Empire.
-Changed Krakow's population to around 140,000 (35,000 pops) from the previous 100,000 pops (source: https://www.britannica.com/place/Republic-of-Cracow)
-Changed "Open Hearth Furnace" to unlock in 1885.
_______________________________________________________________________________________________________________________________________
V0.4.3 - 07/05/2019
-Added Anglo-Canadian/Native/French-Canadian Aristocrats to all colonized states (where the respective cultures exist). Added around (a bit more) 300 french-canadian pops to Newfoundland (based on https://www.heritage.nf.ca/articles/society/french-settlement.php)
-Nationalizing will now give the countries that lost their investment a Reparations CB instead of humiliate and make puppet.
-Removed the decision to make non-colonial states in national states because of reported problems with it.
-Moved 2560 - Darmstadt back to the Hessen state.
-Added an event for France (or however owns Bordeaux) dealing with the 19 June 1857 law that will change the Bordeaux to Wood production and add a temporary modifier to it. Changed Bordeaux terrain from farmland to forest and changed RGO from fruit to wool to reflect history.
-Added greek officers and aristocrats to the "Central Greece" state.
-Added a new condition for Santa Anna (event) to be captured - while Mexico sieges a texan province, it might happen. To balance that, MTTH was doubled unless there's a battle going on.
_______________________________________________________________________________________________________________________________________
V0.4.2 - 16/04/2019
-Zulu will now start with "appointed" instead of "party appointed" for UH reform.
-Moved the port in Corinth to Athens.
-Changed a few RGOs in Japan to basic RGOs (fruit, cattle, wool, fish) from cash crops or industrial goods. They change back to the old RGOs via a decision once the country westernizes (or the area is held by a westernized country - it's not tag specific).
-Gave the artisans in a few countries (in the middle east, north Africa, Persia, Indonesia and Japan) the ability to build ammunition and firearms. 
-Made reforms that affect bureaucrat promotion SPEED affect it less than it did (up to 4% for the last tier instead of 16%).
-Gave Antwerp sea access and fixed the coast of Netherlands a little bit. Moved the port from Bruges to Antwerp.
-Made sure events can't fire for an non-existent FRCA.
-Converted a few more start events to triggered only for performance.
-Changed INVENTION_IMPACT_ON_DEMAND (reduced from 0.2 to 0.15 )
-Increased FACTORY_PAYCHECKS_LEFTOVER_FACTOR from 0.3 to 0.6
-Reduced BASE_COUNTRY_TAX_EFFICIENCY and BASE_COUNTRY_ADMIN_EFFICIENCY from 0.02 to 0.018
-Changed the values of Tax Efficiency given by techs/inventions so the maximum efficiency you can get from techs/inventions is 50% (previous was 53% - 28% from Techs and 25% from inventions. Now it is 30% from Techs and 20% from inventions).
-The Central Bank modifier that you get after enacting the central bank decision will now give 5% tax and 10% tariff efficiency.
-To better account for the increase in good demand from pops, values for the reforms that give unemployment_benefit and pension_level where doubled.
-The AI will now stop using Trade Policy decisions if they have more than 3 million in the bank. If they dip below that, they will start using it again.
-Increased the effects of the province modifier for Electricity and Local Distributions channels (when you have both inventions researched this province modifier event can fire, giving the state a "Commercial Retailers and Electrical Lighting" modifier) from +50% to the production of all RGOs to +80% and the factory throughput from +5% to +10%.
-Stopped the events that give the "Tractors", "Mechanized Mining" and "Commercial Retailers and Electrical Lighting" modifiers from firing if the province has more than 2% unemployed farmers (for tractors), labourers (for mechanized mining) or either (for Commercial Retailers and Electrical Lighting). This should help avoid overproduction. These events will also fire faster if farmers (tractors), laborers (mechanized mining) or capitalists (retailers and lighting) have money on the bank.
-Reshaped Uruguayan provinces. Fixed terrain there and fixed a few RGO icon positions in Indonesia, Japan and Philippines.
-Reshaped Danzig as a smaller, more compact province.
-Vassals can no longer use the decisions to pick a Trade Policy.
-Fixed Great Game CBs so the UK is capable of taking Makran, Sindh and Kalat. Made the militancy values fair for both Russia and the UK and made smaller countries be absorbed faster. Also made the Regency modifier affect the speed a country is absorbed. Changed the events so Afghanistan is the last country to be targeted by either Russia or UK.
-Fixed the "Restore Order CB" not being excluded from the CBs that can't be used with 1 military score or less.
-Fixed a duplicate requirement in the Italian Irredentism decision.
-Limited one of the AI cleanup decisions that remove serfs to once every 365-days per country, to avoid countries spamming it.
-Fixed Punta Arenas and Rio Grande RGOs constantly flipping between gold, wool and coal. Fixed Sandakan constantly flipping between Oil and Iron. Fixed a few constant flips problems in the Australian gold rushes. None of these should have any flipping around anymore.
-Fixed the description of the the "Argentina-Chile Border Treaty" event.
-Overhauled the requirements for the ACW to trigger and cores to spread, so it takes into account the two-party system boosting conservatives and the ideology rework.
-Stopped a potential crash when forming Yugoslavia with the "Create Yugoslavia" decision and the "Integrate Albania into Yugoslavia" if Albania was already integrated into Yugoslavia.
-Fixed India being released by the AI unless Pakistan cores exist. It should be the other way around (India is not created unless Pakistan cores exists). Added a few more requirements such as militancy for the AI to take the decision.
-Fixed name placement in Iringa. 
-Fixed a few colonies that could be organized without holding all the necessary states.
-Revamped the Form Laos decision and made sure the event associated with it doesn't fire for countries that don't exist.
-Made so Hungary inherits social reforms as well as more political reforms from Austria once the revolution of 1848 starts. Changed so that if the player chooses to play as Hungary they (Hungary) now get the same reforms as if they don't.
-Fixed so Pearl Hunting in the arab gulf doesn't end with Abu Dhabi constantly flipping between Oil and Precious Goods.
-Fixed unit placement in Bougouni.
-Fixed the decisions "claim xhosa lands" for the UK and the "force publique" for Belgium. Also fixed a double condition in the arab_union_claims decision.
-Fixed Zambia being organizable for the UK if they organize Rhodesia.
-Gave a few techs for Sudan when the Mahdist revolt happens.
-Changed IMMIGRATION_SCALE from 0.004 to 0.008 and PROMOTION_SCALE from 0.002 to 0.004. This should, in practice, make both immigration and promotion faster when the conditions are right, which will lead to a more dynamic economy.
-Simplified the system that doesn't give research points on conquest for isolationist uncivs by including it in the Isolationism modifier.
-Removed Border Policy and Conscription changes from under the "Government Decisions" "tab" in the decisions screen.
-Changed so the "Long War" modifier happens through an event rather than a triggered modifier. It also has more strict requirements and take into account vassals. Should avoid false-positives.
-Uniting Indonesia as a native through the path of good relations and nationalism now requires the (uniting) country being at least a secondary power.
-Made Belluno part of the Venetia state.
-Minor overhaul of the Neuchatel Crisis event chain. Fixed spaghetti code, cleaned effects and triggers a bit. Also made it so Switzerland can solve the issue any time the claiming country (which can be Prussia, NGF or Germany) drops out of GP status. The only claiming country is Prussia, so if the NGF or Germany is formed by another nation and absorbs them, the claim will also be lost. Fixed one of the Neuchatel decisions possibly being taken more than once.
-Minor cleanup of the decision for Polish minors to unite with Poland. It also requires good relations (more than 50) with Poland/Congress Poland and similar government (a fascist polish minor won't unite with a communist one. Democratic minors unite with democracies and Constitutional monarchies. monarchies unite with monarchies. Communists/fascists only with communists/fascists. Presidential Dictatorships unite with everyone).
-Fixed several typos in decisions descriptions.
-Added a few military goods to the stockpile of countries at the start of the game. Countries with a higher rank have more supplies.
-Doctrine of Lapse events shouldn't fire if for Russia/UK if they are disarmed or recently lost a war.
-Creating Pakistan will no longer automatically remove India cores from Pakistani territory.
-Reworked the claims in the Congo Conference if the country awarded doesn't get all the territory from its awarded owner (removed a special CB that was causing problems).
-Re-did the decision to integrate North and South Yemen so the AI takes it more and conditions are more reasonable.
-Reworked Kunduz province cores to avoid late-game border gore and added a missing Afghan core.
-Fixed a wrong tag in the "The Conakry Protectorate" decision.
-Added the new AFPG flag for the Tokugawa Monarchy. Kudos to him!
-The shastar_vidya modifier for the Sikh should be removed once the country westernizes.
-Indo-Iranian countries like Bahalwapur should join India as long as the Two-Nation Theory didn't happen yet (I should add a way for it to pop up organically too).
-Fixed the "[culture] Rebellion in [state]" (event 97100) so it doesn't happen for India at all and normally doesn't happen for Indo-Iranian countries (can still happen in a few conditions).
-Made sure Indian nationalist rebels won't spawn in India.
-Added another option for the "Colonial Legacy" decision so it doesn't require civilization progress for high literacy (>75%) former colonies.
-Fixed the "Shipwrecked Sailors" event effects.
-Changed the RP gain from the "Western Presence" province modifier from 2% to 1% and added a militancy gain to it. The effects are also usually temporary.
-Unciv Isolationism should now affect CB fabrication speed.
-Moved the event dealing with the Mandate of Heaven to the setup decision. Also made bureaucrats and Aristocrats in China start with more literacy.
-Re-made the Malay sultanates (Johor, Pahang, Perak and Selangor) integration decisions into 2 repeating events for the sphere owner or neighbouring countries. This should clear up some clutter from the British decisions and will make the actual integration of these sultanates a bit more random.
-Fixed pops in Malaysia (lack of aristocrats, presence of some British bureaucrats). Fixed the OOB of the Malay states.
-Reorganized the Spanish OOB.
-Fixed the (NNM) Sulu Protectorate decision being impossible to take because it required Sulu not owning one of its core provinces.
-Reshaped 1842 - Junaynah and 2564 - Salima so there aren't straight borders between both states. The state of Darfur (1842 and 1841) was integrated in Kordofan and Waw (1843) in present day south sudan was moved tot he Sudd state, removing one state from Sudan. Fixed terrain in Obeid Junaynah.
-Gave a new state to France, Champagne. It's made of half of the easternmost Picardie provinces + Chaumont. Franche-Comté now has 4 provinces, same as Champagne, and Picardie has 3.
-Reshaped the provinces in France-Comté to follow the Meuse rivers, partially based on >>133643504. Fixed pops to account for the change.
-Minor reshape of provinces in Anatolia, following for the most part the proposed borders in >>134359994
-Moved province 895 - Mersin from the Adana state to the Konya state. 
-Included 548 - Stralsund and 547 - Greifswald in the Mecklenburg state. That way Mecklenburg has 4 provinces instead of being 6 - 2 provinces states.
-Fixed Ashkenazi/Sephardic pops in France, Algeria, Belgium, Austria, Hungary, Switzerland, Czech Republic, Luxembourg, Netherlands, Germany, Poland, Baltic states, Balkans, Turkey, Italy, Ukraine, Belarus and Russia. Pops there were diversified (so they aren't all artisans) to include all common classes (soldiers, farmers, clergy, aristocrats), micro-pops (5 or less) were increased. A few states that had no jewish pops got jewish pops. French and German Jewish pops were changed to Ashkenazi. Added a small (3%) protestant north german minority to Luxembourg.
-Changed Province 583 from Westfalen region to East Rheinland. Changed province 681 Kustrin from Brandenburg region to Pomerania. Moved 585 - Detmold from Westfalen to Hannover. Moved 538 - Osnabruck from East Friesland to Westfalen. Moved 535 - Nienburg from Hannover to Lower Elbe. Moved 2560 - Darmstadt from Hessen to the Palatinate Region. Moved 693 - Elbing from East to West Prussia. Overall, these changes aim to make the German states a bit more balanced in the number of provinces as well as pops.
-Renamed province 582 - Minden to Bielefeld.
-Made an event for the Ostflucht that can trigger if pops in the East are poor and will worse emigration from the east.
-Fixed the 1850 compromise not properly adding Texas cores back.
-Made the blood and iron event require tech (Open Hearth Furnace) or any year after 1900 and increased its MTTH from 800 to 1200.
-Increased the MTTH of the events that spread CSA cores.
-Minor changes on pop support/opposition too slavery based on ideology. Made African Diaspora culture also have a -50% modifier for supporting slavery and +25% for abolishing it.
-Reworked the stop-gap dismantlement that shipped with version 0.4. Now it works like this:
	*Colonies will be distributed through a period of a year, during which the countries that won the war (and I took steps to avoid the false-positives that happen in the NNM dismantlement) will randomly get events offering them the colonies. In NNM you pay a flat 4 or 2 infamy for this process, but the new dismantlement works with the population of the former colony - you get 0.5 infamy for every 500k pops, capping at 10 infamy. Colonies with less than 500k but more than 250k give 0.25 infamy. Countries with less give 0.05 infamy. The country can choose to get the colony, wait for other opportunities (skip a colony) or drop out of the partition process. Waiting doesn't cost or change anything and dropping out gives you -2 infamy.
	*The final point is how it handles partial colonies. Before all colonies are released any country that is not allied with the loser and is not in a war, dismantled or disarmed and that holds a partial colony (or more specific, certain key provinces of a partial colony) can claim the rest of the colony infamy free.
	*If a country is not picked to be a colony, they will be decolonized after one year of the dismantlement date.
	*The system is not perfect - there's tweaks in values and more colonial regions to add, but the outcomes are varied and realistic enough and the borders drift towards normalization rather than gore. Please report any odd behaviour!
-Made Romania releasable during a dismantlement (previously it was impossible for them to be released).
-Rhodesia is one of the releasable nations if the UK is dismantled (won't be divided as part of the colonial spoils).
-Added a "Back to Africa Act" for non African diaspora-primary New World dictatorships (except communist). If the country owns/sphere/vassals Liberia, they can take a decision to deport African-diaspora cultures. Slaves are sure to go while free pops might escape. The decision works with a timed province event that tries to do the deportation while a modifier will add infamy while the decision is activated. You can't have the "slavery debate" modifier and need the Phenomenalism tech to enact it, among other requirements.
-Slaves now can only join a "Slave Revolt" rebel type. They don't usually get funding but if they do (which I never saw) they might rise. They will free slaves of the provinces they conquer, abolish slavery if they take the capital and kill non African-diaspora and non-slave pops in the provinces they take. 
-Fixed provinces 131 and 130 not having any cores.
-Reworked the Ostend Manifesto so it's worthwhile to take. It can give less infamy and it triggers the event chain to offer to buy Cuba. If refused, you get CBs. Also made the requirements more legible. 
-Tweaked the decision to buy Cuba a little bit. Made it available for the CSA and Texas.
-Changed the Falklands back into "Tundra" terrain again.
-The US should now use their Monroe Doctrine CB on European countries that take Patagonia, excluding the Falklands.
-Made abolitionist GPs boost the abolitionist movement in their spheres.
-Removed hazara as accepted from Persia. They didn't move there until the late 1880's - see http://www.iranicaonline.org/articles/hazara-2
-Changed the has_unclaimed_cores that some people were having trouble with another check that will hopefully not give any trouble.
-Stopped the CSA from having to pay vassal contributions before the Civil War.
-Changed provinces 1377 - Tourane and 1378 - Pleiku from Tobacco to Fish and Fruit, respectively. Changed 1381 - Donqguai from Cotton to Wool. Changed 1370 - Hai Phong from grain to Cattle. 1362 - Satavan from Tobacco to Fruit. 1356 - Luang Prabang from tropical_wood to grain. 1357 - Vientiane from grain to wool. 1351 - Praichinburi from Grain to Fish. Changed 1364 - Phnom Penh and 1367 - Kampot from tropical_wood to grain and fish, respectively. 1368 - Stongtreng and 1366 - Battambang were changed from grain to wool and fruit respectively. 1339 - Haka, 1334 - Ava and 1336 - Magwe were changed from tropical_wood to fruit, wool and cattle, respectively. Changed 2572 - Nan from Opium to wool. Did other changes to Indonesia and Malaysia. This is done to ensure small nations in SE Asia have basic RGOs and can survive even in shortage events. Most RGOs are flipped to cash-crops again with events/decisions.
-Added events to organize production Vietnam, Malaysia and Cambodia to revert a few basic crops to cash crops. These events can be used by (civilized) native tags or colonizers. In Indonesia, Cambodia, Vietnam and Laos, it uses the already existing "Organize/Create X" decisions. Otherwise it will happen on civilizing for these countries.
-Made the decisions to annex Laosi minors or Cambodia non-exclusive to a GP France. Now it requires an SP/GP that owns Vietnam and is in Europe or is Japan, except for Russia and Turkey (unless they have sea power and the merchant marine tech school) or any country that has sea power tech school.
-Added some coal and iron to Vietnam that will show up when they westernize or the colony is organized. Based on http://annales.org/archives/x/blondel.html and https://pdfs.semanticscholar.org/f7e3/82f118604c26ac6fc700297761b6f906e10b.pdf (Mineral resources of Vietnam by Imrich Kušnír)
-Fixed the Mexican OOB where a few brigades didn't appear and some where based on 15 soldier pops. Reduced the number of brigades to be closer to the actual number of circa 6,500 soldiers.
-Texas will start with 3 frigates and a clipper transport. The Navy is commanded by Charles Edward Hawkins.
-Changed how the event to Capture Santa Anna works for Texas. Instead of the NNM requirements where it was based on how much % of Texas was occupied, it will have 4 triggers: any units being in a battle with Mexico, if the Texan Navy is blockading the coast of Mexico, if more than 5% of Mexico is occupied or if Texas occupies the capital of Mexico. Santa Anna will also be represented as a modifier, which will expire around the 1870's (random chance each game) and/or will be removed once they lose the war and/or lose to a revolution. This way the event to capture Santa Anna will never fire if Santa Anna should be dead already.
-Slightly increased the colonial points that are given by the Sea Power Doctrine and Naval Imperialism Doctrine inventions.
-Added missing Togo cores when the colony is organized.

***

Changelog:

V0.4.1 - 09/01/2019
-Fixed the "Reject Pan-Nationalism" decision showing up for the USA. Also made it require either accepted or good schools reform.
-Sea Power and the Merchant Marine Tech School now give up to 400 colonial points through special inventions in the naval tech tree.
-Added Venetian cores in the adriatic coast and south tyrol to avoid assimilation there for a while.
-Made italian decisions that give cores a bit more consistent.
-Added a decision for Italy to accept Maltese if they own the island and are a Constitutional Monarchy or a Democracy (along with a few other requirements).
-Added a decision to give home rule to India.
-Fixed "border policy" decisions not being hidden under government decisions.
-Fixed several CBs that could be invalidated during a war because of rapid changing conditions. Fixed Demand Concession CB not working properly.

_______________________________________________________________________________________________________________________________________
V0.4 - 08/01/2019
-Made the Krakow events (slightly) less CPU-demanding, gave a redundant CB to Austria so players are aware that they get a free CB on Krakow.
-Rebalanced base profitability for a few factories.
-Made coal in different regions (Rhine/Wales/Durham) have "more quality" (25% higher output). (see Zum.de Gpih.ucdavis.edu Bbc.co.uk and Jstor.org)
-Changed 1029 - Glasov, 1031 - Sarapol and 1032 - Chistopol from timber to iron. Gave UK and Belgium the "puddling process" technology. This will make Russia one of the major producers of Iron. Source in Jstor.org
-Changed 1522 - Wuchang and 1613 - Chengde from Iron to Tea and Grain respectively. These will change back to iron sometime after 1856.
-Made the Korean economy a bit more diversified. Changed 1626 - Haeju and 1627 Sariwon from Iron to fruit and Cattle respectively. Changed 1619 - Pyongyang from Coal to Silk.
-Made the RGO change events for high-unemployment provinces happen only after 1850 and need a few techs (bessemer process/steam turbine).
-Moved the Electricity tree more in line with the rest of the other research trees. This makes inventions unlock in more realistic time-lines and gives more time for Electric Gear production by the AI.
-Made an event for the first oil well to be discovered in the 1840's or 50's in Canada, US, Baku or Romania.
-Changed 2407 - Tabatinga, 2287 - Yurimaguas and 2320 - Riberalta, 2286 - Iquitos, 2319 - Santa Ana from wood to rubber. 2410 - Belem was changed from Fish to Rubber and 2402 - Manaus was changed from Tropical Wood to Rubber. Made to represent the early small rubber trade that existed and so the demand for it can be fulfilled before full industrial utilization.
-Provinces that change to oil through event will try to avoid it if there's unemployment in other oil provinces around the world until unemployment is down.
-AI will try to steer clear of the Metallurgy tech tree if they detect significant overproduction of Iron or Coal.
-Made the AI try to get Radio factories more aggressively. Before they would rarely do it. Moved Radio and related inventions from Behaviorism to Psychoanalysis and fixed the whole tree unlock dates to be more realistic. Radio are unlocked starting from the 1890's instead of the 1900's.
-State FRA_1775 - Mauritania renamed to Trab el Beidan. The name will change to Mauritania after Mauritania is organized. Source: Books.openedition.org
-Fixed a "fire only once" command in an event that was supposed to happen multiple times.
-Re-did the Sulphur distribution early game. 2523 - Nauru starts producing it, 565 - Wiesbaden too but 570 - Mainz got changed to Fruit - effectively swapping them to a more accurate location of phosphate mining. 387 - Brussels now starts producing Coal instead of Sulphur. 2226 - Tortola starts producing Sulphur instead of Tobacco. 716 - Kielce lost Coal to Sulphur. 2295 - Lima and 2578 - Tacna were also changed from Cattle and Wool to Sulphur. When the gold rush starts in Lima, that should mark the end of the Guano Era in Peru. 468 - Avignon was changed to Cattle, another French province gets Sulphur after a while.
-Added Iron and Coal to a few parts of modern-day Poland (Mainly in-game Russian and Prussian Poland). These will appear as the game goes on. These changes and some Sulphur changes are based on:
*Source for all Polish changes: Mineral raw materials and commodities of Poland, Piwocki and Przenioslo. See Pgi.gov.pl
*Alsace-Lorraine and Europe by Lucien Gallois, pp1918
*Mines and quarries 1902 By United States Census Office - 12th census, 1900, William Mott Steuart, United States. Bureau of the Census. pp 921-922
-Tunisia gets an iron mine in Gafsa and a sulphur one in Tzoeur, representing the Jerissa mine and the Metlaoui phosphate deposits. This happens after 1890. Sources are En.wikipedia.org and En.wikipedia.orgété_du_Djebel-Djérissa
-Algeria starts without iron mines now. They are found and utilized as time passes from the 1860's onwards. Based on En.wikipedia.org
-Split bureaucrat steel and cement needs between everyday and luxury. Made aristocrat luxury needs more in line with capitalists. Added these needs, in a smaller scale, to officers.
-Jingoism will now carry a minimum 50% spending on troops salary and pro-military carries a minimum 25% on troops salary.
-Officers and soldiers will now need a small amount of artillery (to represent training and replacing of regimental equipment and to be in-line with their small arms needs).
-Fixed a bug that made the Platine War end with Entre-Rios peacing out the moment it began.
-Made a decision to change the RGOs of a given (organizable) colony to the ones that the colonies get when you organize it. This decision costs money. Its main purpose is to allow the RGOs to change even if a colony isn't organized (or if the country in the area is a local one).
-Venezuela should get some Coal province later in the game. Based on Academia.eduÓN_HISTÓRICA_DE_LA_MINERÍA_VENEZOLANA_DESDE_LA_PRECOLONIA_HASTA_NUESTROS_DÍAS
-"Organizing Colony" decisions now need Machine Guns and Market Regulations. They also will change a few RGOs to cash-crop/mining RGOs, making the decisions more worthwhile. Reduced the number of cash crops/mining operations in African uncivs and moved them to the "organize" decisions - these nations were more focused on subsistence than export-economy.
*Nigeria RGOs redone. The source is (An Economic History
of Nigeria 186o-196o Sahistory.org.za uploads /r._olufemi_ekundare_an_economic_history_of_nigerbook4you.org_.pdf )
*South Africa got a few more iron and coal provinces. Mostly based on Saimm.co.za and Isc.hbs.edu Africa_Iron Ore_2013.pdf
*Indonesia got a few iron provinces that will appear later. Based on Aig.org.au the history of coal development in indonesia.pdf
*Mauritania gets an iron province in the north.
*Senegal gets a few cotton provinces. Saint-Louis changed to cotton. Source: Persee.fr pp303 and "La crise trentenaire de l’économie arachidière" by Mohamed Mbodj pp3
*Upper Volta will produce cotton in the south. Diversified starting RGOs a bit (previously it was only grain). Based on Icac.org and Lefaso.net
*Mali will now produce cotton in the south. Diversified starting RGOs and made sure cattle is in the cattle zone while fruits/grain start in the south. They will no longer start producing cotton either. Based on Fews.net copy.jpg?itok=NA3ukgKa and Haskovi.org
*Ivory Coast has a big cash-crop centered economy once colonized. The south will turn to coffee production while the north has cotton and rubber. Based on Legacy.lib.utexas.edu and Horizon.documentation.ird.fr
*Sierra Leone gets Coffee in Freetown after they are organized. Based on Universityofmakeni.com
*Guinea has an economy focusing on Rubber. Other productions are fruit (bananas) and a gold mine. Source: Persee.fr
*The Gambia is unchanged, as it exported groundnuts for most of its history. Source Stclements.edu
*When Guinea-Bissau is organized they will export timber and rubber. Based on En.wikipedia.org
*Niger, when organized, gets a 2 cotton producing provinces. Based on Persee.fr and Persee.fr and En.wikipedia.org
-Reshaped 2069 - Gweru so Matabele doesn't have a land connection to Transvaal, ending in terrible borders. Adjusted events to eliminate other bordering provinces. Fixed a bug that made Gweru end with too much LR.
-Fixed a bug that didn't completely exclude the overlord of the Congo Free State from the Scramble.
-Fixed the Gold Coast Treaty never happening because of a bug.
-The UK will now start as "friendly" with Uruguay.
-Now there are 4 CBs that deal with the scramble - 2 from NNM and 2 from HPM. They work like this:
-West Africa, South Africa and Mozambique regions, where multiple tags are present, are divided in informal (colonial) regions, equivalent to modern colonies. When a country owns a province (or state) in one of these regions it's assumed they are claiming it in the Berlin Conference. What this means is that all nations lose the free scramble CB on any uncivs in that region and only the nation(s) that own provinces inside the colonial region can use the free (new) CB. The new CBs are for demanding states and annexing uncivs in the colonial region and behave exactly like the free scramble CBs, except that they are not available for everyone and are not restricted to SP and GP countries (so if a SP loses their status they won't suddenly stop establishing themselves in that colonial region). If more than one nation owns land in the claimed colonial region - like the British and Dutch in the Gold Coast - they both get the new CBs and will have to compete between themselves for the land. For purposes of Colonial Regions, Mauritania is dependent on Senegal (like it was historically) and as such the owner of Senegal treats Mauritania as if it was the same region.
-The Gambia isn't considered as part of the Senegal and is excluded from the CBs. Prevents the British "leaking" through it.
-Matabeleland is treated as part of South Africa in these CBs.
-Nations can still use the "Establish Protectorate/Demand Concession" CBs to get a foothold in a region. They need time and run the risk of getting infamy for forging an incident, but they can enter the race in colonial regions with other powers like that. Likewise, not using your free CB to finish conquering a colonial region might mean that another uses the principle of effective occupation to penetrate in your colonial region and take it. The CBs are not a 100% guarantee that a nation will get something, if they don't enforce their claims they will get nothing. The post Conference "Establish Protectorate/Demand Concession" are unusable as "wargoals" during a war now to avoid the AI ignoring the rules to swallow whole regions.
-Colonial regions (such as Mali and Niger) that have no occupied provinces by other civilized powers will be treated by the normal Scramble CBs and will immediately shift to the new CBs once a nation conquers a state there. To avoid potential abuse in the form of claiming one state in several uncivs, the old Scramble CBs now carry a cooldown of 4 months when you start and when you finish a war.
-Colonization of uncolonized territories is unchanged.
-Egypt, Ethiopia, and Algeria are included. Eritrea is excluded.
-The CB to annex work against a country with 3 or less states. The CB to demand state works against countries that have 4 or more states.
-Made the conquest of Algeria, Indonesia and Yemen use the same CB and system as the one Portugal uses for Mozambique. This cuts down in the number of repeating events/decisions that are used to give CBs to these countries and it's a more elegant and dynamic solution. Countries can "take over" the colonial claims in the region and benefit from the same CBs. Some countries might keep the claims on the region even after they are expelled if too long is taken to expel them. This also makes the rules the same for Ai and players. The CB was renamed to "Imperialism", can't be used if you are already at war, is always present (given you researched "state and government" and fulfilled the other conditions) and enforce a random 1 to 5 years "waiting" period for it to be usable again after a war (using the CB) is concluded. Annex Imperialism CBs carry a mandatory 3-years wait period.
-When deciding if they have access to some CBs against a nation they are not neighboring but can be reached by sea, countries will now check if they have at least 5 ships instead of only if they have a port. Hopefully this makes the AI declare less wars that drag-on forever.
-Added sulphur and iron to Morocco, they appear after 1870.
-Added an alternative solution path for the Senegal/Guinea-Bissau border treaty.
-Normalized several cores in West Africa so tags there can conquer each other.
-Made the Togo and Namibia decisions have different conditions so one doesn't end up excluding the other. The Namibian decision should now transfer the whole region with the exception of the caprivi strip which is handled differently.
-Renamed "Egyptian Desert" state to "Western Desert" to avoid some name weirdness. Removed the "Alexandria" state and distributed the provinces between Western Desert and Cairo state. Both have 7 provinces each, which is a bit too much for a state (though in the case of the Western Desert it doesn't matter much seeing as it's sparsely populated) but the results should be nicer borders if Egypt ever gets broken up.
-Reshaped provinces so borders and some states follow the rivers in Ivory Coast, Mali and Ghana. Fixed artefacts and adjusted positioning and name placement.
-Portugal's liberal party - that lasts until 1854 - will now start as protectionist. Portugal doesn't start with any Free-Trade party. Based on "Economic Ideas and Policies in Nineteenth-Century Portugal" by Maria Eugénia Mata, pp5. - Run.unl.pt
-"Conquest of the South" decision can now be taken by other Ethiopian countries after a certain date and if Ethiopia doesn't exist.
-Made GPs and SPs low on money be more aggressively protectionist.
-Changed Milan and Bergamo to cotton. Based on Helsinki.fi and Zum.de
-Slightly increased the productivity of slaves (to 40% from 30%).
-Decreased the Cotton Gin bonus from 50% to 25%.
-Reduce inventions that give food RGOs bonus to production by 5% to 10% to avoid late-game overproduction.
-Condensed the 30 vanilla events made for Oil RGO spread into 2 repeatable events (a few of the vanilla events were also repeatable, otherwise there would be more).
-Stopped Rubber from spreading if there's too much unemployment in the rubber market.
-Added the "Copper Belt" in Zambia.
-Doubled the colonial power needed to maintain colonies. To compensate, big ships from Ironclads onward give more colonial power and Naval bases give slightly more colonial power. Small ships like Monitors and Commerce raiders will give less colonial power.
-Made Steel, Cement, Small Arms, Canned Food, Ammunition, Telephones and Radios needed for Overseas Maintenance (this will probably backfire but I'd like to give it another try).
-Reduced the prestige gains in the Sound Toll event chain.
-Changed a few Iron RGOs in Spain, they get a few more after 1865, they also got a silk producing province. Based on "An Economic History of Modern Spain" By Joseph Harrison pp56 onwards and "Economic History of Spain" by By Jaime Vicens Vives pp 663 onwards.
-Reduced max loan amount from "Private Investor" from 5000 to 2000.
-Goa will now start with Precious goods and will flip to Iron after 1885. Partially based on Shodhganga.inflibnet.ac.in 2.pdf
-Portugal will start with a 3 more economy techs to help them through the first years and represent their focus on commerce. To compensate, they lose 2 industrial techs.
-When the event "Retreat to Formosa" happens, Taiwan will inherit all previously acquired unciv reforms that the retreating country has.
-Added an option for localized province names during the game start options. Right now it only has Italy but as time goes on I will add more.
-Added an option for "Economic Non-Interventionism" for free trade countries that limit tariffs from -25% to 25%.
-If Russia wins the Crimean war they will get more influence over the Ottoman Empire (100 from the previous 50), they will remove any Romanian cores from Bessarabia and give all of Dobrudja to Romania. The Ottoman Empire will pay the money they owe in installments to avoid instant-bankruptcy.
-Fixed a NNM bug on the "A Treatise on Economics" event that made the event have the wrong description text.
-Moved substate payments to happen every 5 months and vassal payments to happen every 6 months. Tripled the amount of money transferred each time.
-Trade Policy will be wiped in the event of bankruptcy. The country will be unable to pick a new one for the duration of it.
-Added an option to disable "Foreign Trade policy" decisions at the game start.
-Changed the Kansas-Nebraska Act, Fugitive Slave Act and Nashville Convention decisions so their effects are more easily readable.
-Fixed Wilmot Provisio and 1850 Compromise decision so they properly remove slave-state status. Made the effects easier to read.
-Made sure The Gold Coast Treaty decision doesn't leave anything in the gold coast with the dutch.
-Reworked the events that use the system that makes the AI able to pay large amount of cashes without going bankrupt so it's more optimized.
-Added some coal provinces to Indonesia after formation. Bogor should flip to gold mining in the end of the 19th century. Based on Ier.hit-u.ac.jp p66 onwards
-Fixed the "Bleeding Kansas" event never happening. It will also change the state either to slavery or to a free state, depending on the choice.
-Made so the 1850 Compromise decision can be taken only after the Treaty of Guadalupe Hidalgo was taken and so it's a more mutually exclusive choice with the Wilmot Proviso.
-Made the 54-40 Or Fight! event only fire if the US borders Washington. This will avoid a random US exclave in the area.
-Fixed typo in the vanilla description of the Von Moltke's reform decision. Fixed a wrong description text on the "Rhine Crisis" event. Fixed Lake Victoria being called "Vasa" instead of "Lake Vasa" if the Swedes discovered it. Fixed the text description of the "The Polish Question" event. Fixed one option description in the event "Conflict on Mount Lebanon".
-Stopped Abu Dhabi flipping between oil and precious goods non-stop after Oil is unlocked in the region. When they unlock Oil they will also revert back to Oil instead of fruits.
-Fixed Finland's only communist party disappearing before the game ends.
-When externally forming Arabia, they will now inherit Nejd's reforms. If Nejd is civilized, they will start civilized too.
-"Topple the Qajar dynasty" event won't fire if Persia is already a vassal.
-When forming Romania externally Bukovina and Moldova will always be integrated.
-Fixed a bug that made so the coronation of Pedro II event never fired.
-Merged the Vanilla "Source of the nile" and the 2 HPM events in a single one. The generic name for Lake Victoria (if a nation that doesn't have a custom name for it gets the event) will be present in the 5 options instead of being handled as a separate event. Made it easier to find the source for nations that control any part of the Nile below Cairo, the sphere owners of Egypt/Sudan, and nations with the "Sea Power" tech tradition. It's harder for nations that don't have the Raider Group Doctrine tech.
-Fixed the EIC option giving EIC territories during the Doctrine of Lapse after the EIC was integrated.
-Fixed the railroad between Misratah and Gabes going through the ocean. Fixed the position of the RGO picture for the province of Xiangabouli.
-If the nation that gets the Congo violates the protocol and annexes it, instead of getting a place in the sun CB the GPs will get only the cut down to size CB. The first GP that enforces the CB on the offending nation will get the whole of the Congo from them.
-Any German nation that controls Heligoland and has Nationalism & Imperialism can take a decision to add a German core to the island.
-Added a News story for the Armenian Genocide when it happens.
-Made so the UK can't take the Durand Line decision if Afghanistan is at war.
-Buying Djibouti is a bit more restricted now and requires higher-level tech.
-Fixed Keren in Ethiopia being renamed because of a wrong province number in a decision.
-Changed the Flores Sale decision so Portugal is a bit more inclined to sell it when they are low on money and don't care if the buyer is a GP/SP. Now they get 100k for it and the AI will pay in installments.
-Made so there's some late game coal spread in the US. Based on Eh.net
-Hot Springs, Nashville and Greenville changed to Cotton. Changed Memphis to Tobacco. Based on Qph.fs.quoracdn.net
-The sale of Assab event will only transfer Assab now. The rest of the state will be gradually transferred to the owner of Assab through event if militancy in the province is high enough or if the owner of Assab spheres them. Civilized powers will get an event where they can choose to cooperate and give their Eritrean provinces or they don't and get infamy and possibly war.
-The "Request Missionary" event and decision will now change the requesting country religion if the nation is sphered. Made relations weight more in the AI decision to give missionaries or not.
-Moved Athens to the Peloponnese state and Zante to Central Greece.
-Nerfed British Raj triggered modifier. It will not reduce militancy for core_pops so drastically.
-Increased (a bit) the effects of the Autocracy and Tradition NV (decreases literacy impact on CON, reduced militancy and greater ruling party support).
-The League of Three Emperors will now be usable with Revolution & Counterrevolution instead of needing "Great Wars" to be enabled.
-Divided Italy's decisions to gain cores in Friuli, Venetia, Tirol and the Balkans. Now they can get cores in Friuli and Venetia right away but the decision to get cores in the Balkans and Tirol need Mass Politics and a Jingoist party.
-Made the decisions that remove italian minor cores also remove the cores of Trieste and Friuli/Carnaro. It will also remove Austria cores from Venetia/Friuli if they have cores there.
-Included the Yemeni minors in the "Imperialism Comes to $COUNTRY$" event. Removed restrictions on the event about the sphere owner pacifism and rebels.
-Made Udine part of the state of Venetia and Belluno part of the state of Friuli. Hopefully it will lead to better borders when Italy doesn't finish conquering its borders.
-Made the country that got awarded the Congo not able to colonize for 10 years after they integrated (inherited) Congo. This will represent them focusing their power on integrating the place and the fact that they technically should renounce any right to colonization. If they become a GP this will not be applicable and they will be back at colonizing.
-To represent the lobby of abolitionist countries like the UK, pops in countries with slavery enabled that are sphered by abolitionist countries will have a bit more support for the abolition of slavery. As always, Landowners in slave states, however, will be more likely to be pro-slavery than against it.
-Added custom names for the different government types of the FRCA.
-Made the decisions to change RGOs in Central Asia a bit easier to take. Made a few more RGOs change, mainly based on Bankwatch.org
-Made naval inventions that unlock ships more likely to be invented the further in the game you are. They are also more likely to be invented if you have neighbors with the invention. This should help with spread of the tech and stop man'o'wars being built by civilized countries in the 20th century. Also made these inventions like many of the army inventions that are more likely to happen if you are at war with someone with the invention.
-Added a random event for the conquest of the Coast of Gabon. A random GP/SP with 50k money, capital in Europe, not Turkey or UK and Raider Group Doctrine will get an event giving them the two coastal provinces of Gabon. Libreville will be named in the equivalent language of the country that gets the event (and if they don't have a custom name defined they will be named "Libreville"). The UK has a lower chance of getting the event, but it's still included.
-Re-balanced ship needs to be more in line with their power and size.
-Coal will spread in Mexico from the 1880's onwards in Cohauila.
-Taiwan now produces coal. Penghu in Taiwan will change to Sulphur to represent the guano exploitation in the South East sea.
-509 - Seville changed from Grain to Coal. Rio Gallegos, in Argentina, and Barranquilla in Colombia will later change to Coal too. based on Pubman.mpdl.mpg.de and Spain, Europe, and the 'Spanish Miracle', 1700-1900 By David R. Ringrose pp 299
-Made 3 German provinces (Siegburg, Nuremberg and Bayreuth) change to coal during late game. Luxembourg will also start producing coal. Based on En.wikisource.orgædia_Britannica/Germany
-Reworked religious and cultural influence on conservatism for pops. In vanilla there was none and in HPM it worked in a way that muslims and shinto pops were a bit (10%) more conservative. Now it's divided in steps and encompasses more religions: Mormons, Sunni and Gelugpa are 40% more conservative, Shinto and Mahayana are 30% more, Shiites and Ibadi are 20% more and Orthodox and Coptics are 10% more conservative. This is only applicable for pops that are either accepted or primary culture and share the state religion, so if a pop is under occupation by a foreign power it won't be complacent. Confucianist pops (defined as the East Asian culture group, basically chinese pops) are 10% more likely to be conservative regardless of the situation.
-Made "Two Per State" and "Based on Population" give the same amount of immigrant attraction.
-Made a "Two-Party System" depending on the reforms a country has. If a country has "First Past the Post" and either "Appointed" or "Two Per State", the system will get in place and pops will stop drifting to radical ideologies and will focus on conservatism and liberalism. This will not make other ideologies disappear, it will just strengthen conservatives and liberals. It's possible that a three-party system happens, but it's also possible that either conservatives or liberals lose space to socialists in the two-party system. The two party system tries to emulate Duverger's law.
-Stopped Fascist/Communist/Anarcho-liberal/Presidential Dictatorships from having a malus of -50% (sometimes -90%) to their respective ideologies if the pop was under 6 militancy. The way it worked before was in a way that, right after a successful revolution, militancy went down and so did adherence to the revolutionary ideology. Now this condition only applies for non-radical or wrong governments. So the -50% for the reactionaries/communists/Anarcho-liberals ideologies is still present under a fascist dictatorship or democracy, but not for the fascists in power. In other words, adoption of a certain radical ideology won't be lower if their militancy is under 6 but they are on the right government type.
-Increased the effect that the Autocracy NV has on radical (fascist/anarcho-liberal/communist) ideologies in the right government types. Removed the Tradition NV having any effect on these governments (though their effect on reactionary governments remains).
-Made so that taking the Totalitarian System decision will make pops be way more inclined to adopt the ruling party ideology.
-Fixed and tweaked a few more values in all ideologies, adjusted position of certain modifiers so the most important ones are more visible.
-Stopped pops in the British or American group from demanding something over First Past the Post and Appointed (for British)/two per state (for American) in their respective reforms, but only if their government is "right" (monarchy for the UK, Democracy for the US).
-Fixed one cleanup decision and made a few cleanup events into cleanup decisions.
-Stopped the AI in democratic countries from randomly abolishing Public Meetings because of "The Mud March" event. Now only AI democracies with fascist, communist or reactionary parties in power will ever pick that option.
-Reworked the US parties to remove parties that survived for a few years only and so that there's no two parties with the same ideology at the same time.
-Made the "Greater Arabia" decision more in line with the other irredentist decisions. Arabia won't be able to take the decision if they were formed externally.
-Removed Chile from the Great Game CB.
-Fixed option B of event 97647 having the same text as option A.
-Accepting Urquiza's demand should now get make him appear for the Confederation as a general.
-Moved the Lambert Charter decision to require Nationalism and Imperialism.
-Unciv rebels should now only remove economical reforms, not military ones. They have a chance of not removing reforms at all. To balance that out they will also wipe years of research and put a modifier that will reduce militancy but will also greatly reduce research. The effects are now random (from 5 options) so the results of an unciv reactionary rebellion are not completely predictable.
-Starting Party Loyalty will be wiped ten years after the game start. This won't affect party loyalty gained after the game start, just the starting loyalty.
-Made the Shinbutsu Buri a decision that any japanese-primary country can take if they are a buddhist nation. Changed it to require "state and government".
-The decision to claim the Chaco region for Argentina will now force any vassal that owns lands in the Argentinian Chaco to cede the provinces to their overlord.
-When Finland becomes independent, if Sweden (or Scandinavia) have cores on them they will receive an ultimatum to forfeit their claims or reassert them and get cores in Petsamo. This will hopefully end the cases of "Karelia-only" Finland.
-If both Wallachia and Moldavia are cut out of the Ottoman Empire (meaning they don't neighbor any Ottoman provinces or puppets) and the Ottomans are not a GP, they will now be able to Unite into Romania and will declare independence from the Ottoman Empire. The Turks will get a CB to puppet them back.
-During the Berlin Congress, countries that vote in favor or against the ottomans will gain a small relations boost with each other. Rather than wiping influence and relation, these fluctuations will vary if you supported or not the OE. Made the influence gains during the congress lower than they were to avoid influence wiping. Also gave the AI that is the sphere owner/ally of the OE a chance of supporting them if they defy the congress. If there are any NNM events that are causing too many "sphere" flips out of the blue, please, let me know (screenshots of the event would be even better).
-Soldiers and officers now need a bit of wine as luxury needs.
-Fixed the ultimatum to Portugal decision to include the Matabeleland state.
-Added a new terrain type - Mining District. It's the same as "Farmlands", but for mines. It will be used to represent areas where there was higher-quality ore being extracted. Changed the bonus of both farmlands and mining districts from 20% increase in size of the RGO to 25% increase in RGO efficiency.
-Changed the vanilla "Botanical Expedition" event so it can only happen in overseas provinces.
-Reworked LR in South and North America so all provinces have at least 31 LR - that is, they will have some base growth. Changed all capitals (except for the US and Canada) to 39 LR so they have bigger growth but without the capital monopolizing immigrants. Rebalanced the LR gain for the US provinces so no province reaches 50 and monopolizes immigrants. Reworked the LR increases to happen during the Iron Range and American Frontier decision as well as during the Mexican-American War. This way all countries will eventually have the full LR in the provinces. Removed LR increase from the Statue of Liberty.
-Northern Canada and Alaska are mostly left out from the above changes. In Canada the 38/39 LR provinces are Toronto and Montreal while in the US the 40 LR provinces happen as the game goes on.
-The uncolonized territories in Patagonia and Chaco will get their LR up as they pacify the natives - a random province event. This will also slowly remove the Patagonian cores.
-Made the Homestead Act and the Statue of Liberty bonus to immigrant attraction apply for 10 years each instead of forever.
-Slightly increased Greek pops in Nafplion.
-Added more Aristocrats to Modern Greece states so they don't end up disappearing.
-Organized the several, less used decisions in a single, "Government Decisions" decision-category that can be clicked to reveal the decisions. Did the same for the "Organize Colony" decisions, they are now all hidden under a decision that disappears when you have no more colonies to organize (and re-appears if you have some to organize).
-Re-made the event for Haiti to lose cores on the Dominican Republic after they lost it for a while.
-Removed British pops from Aden.
-Permanently occupying a country that has already been defeated will result in acquiring 0.2 infamy per month.
-Removed Greeks moving out of Istanbul during the population exchanges. Based on Hrw.org
-Made Buenos Aires get "Gateway to Harbor" modifier for 5 years when it's declared the capital.
-Countries can now open their borders without researching state and government.
-Reworked the way colonial nations are dismantled. Now if they are organized they will be released as a puppet and will be annexed later by the victorious countries. Larger colonial nations have a chance to refuse to be annexed, those will have to be conquered and will cost more infamy to claim. The old dismantlement system should kick-in later and guarantee that any left overseas land that isn't freed as a colonial nation and annexed later will be distributed.
-Made Russia be more protectionist when they choose to be, so they have more money and put up more of a fight as the game goes on.
-Changed Muhammad Ali's reform so Egypt can borrow money and will still be able to borrow money after being defeated. If they are defeated they will not immediately fall to reactionary rebels and trigger another war, but they will have a malus for research for 20 years.
-Merged the States of Equateur and Kasai and the states of Kivu and Congo Orientale. These will reduce the number of states, improving performance (Kivu had 2 provinces!) as well as hopefully allow for better partitions of the Congo. Renamed "Bas-Congo" to "Lower Congo". Belgium can rename these states to their historical names. Reshaped a few provinces in the Congo to follow in a better way.
-Stopped the "Colonial Incident" event from making a country lose relation with themselves.
-Serfdom will slightly increase tax efficiency.
-Increase the tax efficiency bonus of the Ottoman Oppression modifier.
-Increased the amount of money distributed to countries in the start. Differentiated it a bit so the top 4 GPs get more money at the start. Countries that start at war will also get more money as a "warchest" so they don't bankrupt early game and spend the rest of the game struggling.
-Increased the number of soldiers in the Dixie south so the CSA has more soldiers when they spawn. This is done so the war isn't over in one year because they don't have any soldiers.
-Russia will start with bad relations with France. Based on Britannica.com and "Nicholas I and Official Nationality in Russia 1825 - 1855" By Nicholas V. Riasanovsky pp. 255 to 257.
-The UK will start with bad relations and influence with Sind, Makran and Kalat.
-Added the Pontianak Sultanate and made it the de facto ruler of West Borneo. In truth the area was divided by several muslim sultans, with the most important ones being Pontianak, Mempawah and the Sambas, while several smaller Chinese Kongsi were de facto independent in the country-side. Changed the number of Chinese to 12500 to represent the estimated 50000 that lived there by 1850. Sources are:
*https://openaccess.leidenuniv.nl/bitstream/handle/1887/19785/Ehnic Tension_Alliance_Clientalism_Pol development of West Borneo.pdf?sequence=1
*https://www.persee.fr/doc/arch_0044-8613_1998_num_56_1_3491#arch_0044-8613_1998_num_56_1_T1_0281_0000
*Southeast Asia: A Historical Encyclopedia, From Angkor Wat to East Timor edited by Keat Gin Ooi. PP1170
*Golddiggers, Farmers, and Traders in the "Chinese Districts" of West Kalimantan, Indonesia by Mary F. Somers Heidhues pp 73
-Changed Pontianak province production from Grain to Precious Metals as it was the most important production in the region until the 1890's. Since there's no record to exactly where in China they came from, made them all Yue so the speed impact is lessened.
-The UK will only get Influence/relations when Sarawak spawns if they exist.
-Sarawak will now inherit Brunei's reforms when spawning.
-Reverted Presidential dictatorships back to vanilla so they only accept reactionary parties.
-Malta, Brittanny, Occitan and NA cultures can now reject Pan-Nationalism (disabling pan-nationalist rebels for their respective primary cultures) if they own their capitals for more than 20 years without ever getting occupied, by rebels or other countries, and there's high literacy, consciousness and acceptable schools.
-Rework of a few CBs so they are a bit more logical:
*Made so very few CBs can be used without having at least 1 military score.
*Treaty Port CB (Punitive Expedition) now requires a country to have at least 10 ships, 10 military score, Naval Plans researched, 250k pops and a Naval Base built.
*Acquire State - No longer possible to conquer far away states as a landlocked country, you will be forced to demand neighboring states until you get ocean access (later on add backstops so you it's harder to "double" your population with uncored/unaccepted cultures?). This also levels the play-field between AI and player since they now can demand the same things (previously the player could disregard rules that the AI could not).
*Demand Concession/Establish Protectorate - Reworked the way the CB works for conquering Chinese states - the rules now apply for any non-african uncivs and they impede a nation conquering populous states without certain techs. These are:
**Overseas states with 500k pops or more and less than 1M - Naval Logistics (Raider Group Doctrine + Screw-Propelled Steamers for AI)
**Overseas states with 1M pops or more and less than 2M - Naval Directionism (Steam Turbine Ships for AI)
**Overseas states with 2M pops or more - Naval Integration (Oil Driven Ships for AI)
You will also need certain military techs regardless if the target state is overseas or not. These are:
**States with 1M pops or more and less than 2M - Machine Guns
**States with 2M pops or more and less than 3M - Bolt Action Rifles + Army Risk Management
**States with 3M pops or more - Modern Divisional Structure + Army NCO Training
**In addition, small countries (<1M pops) need Machine Guns to conquer ANY unciv state with more than 200K pops.
*Scramble for Africa CBs are not affected.
*Changed how the cheaper Demand Concession and Establish Protectorate CBs work with uncivs. Instead of a hard ban on Iranians, Japanese and Korean countries and any country with over 70% westernization, it now works like this:
**Any unciv with 60% Westernization progress ("Partially Westernized Nation") or more can only be targeted by the initial Demand Concession and Establish Protectorate CBs. Scramble for Africa CBs are unaffected.
*The "Place in the Sun" CB is now harder for the AI to use. It won't be used at all by (attacking) Pacifist countries, it will require the two countries to hate themselves more if an anti-military country wants to use the CB and it will require the two countries to really hate each other after the Berlin Conference happenned.
*It's no longer possible to use the Free People and Liberate Country CBs to free states of substates. It's also not possible to use it to free states of countries that you are at war with. It's also not possible to use the Conquest CB while using one of the "Free X" CBs.
-Made a decision for a few countries (China/Qing, Canada, South Africa, Indians) to convert core provinces that are colonial provinces into full provinces.
-Fixed a few cases of isolationist countries getting the RP on conquest because they lacked the correct modifiers.
-Fixed a few flavor events in the Levant to make more sense in regards to what their description say.
-Fixed "Ranchos" decision appearing when you do not own any of california.
-Added a few tea producing provinces to Argentina.
-If the AI owns a landlock Botswana (when SAF and Rhodesia/Zimbabwe exist), it will now release it.
-Added rare events for random droughts or bountiful harvests. This will make RGO producton a bit less linear and constant, as well as providing some temporary boost to emigration. In the future, there will be more random events for plagues and such to diversify production more.
-Changed several of the province-level, spammy "WorkPlaceEvents" to be country-wide events. Most of them had effects country wide or effects to low that barely mattered and this will also solve them being spammed too much. Some could be converted to "OnAction" events in the future, for performance. Currently there's only 3 province-level "WorkPlaceEvents" events. Made the "Blood and Iron" event more generic so it applies to Iron and Coal provinces.
-Integrated the latest version of the Battle Plans Mod and a few new AFPG flags. Kudos for both!

***

V0.3.9.2 - 14/12/2017
-The US won't be able to take the Manifest Destiny decision anymore if they have troops inside Mexico.
-France needs to have any of their original Caribbean provinces (Marigot, Guadeloupe, Martinique) to fire the decision to buy St. Barths.
-Fixed localization in event 5001003.
-Removed a naval base in Bahia Blanca. Again.
-The Tangier protocol can't be fired against a non-spanish GP anymore.
-Renamed Sardinia & Corscia to Thyrrenian Islands.
-Reshaped Chamberry so it's a bit more useful in defending Annecy.
-Fixed the AI selecting the wrong options during the Bedr Khan massacres where the player was the kurdish part.
-Added events for the Balaiada and Cabanagem revolts for Brazil. Added descriptions, images and changed a few things. Kudos to ozyhuboi from moddb for the initial (and most) of the code for this.
-Substate nations shouldn't get the "vassal nation" triggered modifier on top of the "substate" one.
-Forming the Antillean Confederation now requires Nationalism and Imperialism instead of Manifest Destiny.
-Fixed a typo in the popfiles for Lodz making jewish intellectuals pops much bigger than they should be.
-Changed LR in a few Russian provinces around Moscow and in Odessa. Reshaped Ryazan a bit.
-Stopped the January Uprising from happening to Polish primary or accepted tags.
-Added the missing events for the victory of Indian nationalists.
-Stopped the setup event for the ACW firing multiple times.
-Fixed "the alaskan dominion" event firing for North American countries.
-Fixed AI tech priority that could cause resource shortages.
-Changed substate and vassal payment intervals from 25/50 days to 40/60 days, to allow them a bit more money for investing in themselves.
-The decision to destroy Westminster will only be unavailable for British-primary countries instead of it being unavailable to the whole culture group.
-Siam can no longer get the "The Thai Border" event that is supposed to fire against them.
-When forming Malaysia you can no longer steal the provinces of civilized countries (unless they are AI) to form it. This will stop the UK from stealing provinces from Siam.
-The disappearance of natural dyes will now be related only to unemployment in the dye-producing provinces, with different possible RGOs in Asia/rest of the world. The time for the event to fire was cut in half.
-Changed province 980 - Luhansk, 715 - Lublin, 716 - Kielce, 1011 - Tula and 1026 - Perm from Cattle, Grain, Wool, Grain and Iron, respectively, to Coal. Based on History for the IB Diploma: Imperial Russia, Revolutions and the Emergence of the Soviet State 1853-1924 By Sally Waller pp96.
-Changed 1253 - Bardwan from Silk to Coal. To represent the Raniganj Coalfield. To compensate, once natural dye dies out, other previously unused dye provinces in India will produce silk.
-Communist rebels will behave more similarly to fascist rebels in terms of spawning.
-Made the AI give more importance to the techs that give big RGO boosts.
-Changed synthetic dye factories from cheap factories to normal ones and made them strategic factories.
-Fixed a few mistakes in pop promotion to capitalists. Made so that it's easier for the middle-class to promote to capitalists if they are in a state with less than 0.1% capitalists that have factories.
-To better represent the different levels of education between strata in a country, all rich and middle strata pops will start with more literacy than poor strata. The following rules apply:
	--Great Powers
		*Rich Strata (primary or accepted cultures) start with 30% more literacy than the base (average) literacy.
		*Rich Strata (non-primary non-accepted cultures in non-colonial provinces) start with 15% more literacy than the base (average) literacy.
		*Middle Strata (primary or accepted cultures) start with 10% more literacy than the base (average) literacy.
		*Middle Strata (non-primary non-accepted cultures in non-colonial provinces) start with 5% more literacy than the base (average) literacy.
	--Secondary Powers
		*Rich Strata (primary or accepted cultures) start with 20% more literacy than the base (average) literacy.
		*Rich Strata (non-primary non-accepted cultures in non-colonial provinces) start with 10% more literacy than the base (average) literacy.
		*Middle Strata (primary or accepted cultures) start with 5% more literacy than the base (average) literacy.
		*Middle Strata (non-primary non-accepted cultures in non-colonial provinces) start with 2% more literacy than the base (average) literacy.
	--Civilized Countries
		*Rich Strata (primary or accepted cultures) start with 10% more literacy than the base (average) literacy.
		*Rich Strata (non-primary non-accepted cultures in non-colonial provinces) start with 5% more literacy than the base (average) literacy.
		*Middle Strata (primary or accepted cultures) start with 2% more literacy than the base (average) literacy.
	--Uncivilized Countries (At least 20% civilization progress)
		*Rich Strata (primary or accepted cultures OR North/South Han) start with 5% more literacy than the base (average) literacy.
The only exception to these rules are animist pops, which will never get a literacy boost, no matter the country they live in. The different levels between GP/SP/Civ/Unciv is meant to represent the average capability of the rich strata of these countries to get more quality education (or education abroad). Later on the Primitive/Unciv/Semi-civ status will reflect in other things such as CBs.
-Fixed South German literacy in Russia.
-Reduced the amount of prestige required to take the "Become Poland" decision from 45 to 20.
-Congress Poland will be treated as Poland for the purposes of unification. That means that Krakow will try to join Congress Poland if it can and they are both at peace.
-The event that starts the Scramble for Africa will now change RGOs in the Ivory Coast, Ghana and Togo. These countries had a few anachronistic RGOs removed (like coffee) from the native parts and got instead basic (grain, wool, fish, fruits, cattle) RGOs. Once the Scramble starts, to represent the shifting interests that european presence brought, these RGOs will change in the most part to cash crops/minerals in the appropriate regions, which will hopefully fill the gap for cash crops, reduce basic goods overproduction and stimulate more competition during the Scramble. Right now only 3 countries are done but in the future it will be expanded for most countries in Africa.
-Changed Tete from Grain to Precious goods, to represent the center of Ivory and Gold (and the minor gold mining) that happened. Based on "Missionary Travels and Researches in South Africa: Including a Sketch of Sixteen Years' Residence in the Interior of Africa By David Livingstone", "https://urbanlandscapesystems.files.wordpress.com/2017/02/some-draft-pages.pdf" and partially in "The Third Portuguese Empire, 1825-1975: A Study in Economic Imperialism By W. G. Clarence-Smith, pp 102"
_______________________________________________________________________________________________________________________________________
V0.3.9.1 - 13/10/2017
-Fixed one wrong target in the Italo-Turkish war that made Italy declare war on itself.
_______________________________________________________________________________________________________________________________________
V0.3.9 - 12/10/2017
-Krakow will get included in the "Restore Austrian Empire" CB instead of Austria getting a core there if they decide to annex Krakow during the Krakow Uprising.
-Fixed a mistake in the "Restore Austrian Empire" CB that was making it unusable in 99% of the cases.
-Fixed Ashanti moving their capital to Accra day one.
-Made the "Unite Turkestan" decision give cores in whole states rather than provinces individually, cleaned it up a bit.
-Removed event 49511 (Portuguese Mozambique) for Portugal. The event was replaced by an always present "Colonial Conquest" CB for any European nation that owns Mozambique, has pro-military or jingoism, has nationalism and imperialism and has less than 150 relations with a neighboring unciv country that owns any of the mozambican states. It has a 5 year truce, gives 0.5 prestige and adds a random 0.5, 1, 1.5 or 2 infamy each time it's used. It allows for the conquest of any of the Mozambican states, representing the historical claims to the area that Portugal had and that any nation that owns Mozambique inherits. The CB only becomes active once Mozambique is organized.
-Removed event 49515 - The Mozambique Company for Portugal. It only gave 2 provinces for Portugal, which is now covered by the previously mentioned CB.
-Made so the Spanish get Fernando Pó a bit more frequently.
-Removed Wine as a requirement to build artillery.
-Establishing a protectorate over Sulu now requires a province with a naval base and requires the country to own a province in Asia/Oceania. Ending the Merina Monarchy requires the nation to own a province in Africa. This is done as a way to more or less check that the countries have "naval range" to get there.
-Added a "Reparations" CB. It can be added during wars and it makes the defeated country pay reparations while the truce lasts.
-Removed Chilean cores in Bolivia and Peru. Chile will now start the War of the Confederation with a Reparations CB on Peru and Cut Down to Size CB on the Confederation itself. Increase the size of the initial Chilean flotilla based on https://es.wikipedia.org/wiki/Combate_de_la_Isla_San_Lorenzo_1837 and https://es.wikipedia.org/wiki/Guerra_contra_la_Confederaci%C3%B3n_Per%C3%BA-Boliviana
-Argentina will now wait for Chile to start the War of the Confederation before declaring war on the PBC.
-Added an event for the end of the Chilean silver rush (which is something that Chile starts with, with precious goods in two provinces, representing silver mines, that run out).
-Added a Tierra del Fuego gold rush to Punta Arenas and Río Grande around 1880. It's a temporary gold rush and the provinces will revert to wool after a certain date.
-Changed several province RGOs in a few countries so these countries can have access to the 5 basic goods: Livestock, fruits, wool, fish and grain. The full list is: Changed the goods of 2332 - Osorno from Grain to Fish and 2329 - Araucania from Grain to Wool and 2326 - Vina del Mar from Grain to Livestock. 2309 - Calama from Wool to Fish. 2429 - Fortaleza changed from Fruit to Fish. 2459 - Lajes from Fruit to Wool. 2276 - Cuiapo from Fruit to Fish. 2268 - San Felipe changed from Wood to Wool. 2266 - Calabozo from Fruit to Grain. 2275 - Angostura from Fruit to Wood. 2248 - Ibague from Livestock to Wool. 2291 - Wool to Fish. 2281 - Esmeraldas from Fruit to Grain. 2283 - Zamora from Grain to Wool.  2351 - Magdalena from Livestock to Fish. 2410 - Belem from Grain to Fish. 2292 - Trujillo from wool to grain. 2342 - San Pedro from Livestock to Wool. 2341 - Encarnacion from Livestock to Wood. 2340 - Pilar from Wood to Grian.  2345 - Paysandu from Livestock to Grain and 2347 - Melo from Livestock to Fish. 2188 - Puerto Barrios from Fruit to Wool. 2200 - Bluefields from Livestock to Fruit. 2198 - Rivas from fruit to Fish and 2194 - San Pedro Sula from Fruit to Grain. 2338 - Puerto Guarani from Timber to Fish. 2301 - Puerto Maldonado from Timber to Fruit. 1659 - Kobe from Grain to Livestock. 1639 - Okayama from Timber to Fruit. 2049 - Lourenço Marques from Grain to Fish. 2050 - Manjakazi from Grain to Cattle. 524 - Setubal from Grain to Fish. 2110 - Tsaneng from Grain to Wool. 2051 - Inhambane from Grain to Cattle.
-Diversified Taiwan's political parties economic policies a bit.
-Added 1643 - Sapporo in Japan to the Gold Mines events. It will flip the province to precious goods from 1913 onwards. It represents the Konomai gold mine. Removed Kobe from the list of gold mine events and made 1676 - Shizuoka start with precious metals, representing the Toi gold mine. Couldn't find any precious metals mine in the territory of Imperial Japan.
-Changed 2305 - Antofagasta and 2308 - Arica from Sulfur to Wool. Sulfur is only found in the area later and it's one of the reasons of the War of the Pacific. 
-Gave Chile military_staff_system and clipper_design techs, removed the inventions that come with the Post Napoleonic Though, Flintlock Rifles and Post Nelsonian Thoughts from the PBC, Peru, South Peru and Ecuador.
-Changed the PBC, Bolivia, Peru and South Peru to Equality NV. Made easier to accept native cultures for countries with the Equality NV.
-Fixed a bug with groupings that could affect the promotion of a few pop types for the player.
-Changed pop proportion in Korea so the country population make-up is more diverse. Overall reduced the number of slaves and the number of soldiers was greatly increased, allowing them to properly defend themselves.
-Economy tweaks: Changed invention impact on demand from 0.009 to 0.02. Made so Serfs have the same life needs as farmers. Slaves will be slightly less productive in farms than mines, but they are still more productive than farmers. A few RGOs in China and India were changed from the basic 5 goods to tea/tobacco.
-Increased leftover payment for pops from factories by 5%. Increased the amount of money that factories save from 2000 to 3000.
-Changed a few states ( in the Qing + substates, Russia, British India) so they have more aristocrats on states.
-Chile will try to end the PBC a bit more aggressively. If they peace out only with war reparations, they will break the truce and restart the war to free South Peru as long as they have as much score or more than the PBC and as long as Peru is fighting the PBC. If they lose the war, they won't be able to do this. Both Chile and Argentina will also not call allies anymore for the War of the Confederation.
-Removed the emigration incentive that pops had during genocide.  They still won't be stopped by CON or factories, though. Pops that are primary or accepted and are at least 51% the same ideology as the ruling party will have a lower chance of migrating.
-EXPERIMENTAL: Increased the impact on colonial maintenance that railways have from 0.1 to 1.
-EXPERIMENTAL: Accepted pops will behave as primary pops for the purposes of colonial migration. Unemployment due to province occupation will now have a  lessened effect on all migration.
-EXPERIMENTAL: In line with Barrels, aeroplanes and automobiles, producing Steamer Convoys now require machine parts. Slightly reduced production (and consequently, base profitability) of clippers.
-Internal Migration Changes: When migrating, pops will consider provinces with their cultural cores (cores where they are accepted/primary) and that have work available in the factories in a much higher regard than the ones without their cores. Previously, pops only considered if there were factories, regardless of work availability. Aristocrats, clergy, officers and bureaucrats will not consider if a state has factories or not when moving. Clerks and Capitalists give the presence of factories when moving the same importance as Craftsmen. Pops will treat overseas and non overseas provinces differently, giving preference to the later.
-Pop Migration Target Changes: Made so pops care if the country they are migrating to has them as accepted/primary culture (the bonus is 100%, vanilla values). Made so pops try to migrate to countries of their culture groups first (30% bonus if the same culture group) and made so old world culture groups treat their new world counterparts in the same way (British prefer Yankee/Anglo Canadian countries, French prefer French-Canadian, Iberian prefer Latin American cultures, Dutch prefer Boer and so on).
-Militant Socialists will now pass a level of social reforms when they break a country, except for healthcare and education reforms. To balance that out, they enforce national confusion for longer and countries lose more prestige when they win.
-Merged 1806 - Taoudenni and 2609 - Araouane, in the Mali Sahara, in a single province. 1806 is now used as Bayuda, Sudan.
-Changed province 1850 - Kazeh name to Keren. The province will start under Tigray rule. The region was known as Bogos, after the main tribe (Bilen) and was under the Ethiopian governor in Hamasien (Asmara). Based on "The Cambridge History of Africa, Vol 5 pp93-94"
-Changed 912 - Baalbeck RGO from Grain to Timber and 1830 - Sennar from Grain to Cattle and 1838 - Obeid from Wool to Cattle. Based on "The Cambridge History of Africa, Vol 5 pp29"
-Fixed the optional EIC minimod, a bug made it unusable.
-Fixed the UK declaring a conquest war on non-AI Sikh Empire instead of just getting a CB to establish a protectorate.
-Changed the "Djibouti Purchase" decision to a decision that any GP/SP can take, to represent the sale of Obok that gave the french the claims on the area.
-Trade for Heligoland event shall now give Germany cores on the province and disable the Heligoland Question decision if sucessful.
-Changed 1739 - Kufra in Libya to Nuhud, Sudan. Changed province 1839 - Nuhud name to Al-Fula.
-Made so GPs AI don't care so much about N&I and R&C once all colonies have been taken, unless they have the pops to get more NFs.
-Removed key provinces from Egypt at the game start, all of them can be occupied later through decision during the Scramble for Africa and represent the modern borders that were achieved through treaties. Changed the Senussi and Darfur event for the new borders.
-Fixed being impossible to get the modern_central_bank_system_invented flag due to a missing decision/event to give it.
-Sudan will start as a Colony of Egypt and further additions to Egyptian Sudan will also be treated as colonial territories. Based on "The Cambridge History of Africa, Vol 5 pp27"
-Von Moltke's reform should now last 15 years instead of 30. Reduced the effects a bit.
-Added a decision for the Bulgarian Miracle, where the country gets a population boom and a modifier that mainly helps admin/education efficiency (+30%). Russia's Alexander Reforms use the same modifier now instead of the old, unciv modifier.
-Bulgaria/Eastern Rumelia will start the game with a small population boom.
-Added a "Greater Bulgaria" decision that adds core on Southern Macedonia, Southern Serbia and the Bulgarian parts of Thrace.
-Added a generic "Renovate Capital" decision for a all European capitals that start under 40 LR that adds 5 LR and adds the "recently built city" modifier for 5 years. The decision also includes Ankara and Edinburgh but otherwise, only modern national capitals are included. It requires some money and one tech to be taken. Changed Istanbul's LR from 35 to 40.
-Fixed yet another glitch in the rebel files. Made so militant socialists behave more like Jacobins (in that social reform desire swells their numbers like Political Reform desire swells jacobin numbers).
-Renamed Yugoslavia Conservative party from the generic "Conservative Party" to Democratic Party (Jugoslovanska demokratska stranka). The liberal party was renamed to Independent Democratic Party (Samostalna demokratska stranka).
-To invite countries to Yugoslavia, Yugoslavia will need at least 150+ relations with them if they are in no one's sphere. If they are in the same sphere as Yugoslavia, a vassal of Yugoslavia or if they are in Yugoslavia's sphere, the relation requirements is not needed.
-Completely redid the Russian starting units. Now their soldiers won't start tied to pops that have almost no soldiers. Fixed pops in a lot of Russian/Polish/Belorussian/Ukrainian/Latvian/Estonia/Lithuania states. The Russian Imperial Army proper has 300k men, with the possibility of mobilizing another 396k and of recruiting another 200k. Mostly based on stuff from http://marksrussianmilitaryhistory.info/RUSS1914.html and http://cwrs.russianwar.co.uk/cwrs-R-jbarham-chapter03.html
-Gave the United Baltic Duchies starting units. Fixed pops. Added cores through the Baltic region (including Lithuania) to stop Germans from assimilating. The cores go away (and assimilation starts) once Russia dissolves the UBD. Gave starting units to Transcaucasia and made the Guard of Finland.
-Removed Japan, Korea and Persia from the cheaper Demand Concession/Establish Protectorate CB's. They also can't be used in countries with more than 70% civilization progress or countries with the country flag post_colonial_country.
-Countries with the country flag post_colonial_country will not be inherited during the scramble for africa, even if they are uncivs.
-Changed event 4421 - Liberals Protest Harassment to require meetings and voting to happen.
-Tweaked pops in the Balkans/Ottoman empire to remove some inconsistencies (over 50% artisans in Istanbul, 16% soldiers in Greek provinces). Increased pops in a few provinces in Bulgaria, Romania and Thrace so that most provinces start with 3x RGO size. Increased soldier pops in a few places so they last longer and don't all go away.
-Granting the Diet to Finland will remove the Russification decision for Russia that integrates Finland.
-Moved the game end date to a day later to stop loading the last autosave being plastered with the Game Over message.
-Re-did terrain in the Korean peninsula. Changed the terrain of the capital to Farmlands and connected it with the rest of the other farmland provinces, made the northern mountain range and a hilly range in the eastern coast.
-Renamed Shinbutsu to Shinto.
-Reduced the LR in France (by 1 in most cases, by 2 in a few cases). Increased the LR by 2 of 2 provinces (Marseilles and Orleans). A-L and Paris are unaffected. This is done to reflect the slower pop growth in France (which is still growing a lot more than it should).
-The "War Torn" modifier will no longer reduce militancy. Instead it will reduce ruling party support. This is done to avoid the situation of the rebels losing support as they go and to add an impact on the government for the failure of defending a province, even if they win later on.
-The CSA will get two admirals with the "Bonnie Blue Flag" decision and bigger mobilization size.
-Portugal: tweaked pops in the colonies so no province RGO starts near full, tweaked pops in the mainland so Lisbon isn't over 50% artisans and so more provinces have bigger RGO sizes.
-Caribbean and Central America: tweaked pops in Belize so it has officers and aristocracy and fixed the pop proportion in Jamaica (according to the used 1834 census). Made Jamaica the state capital. Tweaked aristocrats in the rest of the Dutch/English Caribbean.
-South Africa: Tweaked pops in the  Cape Colony so there's almost always a right pop type. That meant there's actually boer soldiers and protestant xhosa soldiers lying around, and a few more aristocrats.
-Renamed province 2582 - Kotor to Cattaro, how the city was known back then. The name can be changed back to Kotor with the decision to Organize the montenegrin borders, which also removes Bosniak and Croatian cores on Montenegro. Added aristocrat pops and north italian pops there. Based on https://en.wikipedia.org/wiki/Kotor
-Reduce Albania's starting population by 36% (from 823, which is around 36% less than the starting pops, totaling 520k people at the start). Based on the accumulated per annum growth from 1923 (first census in Albania) to 1836.
-Made so that Serbia, Greek lands under the Ottomans and Wallachia/Moldavia start with population booms. They have different durations.
-Changed the Tobacco protest event chain so the events are triggered by each other instead by flags, made so militancy/CON/ideology/pop amount changes only affect the Shiite Persians. Removed references to capitalists in uncivilized Persia and replaced with aristocrats. Rewrote the events description.
-Changed the Kwa culture color so it's less bright.
-Changed how the AI fulfill Warship Commissions so the bough Ironclads should arrive in a few years instead of a few decades.
-Reduced the total effectiveness of closed borders from -1.9 to -1.5. The effectiveness is dictated by how much you spend on Administration (50% or -0.75) and on Military (50% or -0.75) spending now, and made its effectiveness cost more granular (each 10% percent spent on either gives 5% towards the total, except the first 10% that don't contribute and the last 10% that are counted twice, once after 90% and once after 99%). Changed the description of the reform to reflect the change. Increased the bureaucratic cost of the reform.
-Moved a Naval Base from Tianjin to Peking.
-The SAF dominion event should now rename provinces/states like the decisions do.
-The territory of the Central Africa Republic will now be one state instead of two.
-For the sake of improving the realism a little bit, Genocide scope (more people vs less, more places vs less) should effect infamy gain and effectiveness. The narrower the scope, the less infamy you get and the more people are killed. Changed base effectiveness for the narrowest scope from 30% to 70% to 10% to 30%. Broader scopes are even less effective. Non accepted pops will start to get militant before the event proper. Changed the event to be triggered instead of being a normal event checking for conditions. Animists, Yazidi and Jewish are exempt from the new rules due to their low numbers (the latter two) or low "tech" (animists) and will have the same rules as before. Slightly increased the time needed for organizing everything.
-The Moroccan Question decision for Spain will now give Western Sahara to them, add Moroccan cores there and change Morocco's tech school to the "development" tech school.
-After 1880 and after the Congress, the owner of Ifni can claim Western Sahara if it's still empty. 
-To avoid "Sand colonies", that is, the situation of a GP/SP getting Western Sahara and creating a snake over the saharan territories of Chad, Mali, Mauritania, Niger and Chad, these regions will now be colonized via a decision that you get if you own certain core provinces in a neighboring state (Shingit for Mauritania, Timbuktu for Mali, Maradi for Niger and N'Djamena for Chad). Colonizing these places net 1 prestige besides the territory, and it's meant to represent the various border treaties that established borders in the sahara.
-Both Swaziland and Basotho can ask protection from the owner of the Cape Colony if they are in good enough relations with them and a neighboring civ is threatening to them, and it's after 1860 for Basotho or the Scramble for Africa started for the Swazi. That will make those countries adopt the Cape Colony owner's religion, fall under their sphere, become vassals and abolish slavery (if the cape owner abolished slavery), but they won't be inherited during the scramble.
-Reverted some inventions/techs to be more in line with vanilla/NNM. This means colonization inventions will be unlocked a bit later. Added back the NNM "existing country" flags to stop countries from being released with advanced inventions. The system was adapted so it doesn't require an event but it's tied in the AI-taken "cleanup" system.
-Separated the good "precious_metal" from "precious_goods". precious_metal was renamed to "Precious Metals" and is meant to represent silver, gold and any other precious (or extremely lucrative) metals. The new "Precious Goods" good represent Pearls, Diamonds and particularly lucrative markets (the Suez/Kiel Canal tolls, Hong Kong/Macao, Zanzibar (during the slave trade era)) that can't be represented otherwise. Precious Goods have a lower price than metals (7, while metals is 8) but with tech they can be worth way more with techs. The techs that deals with precious_goods profitability are the last 3 trees of the Commerce Techs. This way we can avoid industry/metallurgy tech affecting precious goods profitability (it was affecting profitability in certain places where it didn't make sense) and makes some commerce techs a bit more useful.
-Removed the Rangaku and Sakoku events and integrated their effects in the "setup" decision, so the events aren't spammed 8 times for Japanese countries. Made so Rangaku doesn't give more prestige than being a GP gives.
-Changed the Unciv Reforms that give RP on conquest so they are not all tied to land reforms, now they are tied to their Naval equivalents.
-The Unciv AI will now go for new units (Artillery/Infantry) before going for Forts/Naval Bases/New Ships. After they got all these techs, they can get the secondary Forts/Naval Bases/New Ships then they go for unit-bonus techs.
-Removed "Steamers Researched" as a factor for inventions under "Steamers". Since you need this research for the inventions to be enabled, these factors were completely redundant. Did the same thing for the Clippers techs/inventions. Changed them for techs under the Industry part of research.
-Isolationism won't bring a global MIL/CON reduction, it will work only for core pops now.
-Changed the "Naval Supplies" unciv reform so it's more useful. Now it gives clippers and steamers tech, allowing an unciv to build steam transports and commerce raiders (but excluding them from building factories, meaning all the material needs to be imported). Changed techs and inventions accordingly so uncivs don't end up with factories. Increased the cost of the tech a bit.
-Reshaped 1480 - Jinzhou and 1479 - Mukden to follow the river borders.
-AI USA will now take the Treaty of Guadalupe Hidalgo immediately and pay back the 100000£ in installments. Adapted a few other decisions to use that system too.
-Changed the impact on industry score from investment from 0.005 to 0.001.
-Made the AI invest more money in the navy during peace time.
-Made Army, Navy and Construction spending minimum to be at least 5%, mainly to help the AI to build (military) stuff better.
-To give the player a chance to fulfill warship commissions, the AI will only fulfill them after june. Fulfilling a commission leaves a country unable to fulfill another one for 3 years instead of 2.
-Changed so the ottomans start with Malthusian thought and basic chemistry but don't start with military-industrial complex or Mechanical Production anymore. Increased the tax efficiency from the ottoman_oppression modifier from 5% to 15%.
-Wallachia and Molvadia will now start as puppets rather than substates of the OT.
-Stopped NNM event 19015 from being spammed because it wasn't checking for puppets properly.
-The AI will care much less about these tech trees while under 40% literacy. Industry: Mechanization, Metallurgy, Power and partially (the latter ones) in Infrastructure and Chemistry and Electricity. Culture: Psychology. Commerce: All trees except the first two.
-Made the AI consider naval techs and army techs in a better way. Removed money as a modifier factor for them getting a naval tech or not. Made it so the AI will consider puppets, spherelings and other GPs in the same continent when deciding if they go for an army tech or not. Made the AI try to leave the age of sail more aggressively.
-Stopped rebels that are majority liberal defaulting to Anarcho-liberals when they are in power and have everything they want.
-Increased SPAM_PENALTY from 10 to 20, hopefully it will stop the AI spamming a few options.
-The OT will still inherit Hedjaz if they enforce the make puppet CB on Egypt but choose to not rule them directly.
-Made so Finland starts with the same techs as Russia. Adjusted Swedish pops in Finland starting literacy. Made so they lose Swedish as accepted either when Sweden abandons them or when the Diet of Finland event happens for Russia.
-Split the Kiev state in 2 and reshaped Rovne/Kovel/Korosten/Mozyr/Slutsk/Pinsk/Proskorov/Zhitomir to better follow the river borders.
-Added cores for RUS, changed the primary culture to Georgian. Abkhazia will try to be integrated there and if RUS doesn't exist, it will go to Russia instead.
-Substates won't be able to take loans anymore, and they will have modifiers to try and get more money from their pops (and they will spend less with themselves overall). Vassals and Substates now contribute to their overlord treasury (every 25 days for substates, every 50 days for vassal). The amount they contribute each cycle depends on how many pops they have but it ranges from 500£ to 2500£. These rules apply to the player as well as the AI, and the money will be taken out of the player automatically by the AI. Hannover, in the condition of a PU, will won't pay anything to the UK. The player can turn off vassals paying money (for them), the AI will never do it.
-RGS will start unable to get any loans. As an unrecognized small state, they shouldn't be able to and this will stop them going bankrupt the first 2 years of the game and defaulting on a bunch of countries.
-Russia can react more aggressively to the annexation of Moldavia/Wallachia.
-Russia can annex Tannu Tuva if it's still a vassal of the Qing/China but the Qing/China is not a GP. Russia needs mass politics for this. China will get a CB on them for this.
-Moved 1488 - Jiayugan from Gansu to Inner Mongolia region.
-Basque/Catalonia/Scotland/RGS can remove the cores of their former masters (Spain/UK) if they are a GP and disarm them with a generic decision. These are the ones I can think of right now, I will analyze any future suggestion on a case-by-case basis.
-Any country with over 50M pops will automatically remove itself from the SoI of a GP, to respect the game rules over sphereing that were being broken a few times.
-Fixed Native pops in Peru. Reshaped several provinces to follow the terrain better. Changed Huancavelica and Huanuco to silver mines, instead of Lima getting a precious metal mine. These regions were the biggest producers of silver during the era, representing Cerro de Pasco and Casapalca/Morococha. Based on "The Bewitchment of Silver: The Social Economy of Mining in Nineteenth-Century Peru" by Jose R. Deustua, pp 22 and pp 27. Changed Puno from Wool to Iron, as it was one of the biggest copper-producing centers of Peru. Based on the same book, pp 45.
-Ecuador and Colombia will start with a truce over a war that happened in 1832 over Cauca. Ecuador will stat with high WE because of that and no money.
-Costa Rica will now start as a dictatorship, as it was one under Braulio Carrillo Colina. Nicaragua will start as one too. Although technically in the "directorate period" that had some "democratic process" in it, it was essentially a period of caudillos couping caudillos and military rule. Fixed reforms of central american nations (some where dictatorships starting with free press, most started with trade unions reforms). Made so the FRCA, Colombia, Venezuela, Brazil and Chile start with harassment instead of non-secret ballots/gerrymandering. These governments were characterized by authoritarianism or caudillismo, this change is made to reflect that.
-When inheriting Hedjaz after the Oriental Crisis, the Ottomans will now get cores on the land.
-Added events for the War of the Pacific and for the Treaties between Chila and Bolivia/Peru, removing cores and setting up relations.
-Tweaked RGOs in Denmark and France. France should have a wool-producing province in the Alps and Denmark will have the only fruit-producing province in Scandinavia.
-Changed the Sound Toll from a triggered modifier that gave some tariff efficiency (most of the cases it wasn't useful for Denmark since they got sphered) and changed it to a precious goods RGO in Copenhagen. Added decisions and events for the Copenhagen Convention of 1857 for abolishing the toll, where the owner of Copenhagen gets a lump-sum payment of 300000£ if they accept. If they don't, the Toll can be abolished when the Kiel Canal is built or by force if someone enforces cut down to size on the Copenhagen owner. Scandinavian countries, Russia, Northern Germany, Netherlands, Belgium and France get a triggered modifier reducing their tariffs and increasing their import cost while the Toll is active.
-Ironclads can be built on Level 2 naval bases (Monitors require a level 3 naval base and are the capital ships of this naval base level. Kinda of a stopgap measure while I don't deal more properly with balancing units better).
-Reworked Danish pops so no province goes over 5% soldiers. Re-did their OOB a bit.
-Fixed a few bugs with varied events.
-Removed the tweaked units from the mod. They were a source of a serious problem with the AI. They will return later once I understand the problem a bit better.
-The US will start with a steamer shipyard to help dealing with early game shortages and avoid the UK owning all production. Reduced the level of the Steamer in Glasgow and gave a Level 1 Steamer in London to the UK.
-Changed the "Ship Construction" tree name to "Construction and Propulsion". Changed Steamers to "Paddle Steamers" and "Iron Steamers" to "Screw-propelled Steamers". Made the later unlock in 1855, as by 1862 (and 1861 during the ACW) Ironclads were already being built in Europe (and the tech unlocked in 1860, making that almost impossible).
-Changed Schleswig-Holstein starting army from irregular to infantry units. The AI disbanded the army immediately to build infantry, so it was fairly pointless.
-The AI will now pay Alaska in installments instead of bankrupting themselves.
-Ramped up the costs of building the canals, buying the Caprivi Strip, building the Eiffel Tower and the Renovation of Westminster. The prices were artificially low so the AI could compete but now that's not necessary anymore. Stopped a bug that was impeding the AI from seizing the canals. In the future, these decisions (related to construction) might require goods to be built, but we are not there yet. The overall trend now is to adapt the events/decisions where a lot of money is involved to stop the AI bankrupting themselves/being too cheapt so they can take it, now that the AI can make payments in installments.
-The minimum before damage for ships now is 10% spending instead of the old 25%.
-Reworked the January Uprising event chain for Poland to be dynamic: it will happen for the owner of Warsaw, regardless of the tag, and will depend on other factors such as how pissed are the poles, War Exhaustion as well as the old factors (recently losing a war, the crimean war for Russia). Reworked how the GPs respond to it: allies of the nation that controlled warsaw will be more inclined to stay neutral or support them while nations that them will support the Poles. Nations with provinces that are polish majority will usually try to stay neutral. Relations are the deciding factors on who they support. When deciding to support, Congress Poland will get 20000£ and 10 of canned food, artillery, small arms and ammunition. These will be in the debt form (meaning the AI will pay automatically it as they get the money/goods for it) and the same rules apply for the player (he doesn't need to pay anything in the exact moment but the AI will take it from them as they have goods available). This is made so no goods just pop out of thin air and everything is always bought. If Congress Poland wins the war in a 8-year time frame, they can "declare independence" which will remove Russia cores on the land and stop Russia from using the decision to get cores there (unless they are Fascist/Communist, in which case they will always try to get Poland back). As a rebel nation, Congress Poland depends on GP support for money as they will start unable to borrow money from the international community (sometimes that goes away naturally after 10 years or once Congress Poland uses the decision after they win the war).
-Highly unstable countries (FRCA, Uruguay, Ecuador, Haiti) will now start unable to borrow money from the international markets (usually for 10 years, sometimes less) in the game start. This is meant to represent the unwillingness to invest in high-risk countries that while will now disappear like rebellious countries, will probably default on the first 2-5 years of the game. This is done so countries have more money to lend once these countries can borrow money later and to stop countries losing money in 1838 because Ecuador went bankrupt.
-Changed 312 - Drammen from Grain to Precious Metal, to represent the Kongsberg Silver Mines.
-Added a decision for Norway to rename their capital to Oslo.
-Fixed a serious bug that was making the AI less likely to build forts.
-To avoid a lot of issues with the AI screwing the Mexican-American War and to be more in line with the rest of the decisions, the Greater Texas decision will require N&I or Texas to be a GP/SP.
-Instead of gaining prestige for giving up their cores in Belgium (and they got more prestige than the UK out of it), the Netherlands will instead lose infamy.
-AI Netherlands will prestige spam less when conquering Indonesia.
-The UK will start with slightly better relations with Portugal and Prussia will start friendly with Belgium.
-When Romania forms, the Transylvanian cores on Serbia will be gone and the population will start assimilating.
-Manifest Destiny decision for the US will require Idealism instead of Romanticism.
-The Congress of Berlin will cede both Novi Pazar and Pljevlja to Bosnia but when someone (usually Austria) annexes Bosnia, both provinces will be given back to Turkey like it happened historically. The exception to this rule is if the one annexing bosnia has a core on the province or if any core on the province is of the one annexing Bosnia, so Yugoslavia or Serbia won't give cored territory or territory that it sees as core.
-Temporarily removed a instance of is_accepted_culture that was potentially causing problems with assimilation.
-Minor economy changes.
-Further divided the Free Trade/Protectionism Trade Policy, but did so through a decision rather than new policies (to avoid diluting pop issues so much and to avoid pops preoccupied with specifics of foreign trade). The decision is completely optional and can be disabled by firing it once and selecting the "never bother me again with this" option in the event that it fires. For those that use it, it imposes minimum (or maximum) tariffs so a protectionist party will try to impose tariffs instead of sitting at 0% tariffs and free trade parties will try to limit the amount of tariffs (and one of the modifiers tied to the options will be max 0% tariffs, so complete free trade). In return, the modifiers that change the base levels of protectionism/free trade can give tariff efficiency, admin efficiency and small bonuses to industry/commerce research, though the last level can also have setbacks. The decision is mainly intended to simulate the protectionist policies of Russia, Ottoman Empire and Austria as well as the "American System". It also helps the AI to accumulate capital. The AI will always choose a policy (and "vanilla status" is a policy) and it will chose based on its current situation. More agrarian and poor countries will tend to go for protectionism while highly industrialized or rich societies like the UK will swing to free trade or vanilla policy, if they can. Spherelings/vassals will usually follow their leader policy if they can, so countries will form protectionist/free trade blocs. The US and a few countries usually try to go protectionism when they can. This of course is all tied to party policy: a free-trade party can't enact protectionist policies and when an election ends and the trade policy changes, the old policy is removed automatically. Protectionist countries under a free-trade overlord/sphere owner will try to go neutral, same thing for free trade under protectionism. The policies last for 10 years, if there's no party change. This is necessary mostly for the AI, as it always sit with 0% tariffs and would rather go bankrupt than use it while countries like the US and Russia used protectionist tariffs. Right now the AI is saving money better and they can still go "vanilla" if they decide to. The system is optional to the player but it has the same advantages for the player that the AI has with it.
-Rewrote the Jefferson Method reform description so it explains a bit better what it does (or should do).
-Integrated the Druze minimod by anon. Kudos and credit to the creator. Changelog: https://pastebin.com/X0hHQzFy
-Integrated the Battle Plans mod. Kudos and credit to the creator. Fixed the name of "Texas Blue" color not displaying properly. Original hosting place: https://pastebin.com/Du7SmxfG
_______________________________________________________________________________________________________________________________________
V0.3.8.4 - 05/09/2017
-Removed the life rating and emigration push effects from the genocide modifier, but doubled the malus to immigrant attraction. Made the preparations_to_kill modifier kill immigrant attraction.
-Made easier for Bolivia and Peru to take the Native Protection Act. Changed the tech requirement for it.
-Fixed several problems with group modifiers in the pop_types file that were assimilating pops that shouldn't assimilate.
-Halved the prestige factor of dismantling forts/naval bases.
_______________________________________________________________________________________________________________________________________
V0.3.8.3 - 04/09/2017
-In order to avoid potential issues when checking religion, all countries have a flag to discriminate their religion. Adapted events/decisions that checked for religion to use the new system.
-Changes to genocide: Made pops prefer external emigration during genocide. Made so that any factor that might hamper a pop leaving a country will be null during a genocide. Primary/accepted-culture pops will lose a huge chunk of militancy during a genocide as long as at 70% of the pop is of the same ideology of the ruling party or a smaller chunk scaled to the proportion of the pop that is the same as the ruling party. Made so militancy/CON is given/reduced more reasonably depending on the party controlling the UH. The focus on killings will make closed borders operate at minimum efficiency during genocides.
-Fixed assimilation in the new world being too slow due to an old leftover modifier.
-Restored vanilla values for literacy's influence on craftsmen promotion.
______________________________________________________________________________________________________________________________________
V0.3.8.2 - 03/09/2017
-Stopped the "reorganize Benin" and the "Integrate Lithuania in the Baltic States" decisions from not disappearing after being taken.
______________________________________________________________________________________________________________________________________
V0.3.8.1 - 03/09/2017
-Renamed "Canned Food Factory" to Cannery.
-Changed Bali from Animist to Hindu.
-Added a 5-days delay for one of the events regarding Transvaal/Matabele to avoid potential crashes.
-Fixed Greece having Armenian as accepted.
-Added AFPG's missing Samoa flags. Kudos to AFPG for the flags.
-Stopped Western Sahara getting Moroccan cores as soon as the Berlin Conference happened.
______________________________________________________________________________________________________________________________________
V0.3.8 - 01/09/2017
-EIC minimod and INNNM minimods are basically integrated as optional minimods in the decision menu at the game start.
-Kudos for AFPG for flags for Vanuatu, Samoa, Zimbabwe, Comoros and Uganda!
-Changed the SSNP religious policy to secularism and citizenship_policy to full citizenship. Changed the Kurdish fascist party to secularized.
-Fixed a bug in event 9406 that would stop it from firing. Thanks anon!
-Corrected being able to build railways in deserts again. That was a mistake.
-Uniting Turkestan shouldn't give cores in Afghanistan anymore.
-Renamed "Liquor" to "Beverages" and "Liquor Distillery" to "Bottling works". The good represents soft and 'hard' drinks. Removed Muslim-countries restrictions on it.
-Made the "Turkish Tea" decision only add tea RGO to the black sea coast.
-Fixed Kamchatka having cores on Buryatia.
-Made sure that Sicily, Sardinia and Romagna lose cores if you use the "Avanti Italia" decision.
-Turkey won't get Azeri as accepted when using the "Greater Turkey" decision. The Fascist party of Turkey now has limited citizenship instead of residency as a policy.
-Changed Sitka's LR to 35 so Alaska can get immigrants.
-Made the initial wars for the UK, Russia and the Ottoman Empire to start with a "Status Quo" CB for the other side.
-Made the events for Alaska, New Zealand, Australia, South Africa and Newfoundland where the countries ask for independence not be exclusive to the UK. It will happen to any country that own these places.
-Made events dealing with New Zealand dynamic, so they don't happen exclusively to the UK but to anyone who owns Auckland. Made localization more generic with variables for possible countries that own the place.
-Added Pontus as a non-releasable vassal to Sinop, Giresun and Trabzon, so greek pops don't assimilate. The tag will be used later in GW dismantlements. Cores go away with population exchanges.
-Added orthodox and protestant equivalent pops in Alaska, so conversion can happen with the lowest chance of bugs.
-Renamed "Cattle" to "Livestock" and "Precious Metal" to "Precious Goods" to be more in line with the stuff it represents in game. Fixed a few localization issues in HPM/Vanilla stuff.
-Jacobins will now check if a country has Free Press, Allowed Meetings, Abolished Slavery and Serfdom, if the borders are closed and if the UH Composition is not "Appointed" or "Ruling Party Only" when deciding not to spawn.
-Jacobins should now open borders and shouldn't roll back the last level of trade unions when they win. They will also change the Upper House Composition to Proportional Representation, except in the US.
-Instead of a country getting 50 War Exhaustion when Rebels win, now a country will get 2.5 WE for each province rebels occupy. Except for Nationalist rebels.
-Socialists won't rise if they have the same reforms the Jacobins need to stop rising PLUS the last two of every social reform and All Trade Unions except Health Care, Education and Penal System. They also demand the abolition of child labor
-Jacobins and Militant socialists will not rise if they are the ruling party and the basic political and/or social reforms they demand are passed. However, if they are not the ruling party and but their demands are met, they will suffer a reduced change to spawn. That means they will try to participate in the democratic process more.
-Fixed a bug with rebels that made them glitch and appear when they shouldn't. Reworked the rebel files so it's more in line with Vanilla than NNM/PDM. Removed Uruguayan-specific rebels and integrated them in the jacobin/reactionary rebels.
-Successful Rebellions should now remove 25% of the loser's prestige (up from the previous 20%) and 30% if it's a nationalist rebellion. They will also remove -25 Plurality from the country (with Jacobins/Socialists removing -10).
-Accepted pops of a non-existing tag will now behave as primary culture pops for rebel purposes. What this means is, they will not join ideological rebels if they can join nationalistic or patriotic/separatist rebels, making independence-seeking rebels much more dangerous.
-Made so Slaves can't join Ideological rebels. They still can join nationalistic rebels though. In the future a new rebel type will be added for slaves, for the abolition of slavery.
-Fixed a bug that would allow infinite prestige by releasing and integrating the Sulu.
-Changed 1162 - Bahrain from Grain to Fruit, 1165 - Doha from Grain to Fish, 1167 - from Grain to Fruit and 2664 - Khasab from grain to Fish. To better represent the RGOs there (fruits being Date). Changed the "Trade City" decision and modifier to "Pearl Hunting", which will change the RGOs from these provinces from their original ones to "Precious Goods" from 3 to 6 months during summer. After that, the RGOs will be reverted. The whole process will be automatic and taken by the AI, so a player will only see the results.
-Changed Dubai from Grain to Fruits.
-"Gateway to a new Land" modifier in Valparaiso will now last 10 years instead of 30.
-Bahrain and Qatar will start in the Ottoman sphere.
-Changed a the decisions for claiming Togo and Namibia so the AI has an easier time doing them. Changed the Congo decision so the Swedes don't always end with the place (there's a much bigger chance of not going to anyone now) and so reading the decision requirements is easier.
-Stopped the Faroe tag from starting with a non existing party in power.
-Removed Prestige of the starting Persian generals.
-Fixed an event having a duplicate ID.
-Added an Equatorial Guinea tag to stop native pops there assimilating. Re-did pops and ownership based on http://www.njas.helsinki.fi/pdf-files/vol22num1-2/moreno.pdf The Fang won't start in the island anymore (moved there in the middle from the 20th century onwards), the island will now produce fruit instead of wool (they were big cacao producers) and both the island and the land will start with some igbo pops. The Spanish won't start owning the land and instead will have event/decision to colonize each place separately.
-Changed the way overseas assimilation works: cores in overseas provinces will now stop the assimilation of both accepted and primary cultures of that core.
-The UK shouldn't start with trinket health care anymore.
-Removed the micro "Wayuu" culture from Colombia/Venezuela. They are Amazonian now. Removed Tarascan and Zapotec and they are all grouped together with Nahua, that was renamed to "Mesoamerican Indian".
-Added a Kreol culture for the islands in Africa.
-Fixed the Golden Stool event.
-Moved all "AI Cleanup" events to decisions to improve performance, made them a bit better and fixed a bug in one.
-Added the "Bulgarian Exarchate" decision for the Ottoman Empire. Thanks anon!
-Fixed the rebel icons being misaligned.
-Fixed a few instances of decisions to integrate tags that were being fired by the AI against the player when it shouldn't.
-Fixed the Navy OOB of Greece of be more in line with https://en.wikipedia.org/wiki/History_of_the_Hellenic_Navy#The_Royal_Hellenic_Navy_of_King_Otto
-Fixed releasing vassals giving prestige instead of taking it.
-Added a tag for Comoros and the flags for it and Turkmeneli and Equatorial Guinea. Kudos to AFPG for the flags.
-Fixed the rotation of the port in Bristol which was stopping the port from appearing.
-Fixed a bug that was stopping Malaysia from being formed.
-Made the AI prioritize "Revolution and Counterrevolution" more so they can get "The Dark Continent" invention more consistently sooner.
-Fixed the gateway_to_harbor modifier for Tokyo lasting forever (like it was in NNM) with one event option for the "A new Capital in the East?" event.
-Made so the Emigration NF can always be used by Communist/Fascist Dictatorships.
-Armament Inventions of the Light Armament tree are now sequential. Meaning that you can only discover "Breech-loaded Armament" if you discovered "Muzzle-loaded Armament" first.
-Added the option to "Disable Bankruptcy Events" (for the player only, the AI will still get it) in the Options decisions.
-Alaska should become the primary culture of the owner once its sold, as long as the buyer is a new world culture. If Alaska is sold to the British, the culture will be Anglo-Canadian. If it's sold to Japan or if it remains on Russian hands, it will keep on being "Alaskan".
-Removed the "african minor" and "North Caucasian Minor" cultures. The Abkhazians will be represented together with the Circassians but they are Orthodox. See https://en.wikipedia.org/wiki/Circassians (The term "Circassian" sometimes includes the Abkhaz and Abaza people since they are originally related to the Adyghe)
-You will also need fruits for producing beverages.
-Fixed a few old references to Saito in the files.
-Increased the population of Korea from around 9 million to around 16 million. Based on Korean History in Maps, pp 99. To compensate for that change and reflect Korea's growth, their LR was changed from 35 to 31. Kudos to anon for this.
-The Netherlands will now lose flemish as accepted when they sign the Treaty of London.
-Reduced the population of the Netherlands proper to around  ~2700000 people, based on estimates derived from "European Historical Statistics, 1750-1970 by B. R. Mitchell". The population of Limburg was increased to 317200 (79.3k pops, previously they had 41.5k pops) based on the same source. Kudos to anon for this.
-Changed the Romanian party names based on https://pastebin.com/jcwPKwLR
-Fixed the capital of Tanzania so it starts in Dar es Salaam. Fixed a few province names, made a few name changes for when the place is colonized. Fixed accepted pops for it and for all African post-colonial nations, and re-did their parties from something generic (and sometimes outright wrong) to more historical names.
-Re-did the way the "Claim" or "Reorganize" colonies decision work. Now they will try to clean native tags core and add historical cores if you own the land. Added a decision to reorganize Buganda, Botswana, Burkina Faso and Ghana. Those were missing. To organize the Niger now you actually need a province in the Niger river rather than a province in the middle of the desert.
-Added tags for Vanuatu, Papua New Guinea and Samoa. In most cases they extend to more land that they occupy in modern times. They are mostly to stop integration.
-Changed Kyrgyzstan's color so it isn't the same as Kokand.
-Puerto Rico and Dominican Republic shouldn't accept their african diaspora cultures at the start, or spanish, anymore.
-Added a decision to form the Antillean Confederation if you have Puerto Rico, Cuba and the Dominican Republic and have Caribeno as primary culture. An irredentist decision lets the confederation claim the rest of the (non-Spanish) Caribbean.
-Uniting with Greece as Cyprus should no longer give Greece turkish as accepted.
-Removed the naval base from Bahia Blanca in Argentina that was messing with the ability tow upgrade the base in Buenos Aires.
-To avoid the "Endless Crisis" bug introduced by patch 3.04, vassal nations will be immune to tension.
-Rhodesia isn't a releasable country anymore. It's only releasable by decision for the UK. The default colonial tag for the place is Zimbabwe. Transvaal, Oranje and Natalia aren't releasable either, since that would mean natives releasing them as uncivs. But you can play as them as you normally would through events that fire to the UK.
-Trucial States will now start as Sunni.
-Parties with pro_atheism religious policy will now deactivate the "islamic country" modifier, but they won't secularize the society.
-Removed the "native protection act" and integrated it into the new Native Policy system, where one can either accept them, assimilate or try to exterminate them.
-Belize no longer accepts British and Afro-caribbean.
-Yucatan was changed from Mexican to Maya primary. They will now only petition to join the FRCA if the FRCA enacted the Native Protection Act, have at least culture voting rights and have more than 50 relations with them.
-Eastern, Central and South Africa Changes:
	-Kenya: Kikuyu culture in Kenya was renamed Kikuyu–Kamba (Kamba and Kikuyu are Bantu from the same family) and it was expanded across the provinces occupied by the Kamba, the Meru and the Embu. The culture represents these people. Oromo in Kenya (representing the Borana Oromo) were changed to Coptic and moved from Garissa to the Ethiopian border. Maasai was renamed to Kalenjin-Maasai and they now extend through all of the Rift Valley Province. 
	-Added a Nilotic Culture, a Cushitic Culture and a Northeast Bantu Culture (Guthrie J) to represent the people from these areas. "African Minors" in the Cushitic Area (Ethiopia, Somalia and parts of Kenya) were changed to this culture. African Minors in Sudan, Kenya and Uganda were changed to Nilotic.
	-Tanzania: Added the Kilombero Culture (Guthrie G). It extends to Comoros, Zanzibar and much of central Tanzania. Reshaped province 2046 - Ujiji and 2045 - Morogoro so their shape follow the existing rivers.
	-Mozambique: Reshaped Tete, Sena, Quelimane, Sofala, Inkomati, Manjakazi, Inhambane and Massekisse to follow river borders (and more historical province borders). Added a Nyasa culture (Guthrie N) that goes over Mozambique, Southern Tanzania and Zambia. 3 of 4 Mozambique States were reshaped to accommodate the changes. Changed a good part of the Yao people from Animists to Sunni. Yao was renamed to Yao-Makonde with the Makonde being the animists in the provinces.
	-Southern Africa: Added a 'Southern Bantu' culture, correspondent to Guthrie S.
	-Angola/Namibia: Moçamades now starts with a Herero majority and a Khoisan minority (https://upload.wikimedia.org/wikipedia/commons/7/71/Angola_Ethnic_map_1970.svg ) Added a Kavango-Kimbundu Culture to Angola, Northern Namibia and Congo that represents Guthrie's Group H, R and K.
	-Added a Adamawa-Ubangi Culture to represent the main pops of the Central Africa Republic and surrounding region. Added a few Fulbe there. The culture is also spread to South Sudan, Cameron, the two Congos and Chad.
	-Added a Northwest Bantu group (Guthrie's groups A to D) that go over Equatorial Guinea, Gabon, parts of Cameroon and both Congos.
	-Added a Central Bantu group (Guthrie's groups L and M) that go over South DRC and Zambia.
	-Reshaped Douala province in Cameroon to follow the river border.
	-Renamed the small Tiv group to Bantoid, which is a culture that spawns what used to be Tiv in Nigeria and the Bantoid languages of the Cameroonian Plateau, including the Tikar. They will be muslim in Bafoussam to represent the Bamum.
	-Renamed the Teda to Toubou. They represent a range of peoples in Chad, Libya, Niger and Sudan (Darfur). They will represent the "african minor" in these places.
	-African minor (slaves) in southern Chad are now represented by the Adamawa-branch of the Adamwa-Ubangi culture.
	-Renamed Sara to Sara-Baguirmi (seeing as they are from the same family and Baguirmi is almost extinct). The Baguirmi "slot" will now be used for the Maban (Biu–Mandara or Central Chadic), representing the minor and rather separatist cultures such as the Hadjarai, the Ouaddaï and other minors.
	Ethiopia: Changed the Harari (that existed in a single province and had 4 mentions) to Habesha, to represent southern semitic-ethiopic cultures (Harari, Gurage, Silt'e, Soddo). Re-did their names. Added some to Harar (since harar didn't start with any Harari, ironically) and added a Shewa core there. Removed the Sidamo (now they are represented as cushitic) and made them animist instead of sunni. Reworked pops so they follow modern distribution better (http://www.languagesgulper.com/eng/Ethmap_files/Ethiopian%20languages%20large%20map.jpg) and re-did states (Gibe state was removed), so Ethiopia is now 5 states of 4 provinces each. Re-did pops in all provinces to represent demographics and distribution better.
Western and Northern Africa:
	-Niger: Merged the african minors to the Songhai in the Outer Hausaland State (Songhai representing here the Zarma people). In Kufe they were converted to Fulbe.
	-Mauritania: African minors were changed to Wolof, Fulbe and Berber where appropriate.
	-Changed the spelling of Toucouleur to Tukulor.
	-Mali: The african minor slaves in the sahara part of Mali were replaced by Maghrebi (representing the Hassaniya). Fixed numbers of the Fulbe a bit. African minors are now mostly Mande.
	-Nigeria: Added a Kwa group (East and West Congo-Benue Groups) to represent all minor cultures Nigeria and parts of Ghana and Benin.
	-Burkina Faso, Ghana, Togo and Benin: Added a "Gur" culture representing all Gur languages, mainly centered in Burkina Faso.They also make the minorities in Northern Togo and Ghana as well as Benin. Spread the Senufo to Burkina and Mali.
	-Added Berber to Libya and Tunisia to replace the "african minor" in these places. Berber (Tamazight) is often a spoken or official language.
	-Fixed proportion of pops and religion of pops in Guinea, Liberia, Guine-Bissau, Sierra Leone and Ivory Coast. African minors will now be represented by "Western Nigritic" in these places, representing the Atlantic branch of the Atlantic–Congo language group. Changed the Liberian event to occupy the countryside in a decision.
	-Cape Verde: Took it out from the "Macaronesia" state and put it together with Guinea-Bissau in a single state. The old "lower guinea" state was used, while the other two provinces of this state (Boffa and Timbo) are now part of the "Guinea" state. Terrain is now mountains.
	-Gambia and Senegal: Fixed pops and religion, now the country won't be purely mande/african minor.
	-Total 8 more cultures compared to the previous version.
_______________________________________________________________________________________________________________________________________
V0.3.7.1 - 18/07/2017
-[Old Version]Reshaped several states in Siberia.
-[Old Version]Stop the decision for naming Lushun from being taking endlessly in certain situations.
-[Old Version]Renamed Buganda to Uganda.
-[Old Version]Stopped the "Independence for Tunisia" event from potential happening repeatedly. Now it only fires once.
-Liberia will now start with the "Developing Academia" Tech School.
-Added some missing Greek Pops to Crete.
-Fixed a wrong party name in Serbia.
-Made the Argentinian tags (SBA, ENT and CRT) non-releasable, to stop them from being released from the Argentine Confederation by war.
-Checked the Ottoman starting army and guaranteed none of the brigades start with missing pops. Reorganized the military to follow the historical organization. Based on https://en.wikipedia.org/wiki/Ottoman_military_reforms#Reforms_of_Abd.C3.BClmecit https://en.wikipedia.org/wiki/First_Army_(Ottoman_Empire)#Formations  https://en.wikipedia.org/wiki/Asakir-i_Mansure-i_Muhammediye and https://tr.wikipedia.org/wiki/A%C4%9Fa_H%C3%BCseyin_Pa%C5%9Fa
-Added Turkish pops back to northern Iraq. They should be around 3% of the total population of Iraq, distributed in Mosul, Rewanduz and Sulaymania and 3% of Syria, distributed in Aleppo and Dayr al-Zour.
-Added a Turkmeneli tag to stop Turkish pops in Iraq and Syria from assimilating if the OT falls.
-Fixed the Greater California decision cores in Sonora.
-Made sure an event for the central Americans states don't fire against a country that doesn't exist.
-54'40 or fight event changed so it can fire if the US isn't a democracy.
-Removed event 16452.
-Stopped the decision to rename dutch wallonia from firing endlessly.
-Troy/Machu Picchu province owners now can take the decision to search for the city.
-Slight increase in Austrian Italy literacy for north Italians to (hopefully) make assimilation bug harder to happen.
-Changed the way the penalty to assimilation for accepted cultures with union tags in a province so it's significantly smaller, making the tooltip for assimilation easier to read. Also made it completely generic: any culture in a province with a core of a union tag that is accepted by said union tag will now count as "primary" for assimilation purposes (aka it will not assimilate).
-Added all pop types to Macao in 1836, so pops have where to promote.
-Reshaped Guangdong a bit to fix map artifacts.
_______________________________________________________________________________________________________________________________________
V0.3.7 - 18/07/2017
-(previous version but forgot to add) Mirza modifier for Persia: RP gain effect cut in half.
-Changed province 12 - Reliance in Canada to Sado in Japan. It starts with around 25K pops, producing precious metals and under the Shogunate ownership. Numbers based on https://en.wikipedia.org/wiki/Demographic_history_of_Japan_before_the_Meiji_Restoration#Former_provinces - Thanks go to the anon who gave the source. Pops come from the Nigata province, which used to encompass the island. Added Sado as a Treaty Port.
-Fixed a few (11) stray pixel clusters, added provinces (and names) to 35 lakes in South America, Australia, Africa and Asia.
-The Tanzimat Reforms now come with a one-year modifier to represent the Ottoman Land Code of 1858.
-Added an event for the Kanpur Massacre. The event can happen in any province with high militancy and primary pops from the colonial nation in India.
-Isolationist Uncivs will not be able to subside imports. Instead, they are forced to institute minimum tariffs, with protectionist countries locked at 95% minimum and free trade countries locked at 25% minimum.
-Added 1100 south German soldier pops to Nafplion to represent the Bavarian Troops in Greece. Added a starting unit that corresponds to these pops. Based on http://www.mwme.eu/essays/bavarian-greece/Haggenmueller_Intro/index.html
-Added a new Party Policy: Welfare policy. Pops don't care about it (as in, it's not an issue they vote for) and it's tied to the party ideology. Its effects the minimum and maximum spending in the Social slider. Socialist parties will push for a full welfare state, with communist and fascist parties adopting a paternalist policy and anarcho-liberals strongly opposing spending on welfare. Liberals, Reactionaries and Conservatives are unaffected.
-Stopped province 1421 - Madura from flipping to Rubber from Sulfur.
-Made being dismantled play a bigger role in unlocking fascist ideology.
-The "Claim the Levant CB" can't be used against GPs anymore, so after a GP takes a piece of the Levant from Egypt it will stay with them unless you justify a "place in the sun CB" against them.
-Reshaped Brescia, Tuscany, Siena, Rome (and surrounding provinces) to follow more natural boundaries such as rivers and be more aesthetic overall.
-Added the Apennines that extend from north to the south to the Italian peninsula. Redid the Terrain in the Italian lands and Corsica.
-Added an Atoll terrain. In the new terrain it's impossible to build railroads and the RGO size is extremely small. Changed a few of the islands in the pacific that corresponded to this terrain. Fixed a few wrong name placements in Polynesia.
-Changed the LR of Brindsi and Messina from 35 to 40 to better represent the growth in these regions.
-Reshaped Aquila, Foggia, Perugia and Ancona to better represent the terrain of the Italian peninsula. Province 10 - Inuvik was repurposed as Pescara in Italy and the old province is now part of 2598 - Fort Liard. Pops for the new province come from Aquila.
-Renamed province 2351 - La Plata to Magdalena. Added a decision to build La Plata that will rename the province.
-Added the French Alps: Grenoble and Digne changed from forest and farms to mountains. Reshaped Valence, Grenoble, Avignon, Toulon and Frejus to better fit with the terrain. Frejus and Toulun terrain changed from Farms to hills, to represent the last bits of the Alps.
-Added the Austrian Alps: Klagenfurt, Judenburg and Sankt Pölten are now mountains.
-Sardinia now is completely hilly.
-Merged province 8 - Ross River into province 7 - Dawson. Province 8 is now Belluno in Italy. Changed Province 732 - Treviso from Iron to Timber and province 8 - Belluno from Timber to Iron.
-Fixed wrong brackets screwing the literacy setup of Italians in Austria.
-Changed LR in 827 - Zante and 843 - Chios from 30 to 35 and 32 respectively. Changed Ionian Islands literacy to be more in line with Greece, lowered plurality.
-Added a Setup for Greece, south germans will start with more literacy, Greece will start with a small baby boom for 4 years.
-Stopped Russia from being able to see the decision to integrate Lithuania in the UBD.
-Integrated 2669 - Amga in 2648 - Yakutsk. Now 2669 is Sondrio, in Italy.
-Moved the starting event about deciding if Crisis will be vanilla or not to a decision, under an umbrella of "optional" decisions. There's a few ways of tweaking the game through those decisions, but to avoid clutter, they all disappear in 1837 (and later on, in other start dates, they will disappear in a year).
-Renamed State GRE_837 from Attica to Central Greece.
-To make sure the "Sonno Joi" province event doesn't fire in case of a Tokugawa peaceful victory, now it requires any japanese-primary tag to be neighboring the country.
-Changed the name of the Australian Fascist Party.
-Using the decision to close borders requires Residency citizenship policy or a Fascist/Communist Dictatorship, meaning these governments can always take the decision.
-During the Senussi and the Algerian Rebellion, as well as the Bedr Khan Massacre, the spawned tags should be able to mobilize troops instead of being unable to fight. Senussi and Algeria should also start with Tuareg as accepted and a general. Changed a few pops to soldiers in Libya and Algeria so they can build a brigade. Fixed the Ottoman Empire getting the wrong CBs for the Senussi if they don't go immediately to war with them.
-Changed the adjective of the SGF from "German" to "South German", to keep consistency with the NGF.
-Changed Trinidad and Tobago and Trieste to Civilized status at the game start.
-Added option to Secularize society for Muslim nations. Non-secular Muslim countries cannot build Wineries or Distilleries and have the old "Islamic law" modifier as a triggered modifier. The Tanzimat Reforms secularize the Ottoman Empire.
-Renamed province 211 - Blackstone to Lynchburg.
-Fixed an issue with a decision that made the CSA capital move to province 211 - Lynchburg (old Blackstone) immediately.
-Fixed not being able to use the decision to integrate Lithuania in the UBD if the UBD owned Lithuanian cores.
-Changed Misri culture color to a darker shade of green by anon's suggestion.
-Health Care and Education reforms now give half of the bonus they used to give. The other half comes from a triggered modifier (that checks once per month) that triggers if administration/education has enough fund. The minimum amount for it to trigger is 20/30/40/50% Admin funding for Health Care and 30/40/50% Education funding for School reforms. Each reform level description has a text that tells you the minimum funding for the full bonus.
-Having the last Health Care reform and fully funding Administration will now give a bonus 0.02% for pop growth. Having the last School Reform and fully funding education will give a 0.10% bonus to education efficiency.
-Civilized nations with more than one state and more than 1 million pops have to invest a minimum in education if they don't want to lose literacy (through a triggered modifier). At 25% literacy you need to keep education spending at 10% at least. At 50% literacy you need to keep spending in 20% minimum and at 75% literacy the minimum is 30%.
-Removed old references to the "Islamic Law" modifier.
-Added a decision that turns Crete in a state for civilized powers in Europe.
-Updated the "Release Vassal" decisions.
-Added a set of decisions akin to NNM's "Release Vassal" decisions that allow you to return cores to individual countries, if they are your puppet or in your sphere. It doesn't return provinces that have your cores in them, though.
-Added a third option to the "Release Vassal" and the "Return Core" decisions to disable the decisions completely for the rest of the game. Useful if you don't plan to use them and just want to unclutter the decision tab.
-Halved all party loyalty in Switzerland, the UK and US. Now party loyalty at the game start doesn't go above 20% (previously 40%).
-When Transylvania joins (and becomes) Romania, it will lose Hungarian as accepted. Similarly when Panama joins the FRCA it will also lose North Andean as accepted.
-Added an event for the Serbian Constitution of 1838 and included Serbia in the liberal revolutions. Based on http://users.ox.ac.uk/~oaces/conference/papers/Bojan_Mitrovic.pdf
-When a country uses the decision to leave a SoI, if the GP refuses to act now it loses 10% of its prestige instead of always losing 20 prestige. 
-Changed the Krakatoa event so it's not a major event anymore. It also doesn't kill 20% of the Bogor province (at the game start that would be 148K people) and now it kills 4% (around 36K people, game start values). It will also destroy a level of railroad and fort, if any are present in the province, as well as a level of the Naval Base in Batavia and it will reduce the Life Rating in Bogor by 1. Improved the event description a bit.
-Changed the Tunguska event so it's not a major event anymore, it doesn't change LR and it only kills pops if there's more than 10k pops in the province, but it completely wipes forts and railroads from the province. Improved the description a bit.
-Changed the San Francisco Earthquake event so it's not a major event anymore. It completely wipes forts, naval bases and railroads from the province and kills 2% of the population instead of the old 10% and it costs £50,000 for the owner of San Francisco. It also has a "devastation" modifier that will severely reduce province production (and hopefully close a few factories). Improved the description a bit.
-The UK will lose Irish as accepted when the Irish Republic Brotherhood event fires, to represent the rise of Nationalism in Ireland.
-Fixed a few instances of acquire_all_cores CB that would instantly white peace, like the '54-40 or fight' event for the US.
-Vassal countries that have vassals can no longer use the decisions to free vassals.
-Fixed a potential bug that happened if Egypt released the Levantine nations before the Oriental Crisis, which would end with the GPs declaring war on Egypt but instantly peacing out. Additionally, GPs will not declare war on Egypt if they don't own any Turkish cores.
-For clarity's sake, the hidden modifiers that affected pop migration that were associated with the last 3 Voting Franchise reforms are now directly tied to the reforms (and added to the old migration bonuses of these reforms, so Universal voting gave 5% immigrant attraction, now it gives 55% (5% + 50% of the old hidden modifier). The old GP bonus to immigrant attraction was moved from the pop files to the static modifiers. Both these changes don't change a thing in relation to immigrant attraction percentage, but they will make things more clear in regards to what reforms are important to attract immigrants and will hopefully help with performance.
-Secondary Powers now have a 5% bonus to immigrant attraction.
-Changes to pop immigration behavior: Capitalists will be 50% more likely to immigrate to L-F countries and 50% less likely to immigrate to countries with planned economy. Intellectuals don't care about general unemployment anymore when deciding where to migrate, they instead care about education funding (starting at 70% funding and ending at 100%, that gives between 10% to 50% bonus to immigrant attraction of these pops, depending on education funding), since they are paid by that slider. Same thing for soldiers and officers (with the military slider). What this means is that these pops will care more about how well paid they will be, since they will only be unemployed if they demote. Less than 40% funding will mean a -25% chance for these pops to pick the country.
-Instead of giving 1% bonus to immigration attraction, the "Underground Parties" reform will instead give -1%. The Harassment reform is now Neutral to immigrant attraction and the other reforms behave as vanilla.
-Stopped a few events that could change the UH/Voting/Electoral reforms during an election from happening during an election.
-Event 4420 - Cabinet Discusses War will not longer give a conquest CB on all neighboring countries, regardless if you can use it or not. Instead, it will only fire if you have a neighboring country with more than 1 state and it will give a single CB to acquire a state in a random neighboring country with more than 1 state.
-Similar to vanilla event 60140 where Liberal/Socialist force the "Appointed" UH Reform, when Socialists/Communists(not in a proletarian dictatorship) get to the UH and Trade Unions are illegal, they will force the "State Controlled" Trade Union reform (only if the country has Revolution and Counterrevolution researched).
-British Poor Strata will be way less likely to demand a change to the First Past the Post reform. Pops overall will care much less to change from FPTP until some basic reforms such as Free Press, Voting Rights and Meeting Rights have been acquired.
-Fixed a potentially serious vanilla bug where artisans didn't actually own their production (which may help to explain why they starved so much, though it seems they still got money somehow).
-Farmers, Laborers, Craftsmen and Clerks now care about Trade Union reforms (before that, no pops cared about those reforms) and will try to push for them. Craftsmen are the ones who care the most, followed by laborers, farmers and then clerks, who care the least. Socialism, unemployment, fulfilled life/everyday needs and CON are the main factors affecting this.
-Cleaned up the poptype files a bit, corrected a few mistakes.
-Decreased invention impact on demand from 0.1 to 0.06.
-Added several Natural Disaster events, all relating to devastating earthquakes (and as a rule of thumb, for an earthquake to go in as an event, it either needs to be very destructive or cause a lot of casualties), namely the 1877 Iquique earthquake,  1868 Arica Earthquake, the 1896 Sanriku earthquake, the Great Ansei Earthquakes, the Great Neapolitan earthquake, the 1908 Messina earthquake.
-Fixed a wrong localization issue with the Enact Anaconda Plan for the CSA.
-Modified the Law of Return decision from Israel to correctly take out money instead of giving, fixing the events associated with it so it actually works how it was intended and to take into account open/closed border status, among other things. Changed the duration of the modifiers for the return of the diaspora pops from 2 to 5 years. Re-localized it so the decision can be used by Armenia too, if they want to bring back the Armenians from the diaspora. Differently from Israel, Armenia needs to be at least a SP to see the decision. The event structured was adapted from the source material a kind anon provided. The events for the law of return for Israel will also no longer increase the immigrating pops literacy.
-Correct a wrong flag for Canada.
-Added a Irredentist decision for  Israel.
-Fixed the localization in the event for German LR normalization and made it fire earlier, when Germany reaches 1895 levels of pops.
-Made the German Namibia event in a decision, added tech requirements to it.
-When a nation asks for home rule, the country that gets the request will now lose the requesting country primary culture as an accepted culture, regardless of their answer.
-Instead of being completely immune to nations asking for home rule, the tags AUS, KUK, DNB and YUG will now get the requests (it was this way in NNM) but the AI will always reject it by default, so they will deal with unrest in the nations that ask for this. Considering the change of the above item, this also means tags like YUG and DNB can slowly lose accepted cultures. To deal with this, accepted cultures have more strict requirements when asking for home rule: they need high CON and MIL (more than 6-7) in a state as well as over 50% literacy. If the culture isn't accepted, just a bit of MIL (usually 2-3) and a bit of literacy (more than 25%) is needed, which is a requirement similar to before. This means that multicultural union tags will become more brittle and vulnerable to internal dissatisfaction, so a big focus should be in keeping everyone happy (or suppressed).
-Iceland won't ask home rule from Scandinavia anymore.
-Norway should declare independence before 1900 if Sweden stops being a Monarchy or if relations dip too low and CON is high. While they declare independence they will also fight for it if they get a "no", so it won't be a simple "refuse forever" case anymore. Sweden will lose Norwegian as accepted when the event happens.
-Condensed the Falklands/Malvinas renaming decisions in one decision (instead of 2) and removed the 2 prestige you could get from it.
-Fixed a possible issue that could end with the invest_in_irish decision being taken endlessly.
-Changed event 31100 about the discovery of Troy. Previously it always gave prestige to Turkey, now it depends on a GP (or SP in Europe/Levant) taking the decision to search for the Aegean civilizations and getting lucky. Added newspaper references that existed in Vanilla but weren't included because someone forgot to add a few lines to the event files. Reworked the event and newspapers text.
-Changed event 46800 about the discovery of Machu Picchu. Previously it always gave prestige to Peru, now it depends on a GP (or SP in the Americas) taking the decision to search for the city and getting lucky. For both events, High education spending and GP status increase the likelihood of discovery. The events give the same amount of prestige and require techs from the Social Thought tree, among other requirements. They become visible in 1850 and 1890 respectively, so players should have time to prepare for them. They are only visible if you fill the other conditions: being at least rank 3, having the owner of the Cusco/Canakkale in your sphere or being a GP/SP in the Americas for Machu Picchu or in Europe/Levant for Troy. This model will be follow for similar decisions/events.
-Fixed a few typos and improved a few descriptions in the events/news files.
-Founding the Suez Canal Company now also requires the business_banks tech.
-Fixed a few party names for Ireland. The Portuguese Fascist Party name was changed from "Estado Novo" to "União Nacional". Yugoslavia's Fascists were renamed to ZBOR.
-To accommodate non fascist but highly authoritarian regimes, Presidential Dictatorships now can have a fascist party as the ruling party.
-Condensed the two decisions to rename Wallonia in a single one, made the description generic enough.
-Countries annexed through the Doctrine of Lapse and the Russian equivalent now can only be annexed once through it.
-Former colonial countries will now be released as uncivs and will have the option to civilize instantly on release (if they have 15% literacy) through a decision. If they do this, their informal status will be "semi-civilized". This means that they get a tech school that greatly reduces their research speed and can be reverted to Traditional Academia when they reach 25% literacy and have a few techs.
-The country that gets the Congo will now be left out of the free Scramble for Africa CBs.
-Lagos isn't needed anymore to form Nigeria, only one province in each of the 3 coastal states.
-Increased the effects of Autocracy/Tradition NVs on Conservative/Reactionary/Fascist/Communist ideology inclinations. Ideological inclinations from NVs will now only affect pops that are primary/accepted in a country. That means that greeks under the Ottoman Empire won't be more conservative just because they are in the Ottoman Empire. This means that in homogeneous countries with these NVs, they will gain more stability but multi-cultural countries will still be rocky by the ideology of the minorities.
-The provincia_cisplatina decision for Brazil now can be taken by an Absolute Monarchy with a Jingoist Party.
-Changed province 900 - Antakya from the Aleppo state to the Adana state.
-Checked and re-did all the pops in the Ottoman Empire in the Balkans, Anatolia and the ME. Pops were changed so minorities always have the 4 basic pop types (farmers/laborers, intellectuals, soldiers and artisans) with additional 2 (aristocrats and officers) in capitals. This is done to avoid assimilation problems, no matter who owns the land. Pops now should always have a valid target to promote to. A few places like Bosnia and Aydin were missing soldier pops, sometimes even turkish soldiers (in the case of Aydin), so that's also fixed.
-Changed the whole of Ottoman Iraqi to colonial governments. This is done to reflect that Mamluk Rule in Baghdad ended only 5 years early, when they still ruled as an unciv with high (or almost complete) autonomy. Turkish pops in Iraq were made in Kurdids pops, so Kurdish parts of Iraq have more kurds. See https://en.wikipedia.org/wiki/Ali_R%C4%B1za_Pasha_(governor_of_Baghdad) and https://en.wikipedia.org/wiki/Mamluk_dynasty_(Iraq)
-Removed Turkish pops from Aleppo. To provide some access to Iraq, Dayr al-Zour will start under Ottoman Rule. This is done until I re-do provinces in the ME.
-EXPERIMENTAL: Disabled promotion on assimilation.
-Added new terrain types for the new world, for small islands and for the tundra/desert/boreal forests. This is made so these terrains don't have a huge RGO size just because they are in the new world and places like Hawaii can have more people than any place in the old world.
-Changed the "Christian Oppression" modifier for the Ottoman Empire so it doesn't give militancy and consciousness for non accepted pops. Instead, AI countries will each year take a decision to give militancy/CON to non Sunni pops in the Ottoman Empire. Previously, any non-turkish pops would get progressively get more pissed off, including the Muslims.
-Made the starting general for Tripoli a bit better.
-Removed the CON reduction in wartime that was inherited from NNM.
-Romanians, Albanians and pops in the Levantine and South Slav culture groups will be much more inclined to join nationalist/patriotic rebels than ideological rebels if they can IF they aren't accepted cultures and have a different religion from the state religion of the country.
-The decision to Annex Bosnia after the Berlin Conference now can be taken by any GP that owns Serbia and Southern Serbia or Croatia and Slavonia or Dalmatia.
-Reduced the LR in Togo from 15 to 10, made a decision to claim the place for Europeans GPs/SPs.
-Changed the citizenship_policy of the Ottoman Empire parties a bit so they have the whole spectrum of options supported and so pops don't end up always going for the same rebels.
-Added Party names for Greece and Serbia, based on a kind anon suggestions and http://www.worldstatesmen.org/Greece.html The "French Faction" (Ethnikó Kómma) are now the liberals and the British Party (Syntagmatikó Kómma) are the conservatives. Previously, it was the other way around.
-Added better description to a few reforms.
____________________________________________________________________
V0.3.6.2 - 02/06/2017
-Province events to gain and remove cores won't work overseas, ever.
-Added missing AFPG flags.
-Battleships won't use fuel anymore but to compensate for that dreadnoughts use more fuel. Cruisers don't require fuel to build but require coal for maintenance.
-Ukraine shouldn't start with Russian and Byelorussian as accepted anymore. Ukraine, Alaska and Belarus have a decision to remove their respective primary cultures from other countries accepted cultures to avoid problems with the remove/add core events.
-Moved "The Dark Continent" invention to revolution and counterrevolution to reduce the cases of recently-released nations having it.
-France will now lose French-Canadian as accepted after the Jules Ferry laws.
-Changed 805 - Salonika RGO from tobacco to cattle.
-Added a decision to declare a "state of emergency" depending on high militancy/war. This will hopefully keep countries in war for longer, but at the end of the modifier period it will give more militancy.
-Renamed the provinces of New Ireland and New Britain to their native names, Tombara and Birara. (source: A directory for the navigation of the Pacific Ocean; with description of its coasts, islands, etc By A. G. Findlay). The common GPs/SPs that are likely to colonize the islands now have a decision to rename the islands.
-Fixed a wrong flag that made event 110086 not fire ever.
-Added AFPG's custom government flags for CAM, MLY, SIA, BRU, DAI, JAM and AZB.
-Fixed a few instances of Colonial countries not getting the post_colonial_country flag, allowing them to use decisions they shouldn't be able to.
-Added a few missing references in NNM to stop post_colonial_country forming formable nations.
-Changed Rhineland starting religion to Catholic based on their capital and changed Eupen-Malmedy north german pops from Protestant to Catholic.
-Fixed duplicate Himalayas region. The region that's Tibet will be known as "Tibetan Plateau".
-Changed the Trucial States religion from Shia to Sunni and added a few shiite persian pops in Dubai.
-Fixed Manchu numbers in Manchuria according to http://uni-koeln.de/phil-fak/ostas/moderne/papers/No%201998-1.pdf pp 23, reduced the population from 6 million to ~3.84 million or ~960k pops. Based on linear growth since 1790 based on the average growth from 1790 to 1890.
-Made sure there isn't a game over if the player wins the argentine civil war as Buenos Aires.
-Stopped the decision to reunite the PBC from accidentally integrating Chile.
-Changed Protestant Lithuanian pops in German Lithuania to Catholic. A few Protestants are still there though.
-Removed von Moltke as a general from the Ottoman Empire.
-Deactivated the Islamic Law decision, given that that's the de facto original condition of muslim societies. I will add a decision for the secularization of Islamic societies in the future.
-Removed a MISCmod event that gave a free tech to Brazil.
-During the Bedr Khan Massacre/revolt, Persia will get an event explaining and warning of the war start.
-Fix a few vanilla bugs in the poptypes files related to the condition "can_build_factory" not working. This stopped a 10% promotion chance artisans got, a -40% to craftsmen demotion and allowed farmers/labourers to move in provinces with more than 10% unemployment among other things related to pop promotion. Now to determine if a pop can build factories, the files check for party policy. The result is that planned economy will have more static classes while laissez-faire/interventionism will have more mobility (and more promotion to capitalists).
_______________________________________________________________________________________________________________________________________
V0.3.6.1 - 27/11/2016
-Fixed unit position in Vigo province.
-Corrected Kiritimati position in the map.
-Fixed event 98235 - Witwatersrand Goldrush so it gives the correct CB if the country is in someone's sphere. if it's a vassal or a GP, however, there will be no CB involved, just the relation hit.
-Tsushima will start as part of the Shogunate.
-To avoid potential problems, the Sakhalin question event won't pop up if there's an ongoing crisis in the world.
-Fixed stray pixels from other provinces in the border of Fort MacKenzie with Lobstick Lake and Jilin with Qiqihar.
-Made an Alaskan culture for Alaska to solve the problem of the old world pops in there. Changed russian pops there to Alaskan, default religion of the tag now is Orthodox, not protestant. Most stuff goes back to vanilla once the place is sold.
-A few cultural unions (Germany, Italy, India and China) will now stop assimilation of all pops in their culture groups as long as there's at least a core of the same culture group in the province.
-Removed Hanim as a surname for turkish. Made Egyptian use actual surnames instead of only Pasha and Bey.
-Stopped Nuba and Kingwana having the same color code. Made Bedouin color more green.
-Canada: Renamed a few canadian provinces. Their names change accordingly as the CNR is built. Added small amounts Anglo-Canadian pops to all provinces in Canada that start colonized and normalized native pops. Fixed missing Metis cores. Re-purposed province 29 - Medicine Hat to province Kyzyl Kum in Uzbekistan. The territory and pops are divided between provinces 24 and 25. Changed province 6 name and made it not start colonized, now colonization happens by decision with "mission to civilize" as requirement. Based on some anon tips, http://www.canadahistory.com/sections/maps/explorers/images/Fur%20trading%20posts.jpg and http://www.northamericanforts.com/Canada/
-Merged the states of Yukon and Northwest Territories in one state and North British Columbia and South British Columbia in one state.
-If A-H becomes Hungary they will no longer get south german as accepted.
-Added an irredentist decision for Romania to expand to the Tisa.
-Germ Theory 2% for the nation being a colonial nation was replaced for a 2% for GPs and SPs with at least 40% literacy and industrial score of at least 20.
-Added 6 new NFs exclusive to colonies. The first one increase the attractiveness of a colonial state by 200%, the second one increases farming efficiency by 50%, the third one increases mining efficiency by 50%, the fourth one increases RGO efficiency in treaty ports and the Suez/Panama Canal, the fifth one reduces militancy in a colonial state by -0.50 and the last one decreases consciousness in a colonial state by -0.50. All of these, except for colonial migration NF, are locked to Overseas colonies ONLY. Most NFs have a downside with the exception
-Added Transylvania cores to Pancevo and Bor to stop the minorities there from assimilating.
-Added a small Romanian minority in Vidin, Bulgaria. Based on https://en.wikipedia.org/wiki/Romanians_in_Bulgaria
-Clippers are now available from the start, meaning that artisans in uncivs can produce them.
-Moved Kotor to the Montenegro region.
-Added naval bases to every tag in Japan, to Korea, Vietnam, Siam and almost all civilized countries.
-Boosted the effect of the Production NFs.
-Fixed the CB in the "seize Lagos" event chain to guarantee it will work with any combination of civilized/uncivilized nations.
-Fixed Ceuta being in Asia.
-Deactivated the new crimes and restored the old, unrestricted vanilla crime conditions for testing purposes.
-Integrated the Misc Mod V2 and the latest version of AFPG's (V9) flag pack. Kudos for the creators.
_______________________________________________________________________________________________________________________________________
V0.3.6 - 15/09/2016
-Changed the maximum effect of the increase colonial/emigration mobility from 2.0 to double the original value (1.8 for Colonial, 1.4 for Emigration).
-Fixed "Annex Fiji" decision making it a state instead of a colony.
-Fixed double decision to vassalize the Trucial States.
-Enacting Radical Reconstruction should remove the Slavery Debate modifier.
-Made sure Argentina has the Liberty NV.
-Getting Baja California during the Gadsden purchase will give California cores there.
-Il Risorgimento event shall now try to annex only italian-culture countries in Europe, it should ignore colonial tags.
-Fixed the localization for event 19366.
-Stopped the Sino-X Friendship Treaty from showing up for Chinese cultures.
-The possible cores the UK can get on Sekondi after a failed gold coast purchase will be temporary.
-Fixed a bunch of countries that would start with better healthcare reforms than basic when released.
-Added a failsafe in case AI US spheres Mexico without all their cores. They will still be able to fire the treaty of guadalupe hidalgo.
-Choosing to abolish slavery during the "King and I" event will no longer give slaves militancy, it will instead remove from them.
-Organizing Ghana should add Akan as accepted.
-Halved the impact of inventions in demand increase.
-Chinese states and substates as well as Mongolia, Tibet, Kumul, Nepal, Bhutan and Sikkim will start with closed borders.
-Organizing Senegal should no longer change its religion. Changed default religion to Sunni.
-Korea should no longer rename Lushun to Port Arthur.
-Divided Ghana in 3 states instead of 2 to make german Togo and Modern Ghana borders possible.
-Renaming Northern New Guinea no longer requires Bougainsville.
-Fixed the islands of Sangihe and Talaud being part of the Philippines instead of dutch/indonesian possessions.
-Changed the Whig (Conservative) Party of Texas economic policy from L-F to Interventionism. Based on The Whig Party of Texas in the Elections of 1848 and 1852, pp26
-Stopped the "Restore America" CB from being usable if the US exists and the second ACW didn't start. Now it's only possible if the US doesn't exist or if the second ACW started.
-Changed Southern Democrats to be pro-residency instead of limited citizenship.
-Democratic (conservative) Party was split in 3: From 1836 to 1860 it's only one, Jacksonian party, pro-military and pro L-F. In 1860 it will be split in 2: Bourbon Democrats, which are pro-LF and anti-military and the Pro-Military and Democrats, pro-military and Interventionist.
-Added a Urban terrain type. This needs some explanation: while most provinces have cities in it, the Urban terrain type only represents provinces that are MOSTLY urban covered. So while London province has the London city, it's too big and it's not only (or mostly) London city, it's mostly field. Provinces like  Gibraltar, Melilla and Ceuta are the main targets of this terrain type. Islands will remain unchanged. To fit in the Urban terrain, a province should have (or represent) less than 1000km². Singapore, while fitting in the category, doesn't have a big enough settlement to fit in. Urban terrain reduces RGO size by 50%, increases efficiency by 25%, adds 2 defense to defending units and reduces battle sizes by 50%. Remember: terrain represents the predominant terrain of the place, so you can have a big urban center in the middle of plains/farmlands, if the province is big enough it will be plains/farmlands. No, I can't change terrain through events so I can't simulate provinces flipping to Urban.
-The Native Protection Act decision now requires primary culture pops in every province, to avoid possible assimilation problems. Fixed a problem with it that made it impossible to be taken.
-Fixed the vanilla Yankee pops in California. There's less pops overall but with more pop type diversity, to stop assimilation problems. Based mainly in historical immigrants https://en.wikipedia.org/wiki/George_C._Yount and historical settlements "During November 1845, California's Commandante General José Castro met with representatives of the American immigrants at Sonoma and Sutter’s Fort."
-Fixed the "American Frontier" decision being taken right at the start.
-Eureka province changed to "Sonoma", since the settlement was there first. Name later changes to Santa Rosa.
Renamed Province 1205 from Bereket to Kyzyl-Su.
-Made Jarvis Island part of the Line Islands province instead of the Kirimati island.
-Re-added Kirimati province. It was in the vanilla files but it didn't exist de facto on the map.
-Reshaped Fayuum so it looks better.
-Canned Food, Ammunition and Electric Gear will now use steel instead of raw iron to make its goods. Profitability was kept more or less the same.
-Since the AI is still a bit reticent, added liquor factories in Belgium, UK, France and US.
-Increased wood output for a few inventions.
-Made all provinces in the US start with 35 LR. The East coast will change to old values (50 for New York, 40-45 for a few places) once the Statue of Liberty arrives, Texas will revert to old values once Oil is found and California will revert to old values once the gold rush starts.
-Added a lot of missing names for bodies of water.
-Establishing the Kaitakushi for Japan should now increase RGO size in Hokkaido.
-Added decisions to reorganize Namibia and Guine-Bissau, as well as a decision to organize and reorganize Madagascar.
-Integrated the Anon's America Minimod. Changelog here: http://pastebin.com/kLQuru23
-Netherlands should lose their cores in Luxembourg regardless if Luxembourg already exists druing the Treaty of London.
-Renamed province 683 from Liegnitz to Waldenburg, as the previous city wasn't in the boundaries of the province.
-Reworked pops in Texas following https://tshaonline.org/handbook/online/articles/ulc01 All provinces in Texas proper start with a small quantity of texans and Texas cores too, to avoid assimilation bugs.
-Added very small japanese pops to the rest of Hokkaido and to the amazon to avoid assimilation bugs in these places.
-Slightly increased the number of bureaucrats in Arkansas and Michigan so they can become states faster.
-Added another factory to Atlanta to stop the craftsmen there from migrating all over the place once the factory there invariably goes bankrupt.
-A few RGO change events/decisions were modified to avoid shortages of late game goods such as lumber.
_______________________________________________________________________________________________________________________________________
V0.3.5.5 - 28/07/2016
-Fixed the adjacency between Penghu and Taiwan.
-S-P should start with All Allowed Rights now.
-Fixed the "Establish the Kaitakushi" decision so you can take it if the shogunate made a peaceful transition to Japan.
-Fixed one more instance where Tokyo/Edo would get a pop growth modifier until the end of the game.
-Fixed the Sino-Portuguese treaty event chain giving Qing a status quo CB. Again.
-"All Allowed Rights" should give a very small decrease in militancy for non accepted pops now.
-You shouldn't be able to release New England and immediately get them to join you again to burn some infamy for free.
-The Annexation of Tahiti event will now only happen in the 1880's.
-USA: Changed the Democrats to be Pro Military instead of Jingoistic and the Whigs to be Anti-Military, based on their stances over Manifest Destiny and the future Democrat anti-imperialism policy.
-Fixed a bug that would allow Russia to integrate Transcaucasia if you formed it externally.
-Gateway to America modifier for New York will now only last 5 years instead of forever.
-Reworked late game RGO flips in the tea decision for UK and a few invention output bonuses.
-Made sure joining the Argentinan substates in Argentina doesn't leave any land behind. Except for the Falklands.
_______________________________________________________________________________________________________________________________________
V0.3.5.4 - 25/07/2016
-Reverted unemployment effect on demotion chance back to vanilla levels.
-Added a Wool province in China, will flip later to Tea.
-Stopped the war from the Sino-Portuguese treaty of friendship from adding a status quo wargoal for the defender.
-Fixed Tokugawa OOB not adding all soldiers because all soldiers were supposed to come from Edo.
-Made so the Communist Party in China is unlocked earlier.
-Removed the vanilla requirement to own Luxor to start the Egyptian Excavations without exerting pressure (the one that gives the modifier that gives infamy). That requirement made starting the excavations without getting the infamy modifier impossible even if you sphered Egypt. The decision to take the infamy and start the excavations will disappear if you have the conditions to take the better decision (you sphered the owner of Luxor or owns it). Also changed the forced event to start the excavations, you can take it as long as any country that owns Luxor is not a GP.
_______________________________________________________________________________________________________________________________________
V0.3.5.3 - 22/07/2016
-Fixed a wrong syntax in an event that would make everyone start the game hating the US.
-Stopped Maharashtra from starting as colonial.
-Fixed a situation that could make Bosnia or Albania infinitely take the population exchange decision.
-Fixed Kazakhstan decision to move capital being taken ad infinitum thanks to a double entry.
-Added AFPG's theocracy flag for Toucouleur.
-Added French pops to a few provinces in Bretagne to help with assimilation.
-A rubber or oil province that was changed due to unemployment should no longer flip back to rubber/oil in no time.
-Since Netherlands doesn't have a lot of cores to free, rejecting the treaty of London will also give a Cut Down to Size CB on them.
-Changing government or losing to rebels that change the government should interrupt genocides now.
-Reworked the borders of the Tidore Sultanate. When taking the 'short declaration' decision the Netherlands should annex the missing territory (it won't show up in the decision effect description but you still get it).
-Removed the Dutch pops in Tidore Biak.
-Reworked pops in Turkmen Berekt to be more consistent with the rest of the desert.
-Russia will try to break the Treaty of Tartu if Scandinavia exists and has cores in Finland.
-Fixed Natuna being in two regions.
-Reworked military consumption of a few goods.
-Increased base production of a few basic goods and slightly decreased output for a few inventions dealing with these goods.
-Western Winds shouldn't fire day one for Qing/Japan anymore.
-Reworked the american frontier a little bit. Names will be changed through decision later, all provinces owned by the US start with a really small quantity of yankees in it. 
-Guano Islands act decision now needs the technology blue and brown water school.
-Made ending the carlist/christino wars a little easier and faster to help AI Spain stabilize better.
-Refuting Manifest Destiny as Mexico should not give any additional cores besides what they start with.
-Increased tech output for Tea, Coffee and Coal. Balanced wool output.
-Decreased the population of province 1987 in the Congo by about 200K.
-Made founding the Suez Canal Company easier. Also made it more dynamic, you can found it even if Suez is not owned by Egypt as long as the owner isn't a GP. Made it easier to seize the Suez Canal when the owner goes bankrupt. Added a decision to seize the panama canal under similar circumstances.
-Made sure you can't take the decision to colonize Ezo unless Ezo has already appeared.
-Made so the "gateway to harbor" in Edo for the Shogunate is temporary too.
-Reduced MTTH for the treaty port events to fire.
-Each time a carlist war ends (with the carlists defeated event), the next one will take longer to fire (aka the MTTH for the "return of the carlists" is increased by 50% each time a carlist war ends).
_______________________________________________________________________________________________________________________________________
V0.3.5.2 - 09/07/2016
-Scandinavia should get a core in Iceland and Greenland when forming, even if the territory is colonial.
-Stopped event 13200 from firing for uncivs that are also vassals.
-Fixed the Liberate Country CB for the Italo Turkish War. Again.
-Reworked pop needs and tech bonuses, mostly restored vanilla values. The old model wasn't working well because of early game shortages.
-Cholera will only spread to japan after 1850 and it will take longer to spontaneously pop up in isolationist uncivilized countries that aren't in the Indian culture group.
-Fixed missing localization for barbed wire invention.
-Gas Defense has a 1% chance of being discovered if you are neighbor to a country with gas attack capability.
-Fixed Fort position in Gorlitz.
-To claim Hawaii you need to either own a province in Polynesia or own a port in the pacific. So US without access to the pacific can't claim hawaii.
-Added a decision for Catalonia to claim Aragon.
-Social reform desire should only affect non animist or above 60% literacy pops, unless the country religion is animist. This effectively mean that ideologically speak, animist pops in africa shouldn't turn communist. They can still join communist rebels though.
-The mormon exodus is now a decision instead of an event. It can only be fired if Utah is non colonial, to stop the modifier form disappearing when the state changes from colonial to non colonial.
-mechanized_fishing_vessels bonus to fish output increased from 0.5 to 0.75
-Changed the shape for provinces in Turkmenistan to the one I originally envisioned.
-Moved Comoros from South Madagascar to "Indian Ocean Territory"
-Fixed the pops of 2585 - Al Jawf in Libya to be most Bedouin with a few Teda instead of being only Teda. Based on https://en.wikipedia.org/wiki/File:Toubou_map.svg
-Reworked pops in Chad. Based on http://pdf.usaid.gov/pdf_docs/PCAAA637.pdf and http://www.catsg.org/cheetah/07_map-centre/7_4_North-African-region/thematic-maps/chad/human-population.jpg
-Fixed event 3600 - Life and Limb not having its effects properly happening.
-Balanced a few event modifiers.
-The events that change Argentina/Brazil governments to democracy will not remove more liberal reforms now.
-Reworked the description, image and requirements of event 36914.
-Made sure Communist Turkey keeps using "Turkish" as adjective.
-Added a missing Tripoli core to province 1742 - Wath.
-The Hungarian Revolution should spawn Hungary as a constitutional monarchy now.
-Sepoy rebels should not rise after the "Stirrings of Indian Nationalism" event. Only normal, nationalist rebels will rise in India.
-Added two more levels to emigration/demotion/colonial migration chance for pops with more than 40% and 50% unemployment. This means that higher unemployment will mean more pops leaving the country, looking for other professions or going for the colonies. Removed the effects unemployment had on religious conversion.
-Removed the events related to the Bear Flag revolt.
-Added a general to the Khanate of Khiva, Muhammad Rahim Quli. Based on http://www.historyfiles.co.uk/KingListsFarEast/AsiaKhwarazm.htm
-Fixed the decision to rename Primorye renaming the state twice to different names. Now each naming should target the right place.
-Fixed province 972 in the decision to re-rename Ukrainian provinces from the Soviet names back to the pre-Soviet names not getting a pre-soviet name.
-Added Baluchistan cores to the map, to stop Baluchi pops from assimilating. Baluchistan is not normally releasable, so the only way to play as it is still forming it with one of the Baluchi tags. Changed the normal capital of Baluchistan from 1219 - Quetta to 1222 - Bela. Quetta doesn't have Baluchi pops.
-Removed Baluchi as accepted from Persia.
-Grouped demotion literacy modifiers (as that was apparently the intention in vanilla) and corrected a few mistakes in pop_types.txt.
-Pops will not move out of a province if there are less than 500 pops in that province.
-Changed FACTORY_PAYCHECKS_LEFTOVER_FACTOR from 0.3 to 0.25, same value as vanilla. Total amount a factory will pay with minimum wage and work hours from their leftovers reform is now 150%.
-Provinces that produce dye should flip to a random RGO (between coffee, tobacco, cotton and grain) when synthetic dyes choke the natural dye market. This will stop entire provinces full of unemployed because of an oversupply of dyes. This will only happen if unemployment is present in these provinces though.
-Changed event 14590 - Disloyal Regiment to be a country event instead of a province event.
-Reworked Ethiopian formation, cores and decisions. Removed the events for the Zemene Mesafint. Added historical events and a decision to claim Ethiopia as one of the minors.
-Changed all event modifiers that used land_unit_start_experience since the values were not in the right scale to make a difference.
-Added AFPG's Ethiopian and Israeli flags.
-Added a decision for the conquest of the south for Ethiopia. Sidama doesn't start in game anymore and Harar starts with only one province.
-Changed Iceland's terrain back to vanilla.
-Gonder, Tigray and Shewa will start with a truce now.
-Fixed wrong localization in the vanilla entry can_build_factory.
-Fixed a vanilla bug that would theoretically allow a province to become entirely or near-entirely composed of capitalist pops. Well it would at least allow to break the capitalist barriers of 0.07% of the population.
-Laissez-Faire will now make capitalist promotion easier.
-Removed, for the AI, the malus that would stop capitalist promotion in a province when the capitalist percentage reached 0.03%. The player can easily circumvent this with the "promote capitalist" NF while the AI doesn't use that.
-Province 1875 - Djibuti will start with Awsa and Warsangali cores.
-Forming/uniting Somalia will also add cores to southern Ethiopia and a few provinces in Kenya. To stop assimilation.
-Fixed the Colombian border, based on https://upload.wikimedia.org/wikipedia/commons/0/0f/Provincias_de_la_Nueva_Granada_1851.jpg http://babel.banrepcultural.org/cdm/ref/collection/p17054coll13/id/206 and http://www.cancilleria.gov.co/en/land-frontier-colombia-brazil
-Added a decision for Brazil for the Vásquez Cobo–Martins treaty to normalize borders with Colombia.
-The US will change their laws to Immigration Quota in 1917, to represent the 1917 Act.
-Added Assamesses and Oryia as accepted cultures for India.
-Moved Nepali from the Indian culture group to the Central-Asian, where Tibet is. They can't form India anymore.
-Changed the units from the Central Asian group (Mongol, Yakut, Siberian, Tibetan and now Nepali) to use the AsianGC instead of the MiddleEasternGC.
-If Pljevvlja or Novi Pazar end up as Ottoman enclaves, an event should pop up to change it to either montenegro, serbia or yugoslavia.
-Canada, New Zealand, USA and Australia start with open borders but they will implement immigration quotas once they reach a certain population. For Australia it's 1 million pops, for New Zealand is 353K pops, for Canada 2.25 million pops and for the US is 26.5 million pops AFTER 1910.
-Reduced LR across Switzerland by 1. Their growth rates were too big.
-Rich strata pops will now try to buy a small quantity of cars for their everyday needs and they will try to get more telephones and radios too.
-Fixed Muhammad Ali Reforms modifier showing the vanilla modifier instead of the proper one.
-Changed so you can Genocide even if you signed the geneva convention, but every time you do while still having the modifier you get 3 more infamy. 
-Added 7K sunni slaves to the province "Salvador da Bahia" in Brazil.
-Fixed unit position in province 2407 - Tabatinga.
-To stop UK immigrants treating India same way they treat other colonies, and to encourage immigration to a few places, a few provinces in Australia, Canada and New Zealand will start with immigration bonus modifiers that will last for 10 to 30 years.
-Angostura in Venezuela should flip to gold after the first half of the 19th century. Based on info from https://en.wikipedia.org/wiki/Venezuelan_crisis_of_1895
-Fixed a few problems with Taiwan and the new provinces in Taiwan. Renaming, province secession and others should work properly now.
-Fixed a few typos in localization variables.
-Externally formed Arabia/Turkestan will start with techs now.
-Immigration Quotas is now a new world only policy. It slightly reduces immigrant attraction but it reduces core pop militancy.
-Changed the scale of the starting party loyalty to allow for quicker changers.
-Made sure South Peru will join Peru once the PBC dissolves.
-Standardized GP relations with each other a little bit.
-Discouraged the US AI from sphering everyone in Asia and the ME.
-Pops will not migrate overseas with closed borders.
-The rich strata should try to buy small quantities of cars, telephones and radios as part of their everyday needs.
_______________________________________________________________________________________________________________________________________
V0.3.5.1 - 20/06/2016
-Fixed two states potentially being named "Mandalay".
-Added a decision to expand RGO size in Ruanda-Burundi and normalize the life rating of the provinces.
-Reduced Capitalists Luxury Needs.
-Basic factories, Cheap and Common factories require less steel to be built.
-Crime fighting can stop the Hamburg Fire from happening now.
-Fixed the "Form Uzbekistan as Khiva" decision. It used to add and remove cores at the same time, causing a crash.
-Stopped a problem in have_core_in making all countries end up with a make puppet CB on Croatia once it gets independent.
-Fixed unit position in Tehran.
-Removed Machine Tools as luxury needs for all pops.
-Reworked pop everyday needs of middle and poor. Steel was moved to luxury only for poor pops, reworked proportion of a few goods.
-Added Kunduz-Badakhshan to the great game CB.
-Made the "Liberate Country" CB work for Italy AI. Hopefully.
-Stopped Issues Suggestion events that increase desire for social reforms from firing before socialist ideology is enabled. Without socialists enabled, the effects are useless since pops will drop all social reform desire without the ideology being enabled.
-Reworked technologies and starting factories to avoid choke points of basic goods in early game.
_______________________________________________________________________________________________________________________________________
V0.3.5 - 18/06/2016
-Merged 2681 - Kikkiaki in 2615 - Krasnoselkup. 2681 will now be used as Taipei. 1485 - Taipei will become Tainan and 2562 - Tainan will become Taitung, on the coast. Added the natives pops and fixed the positions. Credits to anon.
-Fixed a few port positions in Libya.
-Reworked of Laborers life needs: Since Farmers use slightly more Cattle, Laborers will use slightly more wool, so their spendings with everyday needs is similar.
-Tobacco is now an everyday needs for poor pops. Rural pops (farmers and laborers) have different quantity requirements for tobacco, coffee, glass and lumber. Rural pops use less glass, less coffee and less tobacco and more lumber, urban pops use more glass, coffee and tobacco and less lumber. Pops will use lumber as an everyday need to build and maintain their houses. They also use steel as an everyday need for the same purpose as well as for other appliances such as horseshoes, forks, axes, saws and tools in general.
-Poor strata will try to consume Steel and Cement as a luxury need for building and maintaining better houses. They will also try to consume wine instead of liquor as a luxury need and they will try to consume canned food too. They use lumber in their everyday needs for their housing.
-The Middle Strata is divided in 3 informal categories now: The Upper Middle Strata, the Middle Strata and the Lower Middle Strata. The only difference is in their needs: Clerks and Artisans, being lower middle, consume less goods overall. Clergy and Bureaucrats, being true middle, consume the average amount (with bureaucrats still consuming more than clergy) and officers are high middle strata, consuming more than anyone else in the strata. As it was in Ricky, the Life Needs of Middle and High middle strata were doubled. Most needs in the everyday needs category were also doubled and instead of consuming lumber, they try to consume steel and cement right off their everyday needs for their housing. They will also try to consume small quantities of radio, electric gear and telephones.
-The Rich Strata is largely similar to the middle strata. They consume large quantities of steel, cement and lumber for their housing needs and everything else the middle strata consumes, and more. Capitalists consume more than aristocrats.
-Excluded Taiping from the event to flip theocracies.
-Fixed the the ARU not getting Maghrebi as accepted when it claims the Maghrebi. Made sure it really claims the entire place.
-Toucouleur should be formable by theocracies now.
-As the rest of the uncivs, Chinese countries/states should get the first railroad technology if they pick the railroad reform when westernizing.
-Tonghak rebellion for Korea will only happen if the country is a monarchy.
-Removed the event to Inherit Chitral.
-Fixed LRs in Libya.
-Gave Oman cores in the provinces they own in Africa. The event for Zanzibar/Oman to split will remove those cores.
-When Congress Poland is defeated in the November Uprising cores will no longer be removed.
-Fixed a vanilla bug where Artisans and Bureaucrats needed more than 100% luxury needs fulfilled to get a bonus to promote to capitalists.
-Fixed a wrong flag not effectively ending the Carlist/Christino rebels/rebel events.
-Reduced the prestige hit for forgiving a normal debt.
-The First Opium War events should not happen if the UK has a truce with China and it should end military access and alliances with china to avoid it giving any potential infamy.
-Stopped the Netherlands from being able to do the Gold Coast Treaty with themselves.
-Event 13201 - Diplomatic Mission Under Siege, second option will now remove prestige based on how much prestige the country has instead of always removing 20 prestige and it will completely remove the country from your sphere.
-Reduced the price to buy the virgin islands from 500000 to 200000.
-Doubled the MTTH of event 18535.
-The event to distribute colonies (96071) after a dismantlement will now have a "skip this colony" option.
-Province 2036 - Dar Es Salaam renamed to Mzizima. The city can be founded with a decision that can be taken by any Muslim country that holds the right province.
-Changed Vanilla event 38500 - Instead of being only about the voyage to the USA, it involves moving the capital to Zanzibar too. Added a few other effects to it to, remade the description and fixed the localization.
-Changed NNM Event 38505 - Death of the Sultan of Oman/Zanzibar. It doesn't happen only for uncivs and the AI has a chance of trying to leave the country together instead of always separating. Keeping them together has more serious consequences though. The event should also move the capital back to Muscat.
-Forming Czechoslovakia as Bohemia/Slovakia will now require for either countries not to be vassals or be vassals from one or the other and it requires nationalism and imperialism researched.
-Fixed wrong research cost values in the Metallurgy tree.
-The Tangier Protocol shouldn't happen to civilized countries with capital in Africa.
-Uncivs will no longer slowly lose prestige. Adjusted started prestige for nations: SPs start with around 8, Civilized countries start with 5,4,3 depending on the location and Uncivs usually start between 0 and 2.
-Fixed the Kobe-Kyoto Border.
-Re-enabled slavery in China and added slaves to several provinces, compromising 13% of the population. While there isn't good figures on the extent of slavery, slavery wasn't formally abolished until way later. Based on http://www.zum.de/whkmla/sp/0910/hersheys/hersheys5.html#x and http://www.dartmouth.edu/~crossley/HIST74/COURSE/Crossley_CWHS-08_corrected.pdf
-Restricted the RGO bonus for Market Functionality tree to vanilla levels.
-Changed inventions of the Metallurgy tree regarding steel production. Now Bessemer Process gives 10% output, the rest of the inventions give 3%, 4% or 5% to a total of 30% with all inventions and bonus from the metallurgy tree. Steel Alloys invention should now also give a +4% for the production of steel.
-AI countries with less than 6 states and no colonies will not try to commission warships.
-Doubled the MTTH of event 13280 - Angered Aristocracy. The event also requires you to have any reform enacted and to have landowners with either 3 militancy or 6 consciousness in a state.
-Muhammad Ali reforms will now give 5 prestige instead of 10.
-Integrated AFPG's Papal States flags.
-Stopped Capitalists from consuming Rubber and Oil as luxury needs. However, to unlock these goods in your provinces their inventions are needed - Cracking and Edson's Light Bulb, or a factory that uses that good. This is done to ensure that these goods will have a market once they are discovered.
-Added two new inventions: Rotary Kiln and Stiff-Plastic Brickmaking Machine. The first increases Cement output by 15% and the second by 10%.
-Improved the localization of vanilla event 60150 - The End of Female Suffrage.
-Made event 2570 - Living Space only fire if the neighboring countries neighbor the fascist state with a non colonial state.
-Increased the base production of Coal and Iron.
-Added a Cement Factory in London. Based on http://www.fundinguniverse.com/company-histories/lafarge-cement-uk-history/
-Reduced Liquor's value from 6 to 4.4.
-Stopped the French Indochina event from giving a CB to any non vassal country.
-Fixing the Napoleon III coup d'etat event not lowering relations with the right countries.
-Fixed a potential bug that wouldn't give France any provinces during the Treaty of Hanoi.
-Renamed Ottawa to Bytown. The owner of the province gets a decision to rename it to Ottawa.
-Fixed Haussmann's Renovations allow requirements.
-Event 37207 - Louis Napoleon Flees will not happen if Napoleon wins the elections or does the coup d'etat.
-Merged vanilla event 37208 and NNM event 10402, both were about Louis Napoleon being elected. Now only the NNM event remains, but the effects of both were merged.
-Changed the decision to claim Tibet requirement to allow repressive non jingoistic governments to claim it.
-Reduced the LR of 2367, 2366, 2337 and 2338 to be more in line with the rest of the Chaco region.
-"Death of the Sultan", "John Brown's last raid" and "Dred Scott v. Sandford" will not be major events any more.
-Changed provinces 1301, 1303, 1317, 1312, 1222, 1258 and 2640 - all in India and Pakistan from Tea to Fish. Changed 1308, 1311, 1278, 1290, 1228, 1231, 1259 and 1274 in India and Pakistan from Tea to Cattle. Changed provinces 1225, 1235, 1238, 1232 and 1327 from Tea to Wool, in India, Nepal and Pakistan. Changed 1326 - Katmandu to Grain. Changed 1236, 1260 and 1266 in India from Tea to Fruit. All these provinces will come back as tea provinces through a decision as the game progresses, mainly to represent Robert Fortune smuggling of tea out of china but also for economic reasons.
-Changed 1094 and 1096 from tea to fish. They will get the option to become tea-producing provinces later. Based on The Tea Industry by Nick Hall, pp60.
-Changed Qing and Manchukuo starting economical reform from "Administrative Reform" to "Land Reform"
-Changed the production of Lhasa and Lhodrak in Tibet from Cattle to Grain and Wool respectively.
-Changed 1248 - Gaya and 1250 - Bhagalpur from opium to cattle and fish, respectively. Changed 1271 - Indore and 1269 - Udaipur from Cotton to Opium, to represent the Malwa region, a historical produce of cotton. Based on https://www.whitman.edu/economics/Workingpapers/content/WP_25.pdf
-Changed slave throughput efficiency from old 25% to 30%.
-Cultures in the Iranian-Turanian group are marked as 'is_overseas = no' again, as it was in vanilla. NNM changed it for some reason.
-Fixed vanilla Oil spread events changing the wrong provinces RGO to oil in the US because of the changes to american provinces.
-Stopped the events for organizing the central asian events from happening while there's a war going on.
-Changed starting iron RGOs in the USA. Added a decision for the Iron Ranges to change RGO to iron.
-Fixed Nassau's OOB and pops. The same thing was done to Frankfurt, Lubeck, Hamburg, Bremen Based on Germany: the spirit of her history, literature, social condition, and national economy, illustrated by reference to her physical, moral, and political statistics, and by comparison with other countries by Hawkins, Francis Bisset. PP 416. See https://archive.org/details/germanyspiritofh00hawkrich
-It will be possible to get the Realist Literature invention as a GP without Equality NV.
-Fixed event 90908 not giving the appropriate relation hit.
-Improved description and overall triggers for event 98641.
-Fixed a few pop problems in Paris. Haussmann's renovations should now also add a modifier that increases RGO size in Paris and it will require money.
-Reduced the Statue of Liberty modifier to 50% bonus instead of 100%.
-Changed Metz and Prague from Precious Metals and Iron to Cattle and Coal respectively. Metz will turn to Iron and Strasbourg to Precious Metal via a decision. Based on http://www.1902encyclopedia.com/G/GER/germany-04.html and http://www.patrimoine-minier.fr/lorraine_fer/index.html
-France has a decision to change a few provinces to Iron RGO late game, based on http://www.patrimoine-minier.fr/index_france.html and Mulhall's Dictionary of Statistics.
-Changed Trois-Rivières goods from Grain to Iron. Based on http://www.thecanadianencyclopedia.ca/en/article/mining/
-The end of the gold rushes in Australia now shall change more RGOs to Iron in Australia. Mostly based on the maps found in http://www.australianminesatlas.gov.au/history/index.html
-Changed how Potato Blight works from NNM: instead of happening only in non colonial grain provinces, it can happen in any Farm RGO with at least 25K pops. It can also happen even if you have Inorganic Chemistry but only in long Great Wars. It won't happen in Tundras, Boreal forests or Deserts though. Poverty makes it so that an outbreak is more likely instead of being a defining factor if it will happen or not. Increased the MTTH from 250 to 300. It will spread outside NA, SA and Europe after 1900 and it will spread from neighbouring country to neighbouring country.
-Fixed the name of provinces 579, 574 and 547 in Germany.
-The Krakatoa event will no longer remove 10 life rating from province 1414 - Bogor.
-Coffee Rust will also change production in Indonesia to Tobacco.
-Changed provinces 2072 - Hwange and 2069 - Gwero from Cattle and Fruits to Tobacco.
-Changed Colombia RGOs and added a decision for the commodities boom of the late 19th century, based on https://en.wikipedia.org/wiki/Economic_history_of_Colombia
-Changed Zurich RGO from Cattle to Iron.
-Added a permanent modifier for Ireland to reduce their RGO size, to represent the countryside being overcrowded.
-Artisans will use Machine Parts for their shops.
-Forts will also require Steel to be built.
-Every factory type except basic factories and steel mills will require steel to be built instead of iron.
-Increased overall fuel needs for units that require it.
-Forming Scandinavia should automatically annex Scandinavian vassals now.
-Fixed two Irish provinces who were missing intellectuals.
-Reworked the irish famine and oppression modifiers to better represent the historical trend in Ireland.
-Changed province 2531 from Grain to Coffee.
-Made 3 decisions for the spread of late game commodities in SE Asia and the Americas.
-Fixed Ireland starting reforms.
-Changed the UK liberal party from anti-military to pro-military.
-Made Monitors faster than Ironclads. Change Monitor stats so they have better Gun power but less Hull, changed costs for supply and construction so they are bigger than Ironclads.
-Changed 1206 from Cotton to Grain and 1196 from Wool to Cattle. Both provinces are in Turkmenistan.
-Bleeding State, Quantrill's Raiders, Pottawatomie Rifles, Wakarusa War and events will happen only once.
-Removed the vanilla Texas set up event. Effects will now be handled in another general set up event.
-Changed event 44120 so the effect will not be country wide but instead it will affect random states.
-Increased the level of Glasgow Steel and Machine Parts factory.
-Increased average slave growth.
-Completely reworked Civil War events for the US to end event spam. Most events are country events, add modifiers to avoid spam and the few events that are still province events fire one time only, with the exception of the core spread events for the CSA.
-Founding Yadanabon decision for Burma will change the RGO to precious metals, to represent the Valley of Rubies in the province.
-Added decisions to change RGOs for the Philippines, Uzbekistan, Turkemenistan, Tajikstan and Kyrgyzstan. Mostly based on economical data for these nations and what began being produced post 1900. The RGOs are usually for industrial goods or cash crops. A few sources in http://nexus.som.yale.edu/jackson-kompanion/?q=node/103 and  http://pubs.iied.org/pdfs/G00573.pdf
-Farmers and Laborers will try to buy small quantities of Machine Parts as part of their luxury needs, same thing for Aristocrats. These are there to represent replacement parts for tractors, harvesters, pumps, crushers, power shovels and other mechanical appliances.
-Changed the capital of the South Island state from 2513 - Dunedin to 2516 - Nelson.
-Changed province 2524 - Wake to Hamilton, a province in New Zealand.
-Changed the event that renames provinces in New Zealand to be a decision.
-Added an event to flip a few RGOs in New Zealand.
-Added a new reform, called "Border Policy". Only Absolute Monarchies or repressive governments can enact closed-border policies. Jacobins or Socialists rebels succeeding, or changing your country to a democracy, semi-constitutional monarchy or constitutional monarchy will change "closed borders" to "open borders". Decisions were made that allow a nation to change these policies.
-School reforms will have a small influence in assimilation.
-Added one event for the Dust Bowl.
-Improved a few decisions, events and added a missing vanilla localization.
-Capitalists, Artisans and Aristocrats will now start the game with a little money. The amount depends on the pop type and the country status, with uncivilized countries not getting anything. Reduced the starting money for countries.
-Reduced the amount of money factories store from 10K to 2K.
-The Annexation of Tahiti will now give a pop up.
-Merged 686 - Line Islands with 3178 - Palmyra Atoll. 686 is now used as Merv, a desert province in Turkmenistan.
-Added Kunduz/Badakhshan in the game start. Based on https://archive.org/stream/lifeofabdurrahma01abdauoft/lifeofabdurrahma01abdauoft_djvu.txt and http://www.zum.de/whkmla/region/centrasia/xkunduz.html
-To stop assimilation, Turkmenistan, Tajikistan and Kazakhstan will start with their cores in place. Turkmenistan's monarchy name will no longer be "Salor Confederation".
-Added a decision to form Turkestan as an external nation. It requires mass politics to be used, for the country that takes it to be a GP and to sphere or own all the necessary territory (Uzbekistan, Kazakhstan, Tajikistan, Kyrgyzstan, Turkmenistan). Russia will never use the decision.
-Added a decision for the Treat of Akhal.
-Added a few missing bureaucrats for Kandahar. Changed the State capital from Farrah to Herat.
-Fixed a bug with the decision for population exchanges.
-Integrated HP's Hand by a kind anon, a minimod full of new flavor decisions and events, though it does have more for Persia. Removed stuff: RCMP, Petrograd renaming, Deposition of Pedro II - duplicate events. Removed the Second Treaty of Velascos decision, the events for Serial Killers in provinces, the Pastry War and the one for sphering Brunei.
-The "Unification of China" decisions will now add Chinese cultures as accepted, to guarantee China will actually get those.
-Added generals for Imperial Japan. Reworked the % of soldiers in a few provinces in Japan so they have more military score.
-Fixed a few vanilla misspellings of "Upper House".
-Tweaked production values to make the AI spread itself more instead of overproducing a few goods while relegating others.
-Carlist/Christino sympathies malus to RGO output reduced from -50% to -30%.
-Fixed a vanilla bug that made impossible for pops to demand the Good Minimum Wage reform and consequentially made impossible for the AI to pass it.
-Made the AI try to have the maximum amount of capitalists they can.
-France will start with a railroad connecting St. Étienne and Lyon. It will also start with a steel factory. Changed St. Étienne to coal and Lyon to iron production. Based on http://www.arcelormittalinfrance.com/our-business/historyofsteelmaking.aspx?sc_lang=en , https://fr.wikipedia.org/wiki/Saint-%C3%89tienne#L.27.C3.A9poque_moderne , Merriam-Webster's Geographical Dictionary, pp1021, http://www.musee-de-la-mine.free-h.net/ and https://commons.wikimedia.org/wiki/File:Localisation_-_bassin_houiller_de_la_Loire.svg?uselang=fr
-Fixed vanilla event 36622 so it takes into consideration the NGF and the SGF.
_______________________________________________________________________________________________________________________________________
V0.3.3.3 - 21/03/2016
-Fixed a few events where natives where supposed to lose literacy but instead gained.
-The Hungarian-Austrian border treaty now requires both nations to own their main core provinces.
-Stopped the Caucasian Wars and the Crimean War potentially messing up with each other.
-Fixed the National Focus map mode not showing the right icons.
-The decision to annex Hawaii will now always integrate the island as a colony.
-To avoid rebels that can't enforce their demands in Sardinia, the fusione perfetta decision will now reduce militancy in the island.
-You can no longer select the "No Voting" reform during an election.
-Reworked the results of the Krakow Uprising succeeding to be less spammy and only fire when it makes sense.
-Trinidad should now flip to Oil around 1917.
-Changed and fixed a few event modifiers a little bit.
-Stopped the Siberian Railway events from having a chance of giving money.
-Claiming the Maghrebi as the Arab Union will now give Maghrebi as accepted.
-Some bugs related to Patriot rebels should be fixed now.
-Changed event 18100 to fire only if you have the appropriate techs for healthcare. Also made it more strict - it has a base literacy (30%) or consciousness (5) requirement as well as not firing in high militancy (more than 5) or in countries at war. It will not only happen with 30% liberals in the UH but it will also happen with 20% socialists in the UH. Also made the AI more smart when picking up options.
-Fixed a problem in the RGO production with slave pops, they don't give a "bonus" to output but work on throughput now. All credit goes to Delnar_Ersike. Slaves should also be 25% more productive than normal farmers. Based on Historical Perspectives on the American Economy: Selected Readings By Robert Whaples, Dianne C. Betts, pp252.
-RGO spread events that give output benefits - tractors, mechanized mining and distribution channels will no longer happen in slave states and will take longer to happen in serf states, so eventually slavery and serfdom will become less profitable than in free states.  A few more changes were done to RGO spread events: the 50% chance to spread to another state in the same event needs the whole state, instead of only the province, to have an average literacy of 70%. The events won't ever happen if any province in the state is under occupation. To further reduce event spam, the more states a country has the more times the 50% chance of another state with over 70% literacy getting the modifiers will happen. So a country with 10+ more states will have one state more having the chance of getting the modifier, a country with 20+ states will have two states with the chance of getting the modifiers and so on until 40+ states, giving a total of 4 chances of 4 different states getting the modifiers in one event.
-Refusing the Alaskan Purchase as Russia should now give the nation that offered it their money back. Made the AI NEVER bankrupt itself to buy it, even if for the Americans it means not getting it.
-The Sikh Empire can form India but India will now always be Hindu.
-The Treaty of Tartu decision no longer requires the grand_duchy_finland flag.
-Event 49510 - The Grand Duchy of Finland will now only remove 1 infamy instead of 5 since Russia isn't giving up cores or freeing Finland.
-Sweden will be able to Concede Finland as long as it's not a GP. Previously, there was a "less than 300 prestige" requirement. Instead of getting prestige for doing it, Sweden loses prestige and infamy.
-Removed Finnish cores in Petsamo.
-Improved Russian AI reaction to the Treaty of Tartu. The AI will no longer refuse the deal if it means going over the infamy limit.
-Fascist/Communist/Anarcho-Liberal Russia can now break the Treaty of Tartu and get their cores in Petsamo and Viipuri back. Russia can also get their cores back if after the Treaty of Tartu Finland doesn't exist anymore.
-Changed Serbia's color to 161-45-46, one of the official colors of the flag.

____________________________________________________________
v0.3.3.2 - 14/03/2016
-Corrected the spelling of "Jiggs" to "Jigs".
-The third line of the Power, Mechanization and Metallurgy trees should be unlocked in 1840 now.
-Changed the the RGO of 1237 - Panipat from Cotton to Cattle. Changed Provinces 193 - Visburk and 143 - Little Rock from Grain to Cotton. Changed 136 - El Paso from Cattle to Cotton. Changed 101 - Flagstaff from Cattle to Iron and 100 - Phoenix from Iron to Cattle. Changed 1292 - Rajkot and 1295 - Beroda from Cotton to Fish. Changed 1283 - Hydebarad and 1285 - Nizamabad from Cotton to Grain and Fruit, respectively. Changed 205 - Charleston from Coal to Cotton. Changed 415 - Rouen and 418 - Caen from Cotton to Fish and Cattle, respectively.
-Added the following inventions: Lancashire Loom, Cotton Gin, Steam-Powered Silk-Reels and Dobby Loom. Redistributed the Loom inventions.
-The slavery debate event will now increase the number of slaves in cotton-producing provinces in the USA, to represent the growth (because of demand) that the Cotton Gin brought. based on Brian D. Schoen - The Fragile Fabric of Union - Cotton, Federal Politics, and the Global Origins of the Civil War.
-Increased the starting level of the Textile Mill and Regular Clothe Factory in Liverpool from 1 to 3. Added a Level 2 Textile Mill in London. Added a Level 1 textile mill in Trenton and a regular clothes factory in Concord. Changed the number of craftsmen in New england from 500 to 7K and in New Jersey from 0 to 1K. Based on Brian D. Schoen - The Fragile Fabric of Union - Cotton, Federal Politics, and the Global Origins of the Civil War - 2009
-Changed the Textile Mill level in Brussels from 1 to 2.
-Made so that Artisans Fabric/Regular Clothes cost/profit ratio are similar to the cost/profit of the same factories. Same thing for Lumber Mills.
-Clergymen, Officers and Bureaucrats will consume 2 more units of clothes and 1 more units of furniture.
-Fixed the decision "Mining Union of Upper Katanga" requiring Cabinda too. Now it should require only CFS proper territories.
-Fixed a broken pixel in the Geraldton-Perth border.
-Organizing the Congo should only be possible after 1900 now, to avoid problems with the Congo event chain.
-You can Organize Moçambique only with N&I now.
-Returned 2498 - Albany to it's vanilla name, to avoid two "Albany" provinces.
-Great War modifiers will now carry a malus to immigrant attraction.
-Changed the RGO of 1127 - Isfahan from Cotton to Cattle.
-Changed 1601 - Kunming from Silk to precious metals. Transffered the province to Qing. Based on http://www.zo.uni-heidelberg.de/sinologie/research/epm/epm-mines_en.html Changed 1564 - Caozhou from Precious Metals to Silk. Changed 1510 - Luoyang from Wood to Cattle and 1565 - Laizhou from Cotton to Fish.
-Doubled event 12000 MTTH.
-Political Instigators crime will only happen in civilized countries.
-Changed 1493 - Canton and 1501 - Zahoqing from Wood to Fish and 1549 Jiujang and 1545 - Nanchang from Timber to Cattle. Changed 1490 - Lanzhou, 1559 - Xian from Coal to Timber. Changed 1574 - Luan from Coal to Cotton.
-Fixed the shape of Hebei state. Fixed the shape of the Yellow river. Fixed provinces bordering the Yellow river and the Yangtze river to follow the river and not go over it, while maintaining the correct state shapes.
-Reduced the malus of being at war for immigration from 200% to 130%. In most cases, it stills allows for immigration even when at war.
-Reduced the number of craftsmen in Turin from 8K to 1K. Removed the Winery from the state.
-Fixed a bug with how crime icons were displayed in the revolt risk map mode.
-Made the AI nationalize foreign investments. Improved the event description. GPs will ALWAYS do it while non GPs need certain conditions. You can't nationalize if your country allows foreign investments.
-Inventions under Hot Blast will now increase Iron output a little more.
-A few CBs should treat vassals/substates as neighbors for justifying purposes.
-Changed INVENTION_IMPACT_ON_DEMAND from 0.005 to 0.02.
-Fixed a wrong condition that was stopping liberal revolutions from firing.
____________________________________________________________
V0.3.3.1 - 10/03/2016
-The AI will now always try to spend the maximum amount of money they have without bankrupting themselves when building any of the canals.
-If a different ship (from the canal owner) crosses the Suez Canal first, the prestige gain will be higher for that country instead of being the same.
-The Suez and Panama Canal provinces will flip to precious metal when the canals are built, to represent the revenue these provinces brought to the owner and the canals becoming the center of the economy of these provinces. Also to make them more useful.
-Fixed Aborigines assimilating in Australia.
-Terrorist Cells crime will now happen in any province with militancy of 3 or more instead of only provinces with national minorities.
-Added a specific flag for absolute monarchy England, done by AFPG. Thanks AFPG!
-Fixed one genocide option not clearing a flag properly, causing an infinite genocide. Added a few flag cleanups for the events to guarantee no leftovers cause any problems.
____________________________________________________________
V0.3.3 - 08/03/2016
-Changed Naval Schools bonus from research points modifier to a bonus for naval research and a small bonus to leadership as the vanilla description implied.
-Boxer rebels should now give prestige to Qing instead of china when finishing sieging a province.
-Balanced the Bankruptcy reform modifiers a bit.
-Changed the vanilla event 30002 - Regional Fairs. Industrial score requirements are now bigger and so is the required money. AI will also pick options better now.
-To deal with capital ship spamming all ships that give score have a hard limit now. They are: 1 per lvl 5 naval base for Dreadnoughts, 2 per lvl 4 naval base for Battleships, 10 per lvl 3 naval base for Monitors and Ironclads and unlimited for Man'o'Wars. Slightly increased the supply requirements for dreadnoughts and battleships.
-Neutral countries will no longer get CBs (or events for that matter) from bankrupt countries.
-Neutral countries (only Switzerland for now) will enforce their neutrality. Every time someone enters an alliance or gain military access from them they will break it and the country that got the alliance/access will lose 75 relations with them. Same thing for wars, except for the relation hit.
-Greater Persia decision will now give proper cores in the Caucasus.
-Fixed a few instances where a gutter crown event or forming Italy through events could end with a Italy or Germany with French as accepted.
-Stopped the Liberal Revolutions from firing for Switzerland.
-Fixed Persia using the wrong flag for constitutional monarchy.
-Changed province 1194 name's from Krasnovodsk to Novopetrovskoye.
-Rebalanced the political neutrality modifier.
-Added more naval bases to china at the game start, based on https://en.wikipedia.org/wiki/Imperial_Chinese_Navy
-Fixed Ipswitch starting with a level 6 fort.
-Fixed the event for the declaration of Paraguayan being able to fire for the wrong countries.
-Fixed Organizing Nigeria giving the owner not Nigeria the country flag post_colonial_country.
-Fixed jewish pops in Denmark according to http://pastebin.com/Yni8vq8h . The pops are divided in Copenhagen and Aarhus for performance sake.
-A Nation will only get cores in Hawaii when annexing it with the decision if they are in north america. Similarly, Hawaii will only be integrated as a full state if they are in north america, otherwise they will be integrated as a colony.
-Fixed one Ottoman Unit rebelling at the game start in Misratah that made the game start with a battle there.
-Spawning Congo and taking Luhono will now set the pops literacy in the provinces from the old vanilla 10% to 1%.
-Fixed an event not giving the proper CBs for Portugal against Gaza/Angoche.
-Made a Golden Law decision for Brazil.
-Severely reduced the emigration push from Islamic Law modifier.
-Enacting Ottomanism after the arab rebellion was encouraged won't get you any arabic cultures as accepted.
-You can encourage the arab rebellion if the ottomans own ANY arabic culture province, not only mashriqi.
-Granting the arab states self rule during the arab revolt will now remove them as accepted and remove your cores.
-You can no longer encourage arab nationalism if the Ottomans are the #1 GP.
-Fixed a potential way of forming a catholic arab union.
-Fixed the Great Game not working for Chitral and Kazakhstan.
-Fixed a wrong MTTH for event 12140
-Increased the MTTH for the "Canadian Dominion" event repeating if Dominion is refused.
-Worker's Union modifier will no longer give militancy.
-The Ultimatum to Portugal over the Pink Map can now only be fired once.
-Fixed vanilla localization of event 2570.
-Dutch West Indies triggered modifier now only gives prestige instead of a RP bonus.
-Fixed the decision "Lease North Borneo" being repeatable.
-New World countries at war will get a -200% nerf to immigrant attraction.
-Rather than having no bonus to immigration, landlocked nations in the new world will be treated the same as any other nations. The difference is that now the landlocked modifier puts a -150% nerf on immigrant attraction
-Fixed several event localizations and the localization for the NV changes being outdated.
-Slightly reduced the Slavery Debate MTTH.
-The Two Nation Theory decision to form Pakistan will now not automatically integrate pakistan unless they are a puppet and will not remove their cores unless they don't exist.
-Fixed the Dutch East Indies events firing for civilized countries and not checking if you have a truce with them.
-The AI will no longer game over you if you are sphered and has the territory to form saudi arabia.
-Emigration NF will now only b available in a state where all provinces are cores of the current nation.
-Disabled the Irish Integration decision since it was basically pointless.
-Fixed the "Stirrings of Indian Nationalism" not properly clearing the sepoy_rebellion flag from the UK, making the rebellion go on forever. Fixed the event repeating itself.
-Events 97100 "Rebellion in Indian State" and 97105 "Rebellion Against Foreign Rule" have CON and MIL requirements to fire in the case of Indian nationalism, so pops aren't rebelling for no good reason. For the Sepoys, event 97105 will now also require a MIL or CON requirement for non muslim nations.
-Slightly adjusted the Benghazi province shape to stop Sirt from being accessible from Jaghbub.
-Changed the culture color of the Beja so they are more distinguishable from the Sudanese culture.
-Belgium and the Netherlands will now start with a little war exhaustion from the Belgian revolution.
-Stopped event 2550 - Drums of War from firing for puppets.
-If a Crisis for the liberation of Sudan happens in Egypt and Egypt is still a vassal, an event will free Sudan to stop the crisis from carrying on forever.
-Changed the Claim Xhosa Lands (supposedly to start the Seventh Frontier War) to stop it being completely useless.
-Added Tigray as accepted for Gonder.
-You only need Military Statistics to conquer states with less than 1.2 million pops in china as long as you have your capital in asia, neighbours china and you aren't Japan/Philippines.
-Added a few slaves to Macao.
-Added a decision for the founding of Diamang and diamonds in Angola. The decision will also rename most of Angola to Portuguese names if you they own the provinces. Location for the diamond provinces is based on https://issafrica.org/Pubs/Books/Angola/8Dietrich.pdf
-Added a decision for the Sino-Portuguese Treaty of Peking. Any country that owns Macao and Macao alone in China can take it. China/Qing/Taiping can revoke the treaty under a few conditions though, namely if someone else other than the signing country conquers Macao or they become a Fascist/Communist/Bourgeois dictatorship;
-Latvia doesn't have North German as accepted anymore.
-Fixed Germany/NGF being able to get UBD or Banat if formed by gutter crown.
-Silesia doesn't have Czech as accepted anymore.
-Stopped UK AI from bankrupting itself with the "Northern Cape Colony" event.
-The Taiping modifiers should now allow for mobilization during the Taiping Rebellion.
-Renamed Lake Bajkal to Lake Baikal.
-Events 4410, 4411, 15250 and 45100 had their effects modified to take into account that not all intellectuals are clergy. Event 15040 had its localization modified to be more generic so it makes sense with intellectuals.
-Reshaped Odessa, Olviopol, and Vinnitsa borders to follow the Bug river and allow for a proper Trasnitria region. Reshuffled the regions in Ukraine to follow river borders better and to allow for a proper Transnitria region.
-Fixed the mouth of the Bug river and the river in general in rivers.bmp.
-Max Work hours reform will also affect RGO and artisan throughput.
-Changed Kurdish culture color to match Kurdistan and the Ashkenazi culture color to match Israel. Mainly to help differentiate between cultures.
-Renamed Guajira to Wayuu.
-Merged 19 decisions to move your capital in a single one. Not a single effect was lost, the decisions were just merged in a fit-for-all decision. Added 11 more countries to the list of countries that can restore their capitals.
-Rebalanced the output bonus from the Metallurgy and Power tree from the Industry section of the techs. Mainly to avoid late game overproduction.
-Opium is now part of Serfs every day needs.
-Fascist Romania has a decision to claim Transnistria if they own Bessarabia.
-The "gateway to a new land" modifier will now only last 10 years instead of forever in Tokyo.
-Event 12110 - In Them Old Cotton Fields needs 10 cotton stockpiled to fire since it can take 10 cotton form the stockpile and the stockpile can't become negative. The event will also pick a neighbor nation instead of a random one.
-Reshaped provinces in Australia according to one anon design. Thanks anon! Fixed the positions for the reshaped provinces and fixed the terrain for Australia, mostly based on http://www.ecologyandsociety.org/vol7/iss2/art7/figure1c.gif https://upload.wikimedia.org/wikipedia/commons/b/b2/Carte_des_biomes_en_Australie_%C2%B02.png http://www.ga.gov.au/__data/assets/image/0013/12640/GA11759.gif http://www.virtualoceania.net/australia/maps/elevation.gif  http://www.mapsofworld.com/australia/maps/australia-population-density-map.jpg
-Reshaped Balti so modern Bessarabian borders are an option.
-Fixed the terrain in New Zealand, which ended up being one province turned into mountains.
-Tweaked starting pops in New Zealand so pops can assimilate better there.
-Fixed the starting situation for Australia. Kojonup was renamed to Albany and starts with 180 Australian pops, based on https://en.wikipedia.org/wiki/Albany,_Western_Australia Renamed Ophir to Bathurst, Palmerston to Port Essington, Tarcoola to Nullarbor, Alice Spring's to Mparntwe and Tanami to Chanamee. Added pops where it was approriate and settled.
-During the January Uprising, Congress Poland can spawn with Poland's core if Russia owns them.
-The Ionian Islands decision will not longer make the UK transfer Cyprus to Greece. Only the Ionian Islands are covered.
-Forming India should add Manipuri as accepted.
-Added a 1200 melanesians to province 2488 to represent the Torres Strait Islanders.
-The Gadsden Purchase option to sell more than what the americans ask for now will only sell Baja California instead of the Sonora state.
-Reshaped Wisconsin according to one anon design. Thanks a lot anon!
-Changed province 1315 - Chitaldroog RGO from Tea to Coffee. Changed 1312 - Pondicherry from grain to Tea. Changed 2186 - Guatemala from Fruits to Coffee.
-Fixed the localization of two Gran Colombia parties.
-The modifiers that remove RP on conquest for Qing will now happen as soon as the reforms are taken. It also includes any isolationist country, so isolationist countries will not gain the RP for conquest bonus that some reforms give.
-During the Cochinchina Campaign, Saigon should be turned in a coffee producing province to represent Europeans introducing the crop in Vietnam.
-Tweaked the last Child Labor reform a little bit.
-Stopped the crime "Rotten Boroughs" from happening in countries with no voting. It also won't happen in colonial provinces since they don't vote.
-Cleaned up the genocide events a little bit. Cut 8 events from the chain without any lost functionality or option.
-Added Ibadi as a religion. It's the main religion for Oman. The Shiite Bedouins in Oman were changed to Ibadi. The Mashriqi pops in Omani africa were also changed to Bedouin and Ibadi. Increased the proportion of sunnis in Oman proper.
-A few crimes that affect RGO/Factories will also affect artisans. Fixed the localization of Spoils System and Machine Politics. Both crimes, like Rotten Borroughs, only happen in provinces where there is voting: where valid voting pops in non colonial states in countries with voting are in.
-Changed Goa from Fruits to Tea. Changed provinces 2306 - Sorocaba and 2452 - Campinas to Coffee. Same thing for provinces 1439 - Flores and 1446 - Dili (these based on https://en.wikipedia.org/wiki/Coffee_production_in_Indonesia ).
-Farmers now consume a little more cattle than laborers.
-Changed 1323 - Kandy, 1322 - Jaffna and 1324 - Trincomalee from Tea to Coffee. In the 1870's production will change to tea after the rust disease devastate it. Based on https://en.wikipedia.org/wiki/Coffee_production_in_Sri_Lanka
-Swapped the pops of 2453 - Assis with 2306 - Sorocaba. It seems the numbers were inverted. Swapped 2458 - Coffee with 2457 - Fruits.
-Renamed 1991 from Uvira to Rusozi at the game start. Based on https://en.wikipedia.org/wiki/Bukavu
-Expanded the "Explore Congo" decision for Belgium to include more historical names. Added a decision to finish the historical names and to normalize LR in the Congo. The decision also changes province 1987 to iron and provinces 1991 and 1984 to precious metals.
-Going after Neuchatel will now give 25 infamy instead of 30.
-Fixed a bunch of wrong RGO positions in the RGO map mode.
-Changed PROVINCE_OVERSEAS_PENALTY from 0.025 to 0.015
-Added a decision to introduce cash crops (like Coffee and Tea) to Vietnam.
-Increased the number of slaves in the provinces Rio de Janeiro and Sao Paulo.
-Changed back GOLD_TO_CASH_RATE from 0.5 to 1.0
-The "Disloyal Regiment" event will not check the province average militancy, only the Soldiers militancy. If the soldiers fit the category and have more 5 or more militancy the event will fire. This will hopefully make the event take longer to fire and only ire when appropriate.
-Carlist/Christinos Sympathies modifiers will reduce the amount of pops that emigrate, to avoid Spain from depopulating.
-La Guardia Civil and the Scotland Yard modifier will now give administrative efficiency instead of tax efficiency.
-At the start of the game, GPs and SPs will start with more money. GPs (except for Spain and Ottomans) will start with 60K more, SPs (including GP Spain and Ottomans) will start with 30K more and civilized nations with more than 1 state (the ones with one state only get 5K) will start with 10K more and uncivs (except Qing) with 2.5K more.
-Like soldiers, Officers will consume ammunitions and small arms in their everyday needs.
-Jacobins, Communists, anarcho liberals and socialists breaking a country or overseeing a peaceful transition will now remove the Islamic Law modifier.
-Corrected an order of magnitude error for unit_start_experience in the Order NV and the Conscription reforms.
-Reworked the australian gold rushes after http://www.australianminesatlas.gov.au/history/index.html
-Made the Tangier International Zone more stable (less susceptible to fascists/communists/anarcho liberals and jingoism) and made an event to end it.
-The "Terrorist Cells" crime will only happen in provinces with a national minority.
-Changed 2027 - Nakuru production from coffee to tea. Changed 2177 - Oaxaca from Grain to Coffee. Changed 2554 - Misiones from Cattle to Tea. Changed 2213 - Port Au Prince from Tobacco to Coffee. Changed 1180 - Taizz and 1178 - Sana'a from Grain to Coffee. Changes are based mainly on http://cwh.ucsc.edu/brooks/coffee-site/1400-1800.html and other coffee production data.
-Changed the terrain from 1999 - Luanda from Plains to Farmlands.
-Shifted population density in Russia. Perm and Ufa population were cut in half while the west became more populous.
-Changed Base Supply Range (SUPPLY_RANGE) for ships from 200 to 50. Adjusted the Naval Science tree but supply range will be max 275 from vanilla's 320.
-Bali will no longer start lacking a writing system.
-1058 - Ekaterinbug, 1063 - Tomsk will start with precious metals. Redid the gold rushes for Russia. Bodaybo will eventually get a gold mine and gold rush. All this is based on "Russian Settlement in the North By Terence Armstrong", "The Chemistry of Gold Extraction By John Marsden, Iain House" and Beginnings of "Russian Industrialization, 1800-1860 By William L. Blackwell".
-Not supporting the Ottomans during the Ottoman Crisis will break any alliances with them.
-Changed a few Trucial States names and one flag. Now the trucial flag will be the flag of the absolute monarchy state, the UAE flag will serve as the flag of constitutional monarchies/republics and the country will be called United Arab Emirates.
-Ships of Uncivs without Post Nelsonian Thought invented will be less powerful than standard ships.
-Shuffled coffee provinces in Venezuela and Colombia. Dominican Republic and Cuba also produce coffee now, albeit in sparsely populated provinces.
-Changed Ternopil's name to Tarnopol, Lvov to Lemberg. Name will change back if the poles are expelled.
-Reworked the decision to normalize borders between Ukraine-Poland  to have more strict requirements and went back to using the move_pop to move pops.
-The Rich class now consumes tea as part of their everyday needs.
-Added a decision to smuggle tea into Persia. Based on https://upload.wikimedia.org/wikipedia/commons/6/60/Iran_land.jpg
-Added a decision to convert a few provinces in Turkey to tea. Based on http://www.economy.gov.tr/portal/content/conn/UCM/path/Contribution%20Folders/web_en/Home/Sectoral%20Reports%20and%20Statistics/Sectoral%20Reports/Agriculture/tea.pdf
-The short declaration will now only annex countries puppeted by the Netherlands.
-Forming Yugoslavia should now remove North Italian as accepted.
-Changed 2248 - Ibague, 2250 - Manizales and 2256 - Cali to Coffee to represent https://en.wikipedia.org/wiki/Colombian_coffee_growing_axis
-Annexing Hawaii through the decision will now change the island's RGO to coffee.
-Changed Puerto Rico production from Cotton to Coffee.
-Changed the production of 1455 - Manila from Fruits to Coffee. When coffee rust comes to the Philippines, the production will change to tobacoo. Based on https://en.wikipedia.org/wiki/Coffee_production_in_the_Philippines
-Changed the production of 1456 - Vigan from Grains to Tobacco. Changed 1457 - Legazipi from Fruit to Grain and 1460 - Iloilo from fish to fruits. Based on https://en.wikipedia.org/wiki/Smoking_in_the_Philippines#Tobacco_monopoly
-Increased the MTTH of event 12210 - The Old Man and The Sea and event 12220 -  All Tea in $COUNTRY$ from 1200 months to 2000.
-Changed the MTTH of the events that deal with the war time destruction of railways and forts from 500 days to 600 months. They also cover rebels sieging a province, not just units in battle.
-To balanced the 3 crimes that will never happen in countries with no voting, added 3 crimes for countries with no voting: Instigators, Kleptocrats
-Increased the MTTH of event 14620 - Civil Violence from NNM 600 to vanilla's 1000. Stopped the event from being able to fire multiple times in a short amount of time for the same state.
-Reduced starting literacy in Serbia from 4% to 3%. Based on Religious Separation and Political Intolerance in Bosnia-Herzegovina  By Mitja Velikonja, pp 312.
-Reintroduced the RGO spread events: Tractors province modifier will only only happen in provinces that produce tobacco, tea, coffee, grains, opium or cotton. It will also only happen in provinces that are plains, steppes, savannas, hills, dry hills, forests, farmlands or mountains. The bonus is 25%. Tractors invention not only unlocks that but it gives a 5% bonus to the output of these RGOs. The MTTH was increased from 800 to 1000, plurality effects where removed, it will take a lot longer to happen in colonial states and longer but not so much in slave states. It also has a 50% chance of adding the Tractors modifier to another state that has a province with 70% literacy and fill the normal conditions.
-Merged the RGO Spread events that dealt with Nitroglycerin and Machine Tools in a single event, but you still need nitroglycerin and machine tools. It only happens in provinces that have a mine (coal, sulphur, iron, oil and precious metals), that aren't treaty ports and are not Deserts/Semideserts/Tundras/Boreal Forests.
-Vanilla event 22580 - Railroad Trusts shouldn't happen in countries without railways and shouldn't remove railways from states without railways.
-Event 22530 - Local Railway Shares will only happed in countries with LF and will cost money. Made the vanilla EconomicalEvents make a little more sense - take money where they should, not spam so much, etc.
-Made Conquest CB also require you to have a port and the receiving nation have a port or the nation be a neighbor. Made most CBs require the same thing. Landlocked nations taking cores/states will also make more sense as you can only take neighboring provinces.
-Changed Gaslights to Gas Lights.
-Made the "Sign the Geneva Convention" decision remove some unciv modifiers as a cleanup measure. Sometimes the AI civilizes at the same time they get one of the unciv modifiers and they first "click" in the civilizing option and later on the event that gives them the modifier, making them have these modifiers forever. You will have a cooldown from civilizing and taking the "Geneva Convention" of 7 days to guarantee the AI won't get any more unciv modifiers before they clean it up a last time.
-Merged the 4 "Increase Conscription" decisions in a single one for all levels.
-Changed the events that deal with slave pop growth a little bit. Now the only requirement for a province to have a slave pop growth is it to be less than 75% slave.
-The event creating the Congo will give military reforms and the appropriate techs to build the units.
-The USA will lose Dixie as accepted if the CSA takes the "Second Declaration of Independence/Right to Secede" decision.
-Norway will start with Censored Press and UH based on population, based on https://www.stortinget.no/no/Stortinget-og-demokratiet/Lover-og-instrukser/Grunnloven-fra-1814/ http://www.nb.no/nbsok/nb/7b676fd0a90f95de3f7d6a2f807e49d6.nbdigital?lang=no#13 and http://www.nb.no/nbsok/nb/582c7e5546af35aef9080aee4e04fe5e?index=4#0
-Changed 828 - Edirne, 859 - Gallipoli and 858 - Kirklareli from grain to Tobacco. Changed 875 - Antalya from Grain to Fish. Changed 871 - Wool to Grain.
-In the mid 19th century, province 2058 - Moyo will being producing Precious Metals. Based on http://www.onlineresearchjournals.com/ijopagg/art/87.pdf
-Renamed Lake Malawi to Lake Nyasa.
-Fixed Malawai terrain. Should be way more hilly now. Based on https://upload.wikimedia.org/wikipedia/commons/1/15/Mozambique_Topography.png
-Organizing Malawai should change 2067 - Lilongwe production to tea and normalize their LR. Zomba will change its name to Blantyre if the region is colonized by the UK.
-Finished the "Organize Mozambique" decision so it renames more provinces if the Portuguese are the ones taking it. Fininished Mozambique's terrain, based on  https://upload.wikimedia.org/wikipedia/commons/1/15/Mozambique_Topography.png
-Increased the Farm RGO malus to efficiency in tundras, montane tundras and deserts from 20% to 40%. Boreal Forests were up to -30%. Farmlands will give a small bonus (+5%) to farm EGO efficiency. Mountains will give a small bonus (10%) to Mine Size.
-Fixed province borders in Zambia and the province of Songo to follow rivers better.
-Reshaped Jeddah a little bit.
-Finished Zambia's terrain based on https://upload.wikimedia.org/wikipedia/commons/3/3b/Zambia_Topography.png and https://upload.wikimedia.org/wikipedia/commons/f/f1/Map_of_Ecoregions_of_Zambia.PNG
-Fixed China staying a period without any conservative parties available.
-Genocide events should freeze core assimilation/removal events and remove any positive assimilation modifiers of these events.
-Added an option to do the Balkan Population exchanges with Turkey for all regions that start under ottoman control. For now it's only possible to make deals with Turkey, in the future deals such as Greece and Bulgaria will be possible. Doing a population exchange removes the Megali Idea decision and taking the Megali Idea decision removes the possibility of a population exchange.
-Slightly reduced the number of craftsmen in Belgium in the start date.
-Increased the number of Craftsmen in Switzerland to come close to Belgium and added a liquor distillery. Based on International Industrialization Levels from 1750 to 1980 by Paul Bairoch, pp 272.
-Changed aerial_bacteria_and_antiseptic_principle and Vaccination so it gives a +0.01% to pop growth, so the overall pop growth is the same as vanilla.
-Absolute monarchy France will now be called just "France" since the imperial title is associated not with a government type but with a dynasty.
-Artificial Fertilizers should not give a farm-wide bonus but only for farm RGOs that use fertilizer. The bonus was also increased from 2% to 5%.
-Changed the RGOs of Aosta and Novara from Wool and Cattle to Silk. Changed the RGO of Verona from Silk to Cattle. Based on "The Precocious Attempts at Industrialization of the Periphery, 1800-1870" By Jean Batou, pp 317: "It is, however, certain that Lombardo-Veneto and the Kingdom of Sardinia occupied first place in the Continent's production of raw silk"
-Added a winery and a silk factory to Turin, Piemonte, as well as 8K craftsmen and 25 capitalists. Based on http://e-archivo.uc3m.es/bitstream/handle/10016/16820/wp13-02.pdf;jsessionid=6AAB1409E0F423C6F43DA22FA8A95EB4?sequence=1 pp6: "Italy gained since the 1840s a world leadership in the production of machinery for the silk industry, which it maintained until the 1920s." and "Language Maintenance and Shift in Sardinia: A Case Study of Sardinian and Italian in Cagliari" by Maria Antonietta Marongiu.
-Fixed Sigmaringen having foreign investments.
-Changed French starting investment from 8000 in the Papal States to 6000 in the Papal States and 4000 in Sardinia-Piedmont.
-Portugal and the UK will now start allied. The UK also starts with 30K invested in Portugal. Spain start with lower relations and "Opposed" with Portugal.
-Statuto Albertino decision needs less militancy to be taken.
-End of the Liberal Revolution event will now give vanilla's 15 prestige instead of NNM's 25.
-Restored most output related techs/inventions from the industry part of the tech tree back to vanilla values.
-Made Coffee an everyday need for the lower, middle and rich strata. The middle and rich strata will try to consume canned food and more fruits and wool as part of their luxury needs. 
-Made the the "build the CNR" decisions for Canada cost less money but stopped it from "overbuilding" beyond tech and terrain constraints.
-To annex Hawaii through decisions you need your capital in South America, North America, Oceania, Asia or you need to own any province in Polynesia. You also need a port.
-To use the "end the Merina monarchy" decision you need a port.
-Halved the effect of transportation reform to colonial migration.
-If a country only has colonies in Tundras, Montane Tundras, Boreal Forests, Deserts, Semideserts, Islands and Jungles, that is, if a country colonies has no terrain but these terrains, pops will be way less likely to migrate to the colonies.
-The Senussi events will now happen to the owner of Benghazi rather than only for the Ottomans.
-All land military units now need Regular Clothes (except those that use luxury clothes) to be built and maintained and small quantities of Wool and clothes as supplies to repair their clothes, stockpile to dress wounds and etc. They also consume small quantities of liquor to go with their rations and tobacco for the front lines. The quantity changes the later the the unit is activated. Artillery now consume ammunition. Any unit that consumed liquor or wine to be built now consumes that as a maintenance need.
-Dragoons, Hussars and Cuirassier now consume grain (for their horses).
-Artillery, Planes and Tanks now consume ammunition.
-Clipper Transports, Frigates and Man'o'Wars consume clothes and canned foods, in different amounts. The ones that consume artillery also consume ammunition.
-Stopped Commerce Raiders/Ironclads from using less Artillery than frigates and man'o'war.
-Starting with Cruisers ships will also need tobacco. From Ironclad up ships also need, but at very small quantities.
-Since Cruises use fuel, battleships will also use fuel (but won't lose coal as a need).
-Irregulars/Cavalry also eat, but only grain. Cavalry don't use wine to be built, but double the grain of Irregulars.
-Uniting or creating Malaysia while owning Natuna will add Natuna as a core.
-A few techs in the Naval Engineering and Naval Leadership tree now give Colonial Prestige. Mission to civilize doesn't give any colonial prestige anymore.
-Changed the Colonial Range naval bases give per level from 50 to 25.
-Stopped a vanilla event from giving a Add to Sphere CB for SP nations against uncivs.
-Increase the tax efficiency from the ottoman oppression modifier from 0.03 to 0.05.
-Stopped event 14780 from bankrupting the AI.
-Dismantling the Netherlands should release Indonesia instead of distributing the islands.
-Changed Belgium's NV from productivity to Liberty.
-Artisans will require more cotton to produce fabric and more fabric to produce regular clothes.
-Changed the Guantanamo Lease to have more strict requirements. It will also remove cores if it is refused, but it will give a CB.
-Greater Ukraine decision should now give a core in Lublin instead of Nowy Sacz.
-Claiming Sakhalin and Ryukyu as Qing will now give these regions Chinese cores.
-Cutting the UK down to size will now unlock a post-war decision to claim the channel islands as France.
-Fixed the Megali Idea removing infamy instead of giving it.
-Fixed several wrong group modifiers in pop_types.txt
-Stopped Guangdong starting with communists in the UH.
-The events to flip fascist/communist governments during revolutions and for those governments to rebel against non fascist/communist governments were reworked to use just one CB to flip the government and puppet, so it can actually be done in just one war.
-Promotion/demotion chance from pops to Craftsmen will be severely reduced if Craftsmen unemployment is over 50%.
-Changed the "Coronation of Queen Victoria" a little bit. It will still fire even if Hanover isn't a UK puppet, in the small chance it isn't. It can fire from 1837 onwards when William IV dies and it will call an election in the UK. Adapted the event description a little bit to reflect the changes.
-Changed the average Swiss provinces LR from 40 to 35, except for Zurich and Bern. Switzerland got a decision to temporarily attract immigrants, based on https://en.wikipedia.org/wiki/Immigration_to_Switzerland
-Fixed "Anonymous Investor Business" being spelled as "Anynomous".
-Made sure the Treaty of Umtata can only be taken once.
-The event for conquering Sikkim should now give proper CBs.
-Changed Libya to be 2 states instead of 3. Fezzan was merged in Tripolitania. One of its province 1743 - Ghat was re-purposed as Nordhorn, in Hanover. Fixed province names in Libya and reshaped a few provinces, with the base on the original provinces submitted by one anon.
-The Occupation of Western Sahara by Spain should disappear when any GP gets the final colonization invention, to stop potential crisis form fucking up.
-Fixed two HPM danish events that had their localization mixed up.
-The Gold Coast Treaty with the Netherlands show now give Accra to the UK if the dutch own it.
-Merged the events for naming New Zealand provinces in the New Zealand Colony event, made it fire only once and adjust the NZL LR. Reshaped a few provinces in NZ to follow river borders better.
-Province 2081 will get a Namibian core when organizing Namibia or when trading it.
-Forming South Africa should now give the boer_republic modifier for a little while again.
-Forming Italy through a decision now should only give the free people CB if it is applicable (that is, if Italy holds non core provinces). Any decision/event that fires event 96165 - Italian Unification will now take 20 days to fire that event instead of happening instantaneously.
-Fixed starting party loyalty in the USA to match https://upload.wikimedia.org/wikipedia/commons/4/4b/1836_Electoral_Map.png and https://upload.wikimedia.org/wikipedia/commons/c/c7/PresidentialCounty1836.gif
-Reduced Liquor's base value from 6.4 to 6.2.
-Enacting Women's Suffrage will also increase the immigrant attraction of the country.
-Made poor pops fight more for Free Press in very high literacy (over 90%), consciousness (over 8) and if the pop is a primary/accept pop of a country with the liberty NV.
-Added another option for the "Dey's Insult" event.
-Abolishing Child Labor immigration attraction increased from 2% to 5%.
-Gave the Catholic Party of Switzerland Secularized instead of Pluralism in religious issues.
-Added a Freedom of Religion decision that can be taken by Switzerland. It stops all religious conversions, increase consciousness but decreases militancy.
-Fixed Switzerland's parties. Fixed the starting loyalty - Protestant cantons will start liberal while catholic cantons will start conservative. Based on https://en.wikipedia.org/wiki/Sonderbund_War
-Made sure Libya will not be a state when the Italo-Turkish war ends.
-The events for Liberia to get cores on the countryside will now happen even if Liberia doesn't exist, it will happen for the owner of Liberia instead.
-Countries that don't start theocratic and don't have the potential to become one through the formation of a new country will now flip to absolute government, to avoid improper theocratic governments.
-Genocide decision will now cost 100K.
-The other two RGO Spread Events - regarding distribution_channels and electrical_lighting were merged and are now represented as a single modifier. It needs both inventions, boosts both farm and mine output in 50% and can spread up to 3 states at the same time as long as literacy is over 70%. ALL RGO spread events will take longer to spread to overseas provinces.
-Added a decision for countries to commission an Ironclad. As long as someone has the necessary techs and goods and you have the necessary money, you will get it. It takes 1 years for the country that commissioned and 2 years for the country that answered the commission to be able to do it again.  The AI will only do commissions every other month, to stop it from spamming it.
-Changed the Bankruptcy events a little bit. Each event will now have a different description so it's more clear if it's a normal default or a small default. All events got more than one option on how to react to the bankruptcy, and you can now act on small debts at the cost of infamy. On normal bankruptcy, non-GPs will also get a gunboat CB instead of getting a cut down to size CB.
-Going bankrupt will allow the country to take over the Suez of the Panama Canal if the bankrupt country owns it, it's not a core and it's an overseas province. 
-Added the missing localization for HAVE_LESS_PORTS_THAN and HAVE_MORE_PORTS_THAN. Fixed localization for checking the number of ships.
-Reworked the LRs in Switzerland.
-Redid the LRs in the capitals of the countries in Russian control at the game start. They will now start at 40 LR instead of 35, including Moscow and St. Petersburg. All provinces in the Moscow Region will have 40 LR. Mostly based on https://www.marxists.org/glossary/media/places/u/ussr/1982/population.jpg
-Renaming Outer Manchuria should now increase the LR of Vladivostok/Haishenwai from 32 to 40.
-The Monroe Doctrine CB can now be used against any non American country, not just Europeans.
-Monarchy Romania and Republic Romania now use the same flag.
-Reworked the difficulty modifiers for harder difficulties.
-Added a decision and event for the lease of Port Arthur. Can be taken by any GP that owns Vladivostok and has the right techs.
-Corrected a LOT of typos in the NNM/HPM localization files.
-Added a decision for the Guano Islands Act. Any country holding Marcus, Portland and San Francisco or Hawaii can see it and take it, as long as it fills the other conditions.
-A peaceful resolution of the Arrow Incident should still give the UK a treaty port.
-Pops should now be way less inclined to move to the Sahara.
-The UK-Boer wars to annex Orange, Transvaal and Natalia should now end with these states as colonies and not full states. The AI will also be better at deciding what to do during these events.
-Chinese Treaty Ports should be exempt from the "our lands returned" events.
-Reduced the amount of British pops in the Cape Colony. It should be based off http://babel.hathitrust.org/cgi/pt?id=uc1.l0074071051;view=1up;seq=35 but the 1865 census only classify them as European, so it's a guess.
-Increased the amount of natives in Walvis Bay.
_______________________
V0.3.2.3 - 27/01/2016
America Minimod V3 Pastebin (Outdated and already integrated as of the latest version):
http://pastebin.com/mQ9iF4wZ

-Lowered the chance of rich strata pops being communists, both ideologically as well as joining rebels.
-Event 880200 - Grave Consequences, a result of the party scandal events, will no longer fire twice if the party in power wins the elections and the country still has the modifiers.
-Changed PROMOTION_ASSIMILATION_CHANCE from vanilla 0.5 to 0.3. Meaning a pop has roughly a chance in 3 of assimilating instead of having a chance in two when promoting.
-Changed the promotion hit of literacy for labourers, farmers and soldiers for craftsmen so they it's not possible to promote pops to craftsmen regardless of their literacy. The old values were were -14% for under 10% literacy, -9% for under 15%, -6% for under 20%, -4% for under 25% and -2% for under 30% literacy. The new values are -40%, -30%, -20%, -10%, -5%, respectively. This will also slow down quick industrialization in recently civilized countries with low literacy like India or China.
-Changed immigrant attraction NF from 30% effectiveness to 50%.
-Added missing vanilla localizations conditions for vassals.
-During the "Congo's destiny" event chain, added options to play as the Congo.
-Fixed a misspelling in the NNM flags for the Treaty of London events that would potentially allow the decision to be fired multiple times.
-Fixed one unit in Belgium's OOB starting.
-Fixed a broken pixel in Mbanza.
-Tweaked the Congo event chain a bit.
-Fixed the vanilla localization "Let the boys in blue have their way with these fermenters of revolution" to "Let the boys in blue have their way with these fomenters of revolution."
-Boer-formed South Africa should lose British as accepted.
-Integrated AFPG's flags for the Congo and Congo-Brazzaville. Congo especially only had 2 flags in vanilla.
-The Congo decision event chain now requires a country with at least 300K pops (1.2 million people), 2 states and at least 6 provinces.
-The Treaty of Simulambuko decision for Portugal will now give the sphere owner of the Kongo a chance to react.
-The Sulu Protectorate decision will now check if Sulu is in a sphere that is not from the one annexing it.
-Changed the colors of New Zealand and Australia to match national colors better. Changed Australian culture color. Changed the color of Afro Brazilian with Malagasy culture color to differentiate from Brazilian culture better.
-Fixed several vanilla instances of "peace offer" being spelled as "peaceoffer".
-Changed Taiwan's name from "Formosa" to Taiwan. Fixed NNM's Tajikistan being spelled as "Tajikstan". Added AFPG's Theocracy flag for Taiwan in case Theocratic Taiping moves to Taiwan. Changed "Xibei San Ma" presidential dictatorship name to Ma Clique and it's adjective from "Ma" to Hui.
-Fixed several events and decisions that were missing references to South America, the continent.
-St. Barths event will no longer give cores to the nation refusing France.
-Returned Easter Island and Hawaii to the north and south america continents. Fixed Hawaii's name being slightly off the island. 
-Fixed a misplaced effect that could cause labourers in colonial provinces to ignore soldiers restrictions.
-You can't encourage soldiers/officers in colonial provinces unless you take the decision "Reform the Colonial Army".
-Small reshaped in the border of Lucerne and Novara.
-Heligoland Treaty should give 2081 - Linyati/Luhonono in Namibia to Germany if England owns it. Fixed Heligoland treaty event chain not properly checking if germany didn't own Mombasa and consequently giving more than one state to the UK if they did. Removed the relation restrictions from the Heligoland Treaty.
-Added an event for the UK to conquer Luhonono.
-Changed the techs you need to demand concession in China from Mass Politics for countries not in Asia and Revolution and Counterrevolution for countries in Asia to Naval Directionism (with Local Military Government invention) and Naval Logistics (with radio telegraphy invention) respectively.
-Dominican Republic will now spawn with a general.
-Kobe in Japan will now only turn to gold once the owner is civilized.
-Made the gold rush modifier for countries fire with the gold rush modifier for provinces instead of firing in a separate event. Added the gold rush modifier for a few new world provinces where it wasn't happening.
-Changed Vanilla decision for Argentina's law of 1420 to give basic school system instead of RP. If the country already has basic school system the decision will vanish.
-Fixed Steppe terrain not showing its image properly.
-Made christians under the ottoman empire much harder to convert if they are in their own cores.
-Merged province 1724 - Tamanrasset with province 1718 - In Salah. Province 1724 was renamed Orkney & Shetland and used as a province for both islands.
-Merged 2589 - Shoyna in 985 - Mezen, Russia. Shoyna was reused as Tsushima in Japan. Added Tsushima as a treaty port.
-Changed pensions from vanilla 5%-10%-15%-20% to 25%-50%-75%-100%.
-Fixed a few problems with the Baltic States and related decisions.
-Made AI a little more aggressive on trying to modernize their navy. Made them try to get to the 5% soldier barrier.
-AI from countries in the new world will no longer try to get colonies through conquering uncivs unless they are not a democracy and have a jingoistic party.
-The Mandate of Heaven will no longer lower militancy, it will instead make rebels spawning less likely in chinese cores.
-Changed Xinjiang religion from Sunni to Mahayana.
-If Xinjiang goes fascist, they should lose uyghur as accepted. Integrated the event that removes irish as accepted from fascist UK in the fascist revolution events, so it doesn't need another event to fire.
-Fixed one event that could potentially lead to China declaring war on Japan with a Punitive Expedition CB, even though it wouldn't be applicable. Added a few more possible outcomes in case China doesn't own Taipei.
-Fixed Russia missing a core in province 719.
-Unite Wallachia and Moldavia will try to remove all cores of Walachia and Moldavia if they don't exist.
-Reshaped Gorlitz and Dresden to allow more historical borders for Saxony.
-A few map fixes: reduced the size of Frejus font, fixed RGO icon placement from the RGO map mode in Rimouski, Edmundston, Caribou, and Zante.
-Implemented AFPG's flags for the cliques of Yunnan, Guangxi, Ma Clique and Guangdon clique, for presidential dictatorships only.
-Fixed Guangdong starting with trinket healthcare.
-Reshaped the Bacau, Botosani, Suceava and Cernauti to follow more historical shapes and the river borders.
-Removed 4 (3 setup and 1 to remove a bonus when civilizing) events that could have their effects merged in other events without loss.
-Made Arkansas start as colonial instead of a state.
-Fixed Brittany starting with fascists in the UH.
-Fixed a few lost pixels in the Mozambique-Zimbabwe border.
-Fixed the vanilla "Edgardo Mortara" event for the papal states not showing up for theocratic papal states.
-Fixed a vanilla typo in the string NOT_IN_ELECTION_CAMPAIGN 
-Fixed a crash caused by clicking in London province after destroying the westminster clock tower.
-Cleaned the old Krakow Uprising event chain, merged two events in one, changed the effects a little bit. The event chain can now give Austria a core in krakow, to avoid the country being released later.
-Build the Germania Werft decision will now cost money.
-Guatemalan AI will now try to end Los Altos more aggressively.
-Added a decision for Guatemala/FRCA/Mexico to remove cores from Chiapas/Yucatan/Los Altos from their cores given the right conditions.
-Since the Caprivi Strip is now negotiated together with the Heligoland Treaty, the event chain will now try to prioritize german colonies outside namibia. If Germany ONLY has namibia in Africa, then the event chain will get those provinces. In case Germany has other colonies, germany will also get the Caprivi Strip. 
-Added a generic decision for buying the Caprivi Strip off the UK or whoever owns it.
-Expanded the Portuguese navy at the game start, especially in regards to transport ships.
-Removed the sea straits from Martinique, Marigot and Guadeloupe. Hopefully this will stop the UK AI from being so hellbent on starting huge wars with France for a few islands.
-Changed the punitive expedition CB to require 10 Warscore for peace instead of 7 and generate at max 5 infamy from the country justifying the CB. Tweaked the effects to stop the Qing empire from entering a rebel spiral.
-Changed the Dominican Republic annexation for the US to have a more active role by the USA rather than the Dominican Republic. Alsoc hanged so the CSA can take it.
-Changed PROVINCE_OVERSEAS_PENALTY from 0.05 to 0.025.
-Lowered the LR in Oregon and restored the old Oregon trail event. Hopefully will avoid UK-US global colonial wars.
-Integrated AFPG V7. Non used flags: POL_monarchy, NIC and GUA_republic. ITA_monarchy is used but it was modified. Thanks a lot for the flags AFPG!
-AI will try to leave the age of sail more aggressively once its 1855.
-The "All the Tea in $COUNTRY$" event will now not fire if there's ANY farmer unemployment in the province. Done so the event doesn't contribute to a global tea overproduction. It also doesn't make sense with unemployment. The event will also give money to aristocrats instead of capitalists since most probably there won't be any capitalists in the state. It gives the money to everyone equally if there's no aristocrats. Increased the MTTH to 1000 like the old man and the sea event. Gave the same treatment to the later and all similar events.
-Made so the naval_school modifier isn't permanent. Fixed the modifier never being given out properly.
-Blood and Iron mine modifier will now last for 40 years instead of forever.
-Fixed several problems in WorkPlaceEvents.txt, from events that could contribute to goods oversupply to events not firing properly, not having coherent effects or triggers. There were total 17 events that could never fire in the file.
-Fixed a few instances where you could move non new world countries to the new world to get immigration.
____________________________________________________________
V0.3.2.2
Hotfix: Fixed Djibuti life rating, fixed Debar missing cores from a few nations, renamed western slavic minor to Wends, fixed a map glitch in the Rwandan border with the Congo.
-Merged 1780 - Tichit with 1781 - Walata. 1780 will be used as the Macedonian province of Debar.
-Increased the percentage of Albanians in Macedonia from 8% to 13%, so it's closer to the actual number based on the first census of the region.
-"Revolutionary uprising" event for China will now not happen if the tag is a Constitutional Monarchy or Democracy.
-Changed San Francisco LR from 30 to 45.
-Reverted events 14650 and 14660 back to vanilla standards from the old NNM standards. Fixed the vanilla events not properly adding the modifiers.
-Fixed a few modifiers.
-Added Georgian political parties names made by MCG.
-Changed Bhutan units GFX from Indian to Asiatic.
-Made Los Angeles the capital of the California region. Purpose is to make the city grow more.
-Fixed the Neuchatel Revolution event not checking if Neuchatel exists.
-Fixed "The Bosnian Issue" event checking the Ottomans own Nicosia instead of Sarajevo.
-Restored Work Hours and Safety reform benefits back to vanilla levels.
-You now need 3 years in bankruptcy to clear all loans, from vanilla 2 years.
-Factories will now save up to 10000£ in reserves, from old HPM 5000£ and vanilla 1000£.
-Raised the small debt limit (limit which you don't get a CB if the nation defaults) from 10000£ to 25000£.
-Changed the percentage of how much of the factory leftover profit they pay to the pops and capitalists from 30% to 40%.
-Changed Economical issues effects a little bit. Tied it more closely with import cost.
-Changed the Minimum Wage reform values. Now it's 0-40-80-120-160.
-Finished the Chinese Party names. Fixed the parties ending before 1936. Added one conservative party.
-Added a Mandate of Heaven modifier that reduces militancy in China. For now the getting/losing the mandate is the same as it always was since NNM. In the future I hope to make it more dynamic.
-Merged province 1714 - Bechar with 1720 - Timimoun. The province is used as Santa Rosa (Santa Rosa de los Pastos Grandes) to properly represent bolivian claims and chile/bolivia/argentina disputes.
-Changed Officers to happen in state capitals only.
-Added a decision to found the International African Association during the Berlin Congress - the first step to get the Congo. European Secondary Power countries with low infamy and non colonial (or not having african colonies) can make a bid for it. The European GPs at the congress (except for Russia and Ottomans) will vote in the question and if the requirer gets at least 3 votes, the congress will assign them the Congo. If any nation owns Congo cores, it will be required to hand them over or face war. Colonizing Kananga's state will make the decision disappear.
-World Wars will now only be enabled if Great Wars are enabled.
-Corrected Lan Xang starting part not existing, which also caused problems in converters.
-Balanced the event for the fate of the bourgeois after a communist revolution. Now letting them live makes them pissed and wields less money while killing them gives infamy and wields more money.
-Fixed a bug in patriot rebels and potentially in other rebel types too. 
-Slavery isn't "next step only" anymore so a nation can go from slavery allowed to slavery outlawed and vice versa.
-Made a decision for Congo to move the capital to Boma.
-Fixed a few pops in Edmunston.
-Fixed a few problems in the Limburg/Neuchatel crisis. There's still some unresolved issues left.
-Changed Egg Harbor name to Camden.
-Added a tech school specific to Japan, added the ties in the technology files and added a decision for Japan to adopt the new tech school.
-Improved the vanilla tooltips for adding wargoals to explain a few situations better.
-Changed the Jingoism required for adding wargoals from 5% to 5.5%.
-Changed Bahrain Shias to be around 65% of the population
-Returned the caribbean islands to the vanilla west indies/lesser antilles. INtegrated the Leeward Antilles in the lesser antilles. Fixed the naval base position in Marigot. Changed St. Barths to Saint Barths.
-Fixed the Congo history files (several wrongs reforms like trinket health care and technologies while the country starts as an uncivs), fixed the country names (they will only be called Zaire if they are a presidential dictatorship, they will be called Democratic Republic of the Congo if they are a republic) and wrong flags (flag of zaire was used for republics, now it's only used for presidential dictatorship while the DPC is used for republics). Congo also start with all its pops as accepted.
-Fixed La Guarda Civil  Madoz's Deamortisation for Spain events sharing the same localization. Improved the description, stopped them from using the same image and improves the effects of the event. Madoz's event now only fires if you have under 30K in the treasury. Disabled the event 37708 La Guarda Civil since it dealt with something already covered through events, thus being redundant.
-Carlist Spain can no longer establish the Civil Guard, as it doesn't make sense according to the decision's description.
-Stopped Congo from using the european unit models and changed it to use the african unit models.
-Fixed positions for Edson, Canada.
-Changed the Persian Fascist party religious policy from moralism to Secularized.
-Added a missing picture for the Italo-Turkish war event chain and fixed a potential CB/War that could secede provinces that Turkey didn't own in Libya to Italy.
-Added missing localization for national_provinces_occupied.
-Stopped the Gadsden Purchase happening if the treaty of Guadalupe hidalgo wasn't signed or if Mexico has any cores on your land. This will avoid Mexico losing cores in the middle of nowhere and will avoid the treaty unless you don't own any mexican core. 
-Added an event chain for the Congo Free State. SP in europe can petition for the congo during the Berlin Conference, that's when the decision shows up. If you get it or not depends on the GPs votes and there's an event chain dealing with its destiny and exploitation.
-Fixed a bug that was causing Austria to have a ghost CB on NGF/Germany during unification and therefore made impossible for the two countries to ally with each other.
-Fixed Limburg and Neuchatel Crisis not ending properly if Prussia/NGF/Germany claimed the places.
-Fixed Montenegro army having no soldiers.
-Merged the Shilluk culture in the Luo culture.
-Changed African Minor culture color to a brownish color.
-Fixed Uganda pops. Instead of a sea of African Minor, it's majority Baganda in the south and majority Luo in the north. Made around 12% of the population sunni muslim. Based on modern data and http://img.static.reliefweb.int/sites/reliefweb.int/files/resources/25056AF8C870901EC1256F2D0047FCE8-uganda_ethno.jpg and https://upload.wikimedia.org/wikipedia/commons/5/57/Languages_of_Uganda.png
-Added the Lengu culture, representing the over a million speakers of https://en.wikipedia.org/wiki/Lendu_languages They reside primarily in Mungbane province of the Congo. Mostly based on the Ituri conflict.
-Fixed a few vanilla typos, including one in the heart of darkness event.
-Fixed Cartismo party not vanishing when the Partido Regenerador starts existing for Portugal.
-Added the Russian corridor in the caucasus.
-Added 10K Georgian sunni pops to Ardahan to represent the Laz. Based on http://www.tc-america.org/media/Forced_Displacement.pdf
-Restricted event 14700 to north america, south america, europe and australian nations who have a port.
-Reshaped Kustrin province.
-Changed 1377 - Tourane from its french colonial name to Da Nang. Reworked LR in Vietnam: before it was all 30 LR, now the LR varies between 40, 35, 34, 33 and 32 according to population density.
-Changed the asian minor pops in 1381 - Dong Quai from animist to sunni, to represent the Cham.
-Fixed Cambodia provinces having all LR 30 and basically no growth because of that. Based the LR on http://sedac.ciesin.columbia.edu/downloads/maps/gpw-v3/gpw-v3-population-density/khmdens.jpg
-Fixed wrong effects in the vanilla event 4302 "Wealth Based Voting". 
-Fixed the "Form Laos" decision firing a non existent event. Tweaked the decision to remove cores and changed naming for Laos so Laos is the standard name and Lan Xang is only for absolute monarchies.
-Fixes LR in Laos. Added a decision to move the capital to Vientiane. LR based on http://media-2.web.britannica.com/eb-media/60/128060-004-B53FD28F.jpg
-Fixed LR in Thailand, based on http://sedac.ciesin.columbia.edu/downloads/maps/grump-v1/grump-v1-population-density/thadens.jpg
-Readjusted LR in Malaysia with https://upload.wikimedia.org/wikipedia/commons/b/bb/Malaysia_population_density_2010b.png
-Fixed LR in Burma according to http://sedac.ciesin.columbia.edu/downloads/maps/grump-v1/grump-v1-population-density/mmrdens.jpg
-Stopped the Sahel Jihad event from firing against sunni countries. The event will only fire against non sunni countries.
-As long as you have the CFS as a vassal you won't be able to get the dark continent invention. If you become a GP though, the restriction is lifted away.
-Stopped Chad being colonizable from Outer Hausaland.
-Fixed the LR in the Phillipines.
-During dismantlement, colonial regions will now be distributed in a per state basis rather than a per province basis.
-Fixed a few cases where a unusable "add to sphere" CB could be given.
-Merged the ruanda and rundi cultures in one culture: Banyarwanda.
-Changed the representation of the Bantu cultures in the east of the Congo from African Minor to Kingwana.
-Adjusted the pops in the Congo. It used to start with around 10M people now it starts with around 20M people. Adjusted pops, adding sunni pops, new cultures, Ruandi and other cultures based on https://s-media-cache-ak0.pinimg.com/originals/92/97/c4/9297c476366a96e33e2f8b309367bfbe.gif Pop density was mainly based on http://sedac.ciesin.columbia.edu/downloads/maps/gpw-v3/gpw-v3-population-density/coddens.jpg while proportion was based on modern data.
-Added the Chokwe as a culture for the Congo and Angola. They represent also represent the Lovale. Distribution based on https://s-media-cache-ak0.pinimg.com/originals/92/97/c4/9297c476366a96e33e2f8b309367bfbe.gif and https://upload.wikimedia.org/wikipedia/commons/e/e2/Angola_tribes_1970.jpg
-Changed the "GOLD_TO_CASH_RATE" from HPM's 1.0 back to vanilla's 0.5. This is the amount of money generated per gold unit.
-Changed PROVINCE_OVERSEAS_PENALTY from vanilla's 0.005 to 0.05. This will increase the costs of overseas provinces by increasing the amount of required goods, meaning colonial countries need to buy more clippers and steamers, increasing the production and consumption of these products as well as steel and others goods used in their production.
-Changed UNCIV_TECH_SPREAD_MAX and MIN from vanilla's 0.60 to 0.15 and from 0.15 to 0.10 for MIN. In practice, this means that uncivs that westernize later in the game won't start with a lot of free techs, they will have to research them.
-Changed tech_year_span from vanilla 140 to 150. Basically meaning that techs old techs get less cheaper as time passes.
-Changed how the "Integrate Albania" in Yugoslavia event works. It will give Yugoslavia Albanian cores if you own the provinces or if the owner is your vassal and it will give an ultimatum if the country that owns the cores is in your sphere.
-Added a decision for civilized countries with the capital in Africa or the Near East to get Djibouti if they border them and fulfill the requirements.
-Added two new "continents" to act as regions: Polynesia and Oceania. Since the number of nations covered in these territories is small and due to engine limitations, these regions will have no buttons in the diplomacy screen. The main purpose of these new regions is to even out influences in these regions away from Asia and guarantee that overseas maintenance is paid.
-Removed the two Aden to Africa sea straits.
-The only sea strait across Gibraltar connects Tangiers to Cadiz.
-Added a decision and events to deal with the Tangier Protocol.
-Democratic Arab Union will be called United Arab States.
-Hodeida will now start controlled by North Yemen, since according to https://en.wikipedia.org/wiki/Mutawakkilite_Kingdom_of_Yemen the province should only be conquered in 1849.
-Unciv reforms that lower militancy will only do so in non-colonial.
-Extinguished Dry Grassland and added Steppe and Savanna terrain types.
-Adjusted Terrain in SA that should be savanna and in africa, according to https://www.nsf.gov/news/mmg/media/images/savanna3_h.jpg
-Safari events only happen in Savanna terrain now.
-Fixed Awsa spelling to Asaita.
-Fixed typos and inconsistencies in the budget screen tooltips.
-The Asaita province was changed from mountains to desert, to represent the Afar depression and the Danakil Desert.
-Fixed Somalia terrain according to http://www.eoearth.org/view/article/51cbeee87896bb431f69b16c/
-Fixed terrain in Kenya according to https://upload.wikimedia.org/wikipedia/commons/4/45/Kenya_Topography.png and http://www.eoearth.org/view/article/154013/
-Reshaped Nairobi, Nakuru, Kisumu, Lodwar, Garissa in Kenya to follow natural features and Kismayo in Somalia to follow rivers. Fixed Seychelles name being too small.
-Reshaped Mwanza, fixed its terrain, fixed it having a naval base.
-Fixed Tanzania terrain based on https://upload.wikimedia.org/wikipedia/commons/8/87/Tanzania_Topography.png and http://www.eoearth.org/view/article/51cbef007896bb431f69bc01/
-Fixed Uganda's terrain based on http://www.eoearth.org/view/article/51cbef1e7896bb431f69c81d/
____________________________________________________________
V0.3.2.1 Beta
-Fixed a bunch of wrong localizations in the USA/Mexico.
-Adapted the Deseret Irredentist decision to the new provinces in the USA.
-In light of the recent AI rework and taking into account the fact that Oceania has 4 tags, changed the Middle East continent from using the South America slot to use the Oceania slot. Adapted all modifiers accordingly. Hopefully this will also help the USA AI focusing on south america before going over the world for influence.
____________________________________________________________
V0.3.2 Beta
-Changed Beifaren and Nanfaren to "South Han" and "North Han", according to a request and poll. Mainly for consistency sake.
-Changed the colors of Dagestani and Chechen cultures to be less similar to other cultures.
-Rebalanced the initial supply for the 4 basic food RGOs based on tech bonus.
-Changed Alexandria RGO from Cotton to Fish.
-Changed Curacao and Aruba terrain to Island terrain.
-Rebalanced the event that happens for mobilization in times of peace. Mobilizing for long during peace should be considered an act of war by the mobilizing country neighbors that dislike them (< -50 relations) and they will get a free CB on the threatening country.
-Corrected a few typos in the vanilla localization.
-Countries with a L-F ruling party can no longer nationalize their industry.
-"Petitioning to join the FRCA" will no longer be available if the FRCA has a rebellion. Also fixes the bugs caused by playing Panama at the game start and taking the decision.
-Applying for Statehood (in the USA besides the FRCA) now requires the receiving nation (USA, FRCA) to not have any active rebels, less average militancy than 5 and no more than 70% infamy (17.50). Basically, the country needs to be stable and reputed.
-Fixed a vanilla province being called "Equia" and changed it to its real name, Uquia.
-Changed the government name "Democracy" to "Republic", fixed several inconsistencies in the vanilla localization of cultures and mapmodes.
-Changed Livorno back to Leghorn.
-Fixed Taiping starting with Trinket Healthcare.
-Italo-Turkish war event chain will now not happen if Italy is a puppet and/or if it doesn't own Rome.
-Peacetime Mobilization event won't fire for countries with less than 10 military score and rebel units in their cores.
-Integrated the america minimod. A few things were left out: California cores were not removed from the game start. Mainly for people who want to play as that and for the bear flag revolt. Didn't change cotton RGOs around nor increased the starting price of cotton. Balance changes like that will be done later.
-Rebalanced a few triggered modifiers.
-Fixed a typo in the production NV decision.
-Merged Inner Mauritania with Mauritania in one region.
-Merged Sahara and Saoura regions in one region.
-Changed Tonga to Island terrain.
-Removed Congress Poland cores from Bialystok and added to Marijampole.
-Made the game compatible with version 3.04 Beta of HoD.
-Contrary to patch 3.04, you will still get a hit to relation if a country defaults on a small debt with you (small being less than 10000£). You don't get a CB, as it was in vanilla.
-Disabled the event allowing you to skip election events as it was conflicting with the new update. Hopefully will be reinstated soon.
-A released Scotland will have its capital converted to Scottish culture so it can spread through the country.
____________________________________________________________
V0.3.1.8 Beta
-Added a sea strait connecting Biak to Merah
-Changed the decision to expel the manchu from Primorye/Amur to include nanfaren/beifaren pops if there are any.
-Migrating pops will now try to avoid countries at war.
-Added a few hausa and muslim pops to Ilorin based on https://en.wikipedia.org/wiki/Ilorin_Emirate
-Change 1936 name from Makurdi to Nsukka. Removed Tiv as accepted from Sokoto caliphate, added to Aro and changed the province ownership to the Aro.
-Added a few Fulbe pops to Gombe based on https://en.wikipedia.org/wiki/Gombe_Emirate
-Changed Lokoja name to Idah, it starts under Benin rule.
-Added small muslim croat communities to Croatia and Bosnia, based on https://en.wikipedia.org/wiki/Croat_Muslims and https://en.wikipedia.org/wiki/Islam_in_Croatia. Around 700 sunni croat pops are spread through croatia.
-Changed a few albanians and bosnkiaks to sunni serbs in Ulcinj and Pljevlja - total 1.1K pops. Added a few sunni gypsy's - total 200 pops. Added a few catholic albanians and serbs to Kotor - 350 pops each. Based on https://en.wikipedia.org/wiki/Roman_Catholicism_in_Montenegro http://www.coe.int/t/dg4/education/ibp/source/FS_1_10.5.pdf https://en.wikipedia.org/wiki/Islam_in_Montenegro https://en.wikipedia.org/wiki/Demographic_history_of_Montenegro
-Added a few serb muslims in southern serbia and Kosovo, as well as a few sunni gypsys. 2600 serb pops were converted to sunni and 1500 bosniaks were converted to serb sunnis. 600 gypsys in kosovo were added. They represent slav muslims, gorani and other non bosniak converts. Based on https://en.wikipedia.org/wiki/Slavic_Muslims https://en.wikipedia.org/wiki/Islam_in_Serbia
-Added 2500 serb catholic pops in Vojvodina. Based on https://en.wikipedia.org/wiki/Roman_Catholicism_in_Serbia
-Converted 6k Bulgarian pops in Bitola (Macedonia) to sunni to represent https://en.wikipedia.org/wiki/Macedonian_Muslims / https://en.wikipedia.org/wiki/Pomaks. Added a few orthodox serbs and sunni serbs to Bitola. Based onhttps://upload.wikimedia.org/wikipedia/commons/c/cf/Makedonien_ethnisch_%281892%29.JPG
-Added a few muslim greek pops to Florina and Grevena. Based on https://en.wikipedia.org/wiki/Vallahades and https://upload.wikimedia.org/wikipedia/commons/c/cf/Makedonien_ethnisch_%281892%29.JPG
-Fixed a few wrong positions in two provinces in the brazilian amazon.
-Added a few romanian catholics to austrian romania and very few romanian sunnis to Constanta.
-Reworked party names and issues in Italy and S-P. Based on https://it.wikipedia.org/wiki/Sinistra_storica https://en.wikipedia.org/wiki/The_Extreme and https://it.wikipedia.org/wiki/Destra_storica
-The Swiss will break their neutrality if they end a communist or fascist dictatorship.
-Russia and the Ottoman Empire will now start in an alliance, to follow the https://en.wikipedia.org/wiki/Treaty_of_H%C3%BCnk%C3%A2r_%C4%B0skelesi
-Dayr Al-Zour, in Syria, will now start in the hands of Egypt since they conquered Syria in the 1831 Egyptian-Ottoman War.
-Changed Bakel to start under Gabu based on https://fr.wikipedia.org/wiki/Fouladou
-The UK will now start with Child Labor restricted, based on chimney sweepers and 1833 factory laws they passed.
-Adjusted the intellectual numbers in Egypt and France a little bit. 
-Fixed the AI being too obsessed with certain commerce techs.
-Bosniaks can't become accepted in Yugoslavia anymore.
-Theocratic Yugoslavia can't accept any additional pops.
-Removed British as accepted for Newfoundland.
-You can't use the immigration focus if you only have one state anymore.
-Jamaica will no longer started uncivilized.
-Stopped San Diego changing between Oil and Precious metal non stop.
-Fixed Chesapeake Bay sea province location.
-Stopped the AI spamming the Austrian-Hungarian border treaty.
-If you don't own East Bengal when forming Pakistan, it won't add cores to it. The Bengali tag will now turn to Bangladesh too. Corrected the democracy flag.
-Mughals don't get the "Stirring of Indian Nationalism" events. However, they get less cores (a little more than their extent in the 18th century) and they also get less accepted cultures, mainly the ones who didn't have muslim pops were excluded.
-Fixed Madagascar starting with trinket healtchare.
-Fixed French-Canadians in Caribou being Protestant.
-Fixed Senussi event not giving proper CBs if you don't choose to go to war.
-Fixed Zayidi event for the Ottomans not giving the proper CBs and resulting in infamy gain.
-Changed Sherman's march to the sea decision a little bit.
-New England doesn't have Dixie as accepted anymore.
-Fixed pops religion in Edmunston.
-Tweaked pops in Bacalar.
-During the Panthay Rebellion Pingnan Guo shouldn't be at war with Taiping anymore. Same thing for the Dungan Revolts.
-Retreating to Formosa should keep theocratic government and should include Penghu.
-Fixed the Greater Ukraine decision not giving cores on Belgorod.
-The Railway reform will now carry over the tech when you civilize, always. In return, it costs money and it builds railways on the capital ONLY, not on the whole state capital.
-The factory unciv reforms will also cost the basic cost of building then, money only. Also inverted the factories built (Early Industrialization builds cement factories, Industrial Construction build textile mills) seeing as Textile MIlls cost more money and are considered less of a basic factory.
-Implemented AFPG Argentine Confederation flags.
-Changed the Guild Unciv Reform to a Firearms Production Reform, giving a tech and a small arms factory.
-Fixed a vanilla localization dealing with line breakup after the string about building something.
-Corrected another vanilla localization about money not showing the £ sign.
-Fixed the Argentine Confederation not getting the "Rosas Victory" event in the case Entre-Rios backed out of the rebellion.
-Stopped the event to stop the carlist wars from firing for any country.
-Building the Canals will not give you a core there anymore and the canal provinces won't be returned in 'our lands returned' event.
-Changed Falklands terrain to Small Island and removed the port they had. This is meant to fix the British sometimes going for Patagonia. While the Falklands is a large island, it only has very few habitable and cultivable space, so I'm going for that.
-Corrected several NNM misspellings (Phillipines instead of Philippines)
-Made the event for the USA proposing to buy Cuba into a decision.
-Enforcing the CB on Egypt during the Oriental Crisis should result in a net prestige of -5 (counting the prestige they lose when the crisis start and the one they get for integrating Egypt, not counting the surrender event or the events when countries join).
-Ostend Manifesto will now give the proper CBs on Cuba even if the state is not colonial and it will make the AI declare war for Cuba.
-Fixed Manchuria having a few social reforms.
-Fixed a few wrong things in the Armenian Genocide decision.
-Changed the religion of the African pops in St Thomas from catholic to protestant.
-Removed Amazonian as accepted from a few countries.
-Made sure Luxembourg loses its core on Arlon. It was causing some problems in the formation of Germany.
-Stopped the "northern islands" event from firing over and over if Ezo owned Hokkaido.
-Consolidated the three decisions to rename Port Arthur/Lushun/Ryojun in one decision for all, it changes the name according to the country that uses it.
-Changed Greek culture color to the greek blue.
-Fixed a problem with reforming the FRCA and spheres that would turn the spherelings into the tag that enacted the decision and separate of the FRCA.
-The AI Sweden won't abandon Finland anymore if they own Finnish cores.
-Set the UK starting party loyalty for 1836 to match the 1837 election results. Based on https://en.wikipedia.org/wiki/United_Kingdom_general_election,_1837
-Stopped Portage going for New England if the UK signs the Webster-Ashburton Treaty with them.
-Made Outer Manchuria one region again. The Amur region is now a small 3 state region north of it.
-Corrected "last election" parameter for the UK and the USA.
-Fixed Dreyfus affair vanilla event issue change effect not working.
-Added a decision for countries in the America so they are able to add the natives as accepted.
-Forming La Plata no longer peacefully integrates Bolivia if you sphere them. It also doesn't give cores in Acre/Tarauca, Calama, Iguatemi and Antofagasta.
-Integrating Lithuania in the UBD should no longer cede a nation core provinces. It means Germany doing it won't add a UBD core in Memel nor cede the province to the UBD.
-Fixed a few graphical glitches around Loreto.
-The Sanitarium event and modifier will now give pop growth, but just for 10 years and the options will do what they imply they do (take money from the rich strata, etc).
-Added a decision for Banat to get cores on Novi Sad.
-You can no longer use the Ostend Manifesto decision if you own Cuba.
-Balanced industry techs to try and avoid overproduction of steel and under supply of basic goods for uncivs.
-Changed Hainan RGO from Lumber to Fish.
-Punitive Expedition should add and take less prestige.
-Reverted all the values for the RGO increase in the Power tree of the Industry tab back to vanilla levels. Now the tree will boost and apply malus to specific goods to try and balance production and supply better.
____________________________________________________________
V0.3.1.7
-Fixed typos and bad descriptions in a few events.
-Fixed a few lost pixels in Canada and some weird positions for railroads.
-To avoid weird behavior, the Russification of Finland decision now gives Russia cores on Finland.
-You need at least level 5 railroad tech to build a railroad in a Tundra, or Taiga terrain. Before, it was 4. The max level of railroads in these provinces is now 2.
-Corrected a very old vanilla bug with how pops choose countries to migrate. When they checked for unemployment, they checked for farmers, laborers but when they were supposed to check for craftsmen, they checked for farmers again.
-Fixed Terrain in Canada and adjusted the LR of some canadians provinces to stop huge population booms. Based on http://www.fao.org/ag/AGP/AGPC/doc/counprof/Canada/pics/fig7.jpg https://upload.wikimedia.org/wikipedia/commons/6/68/Canada_BMNG.png and https://www.ec.gc.ca/eau-water/3E75BC40-74F5-4BF9-BB3B-3F3A761EBE8D/a9f1e.gif
-Fixed Canadian Pacific Cordillera.
-Integrated AFP V6.
-Preliminary fixes in the LR and terrain of Scandinavia and Siberia.
-Slightly increased Qing starting literacy.
-Stopped the AI from researching techs for bigger ships without researching techs for the ports to build them in the first place. They will also not research the other techs before they get bigger ships and better naval bases.
-Fixed the AI caring too much about the Metallurgy tree just because they owned one province of Coal/iron/Sulphur. Made it care a little more about researching railroads.
-The Ottoman Empire will react a little more aggressively to the Megali Idea now.
-Fixed events for France and Portugal not giving the proper Establish Protectorate CBs.
-Stopped the Transvaal and Orange events firing for Dutch-released South Africa.
-Changed Ulusamudan name to Hailanpao. https://en.wikipedia.org/wiki/Blagoveshchensk
-Reshaped provinces around Tynda to allow to the Aigun treaty borders properly, based on https://upload.wikimedia.org/wikipedia/commons/1/11/China_USSR_E_88.jpg and https://en.wikipedia.org/wiki/Stanovoy_Range and https://upload.wikimedia.org/wikipedia/commons/e/ed/John-Tallis-1851-Tibet-Mongolia-and-Manchuria-NE.jpg
-Reshaped Qiqihar - Ninguta border to follow the river more.
-Changed the decisions relate to Outer Manchuria for Russia, changed the regions, added appropriate names and name changes.	
-Fixed multiple extra quotes on the "Benefits Exploited" vanilla event.
-Fixed a few vanilla instances for add wargoal and war descriptions where "achieve" was misspelled as "achive".
-Changed a few CBs in the platine wars to avoid countries prestige spamming to GP.
-Fixed arabia starting with no party in power.
-Fixed the decision to form Arabia externally not seceding all provinces correctly.
-Stopped the Italo-Turkish war from happening if Italy is a democracy, a communist dictatorship or if it has a pacifist/anti-military party in power.
-Fixed a bunch of Chinese substates using the generic sprites instead of using the Chinese sprites. Changed so that mongolia use the "asian" sprites rather than the generic sprites. Fixed a bunch of parties activating too late or deactivating too soon in chinese substates.
-Changed the Panthay Rebellion a little bit to represent the Muslim project in case it succeeds.
-Added custom names for the Dungan Revolts and Panthay rebellion wars. Added a custom name for the Italo-Turkish War and a few other wars.
-Durban should now be named Pietermaritzburg when Natalia forms.
-Made the AI take into account the prussian_tech_school when selecting techs. Before, only the four basic tech schools were taken into account and the AI would lose their direction a little bit when changing to prussian_tech_school.
-Nations with overseas provinces should now more aggressively try to modernize their navy and build bigger ships.
-Fixed a bug in the Unification CBs (not related to the bug where Germany keeps a ghost CB on A-H).
____________________________________________________________
V0.3.1.6
-Changed Mongolia to start as a Vassal rather than a Substate.
-Unciv rebels should add the war torn modifier for 30 days instead of 365 and should no longer kill 20% of the rich strata but only 1%. This is made to avoid unciv countries being depopulated.
-Stopped the Saudi-Rashid civil war events firing when the countries don't have a single brigade. They need at least one brigade so the event can fire. This is meant to stop eternal wars with no winners because no one has an army.
-Fixed the "Form Saudi Arabia" decision not giving cores on Qatar and the Yemeni minors.
-Fixed a few instances of descriptions that used "the $COUNTRY$" that could end up in a double "the".
-Balanced Taiping nationalism events to be more reasonable in the chinese cores (in regards to militancy and people killed).
-Changed one of the "Taiping missionaries" in state event options killing 2% of all non manchu pops, it will not only kill 1%. Defeating the Taiping also burns more militancy (from -4 to -6) and it kills a random number of people (10%, 8%, 6% or 4%) rather than the old fixed number of 10%. The Militancy and Consciousness given in the case of a Taiping victory reduced from 5 to 1 and 3 respectively.
-Shuffled a few provinces around Burma and Siam to remove the old Shan state that was divided between Burma and Siam, usually causing Siam to go on a conquering spree on Burma. 
-Added a decision for the founding of Yadanabon (Mandalay).
-Fixed the position of a bunch of capitals.
-Fixed Manchukuo having no capital (actually, the capital was in the middle of Mongolia), now they start with their capital in Jilin. Fixed Xinhai and Qinghai capitals.
-Added option to tagswitch to Kashgaria during the Dungan Revolt.
-Renamed Balekungomi to Xining. (https://en.wikipedia.org/wiki/Qinghai#History - "It was during the 1720s when Xining Prefecture was established and its borders were roughly those of modern Qinghai province. Xining, the capital of modern Qinghai province was built in this period as the administrative center.")
-Added events for the Dungan Revolt of 1895–96 and Qinghai. The Qing should annex Qinghai after that.
-Fixed theocracies not being able to implement Islamic law.
-Presidential Dictatorships can also pass Islamic Law.
-Changed the Greater Mongolia decision to give more aesthetically pleasing cores. It also costs a lot of infamy.
-Fixed typos in the Peking Convention for Russia. Fixed the decision requiring Russia to sphere the Qing and the Qing AI response depending on Russia sphering the Qing or not, since it's impossible to sphere the Qing. These things will now depend on WE and if RUssia sphered Manchuria or not. On the end of the event chain when they cede the territory to Russia, the Qing will now annex Manchuria to represent "The Manchu emperors separated their homeland in Jilin and Heilongjiang from the Han Liaoning province with the Willow Palisade. This ethnic division continued until the Qing dynasty encouraged massive immigration of Han in the 19th century during Chuang Guandong to prevent the Russians from seizing the area from the Qing."
-Removed the vanilla Matsuyama Strait that connected Shikoku to Kyushu.
-Stopped the Czechoslovakia union from happening if they are in the different spheres.
-Reshaped Kumul to represent the Kumul Khanate borders better.
-Improved the Mfecane event description.
-Excluded the Sikhs from the decision to form India.
-Renamed and reshaped a few sea provinces in Hokkaido so it's more clear what provinecs allows for marching through and can be blocked.
-Changed the religion of a few Beifaren pops in Tibet, Mongolia and Inner Mongolia to Gelugpa.
-Changed the Literacy decision for uncivs without literacy a little bit.
-Independence rebels (the ones who try to break the overlord-vassal relationship) now only happen in accepted/primary pops.
-The Unification CBs to annex or take states will no longer be valid against GPs.
-The PBC will now get an event to change their capital (or not) once they unite.
-Germany that hasn't their capital in Berlin or Munich will get an event to choose their capital (or not).
-Spain doesn't start with cores on Fernando Pó anymore.
-Restored the reshaped Patagonia back to vanilla shapes.
-Fixed colonizing Christmas Islands giving Western Australia too.
-Fixed a few flags not being set right in the case of the Baltic Provinces and the second tonghak reforms not working as it should.
-Made the AI try to build big ships more.
-Changed how the Physics Nobel prizes work and added custom descriptions for all of them. Now you don't need only prestige or to be a GP, but there are literacy limits. A GP needs at least 55% literacy to try and run for a Nobel. Europeans GPs with high literacy (and lots of pops) also have a higher chance of getting it. Eventually, all the other Nobel categories will get the same treatment. Some Nobel's require specific inventions (like quantum theory or x-rays). Having repressive regimes with no meetings, low plurality or state press also reduces the chances of getting a Nobel in physics
-Stopped the Nobel prizes never happening if Sweden doesn't exist (that is, if Scandinavia forms).
-Fixed a very old vanilla bug that was stopping 116 Nobel prize events - basically all Nobel's after the sixth one - to fire.
-D.C. shouldn't no longer go to the CSA once the civil war starts.
-You no longer get the same colonial troop potential as your non colonial states. Colonial provinces can have only up to 1% soldiers, 2% if they are not animists and you take a decision.
-Added events for the sphere owner of Tunisia to conquer them if Tunisia is running low on money after 1870 and is uncivilized.
-You can no longer win a Nobel peace prize if your infamy is too high or if you are at war.
-Added a decision for the invasion of Tunisia if they are near bankruptcy and their sphere owner has N&I.
-Added a decision to modify the government of any countries you own (in you own their capital), setting the same political reforms as you for them.
-Non-Treaty Port Precious Metals provinces with more than 600K pops in civilized countries will now flip to a basic RGO after some time.
-Reduced the number of communist/anarcho-liberals/fascist rebels and ideology in animist pops in colonies.
____________________________________________________________
V0.3.1.5
-Fixed Ribe being way off the right place and the schewslig border. Thanks for the anon who pointed it out.
-Added Fehmarn island to Kiel Province. It was in vanilla but it didn't show up because the color was different than the color of Kiel.
-Increased Jewish/Islam/Mormon malus to conversion.
-You can't move the political parties reform as long as you have no voting.
-Reshaped Griqualand/Kimberley.
-Reshaped Calvinia.
-Added the Kalahari and Namib deserts, fixed the terrain in Namibia, Botswana, Zimbabwe and parts of South Africa.
-Reshaped Masvingo to follow the shape of Umtali and the mountain range.
-Fixed Madagascar terrain. Now it has jungles. Fixed the coast a little bit and a double river.
-Changed Moçamedes from Farmlands to Semidesert. Reworked the terrain of Angola. Moçamedes also start uncolonized and the owner of Benguela have a decision to colonize it.
-Added the Highveld to South Africa. Before, it was all mountains.
-Added a few protestant native pops to Windhoek to represent Jonker Afrikaner.
-Reworked names in Namibia. All names should change as colonization goes.
-Beaufort will start under English rule in 1836.
-Reduced Scramble for Africa CBs truce timer from 2 years to one year.
-Fixed Caribou being considered a port province.
-Cuba and Ukraine now should move their capitals to their historical counterparts if they own it and they are not the capital. Kamchatka will also move their capital to Vladivostok if they can.
-The Transvaal event should rename two provinces it didn't change the before.
-Renamed Thohoyandu - a town founded in 1977 - to Tsaneng.
-A lot of countries with native or wrong names were renamed in South Africa. All of them have a way of changing their name for modern names at some point or the other, so most of South Africa will use european names by late game except for 
-France can only gift the USA the statue if the USA abolished slavery.
-Angra Pequena in Namibia southern coast will start with precious metal RGO instead of flipping later.
-Fixed Okinawa Islands glitches.
-Reduced the size of South Atlantic Islands.
-Removed Cocos and integrated it with Christimas. Reshaped Cocos. Repurposed it as Penghu, in Taiwan.
-Fixed the terrain of Taiwan.
-Fixed a bug that was stopping the Cede Aden decision from working properly when Aden was not owned by you.
-Fixed West Virgina Slave and Freed Slaves population based on https://en.wikipedia.org/wiki/History_of_slavery_in_West_Virginia. Thanks anon.
-Added a decision to add an australian core in Christmas and Cocos.
-SUPPLY_RANGE reduced from 250 to 200.
-Restored the button to the trade screen that allows pops to buy from the country stockpile. Added a description on how to use it and how not to use it. Use it at your own risk.
-Fixed a few typos in the Bedr Khan event.
-Fixed the Greater Assyria decision missing one core in a new province.
-Make AI research education techs more agressively up to biologism.
-Moved Cape Verde to Macaronesia region.
-Added a decision for the conquest of the Ivory Coast for the owner of Grand Bassam.
-Tweaked a few values for the HPM fascist/communist decisions.
-Extinguished the old Griqualand state and integrated in the Northern Cape state. Moved Beaufort to the cape colony state.
-Fixed the event for the Natalia Republic not checking the right owner of the cape colony and assuming the UK was the owner. Balanced the Accepted the Boer decision to require more money.
-Stopped the French Indochina events from giving CBs on Champasak.
-Added one decision for the French to take Champasak if they have a truce with them (and N&I).
-Hid the Tech Schools under a decision. You can toggle it on or off and it disappears once you choose a tech school.
-Jacobins and Socialist rebels will now abolish slavery and set the the Voting System to Proportional Representation on winning.
-Changed Saxony and Westfalen religion to Catholic.
-Added a decision to Organize Guinea-Bissau, reutilized the Gabu tag for it.
-Changed Hazara and Kashmiri culture colors to be more distrinct form each other.
-Stopped the AI aggresively researching NF techs when they can't use more NFs.
-Stopped the AI going too aggresively for Metallurgy tech tree.
-Capitalized "Sea Power & The Marchant Marine"
-Fixed a bug in the poptypes that was stopping pops from picking issues.
-Tweaked the Hormuz Strait triggered modifier effects.
-Changed the RP uncivs gain when conquering (RESEARCH_POINTS_ON_CONQUER_MULT) from the old HPM 150 to 200. Vanilla, for reference, is 360.
-Made the Talambo Incident - Peru Refusal to apologize don't start a war but only give a CB, to avoid the AI going suicidal.
-Made colonial spell and colonial factory events give MIL and CON since colonial exploitation doesn't give it anymore.
-The SCA decision to move the capital to Gothenburg will only appear if your capital is in Stockholm.
________________________________________________________________________________________________

V0.3.1.4 Hotfix C
-Changed the new world immigration from 300% back to vanilla's 400%.
-Made the AI more likely to build railroads and forts and decreased naval base priority.
-You need at least one tech level to build a fort in a desert province, the change was made so it's the same as Tundra and Jungle provinces.
-Reworked relations in West Africa so the Jihad states hate the animist states more.
-Russia can abolish serfdom if they turn in a constitutional monarchy.
-Soldier pops in colonies will not promote to officers unless they are a primary or accepted culture.
-Sahel Jihad CB will only be available for Fulbe states.
-Added a few native christians to Mboul, Kaolack and Ziguinchor.
-Renamed Kaolack to Kahone. It will turn to Kaolack later since it's a colonial city.
-Removed the decision to civilize the uncivs.
-Added events for the Louis Faidherbe, the Battle of Logandème and the colonial conquest of Senegal.
-Fixed the create UBD decision to set primary/accepted cultures properly.
-Fixed a wrong core in Gwadar.
-Changed the assimilation rate bonus of the new world to not work with any country with their capital in Oceania but rather with countries with Australian as primary culture.
-Changed the RGO of Kumasi from Coffe to Grain and Tamale from Grain to Gold.
-Added an event for the second Anglo-Ashanti war.
-Added an event to restore Brussels as capital of Belgium.
-Shuffled a few provinces in the southern regions of Mexico.
-Made the Rhodesia Charter decision require the UK to actually own the land.

____________________________________________________________
V0.3.1.4 Hotfix B
-The border Treaty between Austria and Hungary now give cores to ensure everything's right.
-Fixed the Refute Manifest Destiny decision requiring Mexico to lose a war instead of the USA.
-Tweaked Slavery and Child Labor movements.
-Fixed the Organize Laos decisions not taking into account Champassak.
____________________________________________________________
V0.3.1.4 - Hotfix A
-RGO size bonus for Treaty ports changed from 650% to 500%.
-Statue of liberty bonus to immmigration changed from 200% to 100%.
-Fixed a few incorrect values for literacy of Armenians and one wrong value for a kurdish minor.
-Restored absolute monarchy title to King.
-Fixed two Antwerps existing.
-A few more tweaks to a few events MTTH.
-Changed the color of Filipinos to not be so similar to spanish.
-Implemented the changes in the color of Tarascan and Dakota.
-Intellectuals in Serbia are now in a level that they don't start losing literacy. They are mainly concentrated in the capital though.
-Fixed a line in the "centralize the kurdish states" decisions stopping the decision from working properly.
____________________________________________________________
V0.3.1.4
-Rejecting the Webster–Ashburton now should give the UK cores on the same regions as the USA to avoid the AI accidentally returning the lands with the "your lands returned" event.
-Reshaped provinces in Sudan to follow the Nile, just like the ones in Egypt.
-Reshaped the Terrain map Sahel to follow the actual Sahel, the Sahel is semidesert now instead of plains.
-Fixed a pixel glitch between Oldenburg and Bremen.
-Fixed the Niger Delta
-Fixed one lost pixel in Limassol causing a glitch
-Fixed Charlton Island and some other small islands in Canada not appearing because the terrain.bmp didn't include it. Fixed small glitch nearby.
-Added localization for the Namibia tag (sorry about that).
-Great Lakes changes:
*Lake Winnipeg is actually several lakes
*Lake of the woods
*Lake Winnebago in Wisconsin
*Lake Simcoe and Lake Nipissing in Ontario
Thanks for the anon who shaped those in the rivers.bmp, I just did the terrain and province part.
-Fixed pieces of other sea near Madeira.
-The decision to set the Trucial States as a vassal now can only be taken once per game and any state that has them in their sphere and good relations can do it.
-Made Isla Tiburon in a real island.
-Fixed Lena river in Bulun province, it used to make a turn to the left, renamed the province to Batagay.
-Fixed the Coast of Siak (maing islands that were connected to each other or to the mainland), added the island of Halib to eritrea. Fixed a lost pixel in Inderagiri province. Added a few more islands of the Rigau Islands province between Singapore and Siak.
-Removed Mahra cores from Oman to avoid Yemen getting cores there.
-Made Bushire part of Fars and Dehkord part of Ishafan.
-Reshaped Aden a little bit so Tabriz takes more of Aden.
-Added the Taganrog Bay.
-Fixed Turkmenbashi Gulf and Garabogazköl
-Fixed the Arabat Spit and that should be the Azov-Syvash National Park now.
-Fixed the coast of Thailand from the Kraburi river upwards and the Kra Isthmus. Added the Kraburi River.
-Fixed the Mekong river and its tributaries.
-Fixed Phuket Island and the Songhkla lake.
-Fixed Chilika Lake and the Padma River/Bangladesh delta, coast and several islands. Added the Bilugyun island.
-Fixed the Dardanelles strait connecting via land with each other.
-Integrated the Sudetenland minimod.
-Renamed province 111 Cody to Cheyenne.
-Made the AI more likely to invest in pop projects and foreign countries. Made the AI prioritize railroads more and less naval bases.
-Fixed Bergen coast (recovered a bunch of islands and the coast that were bugged in vanilla).
-Restored Balabac Island (was present but it was bugged).
-Finished fixing anon's list of glitches seen here: http://imgur.com/a/PqPfv and here: http://imgur.com/a/0TvRw. Thanks a lot anon!
-Tatar Straits are a sea strait again.
-Recovered Smith Island, Canada.
-Re-purposed Province 44 - Repulse Bay to be Guantanamo Bay. Repulse bay and it's pops were merged in Nunavut. Pops in Guantanamo are based on "Guantánamo: An American History Jonathan M. Hansen". 
-Changed the LR and terrain of several provinces to represent the Sahel - the transition zone between the sahara and sub-saharan africa.
-The terrain system has been revised. It follows a biome+terrain model. The added terrain types are Taiga, Arid Grassland (includes Savannas, Shrublands and Steppes), Arid Hills, Alpine Tundra and Montane Forest. I removed Woods and Steppes terrain type since they were redundant. The overall terrain number is 16 rather than vanilla's 11.
-Changed the population preferences for the new terrain types. Pops prefer temperate climate places, then arid grasslands, then cold places.
-Changed the Terrain in Chile to Reflect the Atacama Desert.
-Fixed a part of Ghadamis inside Ghat.
-Fixed one NNM bug that made the congress berlin host get prestige twice and it didn't give any prestige to other countries that participated in the congress.
-Made sure that Guadalupe-Hidalgo doesn't bankrupt the USA.
-Fixed the terrain in Peru. Lima was kept as grassland hills because the climate around it is mild. The terrain in the coast was converted to Arid Hills or semideserts.
-Fixed the Terrain of Peru, Chile and Argentina.
-Renamed Rio Gallegos to El Calafate. Reshaped borders and terrain in the Argentinian Patagonia to better represent the terrain, according to http://www.argentour.com/en/map/archivosmapas/maparelieve.gif
-Reshaped the provinces in Colombia and Bolivia to follow the rivers and geographical features better.
-Added the Serra do Mar to Brazil, fixed the terrains. The hills map was based off http://www.guiageografico.com/mapas/mapa/brasil-fisico.jpg 
-The brazilan biomes were divided between Amazon Rainforest, Atlantic Rainforest (both jungle), Cerrado/Caatinga (both arid grasslands of some sort), Serra do Mar, a mountain range that extended through the coast from the south to the north and the pampas steppes. The biomes were based on http://www.ibge.gov.br/home/presidencia/noticias/images/biomas_grf01.gif, with a lot of adjustments. Other maps used where http://desmatamento-no-brasil.info/images/Imagens/mapa-mata-atlantica.jpg
-Fixed a glitch with a piece of Januria inside Paracatu
-Fixed the USA sphering African minors
-You can take the "Persian Cinema" decision now if you have "the talkies" invention.
-Persia starts with Baluchi as accepted, as it was in vanilla, and the Dar Al Funun decision now needs 10% literacy instead of 12%.
-Swapped Trujilo and Cajamarca RGOs for each other.
-Fixed a glitch in the Juazeiro province.
-Delimited the Chaco and the Cerrado, adjusted their terrains and reshaped Reconquista to follow river borders.
-Divided Saint Martin in Philipsburg (Netherlands) and Marigot (France). Marigot was taken from Baffin Island (Province 45), canada, the former territory of Baffin which is now integrated in Keewating province.  Pops on the new province under france is based on data from the 1885 census found on https://en.wikipedia.org/wiki/Collectivity_of_Saint_Martin. Adjusted the pops of the netherlands part of the island.
-Changed the vanilla Rubber RGO swap event to not effect 977 - Kursk (Russia), now it changes Iquitos (Peru).
-Integrated new party names for a few countries made by anon. Canada and Netherlands got new parties that activate and deactivate at certain times.
-Added Isla La Tortuga as part of Caracas province, it was present in the vanilla map but it was bugged so it was invisible. Fixed the Curiapo Delta and the terrain of the guyanas and Venezuela.
-Added a decision related to the Amazon Rubber Boom for Brazil and the foundation of several cities.
-Adjusted pops of Saint Thomas.
-Fixed the Virgin Islands shape and added Anguilla as part of the british Virgin Islands province.
-Added a decision for the selling of the Danish Virgin Islands. To be able to see it you either need to be the USA or own the Panama Canal.
-Fixed a bugged river in Brazil.
-Fixed the Haiti-Dominican Republic border and a glitch in the island.
-Fixed Peipsi Jarv lake and the Pskov Lake
-Made Abu Ak Abyad an island.
-Fixed a glitch in Tuz Golu lake.
-Fixed Masirah Island.
-Fixed a glitch in Kangan.
-Reshaped Sohar and Nizwa in Oman to correspont to the coast/countryside better and the terrain division. 
-Fixed the terrain around the arabian peninsula a little more.
-Fixed a glitch in Bela.
-Integrated 2664 - Chokurdakh (Siberia) in Abiy. 2664 was renamed to Khasab, it represents the Musandam Governorate and it's now under Oman.
-Reshaped Birjand, Persia, a little bit.
-Added an event for the death of Bahadur Shah Zafar.
-Renamed Mascate Coast to Gulf of Oman (2786). Reshaped Coast of Mascate (2785), Gulf of Oman and Straits of Hormuz. Hormuz sea province is smaller and has a bigger strategic importance to hold the persian gulf.
-Removed the Hormuz Strait connect Abu Dhabi to Jask.
-1071 - Bytantaysk reused and renamed to Qeshm. It's part of Persia, adjusted the pops according to the 1966 census (the population was around 24K - see Security and Territoriality in the Persian Gulf: A Maritime Political Geography).
-2640 - Ziryanka - Siberia - renamed to Gwadar. Under Oman until 1958 when it was sold to Pakistan. 2640 was integrated in 2621. Population based on Sectarian Politics in the Persian Gulf. Shape based on http://www.davidrumsey.com/luna/servlet/detail/RUMSEY~8~1~239395~5511773:Persien,-Afghanistan-und-Belutschis?sort=Pub_List_No_InitialSort%2CPub_Date%2CPub_List_No%2CSeries_No
-Controlling 1071 - Qeshm and 2664 - Khasab will trigger a strategic modifier for controlling the Hormuz Strait (after 1880). This modifier will only happen after 1880 and the effects are : Tax Efficiency +10% Tariff Efficiency +20% 
-Diminished the impact of religion on ideology by 10%.
-Fixed glitch in Kuwait.
-Improved the Belize Purchase description to subtly tell the modifiers that will affect the AI and improved the AI decision making when selecting if they are going to sell it or not.
-Fixed Ceuta starting pops. Based on https://archive.org/details/statisticscolon01martgoog
-Added a decision related to the Guantanamo Bay lease.
-Fixed Prussia starting with Romanticism and consequently being able to react to the Rhine Crisis earlier than it should. They still start with the tech, but need a 1840 tech to enact the decision. The event will also only happen up to 1890.
-You need to own the Wiesbaden province to take the niederwald_denkmal decision, because that's where the monument was built.
-Made sure the UBD will not get events in the formation of the NGF.
-To avoid exploiting, the Yemen and Malaysian minors can't be released as vassals. You need to unify Yemen and Malaysia to release these territories, the minors can't be release.
-Tweaked the Liberal Revolution events in Europe.
-Integrated the America Minimod V2 by anon. Fixed some graphical and position problems and fixed USA not getting cores on Albuquerque. Changelog is:
*Reshaped Alaska to follow the coastline.
*Added an Aleutian Islands province.
*Reshaped the Alaskan pan handle to allow for Alaskan boundary dispute flavor in the future.
*Reshaped and renamed Valemount in Columbia.
*Prince Rupert-New Westminister border in Columbia was reshaped.
*Reshaped the borders surrounding the interior of Rupert's Land to not look terrible.
*Reshaped Washington and Oregon states to follow the terrain map, political significance, and historical population centers.
*Missoula was reshaped to follow historical maps at the time.
*Reshaped California a little bit to follow the terrain map, political significance, and historical population centers.
*Reshaped Utah a little bit to follow the terrain map, political significance, and historical population centers.
*Reshaped Nevada to how the original territory was setup. (According to the 1930 US Census Nevada was the least populated state with less than 100k people or 25k pops making reshaping the province according to modern population centers probably not worth it.)
*Reshaped the Flagstaff-Phoenix border to allow for proper Confederate Arizona borders.
*Used the repurposed Mexican province in New Mexico to allow for proper Confederate Arizona borders.
*Reshaped all the provinces in Colorado to fit proper Texan claims and to follow the Rio Grande river represented in-game.
*Repurposed a Colorado province in Wyoming to allow for the bit of Wyoming that Texas claimed.
*Redid the provinces in New Brunswick and Maine to follow a different historical map showing claims that didn't look total shit.
*Tweaked the pops in New Brunswick.
*Tweaked the positions of many existing provinces like Animas and Rimouski.
*Completely reorganized and reshaped some of the provinces and regions in Mexico to at least vaguely their historical counterparts.
*Reverted Montreal back to its Vanilla shape according to the logic that the city was on both sides of the St. Lawrence river.
*Removed the Texas cores outside of what it owns at the game start and added that to the Texan Claims decision alongside the repurposed province in Wyoming.
*Fixed the Restore Washington decision that moves the capital back to Annapolis and made it use the new D.c. province.
*Added to the event to rename much of Oregon Country to rename the provinces to Seattle, Olympia, Portland, Eugene, Baker City and increase the life rating to normal levels in Oregon.
*Fixed some events for Mexico that mentions the vanilla Mexican regions and made them use the new ones.
*Made the USA start with the new D.C. province as their capital.
*Made the 1861 start take into account the repurposed and reshaped provinces.
*Redid localisation the New Mexico region, reshaped provinces, and others.
*Added a strait between the Aleutian Islands province and Dutch Harbor province.
*Added to the initial event that triggers the Civil War to give cores to the historical Arizona territory to have that secede alongside the rest of the CSA.
*Fixed and changed localisation in Wyoming to fit the historical locations of the individual towns the provinces in Wyoming were named after.
*Renamed Atlantic City to Egg Harbor.
*Merged two provinces and their corresponding pops in the region of Nuevo Leon to be used as a province in New Mexico and as Washington D.C.
*Changed the color of the Dakota culture to remove the resemblance with Texan.
*Changed the color of the Tarascan culture to remove the resemblance with Nahua.
*Increased the life rating of the New Jersey region to 40, Caribou to 35, Tampa to 35, Detroit to 40, Chicago to 40, New Orleans to 40, Houston to 45, Dallas to 40, Austin to 40, San Antonio, to 40, El Paso to 40, Seattle to 40  and decreased Tuscon to 30, Silver City to 30, Phoenix to 30
-Fixed a bunch of railroad positions on the map to try and avoid railroads over water. Fixed a few glitches.
-Changed the LR of north dahomey to be more consistent with the rest of the territory.
-Fixed Rajputana starting with no party in power.
-Made a decision for Bulgaria to move the capital to Sofia.
-Made a decision for Poland to move the capital to Warsaw.
-Changed the Bulgarian Monarchy flag from the Bulgarian Naval Ensign (vanilla) to the actual Bulgarian monarchy flag (which is the same as democracy). Color corrected the democracy and monarchy flags.
-Lowered the starting literacy of Two Sicilies from 25% to 10%. It's based on the fact that in the 1871 Census, no region in southern Italy had less than 80% illiteracy. Papal States starting literacy changed from 35% to 15%. Marches and Umbria had around 80% illiteracy in 1871. Pops in Rome and Viterbo will start with 20% and in Emilia Romagna will start with 22%. Changed Tuscany and Lucca Literacy from 45% to 20%, since the Tuscany region had 68% illiteracy in 1871. Changed Modena and Parma starting literacy from 45% to 20%. In 1871, Emilia-Romagna illiteracy level was 71.9%. Pops in Liguria will start with 35% literacy, 10% lower than the S-P average of 45%. Sardegna will now start with 10% literacy. Italian pops in Lombardy will start with 45% literacy and in Veneto and other parts of Austria will start on 25%. Source for all of this is Modern Italy, 1871 to the Present By Martin Clark, pp 43 and The Birth of a New Europe: State and Society in the Nineteenth Century, pp 156.
-Napoleon III coup will now reduce relations with all european GPs, especially Russia. Changed the event to explain the relation drop. In the case of disposal through event on the restoration of the bourbon dynasty/democracy when he dies, France will get the relation damage back.
-The Crimean War decision for France (the Holy Land question) will now reduce militancy for french liberals, conservatives and reactionaries. Explanation was added to the decision description.
-Alaska will now use a different flag for absolute monarchy.
-CSA cores no longer spread to South America.
-Added the Arbereshe pops to Italy, totalling 96K (or 24K pops). They are represented as Albanians and are orthodox. Added 3550 Albanian pops in Catanzaro, based on http://www.researchgate.net/profile/Giuseppe_Tagarelli/publication/249423568_Ethnicity_and_Evolution_of_the_Biodemographic_Structure_of_Arbreshe_and_Italian_Populations_of_the_Pollino_Area_southern_Italy_(18201984)/links/0c96051e7f4b498a7c000000.pdf. They start with 5% literacy and they are spread in southern Italy. All pops are taken from the south italian pops, so the overall number of pops is the same. Total number of pops based on Modern Italy, 1871 to the Present By Martin Clark, pp42. Most of them are orthodox, but some are catholics.
-Added 30K greek (7500 pops) to southern italy.
-Added 12K (3000 pops) Croats in Aquila, to represent the Molise croats (slavic speaking pops). The source for the greeks and Croats is the same as the Albanian numbers.
-Made the AI more persistent in exploration events, they will try to repeat more often unless they don't have the money. They also now take into account if they have the money or not. Before, they ignored if they had the money, were more likely to pick the "Consider the idea later" (or even not go at all rather than going first) option on the first event. If the mission was lost or unsuccessful, they had a 60% chance of trying again and a 40% of giving up. Now, in the first event, the AI has a 70% chance of going (vanilla: 25%), 20% chance of postponing (vanilla: 45%) and a 10% chance of not even sending an expedition (vanilla: 30%). All the other events where they decide if they will go or not were changed to 75% to go and 25% to give up.
-Animist pops under 50% literacy will now be overwhelmingly conservative and won't join any ideological rebels.
-Animist pops under 50 % literacy will not emigrate unless there's a genocide in progress. In previous versions of HPM, they wouldn't move even with a genocide and literacy didn't play a role.
-Reworked the Moroccan partition so it works better.
-Changed Canada starting reforms to stop them sucking all migrants once they get free as a puppet. They start with no social reforms (except for school reforms), no trade unions and a few more where changed.
-Forming Italy as Corsica will no longer give French as accepted.
-Fascist Italy will now be called Italy.
-Kamchatka, Estonia, Latvia, Lithuania, Ukraine, Crimea, Cossackia, Belarus and Buryatia, when released from Russia through dismantlement, will be released as democracies.
-Chechnya, Circassia and Dagestan will now also be released from Russia in the case of a dismantlement, as democracies.
-Literate pops will now be more worried about abolishing (high literacy pops) and restricting (medium literacy pops) child labor in late game.
-Removed Portugal Core in Cape Verde.
-Fixed POP the issue "Political Rights". Changed a little bit so very literate or high CON pops should press for full political rights more fervently.
-Relaxed the restrictions to pass full political rights.
-Pops will be -10% less likely of picking nations in the new world that are a vassal of a non new world country. This is made to stop Canada from sucking all migrants.
-Increased the Gypsy pops in Belgrade from 2K to 4.5K. Based on The Forgotten Minorities of Eastern Europe: The History and Today of Selected Ethnic Groups in Five Countries edited by Arno Tanner.
-Changed the population of Serbia from 204K pops to 180.31K  pops (721.240). The 1834 census lists 678.192 (169.548 pops) while the vanilla value is closer to the 1841 census. The value for 1836 was reached by calculating an average growth, assuming a constant rate of growth. Based on http://self.gutenberg.org/articles/demographic_history_of_serbia#1834-1863
-Added 17K romanian pops in Bor to represent the roman population. Based on http://self.gutenberg.org/articles/demographic_history_of_serbia#1834-1863
-Changed the number of intellectuals and bureaucrats in Serbia in 1836. The intellectuals became soldiers. The change was based on data from The Balkan Economies C.1800-1914: Evolution Without Development  By Michael R. Palairet, pp 167 ("teacher ratio was in the order of 60-70:1.")
-Serbian starting literacy diminished from 10% to 4%. Based on Religious Separation and Political Intolerance in Bosnia-Herzegovina  By Mitja Velikonja, pp 312.
-The events for the release of Natal, Transvaal and Orange now all have options for a tag switch to these countries.
-Webster–Ashburton Treaty will now happen to the owner of Bangor, be it New England or the USA. Refusing it will also give the UK/MRU/CAN cores on Bangor.
-Added 2.5K sephardic pops in Bucharest and 3K Ashkenazi in Iasi. Based on https://en.wikipedia.org/wiki/History_of_the_Jews_in_Romania
-Changed the Gypsy population of Moldavia to 34750 pops from 20K pops. Based on The Roma in Romanian History  By Viorel Achim, pp 94.
-Changed the population of Wallachia from 311K pops to 350K pops (1.400.000 population). Figures for the 1838 census show a population of 1.5M people. Based on http://censusmosaic.org/sites/default/files/downloads/publications/mosaicWP/mosaic-wp-2013-001.pdf (note: while sometimes a figure of 2 million is calculated, the source kinda throws it down, so I will roll with 1.5M).
-Changed the literacy of Wallachia and Moldavia to 3% from 10%. Numbers are based on The Making of Modern Romanian Culture: Literacy and the Development of National Identity By Alex Drace-Francis, pp 41.
-Bulgaria will now start with Basic Schools. Based on https://en.wikipedia.org/wiki/Education_in_Bulgaria
-Montenegro and "Montenegrin" pops will start in the same literacy level as Serbia. The data from 1900 https://en.wikipedia.org/wiki/Demographic_history_of_Montenegro#19th_century Is very similar to Serbia in the same time frame, and since data for Montenegro is hard to find, I will assume the same level. Vanilla also assumes the same level for everyone (Wallachia, Moldavia, Montenegro and Serbia all start in 10%).
-Literacy for Greece reduced to 8% from vanilla 22% and HPM 15%. Based on data from http://www.cicred.org/Eng/Publications/pdf/c-c19.pdf and http://find.galegroup.com/gic/infomark.do?&idigest=fb720fd31d9036c1ed2d1f3a0500fcc2&type=retrieve&tabID=T0012&prodId=GIC&docId=CX3460500254&source=gale&userGroupName=itsbtrial&version=1.0 and comparative data with other balkan countries.
-Reduced Greece population to 1836-8 levels from 1843 levels. They stat with 185.99K pops rather than 226.80k pops.
-Literacy in the Ottoman Empire changed from 8% to 3%. Vanilla is 4% and NNM is 20%. That's the average literacy, the actual distribution of literacy is this: 3% for turks, Bosniaks and circassians, 2% for arabs and 1% for kurds and assyrians. 4% for Romanians, Georgians, Armenians, Ukrainians and Serbs, 8% Greeks, 10% for Croats and Bulgarians. 30% for Italians and Jewish pops. Albanians: 4% for catholics/orthodox, 3% for muslims. All pops in Istanbul will be 5% more literate than their counterparts in the rest of the empire.
Sources:
Albanians: http://www.wilsoncenter.org/publication/313-brief-historical-overview-the-development-albanian-nationalism
Muslims: https://archive.org/stream/Donald.Qataert_The.Ottoman.Empire.1700-1922/Donald.Qataert_The.Ottoman.Empire.1700-1922_djvu.txt
Bulgarians, Greeks, Jews: http://www.cliohworld.net/onlread/3/Ilchev_To_Call.pdf Note 2, last page.
-Changed the Egyptian literacy to be consistent with the Ottoman changes. Same literacy rates for the Kurdish states. Expect the same literacy rates as the Ottoman Empire.
-Changed Persian starting literacy from 7% to 3%. Based on the fact they had around 12% literacy in 1950. http://www.unesco.org/education/GMR2006/full/chapt8_eng.pdf
-Changed Russian literacy per culture to be consistent with changes. Minorities under russian rule like Greeks, Armenians, Romanians Italians, Germans, Swedes will all had their literacy changed.
-Spain's literacy will also change according to pop religion and culture. Filipinos have less literacy as other pops in the colonies.
-Formin the NGF will now remove the cores of the nation forming it, so only NGF and Germany cores will remain in the core territory of the nation forming it.
-Increase the Treaty Port bonus to RGO size from 200% to 650%, removed the pop growth bonus, the efficiency bonus and halved the rich income bonus.
-The upper limit for Qingdao and Weihai to turn in a precious metal treaty port changed from 20K to 30K pops. Meaning if these provinces have more than 30K pops they will turn in a regular treaty port rather than the "special" one.
-Added a generic Treaty Port modifier for Treaty Ports that don't qualify to change to precious metal. It will only add the Treaty Port Modifier but it won't change the RGO.
-Changed the Law of Guarantees decision for Italy to add cores to Italy too in case they don't have in these regions.
-Added a new decision for Italy to abolish other Italian minor cores after the Law of Guarantees. The decision can be reused as long as there is a italian minor core owned by italy, but it adds 1 infamy each time.
-Reshaped Tabatinga so it actually includes Tabatinga and so that it allows for more aesthetical provinces in the case of a border in the Amazon. Reshaped Tefe.
-The added another option to the Horace Mann event for the USA.
-Install Communism and Fascism CB should cost max 15 infamy each. The Democracy one costs a little less. It also shouldn't showe your with prestige.
-Switzerland and Neuchatel Literacy increased from 70% to 80%. Sources: The Birth of a New Europe: State and Society in the Nineteenth Century By Theodore S. Hamerow, pp. 155.
-Fixed a Vanilla Bug that was stopping the sound of clicking and moving a cavalry unit from playing. Now calvary will have an unique sound.
-Austrian Literacy rework: Literacy for South Germans will be 45%. Literacy for Italians in Lombardia and South Tirol will be 45% and in Venetia 30% while the rest of the empire it is 25%. Literacy for German pops in the Austrian alps will be 10% higher than the rest of the empire. North Germans will start with 60% literacy. Protestant Hungarian pops will start 5% more literate. Czechs will start with 47% literacy. Pops in Aussig and Vienna will start with 8% more literacy. Serbs, Ukrainians and Romanians: 3%. Hungarians will be 12% literate in Transdanubia and western Slovakia, 10% in central hungary and 8% in Transilvanya and edge of the lands of Hungary (see map 1). Protestant pops will be 2% more literate. Slovaks in western slovakia will be 40% literate, while those in eastern will be 20%. Croatians will start with 8%. Slovenians will start at 20%. Polish pops will start at 12%. With the exception of the Hungarians and Austrians, all the other pops data were obtained by extrapolating fairly recent results and the interpretations of maps. See the sources, especially their tables, for more info. Average Literacy of Austria in the game start is 19.8%, while in vanilla it's 16.1%.
Sources:
The Birth of a New Europe: State and Society in the Nineteenth Century By Theodore S. Hamerow, pp. 155.
The Legacies of Literacy: Continuities and Contradictions in Western Culture and Society By Harvey J. Graff, PP 296
Language Planning and Policy in Europe edited by Robert B. Kaplan, Richard B. Baldauf, pp 71.
Map 1: http://www.pitt.edu/~votruba/qsonhist/assets/literacy350.gif - http://www.pitt.edu/~votruba/qsonhist/literacyslovakiahungarykingdom.html
Map 2: https://upload.wikimedia.org/wikipedia/commons/f/f1/Literacy_in_Austria-Hungary_%281880%29.JPG
-Russia literacy got down from 8% to 5%. Byelorussians and Ukrainians start with 3% literacy. Source The Birth of a New Europe: State and Society in the Nineteenth Century By Theodore S. Hamerow, pp. 156.
-Changed Belgium Literacy from 50% to 47%. Netherlands from 60% to 70%. Based on The Birth of a New Europe: State and Society in the Nineteenth Century By Theodore S. Hamerow, pp. 154 and The Cambridge Economic History of Modern Britain pp 204.
-Changed literacy rates for the UK: In England and Wales, the rates are 60% from vanilla's 55%. In Scotland, 80% from 55%. Irish: Munster Region 24%. Connacht: 15%. Ulster: 30%. Leinster: 28%. Pops in Dublin are 7% more literate than others (based on the average of the regions that are Dublin in V2). Protestant Irish will be 5% more literate than their catholic counterparts. Any irish pops outside of Ireland in non colonial regions: 30% literacy. Catholic English pops will be 5% less literate than their Protestant counterparts. All pops in London are 5% more literate than pops in their counterparts. Irish pops will start with 10% literacy in the colonies. Also reworked of the colonial pops: Maltese start with 30%, Austrialians with 40%, Anglo Canadians with 60%, French/French Canadian/Metis start with 45%, the pops in gibraltar, the indians, african and former slaves. Everyone. In vanilla, everyone unaccepted (irish, french-canadian, maltese, etc) was 10%. Vanila National Literacy: 43.3%. HPM National Literacy: 52.8%.
England and Wales Source: Literacy and the Industrial Revolution by Edwin G. West, pp 8.
Scotland Source: The Birth of a New Europe: State and Society in the Nineteenth Century, pp 153.
History and Development of Irish Population Censuses by TP Linehanm, pp
Ireland: http://www.aohflorida.org/marybeth/wp-content/uploads/2013/04/screenshot_462.jpg
-Stopped the small vanilla icon for press rights movements in pops from using a unrelated image.
-Moved Child Labor laws to be under social laws.
-Fixed Morocco flag, made the more modern monarchy flag happen only in HMs governments.
-Tunis will now be renamed to Tunisia if they are not absolute or semi-constitutional monarchies. Fixed the flag.
-Fixed the flag of Tripoli.
-St Barths referendum will no longer give cores, just CBs.
-Set custom literacy rates for Denmark (colonies and pops).
-Set custom literacy rates for the United Baltic Duchies (different pops).
-Changed starting literacy of Portugal from 15% to 10%. Based on The Development of Modern Spain: An Economic History of the Nineteenth and Twentieth Centuries By Gabriel Tortella Casares, pp13 and New Insights From Recent Studies in Historical Astronomy: Following in the Footsteps of F. Richard Stephenson  edited by Wayne Orchiston, David A. Green, Richard Strom
-Belgium literacy change to 47%. Based on The Development of Modern Spain: An Economic History of the Nineteenth and Twentieth Centuries By Gabriel Tortella Casares, pp14.
-Set custom literacy in Finland. Finland will start with 50% literacy, orthodox finnish start with 10% less literacy. Sami start with 20% literacy. Based on http://www.stat.fi/tup/suomi90/marraskuu_en.html
-Fixed the Literacy of Circassia, Caucasian Imamate, Transcaucasia and Abkhazia in the game start to be consisten with the other literacy numbers.
-Changed how the Paraguayan indepence works. Removed the cores from Argentina in Paraguay in the game start and the annex CB is now a puppet CB, reworked the AI chances and the infamy gain.
-Rebalanced the initial modifiers for the substates of Argentina and for Paraguay.
-Added Yazidi kurds to Armenia. Added Assyrians to Armenia and Persia around Lake Urmia.
-Remade the literacy for Transcaucasia and Abkhazia in the game start. Armenians, Georgians and Russians start with 4% literacy. Muslims start wih 2% literacy. Based off The Russian Empire: A Multi-ethnic History  By Andreas Kappeler.
-US literacy raised from 50% to 65%. Based on Education of the American Population By John K. Folger, Charles B. Nam. Still missing custom data for Natives, Immigrants and regional variations in Literacy.
-Adjusted France literacy rates. They will start with average 50% literacy rather than 60%. Pops Paris start with 5% more literacy. Protestant pops start with 5% more literacy. Breton pops are -10% literate. Pops in the north (A-L, French Comte, Champagne, ile de France, Normandie regions) and pops in Pau, Auvignon, Marseilles, Lyon, are 5-10% more literate than the average. Pops in Limousin, Auvergne, Loire (regions) and in Tours, Poiters, Angouleme, Macon, Moulins, Bourges and Dijon -15% and -20% literacy. South germans start 55% literacy, Italians with 25%, Basques with 20% and Catalan 15%. The old average literacy in France was 58%, now it's 47.6%.
Source for average literacy based on: Les niveaux d'alphabétisation en Italie au XIXe siècle by Jean-Michel Sallmann
Regional variation based on https://histoiremesure.revues.org/816, https://histoiremesure.revues.org/816 and Literacy and Geographical Mobility in Nineteenth Century Provincial France: Some evidence from the Departement of Ille-et-Vilaine by Michael J. Heffernan. 
-Stopped Russia from going after Kashgaria every time if the Dungan rebellion succeeded. They will try to focus on central asia a little more.
-Removed the Public Illumination building. The Unciv reform for forts was conflicting with it and building it instead of Forts and because of the hardcoded limit to only one modifier per building, it didn't serve its purpose well. Until I can solve these issues, buildings are out.
-Reduced the duration of the bonus of Budapest being built from 10 years to 5.
-Hungary has a decision to move the capital to Budapest now.
-Fixed a description for Militant Socialists.
-Fixed regions starting unemployed because the game wasn't calculating the province size modifier with Serfs+Farmers.
-Fixed two provinces in Scotland - Aberdeen and Dumfries - starting almost full because they were just a little below the province size modifier limit.
-Diminished the number of Artisans in Trieste a little bit.
-Hungary can now claim Fiume later, to represent the conflict over it. They need to have cores on Croatia and be free.
-Added a decision for an Austrian-Hungarian border treaty to normalize relations over Eisendstad-Sopron dispute. It also exchange pops in those provinces.
-Added a decision to integrate Perak outside the normal event chain.
-Steel Factory is now called Steel Mill.
-Futa Jallon and Futa Tooro now starts with Islamic Law and as a Theocracy.
-The GP or SP owner of the Canarias can establish a colony on Western Sahara on the doctrine of Effective Occupation, started in the Scramble for Africa.
-You need Revolution and Counterrevolution to see the Genocide decision now.
-Ziguinchor will start under Portugal. See https://en.wikipedia.org/wiki/Ziguinchor#History
-Added a decision for the owner of Velingara and Gabu to exchange Gabu for Ziguinchor during the Berlin Congress.
-Added a decision to take Conakry. It can be taken by Portugal or France, based on https://en.wikipedia.org/wiki/Rivi%C3%A8res_du_Sud and the historical presence of these countries in the region.
-Stopped Chinese treaty ports being obtainable if you are landlocked.
-For consistency sake, the paper mill input good was changed from Timber to Lumber. In the Lumber Mill, the description reads "In a lumber mill, timber is processed into lumber. Lumber can then be used for buildings, paper, ships or furniture." and "A paper mill is using lumber to produce paper. Paper is used for books, newspapers and other means of information."
-Renamed "Regular Clothes Factory" to "Clothes Factory".
-Fixed a typo in the Cement Factory description (materiel instead of material).
-Improved the description of all factories by actually adding one instead of the vanilla transcription of the used materials.
-Tanks will now require a Steel instead of rubber.
-Following the notes in ammunition description (and the artisan ammunition template), ammunition will require coal to be produced. It's meant to represent Swag/Cast bullets and the heat required for them. Factories now also don't require less iron than artisans for bullets. Changed the base price of ammunition from 17.50 to 18.00 to make it more profitable.
-Renamed Fuel Refine to Oil Refinery.
-Renamed the misleading "Synthetic Oil Factory" to "Coal Liquefaction Plant"
-To invent radios you need to invent vacuum tubes or it needs to be after 1920. Historically, vacuum tubes were essential for the viability of the radio. Removed the modifier that made more likely for the radio to be invented in Democracy government only.
-Bessemer Steel invention was moved to "Cheap Steel" tech.
-Cheap Steel should give a small bonus to steel production. 
-Renamed Electric Furnace tech to Electric Arc Furnace. Renamed the generic Cheap Steel to "Bessemer Process" and the generic "Advanced Metallurgy" to Open Hearth Furnace. Changed the pictures.
-Fixed the capital of the Guyana region being in the wrong place.
-Changed Dye Factory to Synthetic Dyeworks
-Renamed Lumber Mill to Sawmill.
-Renamed Timber to Wood, to avoid confusion with Lumber.
-Fabric Factory renamed to Textile Mill.
-Fixed missing cores in the "Unite Indonesia" decision.
-Added the 1850 Compromise to the list of decisions of the USA. Taking it will make the Wilmot Proviso disappear, but if you take the Wilmot Proviso the Compromise will disappear. The Proviso will also ban slavery in southern states now and it requires a liberal UH to pass. The Compromise replaces the "clay and douglas" draft and fixed Texas cores. Both can only be taken after the Guadalupe-Hidalgo Treaty.
-Manifest Destiny needs a party in power with either Jingoism or Pro-Military.
-The Ostend Manifest now has a UH requirement, both in % and as a ruling party.
-Persia and Egypt no longer start with Foreign Officers, but they start with Foreign Artillery.
-Dai Viet is now be called Vietnam. Based on http://books.google.com/books?id=0LgSI9UQNpwC&pg=PA120#v=onepage&q&f=false
-Changed Taiping starting with too many techs. When the rebellion breaks out they will start with the same reform as the Qing has, with the exception of reforms that build something. They also can't turn back to Qing, so going Taiping is a path without return. This should plug exploits and the Taiping being more developed. The Taiping also can't use the "get RP by conquest" mechanic, which should stop them from getting a lot of RP from the war with the Qing.
-The Qing now start with Foreign Weapons.
-Landlocked uncivs will no longer be able to pass the naval reforms. Hopefully, this will help them selecting reforms properly.
-Reworked Issue selection for pops, especially the new ones. Fixed a few unintended behaviors and made pops select issues better. For example, pops in the colonies won't push for some reforms at all (like Transportation, since they don't want the colonies flooded with immigrants) so issues for pops in colonies and non colonies shouldn't be exactly the same anymore. Non core (non primary and non accepted pops) won't care about revanchism anymore (meaning the Zulu won't get more jingoistic if the UK loses scotland). Pops in colonies also won't care about revanchism when deciding how jingoistic they are. Countries outside of yankee and dixie should also push for full representation in the UH, especially in democracies.
-Fixed a vanilla bug that made it impossible for pops to push for Jeferson method and consequently Proportional Representation, so the issue existed and was calculated but it would never be pushed.
-Fixed the Netherlands annexing Limburg before it should during the Limburg Crisis.
-Added one decision to Integrate Lithuania in the UBD.
-Added one decision for a german GP that is the overlord of UBD to add north german as accepted.
-Tweaked the Italo-Turkish War to stop GPs normally intervening, though they still can.
-Tweaked the coup events for when a Fascist/Communist overlord has a non fascist/communist puppet. Now they should have a cooldown period of 8 years so the event to flip the government doesn't happen soon after the other.
-The Taiping will not get a modifier to represent the fanaticism in their army and the Qing will get a modifier in the game start to represent the corruption in their army. The modifier lasts for 30 years or until they get one of the military reforms.
-Optimized the vanilla issues code for a lot of issues. The optimization was about how pops in unciv countries deal with the reforms (which they can't pass). Fixed a few vanilla bugs with the aristocrat pops. Fixed a (potential) vanilla bug on how pops deal with secret ballots.
-Fixed BRY_communist flag being corrupted.
-Manifest destiny will give random infamy between 0 and 3.
-Refute Manifest Destiny can now be taken if you have a truce with the USA, you own all your cores and you didn't lose a war recently and the USA lost a war recently.
-Reworked the expel the manchu decision description to be more neutral. It now can be taken by any country with russian or japanese as primary. Improved descriptions and effects.
-Fixed a double river that existed in the middle of the Kalahari in Botswana.
-Fixed the Law of Return decision for Israel moving wrong pops.
-Changed the decision to Create Argentina just to integrate breakway states back in the country.
-Fixed the kaitakushi decision not being able to be taken by the Ezo. Changed the order of the requirements so it is more readable.
-Changed so Buenos Aires start in the Argentine Confederation. Tweaked the Uruguay/Argentine Civil War event chain to account for it.
-Moldova should no longer apply for annexation without being in the Romanian Sphere.
-Adjusted a lot of cores and made other tweaks to south america. Still not did the Chile/Peru/Bolivian conflicts though.
-Changed Renanco name to Laboulaye. Fixed shapes in the area for the conquest of the desert to follow more historical lines and so that the starting borders are better.
-Fixed Isla Trinidad being on the map files but not appearing in the game.
-Fixed the game having a lake that doesn't exist in the Kamchatka peninsula.
-Reworked the MTTH for the NV events.
-Transportation now has bureaucratic costs.
-Renamed Tasmania to Van Diemen's Land. Added a decision to rename it to Tasmania.
-Changed the vanilla new world bonus for immigration from 400% to 300%. Pops will also not take into consideration if you are on Oceania, pops only migrate to countries in the americas or with australian as primary culture.
-Cherokee tag religion is now Protestant rather than animist.
-Changed how Uncivs are divided informally. There's a "new" category of uncivs that lack a flag that is meant to represent uncivilized societies that lack a writing system. They have a decision to adopt a writing system and remove their malus.
-Fixed pop promotion of intellectuals and bureaucrats for the AI, taking into account the AI never goes past 75% in the sliders. When they get to 75%, they will be treated as 100% for promotion purposes. 
-Ashanti lost Ho and Yendi. I don't know why it was like that in NNM, I don't see any reason for them to own the place nor sources. I removed so it allows for better colonization of Togo.
-Changed the Aden Protectorate decision to release Yemen again, as a puppet, if the AI takes the decision but if the player takes the decision, it just changes cores and he can choose to release them later. Added a decision to cede Aden to Yemen.
-Reshaped Zadar to be smaller and allow movement in Dalmatia.
-The peaceful coup events will now reduce a percentage of prestige based on how much prestige you have rather than always being a fixed amount. It will always be 10% of your current prestige except for Presidential Dictatorship coups on democracies, that is 5%. Fixed anarcho liberal coup not removing prestige.
-Added a decision for Yemen/North Yemen to move capital to Sana'a.
-Improved descriptions of some reforms to make its effects more clear, like Peonage, Slavery and Transportation.
-Renamed Tibet Region to Himalaya, as it was the name used in the game files. Changed Sikkim starting religion from Hindu to Gelupga and primary culture from Nepali to Tibetan. Fixed the pops. Based on https://en.wikipedia.org/wiki/Indigenous_peoples_of_Sikkim and https://books.google.fr/books?id=L7gIVNzkN2YC&pg=PA86#v=onepage&q&f=false. Sikkim will start with around 7K pops, one third being Tibetan and the rest being asian minor to represent the Limbus, Gurungs, Murmis, Rais and other people. Religions include animist, hindu and gelupga.
-Jenne will start with the Massina Empire.
-Fixed the Italo-Turkish War giving out the Dodecanese when the Turks didn't own it.
-Sokoto and Nejd will start with Islamic Law too.
-To try to avoid an bug with pop promotion and culture, in the 1836 no pops soldier pops in austrial will start with australian.
-The event for the selling of Rupert's Land will only happen when Canada has enough money to buy it and not bankrupt.
-Changed the 'Canadian National Railway' events to be decisions and you need the money to enact them. This will avoid the AI bankrupting itself with it.
-Renamed the Palmyra (island) to Palmyra Atoll to avoid confusion with the Palmyra province in Syria. Made it and Line Islands have the Island terrain type that was missing.
-Reworked Muhammad Ali Reforms and modifier description. Egypt will start with a small arms factory and a few craftsmen in Cairo. They will only get foreign training and land reform by enacting the reforms and their research malus will be 25% instead of 60%. They also can take loans, but not much. Losing the war will also remove 3 random social reforms (like it was in NNM) but it won't remove 3 random military reforms, just the ones they got.
-Added Amazonian as accepted for Ecuador to avoid them integrating the Peruvian provinces too fast.
-Changed Austria starting draft reform to two years from military service.
-Moved Kherson to Transnistria.
-Fixed Burkina Faso having cores on Ghana. The name of Wagadugu will change to Ouagadougou if the french take the decision to form Burkina Faso. Since Burkina Faso uses an unciv tag, the decision was reworked to avoid Burkina having cores in strange places.
-Prussia will try to annex Hesse-Kassel if they revoke their military access and are not in their sphere of influence. They will pay with Infamy but now they will try to preserve access to the Rhine. Based on https://en.wikipedia.org/wiki/Electorate_of_Hesse
-Assert Hegemony CB now requires Nationalism and Imperialism. All the other "Unification" CBs need that technology.
-Reshaped the Chott el-Jérid to look more like IRL. Added Chott El-Gharsa.
-Added several lakes to Algeria. Thanks for the anon who did the originals for the provinces.
-Moved the initial capital of Algeria to Mascara as it historically was.
-Genocide events will now have a reaction on other countries. The more vague your parameters (every non accepted culture) more countries are affected, but less severe is the reaction (for example, targeting everyone in non accepted cultures lowers your relation with everyone and gives them a humiliate CB on you for 2 years). The more localized, less countries care about it but the reaction is more severe (sunni only would drop to the bottom your relation with all Sunni countries and it will give a cut down to size CB on you). The only exception are animists, nobody cares about animists. 
-Pops that are not of the state religion will take longer to assimilate.
-Remade literacy in the USA. Slaves and afro americans will start with 1% literacy. Immigrants (irish, north germans) will start with a little less literacy than their counterparts in the old country. Catholics start with -10% literacy. Pop literacy for accepted and primary culture is set by state according to the 1840 census (data from Civil War America, 1850 To 1875 By Richard F. Selcer pp. 301) corrected down. The average de facto literacy in the start was changed from the vanilla 42% to 56.5%. The biggest gap between literacy in the state is 28% between the one with lowest literacy and the one more literate.
-Changed the starting literacy of Texas from 50% to 70% for primary culture and 10% to 15% for the mexicans. Based on "Women and the Texas Revolution By Mary L. Scheer pp 88" and "A World Not to Come By Raúl Coronado pp 526". Average literacy in the start changed from 32% to 46.4%.
-Set literacy in Brazil according to state, with a few more literacy in state capitals in the south/southeast. Dropped the base literacy by one point from 8% to 7%. Data for regional state literacy was taken from the 1872 census, taken from "ANALFABETISMO NO BRASIL: configuração e gênese das desigualdades regionais by Ferraro and Kreidlow". Average literacy in the start date changed from vanilla's 7,7% to 5,3%.
-Renamed 2428 - Paraiba to João Pessoa, since in the region the name of the cities not the states is used.
-Changed Puno natives from Quechua to Aimara.
-The Colonial Museum of Natural History event will now cost money to build, like it mentions in the description. It will also be buildable only once, if you already have the modifier you can't build it again, potentially stacking the effects. If you choose not to build it though, the event will happen again.
-Changed Peru literacy. It will start from vanilla's 10% to 9% while the natives will start with 2%. The literacy is set by department, meaning it is basically set by province. The average national literacy in the game start will thus change from 4.4% to 6.4%.
The changes were based on "¿Ahondó o redujo el Estado la desigualdad en el Perú? Una mirada desde la historia by Carlos Contreras Carranza" and Democracy in Latin America, 1760-1900: Volume 1  By Carlos A. Forment.
-Changed literacy in Chile to 12% from vanilla 20%. Based on http://www.ine.cl/filenews/files/2006/septiembre/pdf/alfabetizacion.pdf
-Changed literacy in Argentina from 12% to 13%. Based on "América Latina en el siglo XX: ¿Se estrecharon las brechas o se ampliaron aún más? by Shane Hunt, pp22.
-Fixed a wrong localization in regards to the selling of Tranquebar.
-Prussia/NGF/Germany now has a decision to press the Neuchatel issue and escalate it into a crisis through a decision if they research N&I and the Neuchatel Crisis didn't fire yet.
-The Conquest of Araucania, Desert and the Chaco should now set the natives literacy to 1%. Pops in uncolonized areas always start with 10% literacy in V2 when they should start with 1%.
-The "Northwestern Territories" for the conquest of northwest Canada should now move literacy of the natives to 1%. Same thing for the Cape Colony, Angola and Mozambique events and the Matabele events that cede uncolonized provinces. Previously, the way the game handles literacy means that Matabele actually profitted form being expelled since their new homeland would have 10% literacy.
-Changed starting literacy from Uruguay from 10% to 15%. Pops in montevideo will also start with more literacy and Brazilians will start with the correct literacy. Based on "América Latina en el siglo XX: ¿Se estrecharon las brechas o se ampliaron aún más? by Shane Hunt, pp22.
-Changed the event that increases the slave population to have a bigger increase on population, based on the growth of slaves in the USA during 10 years. The base growth now is 0%, 4%, 4.4%, 4.8%, 6.2%, 6.6%, 8.0%, 8.4%, 8.8% and 10%. The intervals are the same (4, 5 and 6 years). During the event literacy for slave pops will now always drop by 8 points. The event will also only start firing after 1840 so it doesn't fire immediately after the game starts.
-The Trek Boer Modifier now should now put the Boer nations in the same foot as the new world, at least for a time, meaning it can get immigrants.
-Paraguay literacy changed to 11% from the previous 20%. Based on "Paraguay and the Triple Alliance: The Postwar Decade, 1869-1878 By Harris Gaylord Warren, right above 'the price of victory and defeat' in the introduction"
-The gold mine of Colombia will no longer be in Barranquilla but it will be in Medellin, the region that historically produced gold. Moved 70K pops from barranquilla: 45 went to Medellin and 25 to Bogota. This should make Bogota the most populous province. Changed the state capital of antioquia from Cucuta to Barranquila to help in its development. Changed the capital of Guaviare to Casanare, the only non jungle province.
-Reworked LR in north south america and the amazon. Invading Brazil through the amazon should cost more lives, fixed LRs in Venezuela, Peru and Colombia to allow natural growth.
-Izmail now starts with a fort.
-Bolivia will start with 5% literacy. Based on "Historia general de América Latina: Los proyectos nacionales  edited by Enrique Ayala Mora pp435".
-Ecuador natives will start with 1% literacy now while the primary pop start with 10%. Based on comparative data with Colombia and Brazil.
-Decreased the party loyalty effect from 0.004 to 0.003.
-Colombia starting literacy changed from 12% for primary pops to 7% and from 5% for natives to 1%. Based on http://www.banrepcultural.org/node/32671 and La modernización en Colombia: los años de Laureano Gómez, 1889-1965 By James D. Henderson, pp 39. Panama will start with 3% literacy average for central americans.
-Changed Venezuela starting literacy from 11% to 5%, based on comparative data with Colombia and Bolivia.
-Changed a small localization for the election pop up.
-Added a decision for the Russification of Finland.
-The game will no longer use "King" to address absolute monarchs, it will now use Emperor.
-Tweaked chances for the event to change puppets to your government if you are a fascist/communist dictatorship.
-Changed the starting party of Korea from Tonghak to Wangdapa. Tonghak doesn't exist until 1880.
-The AI will no longer use Intellectuals NF in in colonies.
-Stopped Warlord influence from spreading to russian owned outer manchuria, adding Manchurian cores back to it after the Russians removed it.
-Added another condition for the abolition of serfdom in Russia.
-Renamed Bruges to Antwerp.
-Added a few lakes to central asia, mongolia and Manchuria. Thanks for the anon who gave the original shapes.
-Changed the UK starting mobilization reform to No Draft.
-The decision to rename A-L is now available to any germanic country that isn't Elsass.
-The End of the Ottoman Dynasty should now release Tunisia if they are a vassal, besides releasing Egypt.
-Added a few north german, italian, french, bengali, yue and spanish pops to London. Based on https://www.oldbaileyonline.org/static/Population-history-of-london.jsp
-Fixed the party name of japanese anarcho liberals from NNM.
-Renamed Taicangzhou to Nantong.
-Illiteracy in spain is now defined by province based on: http://i.imgur.com/G40uEPR.png The national average decreased from 13.1% to 12.7%. Catalans and Basque pops are average 3% more literate than spanish pops. The literacy vary as much as 4% literacy in the south to 30% in the north.
-Removed starting core of India in Tawang.
-Reshaped Spain to better follow the historical province shapes that are also the modern ones, seem in https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Provinces_of_Spain.svg/2000px-Provinces_of_Spain.svg.png
-Fixed 3 rives in Spain not connecting when they should.
-Changed the starting relations of the Ottoman Empire. They will start with +20 with Prussia, Austria, Spain and USA and -75 with Russia due to their recent war.
-Mexican AI will not sign the Gadsden purchase if the USA owns any of their lands.
-Congress Poland will lose all their cores if they are defeated during the January Uprising.
-One state minors in the americas will now have just -10% to immigration compared to the big states to allow them to get some immigrants. They will completely lose their bonus if they reach 1M pops though and only have 1 state. 
-Reactionary party of Portugal will now have Jingoism to avoid the only Jingoistic party in Portugal being fascist.
-Weihaiwei got a starting port. Based on https://en.wikipedia.org/wiki/Weihaiwei_under_British_rule "The port of Weihaiwei was the base for the Beiyang Fleet (Northern Seas Fleet) during the Qing Dynasty."
-Added Kwangchowan and Shanghai as Treaty Ports that might be able to turn into precious metal provinces. Kwangchowan only turns if they have less than 30K pops and Hong Kong doesn't produce gold and Shanghai only needs less 90K pops.
-Netherlands now starts owning Sumbawa.
-The Organizing and reorganizing decisions for non-arabic african states will now turn that country to your religion.
-Added a decision to Organize Lebanon. The religion that will be in power will depend on who organizes. Sunni will leave sunni, shiite will leave shiite, orthodox will leave orthodox and protestant, catholic, coptics, jewish and mormons will leave catholic. Any other religion will leave the default - sunni.
-Added a decisions to change Lebanon religion if you own the religions and already have the country organized or if the country is your vassal.
-Uncivs with Isolationism will no longer suffer from the the high infamy economical effects from HPM. They will still get containment wars.
-Added Ukrainian party names made by anon.
-The Sahel Jihad CB now can only be used against animists instead of being a free for any CB. Changed so theocracies can also use the CB.
-Fixed sea province 3152 from vanilla having no data at all and consequently having a small almost non legible name.
-Disabled Sigmaringen until I can figure out why the game is not properly accounting for when it's inherited.
-Krakow will now start with the Culture tech school.
-Fixed being able to integrate Indonesia after using the reorganize Indonesia decision if you sphered them.
-The egyptian surrender will no longer fix Ottoman-Egyptian relations.
-Redid the Treaty Port system. Now it uses a CB called Punitive Expedition that makes the losing unciv country pay reparations and lose prestige. It can only be used in countries with a province that can be a treaty port. If you win, you can pick a treaty port. Right now the only countries that have treaty ports are Qing/Taiping, Oman, Persia and Morocco. Don't EVER negotiate Treaty Ports with two countries with the CB at the same time. If you do it, don't peace out with the other country UNTIL you pick a treaty port. Make peace with one, take a port then make peace with the other country.
-The CB for chinese reunification truce changed from 6 years to 8.
-The Scramble for Africa CBs now have a 2 year truce period instead of 5.
-Dismantle Empire, Great War and Become Independent CBs now have a 10 year truce timer rather than 5 years.
-You can no longer use the Add to Sphere CB in countries with 50M+ pops.
-Fixed a vanilla localization that read "(There is no applicable states)" to "(There are no applicable states)"
-create_south_africa decision now needs Revolution and Counterrevolution to show up.
-You can no longer Demand Concession (CB against uncivs to conquer a state) for a chinese state with more than 700K pops.
-You can no longer use the "encourage production" NF on colonies.
-You can no longer encourage Capitalists in colonial provinces.
-Restored the MTTH of Potato Blight event from NNM-set levels (120) to Vanilla levels (250). Made it happen only in Europe, like it's in vanilla. Halved the population effect (from -0.02% to -0.01%).
-Added historical names for a few wars.
-The AI will no longer call allies in the Rashid Civil War.
-Organizing Indonesia no longer change their primary culture.
-Stopped the AI from being so obsessed with getting soldiers to 5% and forgetting to use intellectuals.
-You will no longer be able to use the clergy NF in states with 4% clergy or use encourage capitalist NF in states with 0.7% capitalists. You no longer can use encourage farmers, laborers, craftsmen or clerks in states without factories or without jobs for these. You can no longer use encourage bureaucrats NF in states with no pops of primary or accepted culture. You can no longer use the encourage officers NF in states with 0.2% officers.
-Changed the AI priority for researching education techs. Changed 5 of the 6 education techs to give a 12% bonus instead of 10%.
-Increased RGO size across the world until I figure out how province size is calculated.
-Made the AI a little more inclined to promote Intellectuals.
-Balanced the effects of Child Labor a little more.
-The decision to Claim Bahrain and Qatar will disappear if you have a core on them.
-Stopped the NNM "Independence for X" events from firing if the country is at war. Made the AI way less likely to choose to set them free.
-Fixed troop positions in Madura.
-One state countries in the new world get a -30% bonus to migration, but they still get migration. When they get 500K pops they lose all bonus until they get another state though.
-Moved the event to play as Ezo to the point where the fate of Ezo is decided, to make it playable. Now selecting it makes Japan have them as vassal but it cedes any provinces they own in Sakhalin and give them their cores on Sakhalin. It also removes Japan cores on Ezo.
-AI countries under 40% literacy will no longer encourage bureaucrats in colonies. Except for Russia.
-West Indies region now contains all the provinces that were in Lesser Antilles and were british, while Lesser Antilles contains the french, dutch and swedish islands.
-Halved L-F bonus to output but gave it a 5% bonus to throughput.
-Stopped the AI from encouraging craftsmen/clerks in states with more than 30% unemployed.
-You can no longer use the Scramble for Africa CBs on Ethiopia, you can still use the normal protectorate/concession CBs.
-Tweaked the Franco-Siamese border treaty to give the Laos province to France rather than setting them free.
-Changed two siamese regions to better represent modern divisions and to balance them out a little more.
-Mexico literacy changed to 4% for primary culture and 1% for the rest. Based on "Tendencias educativas oficiales en México, 1821-1911 : la problemática de la educación mexicana en el siglo XIX y principios del siglo XX" By Ernesto Meneses Morales pp 427 note 1. See http://www.gbv.de/dms/sub-hamburg/525863095.pdf
-Changed starting literacy for the FRCA. The rates are 1% for natives. For central americans, it's 9.5% in Costa Rica, 7.5% in Nicaragua, 8% in Honduras, 4% in Guatemala and 7% in El Salvador. Based on comparative data from http://i.imgur.com/MSMirZ5.png
-Returned Beshik to vanilla shape.
-New American Alliance Communist Party renamed to Industrial Workers of the World.
-Reshaped Melilla.
-Disloyal Regiment event MTTH changed from NNM levels back to Vanilla levels.
-Reworked pops in Sudan, diminished the number of intellectuals significantly and extinguished animist intellectuals.
-The possible Treaty Ports in China are 12 as of now, including Macao and Taiwan (which needs revolution and counterrevolution to show unless your capital is in Asia). There is a treaty port in Morocco (Ifni), one in Persia (Qeshm), two in Oman (Gwadar and Zanzibar), one in Yemen (socotra) and one in Korea (Cheju).

_________________________________________________________________________
V0.3.1.3
-Fixed Animas province still being in Asia.

V0.3.1.2
-Added Namibia flags. Thanks AFPG!
-Made Heligoland in a colony again.
-Fixed the Trail of Tears decision needing Guymon.
-Renamed East Canton to West Canton and renamed Canton to East Canton.
-Fixed a potential event who could create British enclaves in Canada during the occupation of the north (of Canada).
-Removed natives as accepted from Peru, Ecuador and Bolivia, so it's back to vanilla.
-Fixed the Monroe Doctrine CB not excluding Bluefields.
-Fixed not being able to use the Place in the Sun CB if you are landlocked but are surrounded by colonies.
-Separated Chiloé Island from Mainland Chile.
-Fixed Isla Navarino being connected to other islands and to Osorno Province. Reduced the size of the Isla de los Estados. Separated Isla Gordon from the mainland. Separated the Tierra del Fuego from mainland South America and made the Strait of Magellan an actual Strait. Fixed Isla Dawson being connected to the mainland, fixed its shape. Fixed Punta Arenas province to better reflect IRL border. Separated from Isla Clarence from the other Islands. Fixed Falklands and South Georgia Islands shape. Fixed Porvenir-Rio Grande borders not being straight. Fixed all the islands and coasts in south Chile from Osorno to the Tierra del Fuego.
-Added a port to Porvenir province, now you can build a port there.
-Made the Guadalupe-Hidalgo decision tell the value it will cost.
-Fixed the coast of Ecuador and added the Isla Santa Rosa ( integrated in Esmeraldas) to the top. Fixed the Panama Pacific Coast up to Panama province. Fixed the rio Orinoco delta. Fixed San Felipe shape. Fixed glitches in Cayenne in Guyana. Fixed the Maracá Island being connected to the Macapá province proper. Fixed a ghost ocean in Sao Luis. Separated Ilha Grande and Ilhabela from mainland Brazil. Made florianopolis in an island. Fixed Carmen Coast. Fixed Porto Alegre Bay. Fixed the Amazon river Delta. Finished fixing the coast of South America.
-Forming Malaysia now should properly remove the cores of Sarawak, Kutai and Brunei if you own any of it.
-Removed the Trinidad - Guiria (Venezuela) strait to avoid the AI fortifying Trinidad with troops.
-Made a decision for Nicaragua to move their capital to Managua if it isn't their capital.
-Fixed two Bahamas Islands that were connecting and they shouldn't and fixed a graphical glitch in one of them.
-Added railroad spawn information to Qina and Aswan in Egypt so the tracks spawn in a more realistic manner.
-Added a decision for Egypt to move their capital to Cairo if they own it and it isn't their capital.
-Fixed the spawn points of railroads in Peru, Chile and Colombia.
-Natuna is now a part of Siak instead of Malaya so Indonesia might get cores on the Island.
-Made Atauro Island part of Dili province (east timor).
-Fixed a part of the Sea of Celebes being in Borneo.
-Fixed Malay-Indonesia border in Borneo. Made Pulau Sebatik and Pulau Nunukan in real islands.
-Creating Indonesia will now remove the cores of the constituent nations (Java, Aceh, Siak, etc) as it gain cores.
-Uniting Malay and Indonesia will now remove cores from the constituent nations.
-Added one event for the St Barths referendum. Changed the pops from swedish to French in the Island. The owner of the island have several options and can hold a referendum, offer the island to the UK, to the Netherlands, to France or keep it. France will respond to each of these situations and can claim the island if they don't get it. The referendum can have a french victory or not, and any loser can ignore the result and claim the island for infamy. The AI will respond and select an option depending on relations, GP status and others.
-Tweaked the Rhine Crisis declaration event and added a missing option.
-Fixed two lost pixels near Titicaca. Fixed the Titica shape and the Peru-Bolivian border there.
-The Dutch East India company events should not longer give CBs on vassals/spherelings.
-General prestige will now give a little more morale to the troops.
-Stopped Ezo from getting cores on Sakhalin to avoid problems.
-kaitakushi decision now requires N&I to avoid it firing too soon and Japan losing the modifiers because of Ezo.
-Made sure Wallachia and Moldavia lose all their cores once they don't exist and romania exists.
-Western New Guinea is now fully in Asia while Papua New Guinea is fully in Oceania.
-Changed Ostend Manifesto decision so it shows the requirements better and improved the AI decision making regarding it. The amount of given infamy is now random from 0 to 6.
-When Fascist, Communist and Reactionary rebels enforce demands the minority rights reform should default to Cultural Rights. Same thing when Fascist/Communist/Reactionaries Coup.
-Merged 2647 - Nizhneyansk in Yukagir. 2647 is now called Lifau, the first european settlement in Timor and former Portuguese capital of Timor.
-Added a custom picture for the White Rajah event.
-The French Foreign Legion modifier now increases mobilization size by 1.5%.
-Lowered the NV gap to mobilization from 1% to 0.5%.
-Changed mobilization values to 5%, 4%, 2% and 1% respectively. Service by requirements malus to education changed from -5% to -1%. To compensate, it will also give a -3% RGO output (less hands on the fields and more on the military).
-Removed the Bima tag, added the Timor tag. 
-Flores and Alor moved from the Timor region to the Sunda Islands region.
-Sawu Island is now part of Sumba rather than Roti. Added a few Hindu pops to Sumba to represent the population of that island.
-Sumba now starts under Dutch rule. That's partially correct. It wasn't under Bali and I can't find any source on who controlled it.
-Added an organized Timor decision. It civilizes the tag, change it to democracy and change it to the catholic or protestant religion, depending on who takes it. Also added a reorganize decision.
-Rebalanced the River of Silver modifier.
-Reduced starting relations for Ecuador and Peru.
-Fixed the provinces terrain and LR in Northern Africa based on http://sedac.ciesin.columbia.edu/downloads/maps/nagdc/nagdc-population-landscape-climate-estimates-v3/place3-biomes-africa.png
-Removed the Tibetan cores at the game start to stop Tibet from being extremely jingoistic the entire game. Added a Greater Tibet decision.
-Substates in China lost their cores in land they didn't own at the game start to stop them from being overly jingoistic.
-Reshaped the coastal provinces of Libya to better represent the Fertile area of Libya. See Biome map posted above. Also adjusted the terrain map for North Africa. Reshaped Gabes in Tunisia. Reshaped Al Arish in Egypt to follow the coast a little more. Reshaped Ziqaziq to be more aesthetically pleasing.
-The result of the reshaping and terrain fix in northern Africa is a better representation of the biome/terrain. It also means that Morocco, Algiers and Tunisia have more "usable" land while Libya has less. Egyptian plains are also only concentrated on the Nile and the Nile Delta.
-Changed Railway position in Rosarito to avoid it passing over water. Changed the railway position in animas.
-The Organize Botswana decision now changes the default (animist) religion to either catholic or protestant, depending on the country taking it. Previously, Botswana would be forever animist.
-Added a Namibia tag, added the cores to the map, made one decision to organize Namibia decision for catholics and one for protestant countries.
-Refuting Manifest Destiny now disables the Guadalupe-Hidalgo treaty even if Mexico isn't a GP.
-Changed the Persian decisions that give RP to give based on years_of_research instead of a fixed amount. 
____________________________________________________________
V0.3.1.1
-Improved the Portuguese Civil Code description.
-Made so the Portuguese events for the conquest of Mozambique don't happen if you have a truce with the uncivs, doubled the time the CB stays around and improved the event a little bit. Did the same for other similar events for Portugal.
-In the event "Schleswig-Holstein Under Our Control", selecting "Holstein may go, but Schleswig is $COUNTRY_ADJ$." will remove the german core in Aabenraa (Danish majority) but won't remove the core on Flensburg (German Majority).
-Fixed the Marmaris peninsula in the coast of Turkey being an island and added the Symi, Tilos, Nisiros and Krevatia islands to the Dodecanese province. Fixed Kefalos being separated from Kos, fixed Kos shape.
-The China tag should now have all the Chinese cultures as accepted.
-Fixed the Qing still losing RP after the Panthay Rebellion.
-Made Euboea Island (Khakhis) in a real island. Made Salamis in an island again and fixed the athens/corinth border and the coast of Greece a little bit.
-Made sure the events dealing with the sudanese rebellion don't give sudan for non european (also excluding Russia and Turkey) countries.
-Removed the Cherokee tag from the start, they will only come back after the Trail of Tears decision.
-Added a flag to guarantee the Found Budapest decision can only be taken once.
-Made so the French Indochina events always give CBs.
-The French Military Mission to Japan now requires Nationalism and Imperialism rather than Iron Steamers.
-Integrated the Faroe party names and event one anon made.
-Added one Lake in Florida and one in Argentina. Worked on the RDS integration a little bit.
-Fixed Scandinavian vassals not under the leader of the kalmar union but still under a scandinavian overlord not getting an event to unify with Scandinavia (and not getting the Kalmar Modifiers) if they were still a vassal. Reforming Scandinavia should also remove all Kalmar related modifiers now and include the scandinavian vassals of scandinavian countries. Schewslig and Schleswig-Holstein are included too and can be inherited when forming Scandinavia.
-To represent the semi independent baltic duchies properly, Daugavpils now starts as part of Russia.
-The vanilla assimilation events (the ones that remove a core from a province you have a core in) no longer get rescinded if the ruling party has a full citizenship policy, only if you have all allowed rights.
-Substates no longer take part in the events (the assimilation events) to gain or to remove cores.
____________________________________________________________
V0.3.1
-Fixed an event that potentially led to Bahrain being at war with the REB tag.
-(Hopefully) fixed Japan accidentally getting the Isolationism modifier after westernizing because of one event.
-Fixed an event/decision description string from vanilla.
-Fixed the Create Malay decision to remove the proper cores.
-Tweaked down the literacy level for a few states in India and Burma.
-Added an "Emigration" NF. It has some specific conditions to be used and it can only be used by the player in non colonial provinces.
-Fixed an inverted localization for an event.
-Excluded the AI from several "useless" NFs.
-You can no longer place a NF in a state if any of the provinces is occupied by an enemy country. The only exception is the Flashpoint NF.
-Having a party with planned economy in power will now lock the railroad and the production NFs, since they become useless in a country with planned economy.
-Made AI value clergy a little more.
-Fixed one greek flag.
____________________________________________________________
V0.3.0
-Fixed a few vanilla bugs regarding pops/events checking for plurality the wrong way. Expect more reactionaries with plurality lower than 20%.
-Changed fascism support a little bit: having over 20% revanchism won't give more than 1000% support for fascism, the maximum support is now 400% with 20% revanchism (this refers to revanchism influence only, it can go over 400% with other modifiers not related to revanchism). Only primary and accepted (with a few exceptions) pops care about revanchism when deciding if they are fascist or not, meaning natives in colonial regions wont care about revanchism. This avoid situations where poles living in Germany, for example, would be more fascist because Germany doesn't own Danzig.
-Excluded Lan Fang from the Warlord era events and the CB. Hopefully, this will keep them out of the Warlord era.
-Increased the LR of Indonesia to stimulate growth on the islands.
-Nations in bankruptcy now will be forced to minimum levels of tax and tariff to raise money. It will also erode the ruling party popularity.
-Fixed Libya and Tripoli not having some parties.
-Fixed Hungary missing a conservative party in 1836.
-Removed Asir as a tag.
-Re-purposed provinces in Greenland: 2591 - Holsteinborg is now Tranquebar. Pops based of https://books.google.com/books?id=YVIOAAAAQAAJ&pg=PA458 pp458. 2632 - Isotorq is now Kwangchowan, China. Scroll down more to see pop division logic.
-Separated Kyushu from mainland Japan. Funnily enough, the strait already existed in the files, so that was Paradox original intention, they just didn't fix it.
-Removed the Nagasaki-Cheju (aka Korea-Japan) strait.
-Changed Dakota culture color to differentiate from Yankee better.
-Made sure the event to normalize the population growth of Africa doesn't give too much LR for any province. 
-Tweaked a few values for mine RGOs technologies so there isn't a lack of late game iron/steel.
-Kaiser Wilhelm's Land decision now rename more provinces.
-Fixed Ryukyu parties.
-Constitutional Germany will now use the normal german tricolor.
-Gave Rio Grande a core on Reynosa.
-The event for the selling of Kashmir will now give a longer CB on Chitral to guarantee it can be used.
-Added a decision for Russia to change St. Petersburg name to Petrograd if they are at war with any North or South German GP and have Mass Politics.
-Ukraine Presidential Dictatorship flag should change from the default republican one to a special one (thanks for the suggestion AFPG).
-Removed any jewish primary state from the list of states that can enact the islamic law.
-Now Russia can't use the free annex_africa CB. Previously, only AI Russia couldn't, so to make it even, AI or not Russia will not be able to use it.
-Fixed a CB France got on Algeria that was lasting too long.
-Making peace with the emperor and changing to Japan no longer will make the Overthrow the Bakufu decision appear the entire game.
-The decision Annex Korea will no longer appear to Japan if Korea doesn't exist.
-Fixed localization in election event 14160 - "A Difficult Situation". The option order for it was inverted.
-Fixed Boxer Rebellion CB not working.
-It's easier to form Arabia externally now as you only need to have the cores sphered instead of annexed. And if you have all of Arabia and get sphered, the AI will force you to release Arabia.
-Fixed wrong positions in province 1080 - Chumikan.
-Changed the Netherlands NV to Productivity.
-Changed the Nationalist China adjective from NNM's Nationalist Chinese to just Chinese.
-Reshaped the provinces Zemgale and Latgale (IRL names) in Latvia according to one anon suggestions and map. Thanks anon!
-Changed Norway NV from liberty to equality.
-You can't use demand concession and establish protectorate CBs anymore unless you border the unciv or you (and them) are not landlocked. Landlocked uncivs need to be reached by land before you can justify and use these wargoals.
-Consolidated the Mahdist events, corrected a few descriptions and changed one image for one better.
-Fixed Istria and the Coast of Croatia. Istria is now a peninsula. Mostar now has a small sea access, so Bosnia has also sea access. To simplify stuff, soldiers can use the islands to skip Mostar and go from Split to Dubrovnik, so Dubrovnik and south Dalmatia is not treated as an exclave.
-The Scramble for Africa events for annexation shouldn't happen if the sphere owner or the sphereling are at war.
-The Ganghwa Incident will only happen if the country owns both Edo and Kyoto and if the Shogunate doesn't exist, in the case of Japan, or Imperial Japan doesn't exist, in the case of the Shogunate.
-Hopefully stopped the German Empire from being liberated as a vassal during crisis.
-Changed the way the Carlist wars work. The events now (should) only take into account revolts in Spain proper, not the colonies. Added a few new images to the Glorious Revolution events. Increased a few MTTH for the toppling of regimes during the Glorious Revolution. Added a decision to Abolish the Fueros, which is required to end the Carlists/Christinos. Added an event that completely stops the Carlist/Christinos events and rebels, it will happen once you Abolish the Fueros and once the Glorious Revolution happened or it's 1895. There's a MTTH of 30 months so it might take a while to fire. Made so discovering cells is a bit faster if there's a unit in the province.
-La Guardia Civil decision for Spain now requires state and government.
-Renaming Sakhalin will now also change the Strait of Tartary name accordingly. The "Coast of Sakhalin" ocean province will also rename to Coast of Karafuto, for consistency.
-Decision to rename Outer Manchuria (Primorye) if Japan, Russia or China own them. Each one has a set of names. Region name changed from Outer Manchuria to Guanwai. Japanese names are based on:
http://libcudl.colorado.edu:8180/luna/servlet/detail/RUMSEY~9~1~23445~80027:Karafuto-Urajio-homen-senkyokuzu---?sort=Non_Sort%2CName_Part%2CDate_Issued&qvq=w4s:/where/Russia;sort:Non_Sort%2CName_Part%2CDate_Issued;lc:UCBOULDERCB1~84~84,UCBOULDERCB1~17~17,UCBOULDERCB1~54~54,UCBOULDERCB1~76~76,UCBOULDERCB1~57~57,UCBOULDERCB1~69~69,UCBOULDERCB1~78~78,UCBOULDERCB1~70~70,UCBOULDERCB1~66~66,UCBOULDERCB1~52~52,UCBOULDERCB1~53~53,UCBOULDERCB1~60~60,UCBOULDERCB1~74~74,UCBOULDERCB1~61~61,UCBOULDERCB1~36~36,UCBOULDERCB1~59~59,UCBOULDERCB1~85~85,UCBOULDERCB1~72~72,UCBOULDERCB1~32~32,UCBOULDERCB1~21~21,UCBOULDERCB1~73~73,UCBOULDERCB1~71~71,UCBOULDERCB1~77~77,UCBOULDERCB1~64~64,UCBOULDERCB1~82~82,UCBOULDERCB1~65~65,UCBOULDERCB1~58~58,UCBOULDERCB1~68~68,CORNELL~3~1,univcincin~32~32,univcincin~27~27,CORNELL~15~1,CORNELL~14~1,univcincin~28~28,BardBar~1~1,CORNELL~9~1,ESTATE~2~1,FBC~100~1,univcincin~25~25,HOOVER~1~1,CORNELL~2~1,CORNELL~13~1,RUMSEY~9~1,univcincin~24~24,MOAC~100~1,ChineseArt-ENG~1~1,CORNELL-AER~2~2,univcincin~34~34,PRATTPRT~9~9,PRATTPRT~13~13,PRATTPRT~21~21,PRATTPRT~12~12,univcincin~31~31,univcincin~33~33,CORNELL-Asia~2~2&mi=13&trs=18
-Added a few more flavor events for Persia.
-Renamed Antigua province to Antigua & Barbuda
-Changed the amount of pops of Tristan da Cunha from 25 to 10. Changed the port from the Gough Island to Tristan da Cunha proper. Fixed Saint Helena pops according to http://en.wikipedia.org/wiki/History_of_Saint_Helena
-Heligoland is not colonial anymore, to avoid huge migration waves to this island. It's also not a English core anymore, but once the germans claim it they will also get it as a core, to avoid any odd behavior and to represent the long time they already held the province.
-Fixed Malta population. Rounded it up from 120K to 110K. Increased LR from 30 to 32.
-Separated Lekfada (Ionian Islands) from Mainland Greece. They were previously connected. The strait already existed in the files, but Paradox forgot to unconnect them.
-Changed the Italo-Turkish war event chain so if Italy wins they will take the Dodecanese too. Also fixed a typo that prevented the event to fire in some cases.
-Made Chinese a little more mobile than before. This will mean some immigration to the new world, hopefully.
-Added a "Island" terrain type, made to represent small islands. The criteria used to assign the Island terrain type was area, around 500 km². Sometimes, exceptions were made for sparsely or inhabitable islands that exceed 500 km², e. g. Galapagos. Archipelagos were decided on a case to case basis. The one with no island bigger than the limit were classified as Island, the ones with one or more islands bigger than the limit but low population were usually left with the old terrains. The Riau Archipelago is a problematic case, but it was left as a normal terrain rather than Island. The terrain type provides a malus of 25% to RGO size, it has lower supply limit for troops and it attracts less pops than the old types it was used. For comparison, the modifiers for pop selection of province are: -95% for Arctic and Desert, -90% for Island, -40% for Mountain and Marshes and -30% for Jungles and Semi deserts. NOTE: Paradox size for islands doesn't represent real sizes. You have islands that are smaller than others being bigger in the game. Don't use that for reference.
-Few pop corrections for a few islands. Made the northern part of the Kurils Arctic terrain and the southern part Mountain terrain. Falklands changed to Arctic terrain. These changes are made to better reflect the climate and topography of these regions.
-Added a missing flag for the Greater Norway decision.
-Fixed Dravidistan duplicate parties.
-Changed Kythira from Nafplion to be parte of Zante's Ionian Islands.
-Reshaped Nice to be more historically accurate. Based on http://en.wikipedia.org/wiki/County_of_Nice
-Fixed 1194 - Krasnovodsk being in Asia instead of the Near East.
-Fixed Kotor having an austrian core.
-Fiume now starts with a port, to represent its old and strategic port. Removed the one from Trieste.
-Hungary loses Fiume during the Hungarian settlement. While the city was disputed after that, having a port exclave of Hungary doesn't work.
-South Sakhalin population changed from 1020 pops (4080 people) to 600 pops (2400 people). Based on "The UN Declaration on the Rights of Indigenous Peoples and the Ainu people of Japan. pp 4". The number is from 1875 but since populations stays static in uncolonized areas, the figure will be very close to reality. More than the vanilla one, at least.
-Pogobi population changed from 1020 pops (4080 people) to 525 pops (2100 people). Based on http://www.siberian-studies.org/publications/PDF/sikdegraafshiraishi.pdf apud the All-Russian census of 1897.
-Changed the Shumshu (north Kurils) population from 1000 pops (4000 people) to 55 pops (220 people). Based on http://en.wikipedia.org/wiki/Ainu_in_Russia. Changed the population of the South Kurils (Etorofu) to 500 pops (2000 people), based on the same source.
-Ezo population changed from 200,220 pops (800,880 people) to 15,000 pops (60,000 people). The data is based on http://www.hkd.mlit.go.jp/eng/02.html and Race, Resistance and the Ainu of Japan by Richard M. Siddle (see http://i.xomf.com/qghws.jpg). 
-Changed 1644 - Nemuro name to Meakan. Meakan (Nemuro) and Ishikari start outside the control of the shogun, as he only took control of the whole of Ezo later. The Shogunate takes the rest of Ezo in the "Opposition to the Bakufu" event.
-Renaming Ezo to Hokkaido will now happen with the decision to establish the Kaitakushi. The new decision is meant to populate Ezo/Hokkaido, reflecting the policies of resettlement that led to the region being so populous in the first place. So it does more than just renaming. It will also change Ishikari name to Sapporo and Meakan to Nemuro.
-Moved the Hakodate province port to be in Hakodate rather than far away from it in a random place.
-Animist pops will not emigrate. This is meant to represent the animists where usually nomadic/primitive tribes, and just because they got in a country as a state doesn't mean they suddenly want to go to the USA.
-Fixed Kazakhstan and Chitral not being part of the great game CB.
-Added the province of Kwangchowan (2632), a potential treaty port. Renamed Zhanjiang, a name that only came into use later, to Maoming. The pops on Kwangchowan were defined using the following logic: Considering the population was 189K in 1911 (47250 pops) and that from the 19th to the 20th century the population doubled, that will give us around 23625 pops. Pops were deducted from Zhanjiang, the province the new province was formerly part of. Zhanjiang RGO changed from Silk to Grain and Kwangchowan RGO from fish to Silk.
-Reshaped old Zhanjiang (now Maoming). The Eastern part went to Nanning, Nanning got a port and sea access. Hainan is now part of the Guangxi region. The Hainan region got renamed to East Canton.
-Fixed Damagaram extra cores in Sokoto.
-Removed some lost pixels from the vanilla map.
-Changed 2637 - Novo Mariinsk terrain from Mountains to Arctic. Cleared an object (graphical glitch) from vanilla in the province that was basically a piece of the Bay of Oljut in the province and fixed its coastline which was also glitched. Renamed Novo Mariinsk to Vyon, the village that existed there at the time.
-The loss of the Mandate of Heaven is no longer a major event (it will not show up for everyone).
-Fixed the Unequal Treaties turning the conquered provinces in colonies for the Qing.
-Selling of Assab doesn't happen if the owner is sphered.
-Kamchatka is now released as a free nation if Russia is dismantled.
-Kamchatka should get Sakhalin and the kurils if Russia is dismantled.
-The CSA can't demand the 36" parallel if Mexico refuted the Manifest Destiny AND it is a GP.
-Made the RGO size malus for Deserts and Arctic terrains more severe.
-Corrected graphical glitch in the Bahamas.
-Fixed lake Dongting and Lake Poyang in China. They had "ghost" attachments.
-Reshaped Ardahan and Kars based on http://upload.wikimedia.org/wikipedia/commons/9/92/SanStefano4.jpg and http://upload.wikimedia.org/wikipedia/commons/6/65/The_Russo-Turkish_War_in_Caucasia%2C_1877.gif This opens the way to a conquest of Kars by Russia without horrible borders.
-Added Caucasus Greeks to Ardahan, Batumi and Kars. The numbers are based on the Russian Census of  1897 rounded up: 8250 Greeks distributed in Ardahan and Kars, 300 Sephardic jews in Kars and 1250 greeks in Batumi. Added 4000 greeks to Tbilisi. 3500 for Poti. 325 Greeks and 200 Sephardic jews for Erivan.  For references, See http://en.wikipedia.org/wiki/Kars_Oblast and http://en.wikipedia.org/wiki/Batumi_Oblast and http://demoscope.ru/weekly/ssp/emp_lan_97_uezd.php?reg=450). 
-Hungary reclaim Croatia decision now gives cores on Slavonia and Fiume too.
-Changed the name of Budapest province to just Pest.
-Made a decision for the unification of Budapest. It will change the province name to Budapest and start a population boom.
-Made a decision for Greece to move their capital to Istanbul and rename it Constantinople. It DOESN'T give an alert when it's available and it will only show up when you own the city.
-Stopped the Warlord era changing the government of non puppet Chinese states.
-Added Brno to Bohemia region in an attempt to stop the German AI making ugly borders.
-Lake Rudolf (3236) renamed to Anam a Cheper.
-Restored Gran Colombia color back to vanilla.
-Merged Lutlin (2590) to Vyon. No one (almost no one) lives in Lutlin, and even less people lived there at the time. Lutlin was re-utilized as Ceuta. Reshaped Tetouan and Tangiers to better reflect the Tangier international zone that was created.
-Changed the Gibraltar strait passage - Now a unit can only move from Cadiz to Ceuta or from Gibraltar to Ceuta.
-Changed Melilla 3100 pops, which was supposed to represent the Population of both Melilla and Ceuta in vanilla, to 500. Ceuta's population is 1750. Both are based on http://www.um.es/ixcongresoaehe/pdfB9/Las%20principales.pdf, pp2. 
-Reshape Yizhou and Laizhou so Yizhou borders Qingdao. Changed Qingdao from East to West Shadong region. Weihaiwei and Qingdao are in different regions now, meaning you can't get both with one CB in a unequal treaty. 
-Fixed lost pixel in the vanilla map in the coast of Suakin.
-Fixed the West Coast of Africa from Mauritania to Liberia. Several glitches fixed and improved the coast.
-Fixed the Nile Delta. Removed "islands". Improved Shape. Fixed the Suez and buildings int he Suez province to fit in the reshaped delta.
-Major province reshape in Egypt: Nile city provinces now follow the Nile properly. Egypt states changed from 7 to vanilla's 6. Fixed the capitals of the regions so the appropriate cities get more pops.
-Egypt no longer loses a core in Halaib in the Mahdist war.
-Initial Egyptian navy will now start at alexandria because they have a port there.
-Creating Indochina no longer gives a naval base in Saigon, to avoid a  bug where the naval base was destroyed if it existed there.
-Removed "Greater Tatarstan" decision. Area was mostly Russian.
-Changed Transylvania religion to Orthodox.
-Changed Kalmykia NV to tradition.
-Changed Greater Norway decision to give a core on 319 - Ostersund.
-Changed the events to rename Istanbul to decisions.
-Fixed all a lot of decision images to use the same tone/color.
-Fixed an artifact in Awaji Island.
-Heavily reduced the "shortage of women" modifier effects on population from the Chinese event of the same name. Added a picture to it. Added several pictures to the Taiping Rebellion (4 or 5, previously only one was used for all events) and fixed a few typos in descriptions.
-Slaves now start with the lowest possible literacy.
-Rebalanced literacy in all Arabic states + Afghanistan and states in central Asia (minus Persia). Pops from primary/acceptep culture start with 3% literacy, non accepted start with 1%. Most states in central asia start with 1%. States in North Africa start with 4%. Previously, some states like the Trucial States started with 30% literacy and Afghanistan had a literacy rate close to 2015 levels.
-All sub-saharan states will now start with 1% literacy. Few exceptions in Ethiopia.
-All Boer pops now start with 30% literacy, even if they are living in ares under unciv control.
-Changed Algeria changes: Changed Setif (mountains) RGO from Wool to Iron and Biskra (Desert) from Iron to Wool. Changed the RGO from 35 to 20. Changed Tlemcen (plains) RGO from Iron to Fruits. Changed Mascara (mountains) from Fruits to Iron. Changed Ouargla and Tuggurt LR from 35 to 10. Changed Naama and Laghwat LR from 35 to 20.
-Changed Taza (mountains) from Wool to fruits and Figuig (desert) from fruits to wool. Lowered the LR of Figuig, Rashidia and Warzazat from 35 to 20.
-To represent the loose relation the Kurdish emirs had with the ottomans (and the persian Shah), the kurdish states were changed from substates to vassals.
-Changed unit position in Hakkari (Bay).
-Fixed a map glitch in the coast of La Coruña, Oviedo and Santander.
-Reshaped Pau, Pamplona, Bilbao and Logroño to be closer to Basque regions according to an anon suggestion.
-Reshaped so Mt. Sakurajima doesn't touch Kagoshima. Reshaped Amakusa islands so they are don't touch each other and are slightly less strange. Removed the weird island that was supposed to be the Sadamisaki Peninsula and shaped the peninsula to the best the engine can do it. Added the "coastal" colors to the parts of japan that didn't have it, this avoids weird artifacts results from hills touching the sea. Moved Uto Peninsula to its right place.
-Corrected a typo in the Treaty of London (1864) (Ionian Islands) description and made it only possible if greece exists.
-The german reaction against a invasion of the rhine will not happen if germany exists of the three hurrahs decision was taken and it won't include the danubian federation of the united baltic duchies if they exist, to avoid weird behavior.
-Forming Germany as Luxembourg should no longer give French as accepted.
-Stopped A-H, UBD and DNB from using any of the War of Unification or "Hegemony" CBs.
-Integrated the America minimod, reshapes a lot of provinces in the Americas and allow for a more aesthetically pleasing 54" or fight borders.
-Fixed glitches in the African coast on Dakhla and Nouakchott
-Fixed a Glitch in the curonian lagoon and on the Vistula lagoon and closed the Strait of Baltiysk since it fucked stuff up and didn't have any function
-Corrected a huge error (missing part) between Stralsund and Schwerin coastal border. Corrected Lolland being connected to Sjaelland. Corrected Rugen being connected to the mainland. Corrected a bay in Copenhagen (the Roskilde Fjord). Corrected some Aland Islands that were connected. Corrected Gräsö Island being full of artifacts and connected to mainland sweden. Changed Sealon from being part of Uppsala. now it's an island and it's part of Vasteras. Fixed the Indalsaven river disappearing because it was passing through the middle of Lake Storsjon and not coming out.  Fixed a glitch in Osel.
-Made a decision for Texas to claim the Rio Grande border.
-Texas, California and Deseret now can refute Manifest Destiny.
-Fixed ghost rivers in Quebec. Fixed Great Salt Lake and San Francisco Bay.
-Reshaped Las Vegas, Mariposa and Monterey to accommodate the 36" Parallel (the slavery line).
-Manifest Destiny for the USA no longers gives Tucson. That's covered by the Gadsden purchase.
-Changed CALLALLY_RELATION_ON_DECLINE from -20 to -40.
-Fixed a wrong flag int he FRCA events that would potentially break Honduras breaking away. Made the republics that declare indepence get their capitals in the right place. Honduras also renames their capital to Tegucigalpa.
-Added an event for El Salvador declaring independence.
-Added a port to Managua and changed Rivas port from the Pacific to the Atlantic.
-Fixed a free people CB going to the wrong country during the FRCA wars and changed the default fee people CB from 1 year to 30 months.
-Fixed Nicaragua-Costa Rica border. Fixed a small bug on Bluefields and Liberia. Fixed Bluefields not having a port. Fixed the border of Nicaragua - Honduras.
-Stoppped the FRCA countries from immediately applying for statehood after they get peace with the FRCA (Now a country will only apply if it has 150 relations with the FRCA and it doesn't have a truce with them).
-Fixed Ambergris Caye Island.
-Uniting Germany or turning into A-H give some relation boost between Austria/Germany.	
-Fixed Cape Breton Island not being, well, an island. Fixed its inland. Fixed Nova Scotia and Prince Edward Island coasts.
-Limburg should be renamed to Maastricht once it's integrated by the Netherlands.
-Added a decision for the Netherlands to rename the Wallonian provinces (and one that renames it back to normal).
-Corrected all the FRCA decisions and events to not talk about the USCA.
-The Belize purchase and the Miskito Coast crisis decisions can be taken any nation that hold the capital of Guatemala and Nicaragua, respectively for each decision, and has Central American, Mayan or Mexican as primary culture. Also stopped a potential bug that would make the player purchase Belize from Belize and a bug in the NNM event chain about the purchase. You can't use these decisions if the owner of the province has the capital in the Americas.
-Removed British, French and Dutch from accepted for Guyana
-Added the Nicaragua Crisis of 1895 (that can happen with any country, really, either the FRCA or Mexico or any country that uses the decision to annex Bluefields).
-The NV change decision for uncivs will have the modifiers the NV will give in the description now, color coded like the game displays them.
-Slightly rebalanced some units performance in battle in different terrains: Artillery and Tanks should suck in mountains and forests. They move slower, deal way less damage and are more vulnerable to attack. Planes do a lot less damage in forests and are a little more vulnerable to attack. Calvary wasn't changed yet, but it will be so in the future if everything is working well.
-Fixed Dalmatia starting with Anarcho-Liberals.
-Increased the MTTH of one arab uprising province event.
-Fixed a potential bug that would make two sicilies be locked in an endless war with a non existing Sicily.
-Fixed typos in the "Occupy Misiones" event.
-Fixed typos in the Danubian Federation event chains.
-Integrated AFP V5.
-Fixed Pakistan still being part of the Doctrine of Lapse event chain.
-Re purposed 2662 - Nizhnekolymsk in Siberia to be Animas - New Mexico. It's included in the Gadsden Purchase.
-Fixed a localization problem in the systematic extermination event chain. The decision also shows the "allowed" governments but it will still disappear if you don't have one of those governments. This is made to be more clear.
-Increased the Colonial Transportation effect on colonial migrations.
-Added the Gadsden purchase event chain. It appears once you own the provinces around Tucson and Animas. There are 3 possible results (full demands meet, historical borders and no border change). The way the AI responds depends on very good (or bad relations) and GP status. In case of total rejection, you can eat 10 infamy to get cores on the historical borders.
-Restored a Denmark vanilla event that was commented out.
-Added a decision for the selling of the Danish India. It disappears if Denmark is a GP. Needs state and government and it doesn't give an alert. Compensation is 20K.
-Reworked the Italo-Turlisk War AI for selecting the options to make the AI more reactive to different conditions instead of just going for the historical choices.	
-China/Taiping/Qing can now claim Sakhalin/Outer Manchuria if they are united, own all their cores and have nationalism and imperialism besides being a GP.
-Integrated the Persian minimod V2. Some things were left out: Most custom govermnet names, the event dealing with famine, the one dealing with aryans, the ones about a persia choosing a path and the ones forcing Russia or the UK sphering them. Some things were fixed, namely the anglo persian oil company event that was supposed to fire for Persia once the UK founded the company, made the decision to found the APOC require Persia to exist. Fixed a few typos. Added pictures to the Ulama event chain.
-Added a tag for the Faroe Islands.
-Added a tag for Sigmaringen. Prussia/NGF has a decision to integrate it.
-Changed the Gold Rush in Alaska. Only one province, Kenai, will turn to produce Gold. The other gold producing provinces are now in San Francisco, San Diego and Los Angeles. San Joaquin doesn't turn to gold producing anymore.
-Sitka and Yakutat are now Arctic terrain.
-Changed Sitka-Canada borders to be right
-Fixed Pearse and Wales Island being part of Alaska. They are now part of Canada. Fixed Sitka - Stikine border.
-Colonization costs are restored to vanilla levels, but now high level naval bases give more colonial power.
-Made the AI use the Expedition to the Black Hills decision.
-Improved the Ezo event chain, made possible for Ezo to get all of Sakhalin if Japan/Tokugawa owns it before Ezo appears. The Republic will always get cores on the parts of Sakhalin that japan owns.
-Made initial adjustments for the coast of Alaska: several fixes, disconnected Sitka islands from Yakutat, fixed the northern border, made Vancouver Island in an real island.
-Fixed Tunisia - Algeirs Border around Lake Chott el-jerid.
-Made Haussman Renovations decision for France always show.
-Stopped the war to take over all of Algiers to call allies automatically. Made it also not fire when there's a truce around.
-Changed the Conchinchina campaign CB durations to 5 years from 1 year.
-League of Three Emperors decision and Anlgo-Japanese alliance decisions now can only be taken when great wars are enabled.
-The French Foreign Legion no longer gives a bonus to immigration to France.
-The Rhine Crisis escalation now has 2 outcomes: It can lead to a NGF/SGF united or it can lead to the NGF asking southern states to join. Reworked the chances of the states joining in the later. 
-Added a decision to claim Greater Croatia.
-A-H Can no longer form Germany.
-Fixed a vanilla map problem of a part of the East Hudson bay being in James Bay.
-AI states with slavery will no longer get the free CB against uncivs in Africa.
-Reworked the LR of the coast of Congo and Cameroon. It will be treated like the Heat of Africa (LR10).
-To avoid infinite wars for Formosa, a Formosa (formed by a government in exile with the event) can now remove the Chinese cores from their island if they have a truce with China and Nationalism and Imperialism researched.
-Fixed the Isle of Wight being connect to the mainland british islands. Fixed River Severn ending in the wrong direction. Fixed Anglesey Island being connected to the mainland. Fixed the Moray Firth. Fixed Shetland and Faroe Islands. Lots of other fixes on the coast of the British Isles.
-Added Tupinamba as accepted to Brazilian.
-Changed the name of Johor Bahru to Tanjung Puteri in the game start. Renamed Kuantan to Kampung Teruntum. Johor Bahru and Kampung Teruntum will be founded later. Added a decision for the sphere owner of Johore to annex it if they have revolution and counterrevolution.
-Added the Sultanate of Pahang and a decision for the Civil War in Pahang, it will end with Pahang losing their independence. Added slaves to Pahang.
-Added the Sultanate of Perak and an event for the Perak War, it will end with Perak losing their independence. Added slaves to Perak. Both sultanates were completely independent and had slavery. See https://en.wikipedia.org/wiki/Perak#British_colonialism, https://en.wikipedia.org/wiki/Sultan_of_Pahang and https://en.wikipedia.org/wiki/Johor_Sultanate.
-Added Siam cores on Pahan and Perak since Siam tried to conquer both in the past. They will go later if they sign a treaty (representing the Anglo-Siamese treaty). The decisions and events for the demise of the Malay sultans have no infamy attached to it, only the Pahang Civil War has it, so waiting to fulfill them is advantageous. Improved the LR around the area from 30 to 35, some of the improvements only come with the foundation of the new cities.
-Tried to make sure when Romania is formed Wallachia and Moldavia lose their cores.
-Renamed Kuala Lumpur to Kelang. The name changes later when the other provinces in the area get renamed.
-Added the Selangor Sultanate and gave a decision for a GP to annex it by establish a Resident there.
-Creating Malaysia no longer releases it as a vassal.
-French language schooling now removes Breton as accepted and appears from the start.
-French dismantling Germany no longer gives a core on Saarbrucken.
-Fixed Brunei shape.
-Fixed the Batang Kemena river being duplicated.
-Dismantling the NGF should also remove the Alsace and Lorraine cores.
-The reforms that reduce education efficiency have that malus reduced a little bit.
-The Iwakura mission now gives a school reform if Japan has no school reforms. Improved the description of the decision.
-Added a decision for Japan to enact the Imperial Rescript on Education. It's available for Japan only - not the Shogunate.
-Added the Shinbutsu Bunri decision for Japan. It changes the religion of Japan to Shinto. Changed the initial religion of Japan and the daymios back to the vanilla Mahayana.
-Changed the Alaskan Purchase to avoid the AI going bankrupt over it.
-Made the Indochina campaign give proper CBs to finish Dai Nam.
-Renamed Cheyenne to Rock Springs to match the province shape.
-States with slavery allowed will not be able to use the "Scramble for Africa" CB.
____________________________________________________________
V0.2.9.9O Hotfix
-Fixed two provinces being called Yekaterinodar.
-Increased the output of mines and Iron for certain techs to avoid late game shortage.
____________________________________________________________
V0.2.9.9O
-The "100 days of war" event no longer fires if you didn't lose a war. To compensate the MTTH was reduced.
-Forming Scandinavia no longer keeps the leader of kalmar union and the customs union modifier. Why the hell it didn't remove that before?
-Added an option to keep a democracy in the "a return to bourbon rule" event for democratic Spain.
-Fixed parties in Lan Fang and China.
-Made sure Prussia/NGF/Germany doesn't keep cores in Neuchatel after the crisis ends.
-Fixed the Indian Nationalism event to fire only if there's indian pops in the province. Before it checked only if it was an Indian core.
-Fixed a potential crash with the destroy monuments decision.
_____________________________________________________________
V0.2.9.9N
-Fixed wrong modifier names for an event
-Fixed the vanilla bug of the Azov province port missing
-Fixed a problem with the Ezo republic event if the player choose to play as the Republic
______________________________________________________________
V0.2.9.9M
-Fixed a bug with an australian event giving more LR than it should and firing non stop
-Homestead Act now requires state and government at least to fire, it reduces MIL and CON a little bit. Hopefully, it will help the USA be a little more stable.
-Rebalanced a tech tree in Commerce so most of the RGO bonus stuff is on the industrial "power" tech three instead of of the Commerce one. There's still some there but the big bonus doesn't come from there.
-Rebalanced AI priority with a few units, guards are now more useful than infantry (they don't have less defense) and increase the maintenance cost slightly for some units (tanks, guards and planes).
-Added NZL and Australia as countries that can take the decision to encourage immigration.
-Moved Bonny from Warri to the Aro Confederancy. Historically, the town never had ties with the Warri and was closer to the Aro.
-Fixed the vanilla bug of Tsushima not appearing.
-RDS was updated
______________________________________________________________
V0.2.9.9L
-Fixed a potential bug with one event
-Made the event to slow down germany's population growth now only fire in the late 19th century
____________________________________________________________
V0.2.9.9K
-Winds of westernization now happens if your neighbor a GP or a sphered country
-Pre-Mobilization modifier now has a bigger economical impact but it doesn't have a CON impact
-To simulate the lower birth rate that a industrialized society brought, when germany hits around 60M pops they will get an event that lowers all LRs in their cores from 40 to 35.
-Fixed China not having a reactionary party late game
-Tweaked some values to encourage the population boom of Egypt and China
-Restore america CB no longer gives any prestige
-Changed the Two Nation Theory decision to so a nation can externally add the cores more easily
-Changed New Zealand and Australia NV from Liberty to Order. Hopefully, this will avoid frequent GP Australia.
-Changed the names of the Circassian parties, adjusted some cores.
-Added an event to adjust Australian RGOs: some gold mines will dry, some places will change. The Australian capital also starts as Melbourne (they were de facto the capital) but it will eventually change to Sydney.	
-Sligthly reduced Egypt starting ltieracy to compensate for the large growth bonus they get and to stop very early westernization. Now you really need to win the oriental crisis.
-Seizing lagos will now damage UK's relation with nearby rulers.
-Added an event to normalize UK relations with arabian rulers after the UK takes Yemen.
-Spanish-american war no longer makes either side call allies, it doesn't happen when the USA has a truce with Spain.
-Makran, Kalat, Kokand, Khiva and Bukhara now all start with foreign weapons. Based on http://www.iranicaonline.org/articles/firearms-i-history and other anon sources.
____________________________________________________________
V0.2.9.9J
-The Manifest on Unshakable Autocracy now can only be taken if Russia is not an absolute monarchy.
-Removed technologies that the Qing shouldn't have at the game start.
-The Qing doesn't lose research after conquering Taiping anymore, but it also doesn't get any research points when conquering anything anymore.
-Fixed the recognize Cuba/Philippines decision (thanks Rylok).
-Removed the spanish cores from the spanish-owned islands east of Philippines.
-Fixed a graphical bug from the Siberia mod near the Arctic Ocean.
-Nerfed the increases in RGO efficiency in the "power" tree of the Industry section.
-To avoid Switzerland getting to GP, east and west Switzerland were merged in one "Switzerland" region. To compensate for the prussian core that would allow them to annex the whole country while pushing that claim, Neuchatel is now a tag, a vassal of Switzerland and in the Prussian sphere. Events to simulate the Neuchatel crisis were added.
-Two Sicilies lost 2 military and industrial techs and 2 units at the game start. The Expedition of the Thousand decision now gives a conquest CB on Two Sicilies and one acquire state CB in the Papal States.
-Added another missing effect description (thanks Paradox).
-Fixed Champasak not being releasable as a vassal, gave Siam a decision to annex them for less infamy.
-Made so the Sicilian revolt makes them start at war with Two Sicilies
-Added an option for the chinese to rename Port Arthur back.
-The treaty ports now include Weihaiwei and Qingdao again, but only if they have less than 20K pops.
-Added a few protestant pops to coastal south china to represent missionary activity in the area.
-Added the events and decision from the persia minimod by H.P. Thanks a lot!
-Added a decision to claim Greater Iran for Persia. I still need to do something about pan-Iranism and the relations between pan-arabism, pan-turkism and pan-iranism.
-The Eastern Question and the Crimean War can still happen if Turkey is a GP.
EXPERIMENTAL -Added decisions to stabilize a proletarian/fascist dictatorships. You need mass politics to enact them (and some have some other requirements), they have an interval of around 2.5 years between each and they represent the shift to a totalitarian system.
-Added generals to the Taiping at the start of the Taiping rebellion.
-Added an option for China to claim Tibet.
-To avoid exploits, the decision to free vassals is only available for civilized countries now.
-Changed the Yemeni sultanates conquest decision so it can be taken only once per game, so the first country that takes it will be the only country that can take it.
-Decreased the MTTH for russia to annex vassals in the great game
-The infamy reduction you get from releasing a nation was reduced from -5 to -2. I considered removing it altogether.
-Crisis cooldown changed from 36 to 24 months to allow for more crisis late game
-The AI will now get the final 25% education and administrative efficiency when they reach 75% spending.
-Uncivs get a baby boom when westernizing now. It can last 4, 3.5 or 4.5 years.
-Pandemic influenza now spreads more slowly between neighboring countries.
-The Taiping can now rename Nanjing to Tianjing, and china/qing/chinese states can rename it back.
-Tweaked the Sikh Empire modifier to be less OP.
-Fixed the decisions to recognize the caucasus countries to appear only if they are not part of a sphere and are uncivilized.
-Civilized Countries with a gold rush in the new world and with a capital in the new world (or africa) will correctly get a global immigrant attraction now.
-Added an event for the welcome stranger.
-Fixed a few terrains and LRs in Arabia.
-Added a decision for a GP to integrate rogue states (like bahia and pernambuco) back in Brazil if they sphere both.
-Lowered ottoman starting prestige back to vanilla levels.
-Made equality assimilation and militancy reduction bonus higher.
-Changed the terrain from South Georgia
-Doubled the starting population of the Sokoto Caliphate. Now the full Sokoto (Sokoto + Bornu) should have around 10M people.
-Changed Lagos production from tropical wood to Fish and Ibadan from Coffe to grain.
-Added an option for countries in the Americas can take to burn some money and get a short immigration boom. It can only be taken once. Currently, only the Brazilian AI will take it.
-Changed 765 Cagliari from sulfur to coal.
-Fixed one NNM event.
-Added one event for the Abdelkader El Djezairi revolt and the final conquest of Algiers.
-Increased a few LRs in Italy and changed the production of rome from fruits to Grain
-Germans and Italians are now a little more likely to emigrate after 1880.
-Fixed the Krakow question events to give the event for the NGF/PRU/Germany if they exist.
-Increase the LR in Egypt in a few key provinces, lowered it in others. A better change will come in the map phase as much stuff needs to be redone.
-Slightly increased the MTTH of diseases events. They were killing too many people.
-Islamic Law can now be taken by uncivs.
-Added a irredentist decision for Norway.
____________________________________________________________

V0.2.9.9I
-Changed the maximum amount you can loan from a single country from 10% of tax base to 20%. Hopefully, this means countries will be more encouraged to get their money back if a country goes bankrupt.
-Finished party names and policies changes for Baltic States. The UBD will also not be affected by the liberal revolutions anymore. Thanks for the good work anon who made http://pastebin.com/hLZRbHzp
-Made so the Greek decision to pass constitutional reforms require either 40 prestige or state and goverment researched. The prestige gain was halved.
-Fixed a vanilla event description.
-Made sure Yazidi Bohtan can't take the Islamic Law decision.
-Complexified the Limburg Crisis by making an expanded event chain. Instead of trying to use the shitty crisis system, if the germans try to take Limburg, it will spark an international crisis where european GPs can define their position. If the NGF/Germany manages to unpuppet Limburg and sphere them, they can annex it. If they don't DoW the Netherlands for six months, they will lose their chance. There's several paths where Limburg will end now, from German annexation to early dutch annexation.
-Jingoism required to add a wargoal increased from 4% to 5% to stop AI blobbing.
-Changed how cholera spreads: It doesn't spread to Arctic or Desert provinces, but it spreads faster in Marshes and Jungles. It also needs at leas 35K pops in a province for it to spread there.
-Other diseases that kill a random % of pops in a state now don't affect states with less than 10K people. Pandemic Influenza won't affect provinces with less than 3K people. Too small or remote provinces wouldn't be affected as much by pandemics and this helps prevent small islands or places with very small population from being wiped out.
-Changed the diseases rework so diseases can happen in one province countries, to avoid shit like 1M pops country with no diseases. Changed the 100K total country pops requirement for diseases to happen from 100K to 50K.
-The Italian Red Shirts will no longer offer Italy to a theocratic government.
-Changed Western Slavic name to Western Slavic Minor.
-Made France/German AI a little more aggressive when research coal/steel technology.
-Fixed the decision for the dutch to propose a treaty over the Aceh happening more than once.
-Made so the British don't get the death of Ranjit Singh event if they are not neighbours of the Sikh Empire.
-Made the population of the Faroe Islands be Icelandic in culture
-Changed Bekeret (1205) LR from 20 to 15
-Changed Austria's cores from Vanilla to NNM standard
____________________________________________________________
V0.2.9.9H
-The employee limit needed before "upgrade all" would upgrade/expand a given factory changed from 90% to 75%
-Increased the debt limit of factories from 2500 to 3000 and the leftover paycheck from 25% to 30%
-Fixed a bug that made Sweden have the liberal revolution modifier forever
-Moved Belgium's Machine Parts factory to Wallonia
____________________________________________________________
V0.2.9.9G
-Corrected the game over message from vanilla to have proper capitalization.
-To balance immigration, changed Canada NV from Liberty to Order, Argentina from Liberty to Order, Brazil from Liberty to Equality.
-Event to free Liberia only happens if the USA is not at war.
-Caouzhou (1564) will flip from gold production to grain production sometime late game so China doesn't swim in the money of 8 million people working in a gold mine.
-South American nations got natives as accepted to stop them assimilating in the main culture.
-Made Medan have a port so you can station ships there or build a port.
-Korean name and flag will change once they stop being an absolute monarchy.
-Fixed so Yazidi don't convert if they are in the near east, not asia.
-Decreased the cost of the artillery unciv reform and gave it the bonus of conquering uncivs that was on building forts.
-Forming the Arab Union as Egypt will now remove cores from the greek islands and Cilicia, so the Arab Union cores stays in the arab world.
-Balfour Declaration is not available to Iranian/Turkic/Arabic cultures anymore.
-Removed Samos, added Qatar. The Sphere Owner of the Trucial States now can add Qatar and Bahrain to the Trucial States pact, making management of a sphere there more simple.
-Added a decision and province modifier for Qatar and Bahrain to avoid the pops there from starving to death.
-Several substates from uncivs were removed. The reason is that, while most have a degree of independence, they are not working with the economy. Usually, uncivs survive by sharing a market with the sphere owner or by producing the resources they need themselves, but substates usually don't get either and the people just starve to death. 
-For balance reasons countries with less than 100K pops will not get any disease events, same with single province countries. Diseases also don't spread as fast in the Near East as in the rest of the world. The reason for this is the aridity and the high mobility of the populations there, which prevents diseases like the spanish flu (in game just called strange flu) going pandemic. Once countries in these regions civilize though, they will be treated as all other countries, since it's assumed a good part of the population settled and we have big urban centers connected to each other that make pandemics plausible.
-Reworked starting wars to minimize prestige spamming from parties involved. Brazilians are dealing with a rebellion, so they will not get any prestige from the war. Netherlands will only get the lands from the Padri war.
-Added an event for the British conquest of Sikkim, the Bahrain-Qatar War and the British war to sphere Bahrain.
-Commented out the Oregon Trail event that to avoid crisis over colonized land. The land now gets its LR and Baker city back when the Seattle renaming event happens.
-Added a decision that the Ottomans, Persia and Arabia/Nejd can take to claim Doha and Bahrain for free if they have N&I researched. Historically, the Ottomans even occupied Doha and the Persians claimed the region which led the british to rename the region the "arab gulf" instead of Persian Gulf to dismiss their claims.
-Added a decision for the sphere owner of the Trucial States to Puppet them if they have revolution and counter-revolution researched. This represents the increase of GP interest in the area and the history of the Trucial states. In exchange, the Trucial States abolish slavery and get some research points.
-Added events for the Black Flag Army in Luang Prabang and their surrender to a neighboring GP (that isn't China/any of the southeast asian countries).
-Added events to simulate the Franco-Siamese War (which can happen to other GPs if you are on Dai Nam).
-Cracked down on another event that would allow the UBD to petition for annexation in Germany.
-Added caribeno back to haiti to avoid assimilation, they lose once the dominican republic breaks free.
-The Oregon Crisis will not add cores for the UK in Idaho.
-Fixed a missing core for Russia in the Caucasus and add a temporary modifier to encourage immigration and help them stop the state from being colonial.
-Moroccan monarchy flag will change to modern flag if they stop being an absolute monarchy.
-Chitral will ask help from the British if they neighbor them and the berlin conference already happened.
-The $COUNTRY_ADJ$ Territories event, in which puppets asked for their cores their overlord owned, was disabled for the AI, since the AI always takes it and accept it which lead for the AI returning parts of India to indian minors. Now the event will only happen to the player.
-South African Cores can now spread up to Namibia.
-Fixed a bug about a province in uzbekistan being in 2 regions at the same time
-To avoid too much unemployment in the countryside in the americas, especially in the USA, the RGO bonus to size was doubled.
-When Persia becomes a constitutional monarchy, they will change the name to Iran and the flag will change too.
-Removed the Scandinavian cores from Scandinavia and the tag is also not considered a normal cultural union anymore. You still can form Scandinavia though and the cores will be added as such. For all purposes, Finland nor Finnish as accepted are included
-Added a missing localization line from Vanilla about the location of the capital.
-Fixed Sakhalin being shown as "Russian Asia" if they own all of it.
-Lowered overall US influence and relations in the americas to stop early sphering.
-Fixed the external formation of argentina decision to make sure all land goes to them.
-Russia will more aggressively annex their substates now.
-Rebalanced Serf needs.
-Changed Yurimaguas (2287) from Ecuador to Peru. They still have their cores, the region was disputed.
-Changed sphering so relations matter more. Lowered starting relations and sphering status for SA countries with the USA to avoid aggressive and extremely early sphering.
-Fixed the Baluchistan decision so it gives cores on Baluchistan proper, including Persia.
-Changed how the autocracy NV works on ideologies: On Democracies, Monarchies and Presidential Dictatorships pops will be more prone to be conservative. However, in Bourgeois, Proletariat and Fascist dictatorships, pops will be more inclined to the ruling party ideology. The exception are Aristocrats and Capitalists, and they are way less inclined to be communist now.
-The USA will now lost the homestead act if it has less than 3 states or doesn't have any port.
-Shinto added on the list of religions that makes pops usually conservative.
-Severely nerfed the militancy gain from the colonial exploitation modifier to avoid africa exploding.
-Added a decision to form Somaliland as a colony.
-Severely nerfed anarcho liberals under autocracy NV.
-Added a "Found the Suez Canal Company" decision to end stalemates over sphering Egypt.
-Increased the usefulness of the railroad and build factories NFs.
-Reworked some technologies priorities for the AI.
-Made so the US AI can take the "reconstruction act" more aggressively to try and stabilize the country in the post war. It also reduces overall militancy.
-The Ottoman Empire will release Egypt if during the scramble for Africa it ever drops from GP status.
-Russia now has a decision to reform the government after losing a war after the Crimean war. This will change their tech group to military-industrial complex along with other benefits.
-To increase the Russian ability to hold a large army and to reflect the historical mines in places, 2689 in the Urals will flip to gold at some point. Semipalatinsk, in Kazakhstan and Kirensk near lake Baikal will also turn to gold.
-Increased the MTTH of the chinese war of reunification and the increased the average time they take to happen too. The events also don't happen anymore if the country is a puppet.
-Pops in overseas provinces (colonies) will enjoy a reduced militancy. It's not much but hopefully it will avoid Africa exploding in a trillion rebels. 
-To avoid the AI releasing african puppets to try and colonize more, they will only pick the options to civilize and organize the african countries in 1905.
-Corrected the Expel Manchu decision so it sends people properly to Inner Manchuria instead of sending them to another part of Primorye (inb4 deportation crash, fuck you game).
-Renamed Port Hope Simpson to North West River (yes, it's the name of a city).
-Added a decision and events for the Titanic. You need to have at least Steel Steamers for the decision to show up.
-Made the AI try to build the canals more aggressively.
-Made Pops be even less inclined to move to deserts and tundras.
-Changed Deseret's color 
-Made a decision to add Finland cores and Finnish as accepted to Scandinavia, separately. You also can't form Scandinavia with Finnish as accepted anymore.
-Changed some social reforms values that reduce pop needs to keep global needs up.
_______________________________________________________________
V0.2.9.9F
-Fixed for the last time the Moroccan question decision. Thanks for finding the double ID anon.
-Fixed the Vatican Council decision. It now only appears when the Papal States are a theocracy.
-Merged North and South America in a single continent and used the slot to fit a new "continent" called Near East. It goes from Suez to Persian Azerbaijan, and from Uskudar to Afghanistan, including Cyprus, Makran, Kalat and Central Asia. Hopefully, no more japanese Turkmenistan. This will keep the Japanese out of the middle east and the americans in america.
-Made sure there's political parties around the earliest date Fascism can unlock.
-Fixed a bug that removed one Paraguayan modifier too early.
-Changed the Temperance League events to check for the capital majority religion instead of the general country majority religion so the Netherlands is not treatead as a muslim nation because of Java.
-Added a Karelian core in Petsamo to avoid Russian exclaves
-EXPERIMENTAL: Burgueious and Proletariat dictatorships now can add political reforms on the face of a strong political movement and if they have 9 average militancy.
_______________________________________________________________
V2.9.9D
-Fixed (again) the Spain decision for the partition of Morocco.
-Balanced a few decisions and modifiers, decreased relations of the yemeni and the somali sultanates to incentive conflict.
-Suffragette movements will not happen outside Europe, North/South America and Oceania now. And it will not happen in muslim nations. It also requires a high average literacy (more than 70%) so illiterate countries will not be pressured soon.
-Stopped the AI from instantly going to war against its puppets during fascist/communist revolutions. It wasn't working out so well so the AI will not only get the CB.
-The end of the Ottoman Dynasty will now set Egypt free in case it's still a vassal.
-Changed the Mughals Color
-Balanced some the tradition NV, some modifiers and events.
___________________________________________________________________________________
V02.9.9C
-Rebalanced a few events.
-Tanzimat reforms for the Ottoman Empire now abolish slavery and serfdom.
-Autocracy NV now doesn't prove a direct decrease to CON, but reduces the impact that literacy has on CON gain.
-The Mughal Empire can get Bengali as accepted, to differentiate them from India.
________________________________________________________________
V02.9.9B
-Fixed a bugged Spanish decision.
-Fixed Cizre being in South America
-If an external nation creates argentina that still owns Tarija, it should give Tarija to Argentina back.
_______________________________________________________________
V2.9.9
-Removed Kola region, it's now all Karelia. The region was too small and had almost no one. Reshaped
-Renamed a bunch of Russian provinces that had the wrong name.
-Reshaped Petrozavorsk so that Karelia ends in the Svir River.
-Fixed a graphical glitch near Singapore.
-Fixed the AI Netherlands not getting their proper CB in the Padri War.
-Removed the BYZ tag. Megali Idea is still in.
-Fixed a missing core in Kokand Kazakshtan, fixed one province LR in Sumatra, rebalanced the Bukharan cores and fixed the Padri War (which will be settled through an event).
_______________________________________________________________
V2.9.8
Special thanks for the help of AFPG, Siberian Mod Guy and Baltic states party guy. Your work helped a lot, thanks!
-Autocracy and Tradition NV now makes more people conservative than Order
-Sunni and Shiite pops are now usually more conservative too
-Added the Kurdish states that existed in Persia/Turkey/Iraq. Most are sunni, exceptions are Ardalan (shiite) and Bohtan (yazidi). Any (exception is Bohtan) of them can become Kurdistan if they are civilized and researched N&I.
-Added the Yazidi religion. Bohtan is the only Yazidi state in the game. They can claim the Kurdistan cores if they civilize and research N&I. Yazidis are one of the least mobiles and less prone to conversion pops.
-Amapa, an old small unpopulated province in the north of Brazil, got its population integrated in the Macapa province. It's now used as the Jezira province in the Ottoman Empire.
-Fixed a vanilla province fort building location.
-Changed the name from Urumia to Urmia.
-Building canals now gives the nation that built it a core there.
-The Ottoman decision that gave Misri as accepted now gives Mashriqi as accepted instead of Kurdish.
-Lowered the Ottoman Empire and Paraguay starting Literacy. Ottoman Empire should start with 9% average literacy. Paraguay starts with 15%.
-Tweaked infamy for some decisions for the Netherlands, Ottomans and the genocide one. The infamy gain was lowered in all cases.
-Made Two Sicilies Reactionary party State Capitalism again
-The NNM description now explains the war against Argentina is for a democracy there, not for the independence of Entre Rios.
-Rich strata pops no longer immigrate to communist countries
-New World countries only get their 400% vanilla immigration bonus if they are a constitutional monarchy, democracy or presidential dictatorship.
-Fixed the Sikh Empire mobilization size so it's closer to what Rylock intended. Ranjint Singh will also hopefully get a few more years of life.
-Drastic rework of the Isolation modifier to make more sense. Import Cost and Loan Interest were massively increased and some of the other effects were removed. Thanks for the input, anons.
-Added a tag for the Principality of Samos and gave them Chios. They pay tribute to the ottomans and can be integrated later. http://en.wikipedia.org/wiki/Principality_of_Samos
-Reactionary Two Sicily party now has state capitalism
-Reduced overall Greece starting literacy based on data from http://unesdoc.unesco.org/images/0000/000028/002898EB.pdf https://www.academia.edu/2084631/Informal_Learning_in_Late_19th_and_Early_20th_Century_Greece_Greek_Children_s_Literature_in_Historical_and_Political_Contexts
-Added an event for the selling of Kashmir.
-Made so United Baltic Duchies (hopefully) don't apply for statehood in Germany.
-Being mobilized in peace time now damages your relations with your neighbors, even allies, increases WE and diminishes the WE and infamy reduction.
-Overall revamp of the AI tech priority.
-Made sure Tajikstan, Uzbekistan, Turkmenistan and Kyrgyzstan get released if Russia is dismantled. Added events for the westernization and for the organization of these cores, replacing the old NNM stuff.
-Changed party loyalty NF effectiveness from 0.001 to 0.004
-Ryukyu can't be inherited if it's a player
-Added the Princely state of Chitral and gave them Chitral.
-Added Pakistan tag and the decision to put cores in its place. http://en.wikipedia.org/wiki/Two-nation_theory#Start_of_Muslim_self-awakening_and_identity_movement_.2819th_century.E2.80.931940s.29
-Made so Guadalupe Hidalgo doesn't bankrupt AI USA anymore.
-Panjabi, Sindi and Bengali are not "indian" culture group anymore. This is made so these mainly muslim groups don't want to unify with India normally. They are Indo-Iranian group and get the same leaders and sprites as Indians.
-Fixed a vanilla province name in the Caribbean being too messed up.
-The FRCA capital now starts in San Salvador rather than Guatemala City.
-Added a decision to form Pakistan. You need to have Baluchi, Panjabi, Sindi or Pashtun as primary culture and you can't be India, The Sikh Empire or the Mughals to do it. You need to be a great power and have revolution and counterrevolution researched as well as owning all the cores for the sikh empire, Kalat, Makran and Sindi
-The UK now starts with Australian as accepted.
-Fixed so that vanilla "factory safety events" that give reform desire don't happen if you don't have any factories (actually, any industrial score).
-Added a Karen tag and the karen nation. Added a few protestant Karens in Karen-majority British Burma so they can convert to protestant.
-Added a decision for the Durand Line and the settlement of the Afghan-Indian Borders.
-Serfdom can only be re-enacted if you have an absolute or semi-constitutional monarchy. You can however, at the cost of infamy, issue a decree to abolish serfdom and re-enact slavery.
-Made a decision and events for the Spanish conquest of Western Sahara and the Partition of Morocco.
-Gave a fort to Madrid and Lisbon.
-Kuwait now starts as a vassal of the Ottoman Empire that also can be integrated later. http://en.wikipedia.org/wiki/History_of_Kuwait#Al-Sabahs
-Added a Maldives Tag and a core on the Maldives.
-Balkan countries no longer get the "small but efficient" triggered modifier.
-Monarchy Uruguay is not called "Cisplatina" anymore. It will be just called Uruguay.
-Added a decision for Persia to end its Kurdish minors independence.
-Changed so the Dar-Al Funun modifier for Persia lasts 10 years instead of forever. Wouldn't make sense for them to be an advatange over every civ because of one university.
-Tweaked the Yemen decisions: You no longer need Aden, just the 4 states, and they can be your vassals or be in your sphere. This will also make forming Yemen easier as one of the sultanates. Forming Yemen as a GP no longer cedes Aden to them, you will keep it and you get a decision to cede the province to them (no alerts). All Yemeni sultanates now also start with core on each other, so conflict will be more common.
-Fixed a vanilla map defect in the provinces in northernmost siberia and integrated the Siberia mod by anon.
-Added catalan pops to Sassari on the basis of http://en.wikipedia.org/wiki/Alghero. A third of the population is Catalan now.
-Made events for the rise of Badr Khan, his conquests and the Assyrian massacre.
-The deport poles decision no longer removes Ruthenian Cores
-Croatia Independence decision now can only taken if they own the Croatia region and Dalmatia or Slavonia.
-Changed Japan's color. It stays the same old as an Absolute Monarchy and only changes once the government changes from that.
-If Romania unites and it's still an ottoman substate it will convert to a puppet instead.
-Added decision to unite North Yemen with Yemen.
-Merv renamed to Chardzhou. Merv was destroyed in the 18th century.
-Changed the Kazakh-ruled area. Most of Kazakhstan was dominated by kazakh nomads, so no real control of the land. A lot of the provinces were made empty. Some that made part of the Khivan influence were added to it, and I double checked all of central asian borders. Bukhara and Afghanistan gained quite a few cores.
-Removed the channel islands strait to stop French AI from garrisoning Caen. Reorganized the French military so now they start tidy.
-Rebalanced the Conscription sizes from the reform. The gap between reforms is 2.5%. The maximum gap (Mandatory Service vs No Conscription) is 10%.
-Changed so the Sunda Strait makes "Indonesia" written across the two islands (Java and Sumatra) rather than written once in each island.
-Indonesia cores now spread up to New Guinea.
-Added events to the Anglo-Siamese Treaty of 1909
-Integrated flagpack v4
-A free Samos will apply to join Greece.
-Malta and Heligoland LR reduced from 35 to 30. They are small islands so there shouldn't be any bonus in pop growth besides the normal ones.
-Changed Nagano and Kobe RGOs, giving Nagano to Kobe and vice versa, so Imperial Japan stops producing only tea while an unciv and everyone there starves as a consequence. They will starve a little less.
-Made sure the UK is not affected by the liberal reforms events.
-The Empress of India decision now, together with a monarchy, will trigger the Empres of India triggered modifier that will last as long the main cities in India are a colonial posession and the government is a monarchy. This modifier will do the same thing as before (prestige and research gain) but it will also improve ruling party support, diminsh social and political reform desire and core pops militancy by a little bit. This is to simulate the stability the empire enjoyed.
-Made the events for the Massacre of Bedr Khan, it's rise and fall from power. Mostly based on "Aboona, H. Assyrians, Kurds, and Ottomans: Intercommunal Relations".
-Changed Maritime Union color to differentiate them from the FSA.
-The badboy gained from inheriting Egypt in the Oriental Crisis was diminished from 5 to 2.
-The event for the Egyptian Surrender now makes Egypt a puppet of the ottoman empire but stops the event for the Ottoman empire to inherit them. This is done to represent the the limited rule of Ali Pasha that came with the Egyptian surrender and their obligatos to the Ottoman ruler.
-Implemented the Lithuanian party names/policies change suggested by http://pastebin.com/G8K4D9PS
-Decision for Argentina to rename Falklands to Malvinas, the UK also gets one decision to rename it back.
-Prestige hit the Ottoman empire takes for other countries helping them during the oriental crisis diminished from 5 to 1.
-Sweden starts with 10 prestige like the other Civilized nations in europe. Nice try Johan.
_______________________________________________________________
V2.9.7
-Fixed so Russian can't suddenly integrate UBD or TCA. Later that will be changed so there will be a war, but for now they just don't integrate.
_______________________________________________________________

V2.9.6
-Fixed Trarza cores in the desert.
-Fixed Albania not joining a player formed Yugoslavia.
________________________________________________________________
V2.9.5
-Arab Union now has a decision to get cores in the Maghreb
-Sicily now loses its cores once Italy forms
-Tweaked the Wallachia/Moldavia decisions for the Ottoman Empire
-Reverted the Fort Fix for uncivs because it was screwing up the province interface. Fucking building modding is hell.
________________________________________________________________
V2.9.4
-Added Pernambuco as a Tag, re-added Adamawa as a sokoto substate
-Reworked pops in Punjabi/northern India: Delhi was an island of Punjabi (now it's more spread near delhi) and places like Allahabad barely had muslims
-Reworked Mughal cores to make more sense and be a little bigger
-Reworked life rating in Africa so colonization works from the outside to the inside and the heart of africa is one of the last things to be colonized.
-Central Bank Decision modifier no longer affects tax efficiency.
-Added two generals for Spain and two for Portugal at the game start. Fixed the name of the conservative party of Portugal.
-Added Duchy of Limburg and events for its release and annexation. It can also spark a crisis.
-Changed FSA adjective from "free american" just to "american".
-Corrected a vanilla description that didn't properly add a new line.
-Made so Muslim pops are less likely to emigrate from muslim countries.
-Tweaked the deportation decision that expels poles from G-L and sets Ukrainian cores.
-Reduced AI aggression against uncivs a little bit.
-Added a decision for free United Baltic Provinces to select the future of the country.
-United Baltic Provinces now start as a russian substate, with russian cores. The Russification option for them integrate the territory in the Russian Empire. This change is based on http://en.wikipedia.org/wiki/Baltic_governorates (Similarly to guberniyas of the autonomous Grand Duchy of Finland, the Baltic Governorates until the end of 19th century were not a subject to the common civil and administrative laws of the Russian Empire). North German is the primary culture. See http://en.wikipedia.org/wiki/Governorate_of_Estonia http://en.wikipedia.org/wiki/Governorate_of_Livonia
-Changed the name of democratic PBC to Andine Federation
-Latvia starts with Protestant as their religion, name changes to Iskolat if they turn Communist.
-The Khanate of Khiva now starts with the turkmen regions that were persian. Hopefully, this means Persia has a little more time before Russia comes breathing down their neck. Persia didn't lose their cores there though, as they had claims in the area, and they only lose if a civilized nation takes the area. The change is also based on http://en.wikipedia.org/wiki/Khanate_of_Khiva, event though who owned what is kinda nebulous.
-Arab Union tag is now less overpowered - only countries with misri/bedouin/mashriqi primary culture can take it and it will gave cores in countries with that primary culture. Maghrebi/sudanese/tuareg are not accepted anymore, and now the Maghreb/Arab Union have clear "spheres" of formation/influence - Arab Union gets Egypt, Levant/Middle East and the Arabian Peninsula while the Maghrebi Union has all the countries up to Lybia. Added a decision for the Maghrebi Union to claim the Sahara up to mauritania/Lybia line.
-Fixed the reform that built a fort for uncivs to actually build a fort
-Increased the MTTH of the NNM emboscada event so it is less likely to happen every time. It still happens and I couldn't find a satisfactory option to include, so try to not have any revolts while the maria da fonte revolution started. Also made the revolution happen only in mainland portugal rather than anywhere that Portugal owns.
-Added a flavor event chain for late game Russia
-Added a flavor decision for sunni/shiite countries
_______________________________________________________________
V2.9.3
-Cyclades is now part of Attica Region rather than the Aegan Islands
-Fixed the Greater Finland decision to give cores on Kola too
-The Taiping now start as a theocracy, on the death of the leader they can pick if they turn into a monarchy, republic if they keep being a theocracy or turn in the Qing.
-Changed the effect of "curse of the pharaohs" event. Now it only affects pops with less literacy than 60%.
-Added an event for Germany to re add cores for the Bavaria, Saxony and the cities of Hamburg and Bremen. This is done to represent the special status granted to these lands.
-Added a decision for the Mughal Emperor to declare a Jihad once the Sepoy Rebellions starts, to get the him free and get the possibility of the British to conquer Delhi. Players beware, the british have a high chance of DoW you, they got a CB on you for 2 years.
-Fixed a few event description typos.
-Restored pop growth for medicine reform back to vanilla levels.
-Rearranged a few states.
-Made the AI more likely to up the conscription though decisions.
-Von Moltke Reforms modifier now expire like in Vanilla.
-Made an event for France to change to military-industrial complex once they lose A-L and to selection Mandatory Service.
-Increased the MTTH for one event regarding sphere disputes.
-Fixed a potential bug in the events of the south american wars.
-To compensate for no more Occitania, the dismantlement of France during a great war now involves territorial gain for the nations participating. In the old way, the nations only got cores, now they take the provinces. Belgium gets Dunkirk, Lille, Arras, Cambrai and Charleville in addition, while Italy.
-If the Papal States turn monarchy they change their name to Lazio.
-Added functionality to treaty ports. Now any non Asiatic countries that own a treaty port in China (with no other neighboring province owned by you) gets a modifier that increases pop growth and RGO size. The province RGO is changed to precious metal to simulate the increased trade and importance of such ports, since the Europeans didn't see the goods as much as they saw the money and taxes. If an Asiatic country gets a hold of the port, all this is reverted. The only exception to this rule is Hong Kong, which will stay with the bonuses once they get it no matter what. The port also needs to have a low population to get the bonus.
-Added an event to simulate Chinese migration to Hong Kong.
-Muslims pops are usually more in favor of slavery.
-Decreased mobilization size that reforms gave across the board. Now the values are 15%, 10%, 5% and 2.5%.
-Slightly increased cost to create state
-Railways now make mobilizing faster than vanilla
-Health Care reforms now influence the frequency of Disease events, so from "acceptable healthcare" on diseases should take longer to happen. Made the time the outbreak lasts random.
-Added an event chain for radical ideologies (fascist/communist) governments to change the government of their puppets. As radical ideologies, they can't keep a non radical government like "traditional" governments can.
-Added the Fifteen Amendment decision for the USA
-Senj is now a part of Dalmatia to avoid any Italian ugliness on Croatia since they don't always seem to use the NNM event to return lands right.
-Fixed a description in Vanilla regarding elections.
-Renamed Aristocrats to Landowners. This is done so if the country turns in a Democracy there won't be any "Aristocrats" around.
-Tannu Tuva start as a Qing Vassal now, they own Urankhatai.  Fixed their monarchy flag. Fixed its starting reforms which were from a democracy rather than a monarchy. Also fixed social reforms for Mongolia and Tannu Tuva, both started with some social reforms like workhours passed.
-Made Lumber be more used than timber. Hopefully it means you can't get rich just of selling raw wood, you gotta process it for most things it is used.
-Halved the CB generation speed hit from vanilla WE
-Gave techs to Transcaucasia in HPM, made an event for it to get cores on their lands if they break free
-Deseret will not apply to join the USA anymore
-Changed Aristocrats name to Landowners so it makes sense outside monarchies.
-Theocracies can't enact voting reforms anymore. They can only be toppled through revolution.
-Changed Lanfang starting government to Presidential Dictatorship, since the engine can't handle non civilized democracies.
-Made a decision for Russia to get cores on Tannu Tuva. China, however, doesn't lose their cores there anymore, and the region should be disputed. You can also peacefully annex Tannu Tuva if they are in your sphere and are not a vassal, and you took the first decision.
-The Central Asia decision for Russia got moved to an event.
-Mongolia has a random chance of turning Theocracy during the Xinhai revolution
-The Egyptian rebellion against ottoman rule now ends after the berlin conference instead of going on indefinitively
-Communist or fascist governments now rebel against their overlords if they are not of their respective ideologies.
-Fixed a NNM issue that made the arab revolt events go endleslly, even after the event telling you that it ended.
-Non sphered AI Polish minors adjacent to Poland should ask for annexation now, giving Poland cores there.
-Manifesto of unshakable autocracy now repels reforms and decreases militancy. Thanks for that anon!
-Fixed the event that was cleaning crisis flashpoint even when it shouldn't.
-Fascist governments can't allow slavery, communist and fascist governments can't allow serfdom anymore
-Integrated some of the Fin_PoP_Fix changes. Didn't integrate pops because some stuff (like estonian serfs) didn't make sense and Ingria with cores could end up with a rebellion in Russia for indepence when that wouldn't make sense in that region.

_______________________________________________________________
Version 2.9.2 - Saves compatible with version 2.9.1
-Added a missing flag for a Ottoman decision
-Fixed the event to annex Darfur not giving proper CBs
-Balanced a few Ottoman decisions/events
-Removed old references to telegraphs from the terrain file
-Balanced a few events, added two clean up events for alternative scenarios
-Made sure the Pinsk Marshes decision fire only once.
_______________________________________________________________
Version 2.9.1
-Fixed potential crash with deportation events
-Fixed a russian decision who kept firing ad infinitum
-Madagascar starts as animist. http://www.content.eisa.org.za/old-page/madagascar-late-merina-kingdom-1828-1896
-Kamchatka gets a core on Primorye when the Russians do.
___________
Version 2.9
-Added a decision for polish claims in the eastern provinces.
-Added a decision for Lithuania to move their capital to Vilnius.
-Bankruptcy law now needs a tech to be unlocked.
-Added a decision to deport the poles from Galicia-Lodomeria so to set the countries borders.
-Fixed Germany/NGF/Prussia not giving up Eupen-Malmedy after a great war.
-Removed British core from Norfolk Islands
-Removed Russian cores from Estonia and Latvia. They can get it back starting 1870 by taking a decision to start the russification of these lands. They can take the decision even if they don't own the baltic states, and they will get their cores back. (http://www.estonica.org/en/History/1850-1914_National_awakening/Russification_period/)
-Added serfs to Georgia and the Guria Rebellion (which can happen in any core of Georgia under Russia, really, if the conditions are met).
-Transcaucasia start as a russian substate in 1836. (based on "The Viceroyalty later expanded to encompass the territories acquired by Russia in a series of wars with the Ottoman Empire, Persia, and the local Caucasian peoples. Headquartered at Tiflis (Tbilisi, Georgia), the viceroys acted as de facto ambassadors to neighboring countries, commanders in chief of the armed forces, and the supreme civil authority, mostly responsible only to the tsar.") Besides the slow down on the russification, there's the added bonus that Russian won't blob in Trabiz in Persia every time as the state serves as a buffer.
-Immigration NF now gives 30% chance instead of vanilla's 20% of a pop to immigrate to that state.
-Fixed the description of one of the NNM Unequal Treaties.
-Fixed Slavonia/Croatia overlap bug.
-Fixed the Integrate Albania decision.
-Added a slovenian core on Trieste.
-Added a Greater Finland decision.
-Removed Lithuania from the United Baltic Duchies
-Changed so Georgia and Transcaucasia use the RussianGC instead of the MiddleEasternGC
-Added Abkhazia to the game on the basis of their Independence (http://en.wikipedia.org/wiki/Principality_of_Abkhazia). They are absorbed in the russian empire once the russians finish pacifying the caucasus ("The autonomy of Abkhazia, which had functioned as a pro-Russian "buffer zone" in this troublesome region, was no more needed to the Tsarist government and the rule of the Shervashidze came to an end; in November 1864"). North Caucasian Minors there represent the Abkhazians. They start as a sub state of the russian, though maybe they should start as vassals.
-Fixed massive unemployment of farmers due to immigration to Jerusalem if Israel is formed.
-Fixed the province names Novorossiysk to Yekaterinodar and Ekaretinodar to Timashyovsk. The region is now known as Circassia. The names (with exception of Timashyovsk, since that's the biggest city of the region, Yekaterinodar is more to the south) are restored back to vanilla once the caucasian war is over.
-Circassian war events are done, as well as the diaspora and killings and the integration of Abkhazia. GPs now can support circassia.
-Changed the name of Kota Bahru to Kota Kubang Labu, as the city wasn't called that and wasn't the capital at the time. They get an event to change the name after a while.
-Added Kedah, Kelantan and Pattani as the Malay vassals of Siam (http://en.wikipedia.org/wiki/History_of_Thailand).
-Added Moldova tag.
-Added the possibility for Lao cultures to form Lan Xang (which is also the Laos tag).
-Integrated the fixed Yugoslavia and Albania (which was further fixed) and the integrate Bulgaria for Yugoslavia decision by anon. Thanks for that!
-The Homestead act for the USA will be revoked (via event) if the party in power is not liberal and the government isn't a democracy (meaning Constitutional monarchies still can keep the homestead act with a liberal ruling party).
-Added decision for the CSA to claim the 36"30' Parallel.
-Improved the text in the communist revolution decision about the future of the rich class and added an option to kill them instead.
-Fixed the Hold election and the nationalize effect descriptions so they don't stick to other words during descriptions.
-Added the Sicily tag and the Sicilian revolution of 1848.
-Changed the flag of democratic Venice to the historical one and the name of a democratic Venice to Republic of San Marco.
-Added a new general for Austria.
-Added a new flag for Theocratic Italy.
-Removed Occitan Culture and Occitania tag from the game.
-Fixed the "promised free press" vanilla event spam. Now it doesn't happen in communist/fascist dictatorships and you can back down on your promise. The other two reforms that could end spamming the player also have the same treatment, so now you can go back on promising free press or any other thing without being spammed to oblivion.
-Fixed the Baluchistan decision leaving one province without cores if it was taken by Kalat.
-The Chinese cultures are a little less likely to emigrate now.
-Increased the MTTH of the pioneer column event.
-Fixed GPs not colonizing states of africa that had cores from other nations that existed.
-Fixed some region names in Argentina
-Made one state countries in the new world not get as many immigrants. Once they reach 1M pops, they lost the 300% vanilla bonus for being in the new world. Landlocked countries also lose that bonus until they get a port.
-Tweaked Paraguayan decision from giving up to 30 prestige to give up to 10. Tweaked their modifiers.
-The Qing should inherit the Kumul Khanate properly when they westernize now.
-Fixed Idaho not being entirely colonial.
-Tweaked the discover the Lake Victoria event. Takes more time now.
-Tweaked Bureuacracy reform values.
-Added option to target specific religions in the genocide decision.
-Cape Verde start as a colony of Portugal instead of a State, but Portugal starts with a core there.
-Add cores of Hungary in Fiume and Eisenstadt.
-Added a second Donghak (Gabo reform) and tweaked the first one to do what the orignal reform doesn: Abolish serfdom, slavery and reform the bureaucracy. The second one declares indepence from an Overlord and adds more research.
-Added a tag for Fiume with North Italian as primary.
-Added the Croatian-Hungarian Settlement.
-Added a decision for the Czech culture group to incentive the Skoda Works, similar to the Krupp decision for the Germans.
-Fiume and Trieste use now the ItalianGC instead of GenericGC.
-Balanced the technology groups: All generic tech groups now have a total -15% and a total +25%. Special tech groups can void this rule.
-Savoy and Sardinia can't be normally released anymore, to avoid a exploit that allowed Sardinia Piedmont getting South Italian as accepted by abusing the release.
-Overall diminished the prestige gain from the Argentine Formation event chain.
-Changed the Papal Stated democratic flag to match that of the Second Roman Republic
-Removed the Bureaucracy Reforms: the AI didn't handle it very well.
-Changed the life rating of Slutsk, Mozyr and Korosten form 35 to 15. These provinces correspond to the Pinsk Marshes. A decision can be enacted to drain the marshes.
-Changed the the 6-level telegraph to a 2 level Public Illumination as the additional building. The old system wasn't working so well (because the AI is shit and doesn't save money, nor invest in projects) and people raised concerns it was redundant. The new building has two levels (first is gaslights, the second is electric lights) and provides 3% more efficiency for factories per level and is also used in an event that electrifies mines, giving more mining efficiency (since buildings are hardcoded to have one event only, thanks a lot Paradox, I had to go with that). In the future, I hope to use the presence of railroads and gaslight illumination to make annexed uncivs "naturally" civilize - meaning that if the annexed unciv capital has lights and railroads, it turns in a civ (just that, they don't get indepence or anything like that).
-Moved Gaslight invention from Organic to Inorganic Chemistry.
-Finished Imam Shamil events capture.
-Added a quick decision to simulate the Armenian Genocide.
-Made Wallachia and Moldavia start in the Russian Sphere rather than the Ottoman (The 1829 Treaty of Adrianople, without overturning Ottoman suzerainty, placed Wallachia and Moldavia under Russian military rule) to represent Russian greater than average influence in their affairs. They start as Ottoman Substates now and Austria has a measure of influence in their affairs too. The Ottoman Empire now has a decision to integrate them as long as they are substates and romania isn't formed. They can accept integration or they will try to fight for their independence.
-Added decision for the Ottomans to end Tunisian self rule.
-Excluded the Ottomans from creating Yugoslavia, as it wasn't in their interest to create an orthodox state in the balkans
-Changed the 1836 ownership of Timbuktu from Bamat to Massina
-Added one event about the natural formation of the Toucouleur Empire.
-Added one general for Tripoli, Bambara and the Ottoman Empire at the game start.
-Fixed the Create Romania decision so it doesn't appear for the Ottomans if they own any province with a romanian core.
-Fixed so the decision to encourage arab nationalism doesn't appear for the ottoman empire
-Added 2 new events for countries with the NV productivity and the NV autocracy and tradition. In vanilla, all NVs have events tied to them, and those were missing events.
-Modified the Brazilian NV to Liberty
-Changed Zhambyl name to Namangan-i Kochek. The province now starts under the Kokand Khanate (http://en.wikipedia.org/wiki/Taraz#Kazakh_rule).
-Changed the name of Kyzylorda to Ak-Mechet. Kyzylorda is a soviet name. Changed the name of Alma Ata to Zhetysu. Alma Ata is also a soviet name. Rename lake "Balchasj" to Balkhash. You get a decision to rename all of those, minus the lake, to their historical names. Semipalatinsk renamed to Ayagoz. Yasi renamed to Turkistan http://en.wikipedia.org/wiki/Turkistan_%28city%29. Adjusted the borders of the Kokand Khanate-Russia. Shymkent renamed to Chimkent, start under the Kokand Khanate http://en.wikipedia.org/wiki/Shymkent. 
-Kazakhstan monarchy renamed to Kazakh to represent the Kazakh Khanate. They start with Turkistan as their only city.
-Zhetysu and Qaratal start as part of Xinjiang now. They were seceeded later to Russia (In 1864, the lake and its neighboring area were ceded to Imperial Russia under the Protocol of Chuguchak) http://en.wikipedia.org/wiki/Lake_Balkhash.
-Changed the Aqtau (town founded in 1964!) name to Krasnovodsk. Now the region starts in control of Khiva (http://en.wikipedia.org/wiki/Mangystau_Region).  Changed Ashkhabad to Ashgabat. Starts in control of Persia. Changed Kyzyl Arat to Bereket. Starts in Control of Persia. Both based on http://en.wikipedia.org/wiki/Treaty_of_Akhal. Changed a few provinces in the are to semi-desert.
-Changed Qaraganda name to Akmolinsk, starts in Russian control.
-Added a general to Kokand and Bukhara in the start date.

______________________________________________________________________
Beta 8
-Add a new picture for the mormon exodus event
-Added a irredentist decision for deseret (they finish getting cores the two states they have cores in)
-Added a few north italian pops to Corfu to represent https://en.wikipedia.org/wiki/Corfiot_Italians
-Integrated Alternative Flag Pag V3 flags
-Fixed Webster-Ashburton treaty not displaying information properly and not removing one core properly.
-Tibet starts now as a theocracy.
-Rebalanced conscriptions and mobilization size: From mandatory to one year goes 20-15-10-5 and NVs goes Order (5%), Autocracy (4%), Productivity and Tradition (3%) Liberty and Equality (2%). Techs can give up to 10% of mobilization size, making the maximum amount a country can normally achieve 35%.
-Made telegraphs cheaper
-Rebalanced most of the NVs
-Fixed one NNM event that was spawning endlessly, causing AH to have infinite prestige
-Fixed MUG and MEX flags
-Customized Nejd party names
-Changed Syrian fascist party name to be of the older movement http://en.wikipedia.org/wiki/Syrian_Social_Nationalist_Party - changed the flag accordingly and added a irredentist decision available for Syria based on the party and historical ambitions of a unified fertile crescent state http://en.wikipedia.org/wiki/Greater_Syria
-Countries in a Great War can jump right to Mandatory Service as a reform
-Changed Teresina's name to Vila do Poty. Added a decision to build Teresina and Belo Horizonte.
-Changed Palmas province name (city didn't exist until late 20th century) to Vila da Palma
-Changed a few region names in brazil
-Event for the abdication of the brazilian emperor leads to Desterro being renamed to Florianópolis
-Rearranged capital provinces of the regions in Brazil so they correspond to the most populous cities/provinces, since pops are more likely to move to regional capitals.
-Changed province 745 name from Leghorn to Livorno.
-Rome now starts with a level 1 port.
-Added a decision to build the Fatherland Altar for Italy. Added a model for it, albeit it's not very good.
-Fixed the serfdom abolished events and decisions so the pops convert to laborers too in the appropriate provinces.
-Added an event to Finland to decide their fate if they stop being a russian vassal. They can choose between continuing to be a monarchy (looking for a king somewhere else) or to declare a republic. In either case, the specific government will be decided by the reforms. If you choose republic and doesn't have enough reforms, after some time it will be couped to a dictatorship. Same thing with monarchy.
-Made most of the canadian countries now have britishGC as their units, minus quebec that uses the french one
-Algerian Rebellion event doesn't  fire when you have a truce with Algeria
-Fixed russian province name from Elitsa to Elista. Changed Donbass region to Don Host Oblast. Changed Kramatorsk to Bachmut. Added Yekaterinoslav to the Zaporizhia region and changed the name of the region to Yekaterinoslav since Zaporizhia was founded in the beginning of the 20th century.
-Changed the color of Native American Minor culture.
-Added a small arms factory to Saint Etinne and deleted a ammunition factory from paris, based on http://en.wikipedia.org/wiki/Manufacture_d%27armes_de_Saint-%C3%89tienne
-Changed the event to clean up serfs when a nation with serfdom abolished conquers somewhere with serfs to be activated by the ai so the cleanup doesn't disturbed the flow
-The % of jingoism required to add a wargoal was diminished from 7% to 4% to compensate for the added reforms.
-Removed Azerbaijan as accepted for Transcaucasia. Added a decision to convert transcaucasia to Sunni, Shiite or Orthodox (the default). If converted to Sunni or Shiite, the Azeri are set as primary culture and Baku as the capital, and armenian and georgian are removed from accepted. The process is reverted if a christian nation makes the country orthodox again. The decisions show to the respective countries (so a convert to sunni only shows to a Sunni country), but since apparently there's no command to check a nation religion, I'm using the nation's capital main religion (so the Ottoman Empire, for example, Istanbul is majority Sunni so they count as Sunni for the decision). If anyone has a capital that fucks up this rule in the game start, let me know. To take the decision you NEED to be Transcaucasia puppet master, and the decision is NOT available for transcaucasia to take.
-Transcaucasia can't take the Claim North Caucasus decision if one of the north caucasian countries exist.
-Renamed Antioch to Antakya, as the name fell in disuse a long time ago.
-Tweaked the French Revolution and Napoleon Coup event chain.
-Increase tension NF now unlocks once the first country research revolution and counterrevolution.
-Fixed a vanilla typo in the peace offer pop up.
_______________________________________________________________________________________
Beta 7
-Fixed Warri typo making them start with no party.
-Fixed wrong Sokoto core.
-Reshaped a few provinces. Trieste got thinner and annexed the coast part of Gorizia (who lacks a port so it's useless) and Postojna got an access to the sea and a port.
-Added a port to Ferrara.
-Changed the South African events so they don't give cores to the UK, they give CBs to the UK. They don't happen if the Netherlands stopped the Trek.
-Removed Yugoslav and PLC cores.
-Changed south italian literacy so it's a little lower. 
-Changed the CB speed for some CBs from NNM to vanilla levels.
-Changed the literacy levels in Russia according to https://i.imgur.com/PU7wB4p.jpg - North germans and ashkenazi have the highest literacy levels, followed by estonians and latvians, then poles and lithuanians. Siberians, tatars, yakuts, and other steppe-far away ethnies now get less literacy. Russian average literacy in the game start is the same as vanilla.
-Fixed cores of Poland: Pre-WW2 stuff was taken off, Poznan cores are back. Re-added Pomerelia: They consist of the Polish corridor and their main function is to guarantee pops there don't turn german.
-You can't build ports in arctic terrain until you reach level 5 ports.
__________________________________________________________________________________

Beta 6
General Changes:
-Added events and a decision to model the Anglo-Duitch Gold Coast Treaty of 1870 (which gives the CB and the all clear for the dutch to start the Aceh War). The event is kinda dynamic so if the dutch don't have the gold coast the treaty still can happen, but the colonies that will be given will be random colonies with sea access.
-After a civilized country conquer Aceh, there is a chance, after some time, that a Jihad is declared, resulting in a 20 years long nationalist agitation. This is made to reflect IRL events. If the country is sunni, then nothing will happen.
-Fixed a vanilla description regarding Religion triggers being completely wrong.
-Fixed typos in the rebel_types file.
-Melilla is now a spanish core (on the same basis as the Canarias are a spanish core), through Morocco didn't lost its core there. The province now has a fort and the size in map was diminished.
-Reverted the ACW back to vanilla levels.
-Changed the adjective of Quebec to Quebecois.
-The Kumul Khanate will now be annexed properly when the time is right.
-Added decisions for a country in war to force their conscription level up. The AI will use it too. The decision doesn't give an alert (doesn't make the decision button flare green) and it only appears when you are at war.
-Stopped CSA separatist/nationalist rebels from appearing before the civil war. After that they can appear.
-Communist government get a decision to up the bureaucracy and child labor.
-South Africa is no longer released instantly by the AI, they will release it around 1910
-Decision for the Dutch to gain Boer as an accepted culture.
-Fixed rebels double appearing bug. Fixed the instant white peace of crisis war. It seems all arcane bugs are fixed.
-Increased Pashtun radicalism. Added radicalism for the Tajik. Added new surnames for both cultures, so generals aren't called only "khan".
-Broke up North Caucasian culture into 4 cultures: Chechens, Circassians, Dagestani(a mix of a lot of ethnies, mainly Avar) and Caucasian Minor (Ossetian, Abkhazi). They are all in the Caucasian Culture group. They got assigned radicalism levels and names, most surnames are based of tribe names, that seems to be the dominant tradition in the place. https://upload.wikimedia.org/wikipedia/commons/b/b0/Caucasus-ethnic_en.svg
-Changed the Kumul Khanate color.
-Fixed pops in the Caucasus. Chechens are now numbered around 1.5 million ( 375K pops, source https://en.wikipedia.org/wiki/History_of_Chechnya#Conquest ). Circassians are now numbered around 3 million (https://en.wikipedia.org/wiki/Circassian_nationalism#Russian_invasion.2C_conflict_and_Muhajirism and https://en.wikipedia.org/wiki/Ethnic_cleansing_of_Circassians#Genocide_question ). 
-Luhansk is now part of the Kharkov region rather than Donbass Region.
-Circassia, Dagestan and Chechenya gets a decision to unify the Caucasus against the Russian threat, like the caucasian imamate tried. The decision can be taken only once (the first country that civilizes takes it) and gives accepted pops (circassian, dagestani and chechen) and cores on the other two countries.
-Ottoman has a decision to try and conquer Montenegro (they get a CB for 5 infamy since their indepence wasn't really recognized).
-Civilized countries bordering the Yemeni sultanate can enact a decision to get conquer CBs on them for less infamy.

Map/Flag Changes
-Decision for the Chinese to claim Sakhalin and Manchuria
-Singapore is now an island.
-Added Eupen-Malmedy to the map. It's the old Spa province changed a bit. The old Belgian territory of Spa was integrated in Liege (thanks anon for the suggestion). The pops were changed according to https://en.wikipedia.org/wiki/Eupen-Malmedy so the majority of the province (80%) is nort german. Most Walloons were moved to Spa (that is, Liege now) so the province population grew. If Germany/NGF/Prussia get dismantled in a Great War while owning the province, the province will be ceded to Belgium.
-Fixed Malaysia monarchy flag (wrong proportions)
-Torching the summer palace now torches the palace.
-Moved the model being used in Edo to Beijing, that's the summer palace now.
-Returned Taizz to North Yemen. Looked horrible on the Ottoman hands, though they did hold the coast of the province.
-Changed the monarchy flag of Persia to match the historical flag. Changed the republic flag to match a historical flag that was less religious, the modern flag is now used for a theocracy. Persia will now change their name to Iran if it ever stops being a Absolute or Semi Constitutional Monarchy.
-Added Chechnya as a tag. Later on I will split the caucasian pops, do events for their diaspora and relocation.
-Montenegro starts as a Theocracy and changes to an absolute monarchy down the line via event.
-Jacobins should push the debt law reform to the next level up to debtors prison one they break a country.
-Australasian is now only called Australian.
-Reworked the Russian Army: they now have the biggest land army of the world at start and a lot of soldiers

Balance changes:
-Greatly increased the MTTH for building destruction events.
-Changed the Pioneer Column effects so Rhodesia is not as likely to appear, only their cores.
-Reactionary rebels in Presidential Dictatorship in the Americas are now way less likely to appear.
-Immigrant Officers no longer demote.
-Defeated countries in great wars will now have their conscription level forcefully lowered to "No Draft".
-Mountain Terrain reduction of battlefield size was changed from 66% to 70%.
________________________________________________________________
V0.2 Beta 5
-Renamed Sulawesi to Bone Sultanate if they are a monarchy
-Renamed 1448 - Jilolo to Tidore
-Renamed monarchy Maluku to Tidore Sultanate and changed so they have their holdings. Made them a puppet of the Netherlands.
-Renamed Kaupeng to Koepang
-Gave Yogyakarta and Surakarta to Java, made them a dutch vassal.
-Changed the Dutch East Indies colonies according to http://upload.wikimedia.org/wikipedia/commons/d/d1/Evolution_of_the_Dutch_East_Indies.png and http://3.bp.blogspot.com/_H1QEUZthYs8/TIxiHMc2BxI/AAAAAAAAAAk/oQj0_ZxGY4Q/s1600/Evolution+of+the+Dutch+East+Indies,+Map.png and other informations.
-Consolidated the Dutch OOB: Integrated all their divisions in one divisions, changed one cavalry and 2 infantry to artillery. The numbers of brigades are the same, the type changed for 3 and the army was consolidated. Changed some frigates to transports. Added historical generals. Added garrison troops to Borneo and Suwalesi.
-Finished the Russian generals
-Deleted some russian frigates. The colonial points lost are recovered by getting a level 2 naval base in the Aland Islands. Moved the finnish naval port from Turku to Helsinki.
-Copenhagen port now is level 2
-Moved the Dutch naval base from Rotterdam to Amsterdam. They got a level 1 fort too.
-Russians lost 2 man'o'war, the Riga Naval Base got upgraded to level 2 and and Odessa got a naval base. Russia starts with 70 free colonial points and a average debt of 900, while on vanilla that average debt is 1400
-Made the USA lose their statue of liberty modifier if the second ACW begins
-Fixed the rename decisions of the USSR to only show in countries that own those territories
-Fixed the Darfur event for Egypt
-Tweaked the colonial migration values for terrains: people are less likely to choose to go to coastal deserts and jungle provinces, but those are still picked more than mountains and marshes. Rules apply for colonial transportation too.
-Halved the effects of colonial transportation
-Made animist countries have an extremely hard time to convert pops to their religion - only moralist countries with some very good policies should be able to do it
-Made Arab Union green color slightly lighter
-Made last levels of social reforms reduce social reform desire by a little bit.
-Made a triggered modifier that reduces by 20% social reform desire if you have all reforms passed. This should stop communist and socialists becoming so widespread in countries with all reforms met and will neutralize the effects of all union reforms passed.
-Made the genocide decision be a little more clear when you can do it again.
-Made Aqaba have access to the red sea, so it's now a port province.
-Stopped the Poland Lithuanian Commonwealth from becoming Poland via decision, they now can only become it once they take the decision to dissolve the commonwealth
-Changed the serfs abolishing decisions and events to be more clear with the info, made an event for countries that abolish serfdom to convert all serfs to farmers because them slowly promoting to famers simply didn't work.
-Made a decision for the dutch to abolish the javanese sultanates and integrate them
-Changed the Polish Lithuanian Commonwealth color.
-Added the Padri war for the game start
-Added the Jambi War
-Made a decision for the dutch to integrate Tidore, so now the dutch can get all their historical territory
-Made Siak a dutch puppet as according to http://en.wikipedia.org/wiki/Pekanbaru ,the decision to integrate Tidore also integrates them.
-Corrected a typo in one of NNM decisions regarding Puerto Rico
-Reverted the ideologies unlocking through technology, wasn't working very well. Still, countries that first discover communism/fascism get a small boost. Fascism unlocks a little earlier (1900 instead of 1905) and only after Great Wars are unlocked. 
__________________________________
V0.2 Beta 4
-Lessened by half most negative effects of reforms on literacy, making it a little more forgiving.
-Fixed a potential crash related to putting province modifiers as a parameter for pop ideology
-Upped Brazil literacy back to vanilla levels
-Balanced serf basic needs a little bit.
-Rolled back experimental features: Railroad cost back to vanilla, naval bases don't decrease import cost and artisans can't make fabric out of wool anymore
-Fixed Argentine Confederation and Buenos Aires NV not changing at the game start bug. Apparently, the 1861 section was causing it.
-Moved Fabric factory activation to No Standard tech of the commerce branch. You can't have 2 building activations in the same tech, so that was causing a problem.
__________________________________
V0.2 Beta 3
-Pops with less literacy than 40% will never join jacobins or socialist rebels (that's a vanilla setting)
-The last two levels of (most) social reforms reduce the chance of militant socialist rebels spawning
-Integrated Telegraphs, railroad infrastructure contribution was cut in half while the other half is given by telegraphs. By lack of satisfactory modifiers, they increase movement speed a little bit, half than what railroads give. They use cloth since that was used as a isolator http://en.wikipedia.org/wiki/Electrical_wiring#Early_wiring_methods Unfortunately, I can't change the invest icon in the production tab, so it will still be a railroad. I had the icons done though. They also spawn railway tracks in the map, since they add infrastructure. I also can't change that, since it's hardcoded. Sorry.
-Fixed Korean party names.
-Uncivs with the tradition NV can change their NVs once they reach 50% westernization, the AI will also change it. I will improve that later, make it an event for the AI random chance to be better.
-Added an starting event for Nejd to model Wahhabism in Nejd.
-Added events for the destructions of forts, railroads and telegraph lines during battles. If you don't want them, just delete the Building Destruction.txt from the events folder.
-Excluded England, Sweden, Russia and Greece from the Springtime of Nations event. It WILL still get the "an age of Liberalism" event.
-Added Huguenots (French Protestans) to A-L, northeast France and Chevenne. Around 250-300K pops.
-Made pacifism less likely as an issue in uncivilized countries.

___________________________________________________________________
V0.2 Beta 2
-Changed Seoul name to Hanseong.
-Changed the Penal Labor reform to Transportation. Now it makes pops more likely to emigrate to colonies when enacted. It also makes them more likely to go to desert/arctic terrains in countries without any colonies.
-Implemented serf pops. They are usually conservative, don't give any trouble, are 5% more efficient than farmers, can work in mines or farms. Any poor pop with the exception of soldiers will demote to serfs up to 40% of the population.
-Added 4.19M pops or 16.76M people serfs in Russia. According to Wikipedia: the 1861 Emancipation Manifesto proclaimed the emancipation of the serfs on private estates and of the domestic (household) serfs. By this edict more than 23 (5.75M pops) million people received their liberty. That way, the russian serfs have some space to grow.
-Added serfs to all of Congress Poland.
-Changed the Slave pops in India/China to serfs to better represent what these pops were.
-Corrected a typo in the Vanilla Manifest Destiny decision description.
-Added an event for the Prussian Constitution of 1848. It will keep the liberals at bay for some time and pass the reforms and concessions the king did.
-Fixed some missing description localizations for some authors inventions.
-Muslims now enjoy the same penalty for religious conversion as Jews (in non muslims states, that is).
-Lowered the average time to build the canals.
-Upped Chicago LR to 40 so pops are more likely to move it there.
-Hamburg start with fortifications now.
-Australian is the primary culture of Australia now, they also get aborigine as accepted. Might change that later. Added australian pops in australia so when they get free they can convert pops to australian. In vanilla, the australian culture exists in the files but not in the pops, so it never appears. Change the culture of New Zealand and also made it australian, but now the culture is called Australasian, to represent the cultures of Australia and New Zealand (I'm still more partial for it being only Australian).
-Changed the names from New Zealand form their english names to native names. The names change later with colonization.
-Fixed China/Qing party names. Changed some party names to add some flavor. Add another Chinese liberal party that gets unlocked in 1860 (Yangwu Yundong or Foreign Affairs Movement) and renamed the Chinese Liberals to Yangwu Pai (Westernisers) (most stuff came from http://www.lse.ac.uk/economicHistory/Research/GEHN/GEHNPDF/Conf10_Deng.pdf
-Made an event to make sure Canada get its northern borders.
-Changed the literacy of the Italian pops under austria. Now they start with the average 40% that the North Italians share, with the exception of Lombardy that is slightly more.
-Fixed the Mafia crime so it does what the description says it will do.
-Fixed St. Pierre pops.
-Changed the finnish animists in provinces 982 and 2587 to orthodox.
-Made the Jirim Chuulgan province (1533) a part of the region Heilongjiang for better borders.
-Changed the shape of petsamo a little bit.
-Made Zumbo and Songo a Portuguese colony as it historically was according to http://en.wikipedia.org/wiki/Zumbo Songo was made on the basis of the strong portuguese influence in the area, that went up Tete, in the confluence with Songo and Zumbo.
-Changed province 2581 name from Mataka to Chiconono. Mataka was the name of one of the Yao leaders, and according to the internet, the center village there was called Chiconono. http://en.wikipedia.org/wiki/Yao_people_(East_Africa)
-Changed province 2070 name from Mutare to Umtali, as it was its name. http://en.wikipedia.org/wiki/Mutare
-Added 5 new events dealing with the portuguese conquest of Mozambique and the fall of Gaza. Fixed the portuguse and Gaza starting borders in the area (they lost 2057 - Sofala to Gaza).
-Fixed Kongo's capital. Now it's on province 2001, Mbanza, as it was set by king King Pedro IV of Kongo in 1709.
-Fixed a localization bug with the Treaty of Tartu and a typo in one of vanilla inventions.
-Desert starting religion is now Mormon (so it's the only Mormon tag in the game), and starting government is theocracy.
-Changed how the game address you in a fascist dictatorship from Fuhrer to Supreme Leader.
-Viipuri changes to Vyborg ist he Finnish cede it to Russia in the Treaty of Tartu event
-Fixed Finland not having any techs in the game start
-Changed how jacobins stop forming. They will stop forming in a democracy with at least universal_weighted_voting that doesn't have a reactionary, fascist or communist party in power, but in a hms_government they will rise until there's a liberal party in power.
-Changed colonial migration a little bit: Pops that aren't of the state religion and aren't animists will be more likely to immigrate to the colonies IF the ruling party policy is moralism (since they face persecution, they try to find liberty in the colonies). Religious conversion in colonies suffer a penalty (not enough state control).
-Added Bahawalpur and gave Bahawalpur province to it. Made it a satellite of the UK.
-Fixed Prussian starting alliances. Now Prussia start allied with their SoI to avoid the huge amount of clicking to get them in in the game start. Gave them a boost to relations to represent what happened after they got an allaiance after the game start.
-Made an event for Tuscany to inherit Lucca by default around 1847 or Sardinia/Two Sicilies if they have Lucca in sphere.
-Fixed Austria start so they start allied with their sphere (the italian sphere).
-Changed the Bavarian Reactionary party name to the their historical name.
-In the Treaty of Paris when Russia loses the Crimean war, the Aland Islands are ceded to Finland, demilitarized and Russia loses its core in it.
-Added a special form of government (theocracy) and a special form of rebels (islamic fundamentalists). They only appear in specific conditions.
-Added events for a GP protectorate over Sudan.
-Added events for the Mahdist revolt in Sudan.
-Stopped Substates and Vassals from being able to take the Leave SoI decision, so it's not abused to get free easily.
-Changed province 1845 Yambio name to Bahr el Ghazal
-Stopped Egypt going back as a vassal after the Oriental Crisis.
-Added 4 events to egypt or sudan owners to cover the Mahdist revolt, the conquest of South Sudan and of Darfur.
-Removed the accepted cultures from Liberia (as they really segregated those guys) and added events for the Liberian Independence in 1847 and their conquest of the rest of the country. Changed it so Liberia starts as a US colony. Also fixed the Liberian parties names.
-China should lose their cores in 1469 Uriankhai/Kyzyl once Russia takes it and rename it. The provinces in Outer Manchuria and Kyzyl also gets a 3 year modifier to encourage russian immigration and kickstart assimilation.
-Renamed Lake Tchad to Lake Chad and renamed Lake Victoria to Nalubaale. Added an event for European explorers to find it and rename it, depending on their culture group.
-Fixed NNM separatist rebels spawn_chance screwed syntax
-Disabled the Dominion system
-Craftsmen will demote to serfs until 80% of the province is serfs, while farmers and labourers stop demoting at 40%.
-Slaves don't have needs anymore. They didn't buy anything because they got no money and needing something only got them pissed because they couldn't buy stuff.
-Stopped pops from demoting to serfs in areas they historically were abolished/didn't exist. SO the baltic states will not have serfs, nor italian provinces of austria or austria proper, even if Austria and Russia have serfdom.
-Added 269.95K serfs to Transylvania (a little more than the 243K they had according to http://mek.oszk.hu/03400/03407/html/383.html ). 
-Finished adding serfs to Austria, totalizing 21% of the pops or almost 2M. In contrast, Russia starts with a third of its pops as serfs, 4 M pops.
-Added a decision for Russia to expel the Manchu from Primorye
-Reduced the RGO bonus of reforms, to avoid early game overproduction.
-Fixed reform desire. Made it more focused on the vanilla reforms. After a country has some basic rights secured, pops will start focusing on other issues. Added UH reform desire. Previously, pops were happy with voting and having the UH as appointed only.
-Fixed the Congress Poland start. It has a warning and the January uprising starts in Congress Poland.
-Made an event for the abolition of serfdom in Austria.
-Made an event for the sale of Zeyla
-Gave Taizz to the Ottomans
-Made an event for the Pioneer Column and the foundation of Rhodesia. The event move british soldiers from cape colony to Rhodesia.
-The Rhineland starts with a steel factory rather than a fabric factory. Meant to simulate Krupp's steel factory in the area.
-Added a historical general for Brazil.
-removed reform desire for Bureaucracy reforms and for Proportional representation in the UH, but they still want two per state. Reform desire for these didn't make much sense.
-Changed vanilla universal voting reform desire that could happen before universal voting was the next reform.
-Event for culture groups to rename Istanbul
-As a provisional measure, a theocracy turns into a HM's government once they pass enough reforms.
-As a provisional measure, Russia and Austria abolition of serfdom immediately changes all serfs to farmers.
-Stopped slaves and native cultures in the americas to assimilating in the primary culture
-stopped non american/oceanic countries from enjoying the assimilation bonus of the continent

Experimental Features:
-Ports reduce importation cost in 0.1% per level. The objective is to simulate infrastructure of big ports.


To do (short term):
>No option to send the afro american pops to Liberia, as originally planned

Make decision to rename South Tirol according to German and Italian names.
-Check why rebels are double appearing.
-Make egypt inherit Hedjaz if they win Oriental Crisis
Make a flag for the LIT, LAT and EST cores so Russia doesn't get serfs there. Make the changes in the pop files and implement via the cleanup event. Apply the same things for Italian austria and austria proper.
Event for integrating the Kumul if they are your vassals and you are civilzed
event for uncivs with tradition to change their NV

To Do (future):
Make soldiers and officers state capital only?
Add an Island terrain type with a smaller RGO size.
Make an event to make the spanish to share Morroco with whatever power gets it
http://en.wikipedia.org/wiki/Maxim_gun
https://en.wikipedia.org/wiki/Corinth_Canal#Construction_of_the_modern_canal

Notes:
NEVER make a pop promotion depend upon a province flag. It WILL fuck things up.
NEVER make a pop issue less than 1


__________________
V0.2 Beta
-Changed CZH, SLV and BEL fascist flags to the historical flags. Corrected party names, corrected all Croatia's Party names, corrected some of Canada and Brazil party names.
-Made Australia, Canada and New Zealand use the BritishGC group
-Removed the Ainu tag, added the Ezo tag and added events for their Independence.
-Made Norway start with basic school
-Made the Sweden school reform event actually change the school to basic school
-Made a new technology, splitting the effects of bacteria and antiseptics, called it germ theory (made to represent the maturation of bacteria theory principle)
-Prussia, Austria and Belgium start with historical generals. Eventually, I want all nations to start with historical generals.
-Made sure the UK conquers the Sikh (at least they get the CB to do it)
-Renamed some nation governments like TUR communist and PBC republic.
-Tied health reforms to tech, so you can't have good healthcare without techs. You will be able to tell the necessary techs by hovering the mouse over the next reform that you can take.
-Changed vaccination discovery chance to use a more reasonable tech
-Made the crisis system dynamic - the first nation to research revolution and counterrevolution will stop the events that cool tensions in non colonial nations around the globe. You will be able to use the increase tension NF when you have researched revolution and counterrevolution.
-Added 5 more images to the historical events of Mexico
-Made participation in elections (election events) optional. An event will fire before the events start to ask if you want to participate in the elections (that is, to have the vanilla election events) or you forfeit it. Forfeiting it will make the issues move randomly in random non colonial states. Elections now last 7 months instead of 6 because it takes one more month for the elections to start for real.
-Added an event for the historical change in child labor laws in Prussia
-Removed TAGs: PZN - Poznan, LEO - Leon.
-Added 6 new reforms for civs and 5 for uncivs
-Added the new reforms for all countries.
-Balanced several reforms: State Press give some ruling party support. Party Free Trade/Protectionism are not the sole decider of tariff sliders. Economic policy also plays a role. So Free Trade/Protectionism decide about half of the stuff, with Protectionism letting the tariffs up to 50%. Protectionism ups the tariff limit limit in 10%. State capitalism ups in 25% and Planned Economy let it be fully unlocked. But the more control over the economy you have, the bigger the import costs. Party war policy also plays an important facytor, both in conscription and military spending. Jingoist parties can put 100% in the military budget, pro military can go up to 75%, anti military can go up to 50% and pacifist can go up to 30%
-Changed so there is no promotion to capitalist or aristocrats under a communist government.
-Added a decision for communist governments to nationalize the industry, get money based on taxes and convert all rich strata to farmers and craftsmen.
-Adapted the flag that made less likely for capitalists to develop under serfdom to apply to all countries with the serfdom reform.
-Changed it so communist governments can't encourage capitalists or aristocrats.
-Fixed several vanilla bugs related to pop issue choosing and pop literacy.
-Made disarmed nations (nations paying war reparations) influence in pop going fascist (that is, pops are more likely to go fascist in these nations).
-Changed the way pops side with slavery. More educated pops with high CON (with the exception of aristocrats in slave states) will be generally pro abolition. Pops in slave states are always less inclined to abolish slavery. Officers and soldiers in war time will want to abolish slavery. Farmers and Laborers unemployed in a slave state will be way more inclined to support abolition. Reactionary pops will be a little more inclined to support slavery while liberal, communist, socialist and anarcho-liberals will be more inclined to support abolition. Capitalists will always be less inclined to support slavery. This all means that a pop with high education will have a hard time maintaining slavery while a country with less literacy will have an easier time. 
-Adapted the ACW slavery events for the new reforms and added new images for some of the more important events.
-Adapted all other slavery related events to take into account the new reforms
-Added 2 historical generals and one admiral for the french in 1836 (related to the conquest of Algeria). Added one more historical general for Algeria.
-Added an event for the rise of the Senussi, so the ottomans can conquer them and the Italo-Turkish war can end with Lybia's borders, maybe. You can play as them in the event but they have 3K pops and less than 1% are soldiers. Good luck!
-Removed old terrain system.
-Made ideology unlocking more dynamic, it's based on research now. Fascism unlocks from 1900 with the invention of Doctrine of Fascism. Socialism with Karl Mark and Engels invention form 1845. Communists from 1860 with the historical theory, karl marx, engels and if you already invented socialists, hopefully unlocking around the first international. Anarcho-Liberals with from 1840 from pierre joseph proudhon. Changed the descriptions for unlocking these ideologies. Made it so the country that unlocks fascism has some pops converted to fascist ideology to simulate an Italy-like situation. The first country that unlocks communism gets a very small boost to communists in their capital. to 
-Added a modifier for the Zulu to simulate their military focus and dominance in the area. Tweaked Matabele pops and added the king of Mtabele as a General named Mzilikazi. Added events for the Mzilikazi migration to Matabeleland (when that happens the region will be renamed that, the region is now vanilla named as Rozwi) and for the Mfecane.
-Added a historical general to Suali and Basotho.
-Changed the name of Natal-Zululand to Zululand only. When Natal is declared, the region will change the name. Changed the name of the region Vrystaat to Basutoland. It will change to Vrystaat with Transvaal. Changed the name of Ladysmith to Emnambithi. It will change to Ladysmith once Natal is declared. Changed Lydenburg to Ga-Riba, it will change to Lydenburg. Changed Pretoria to Ga-Rankuwa. Changed the name of the region from Transvaal to Tky-Gariep. Changed the Kimberley region to Griqualand and Kimberley to Griqualand. Changed Bloemfontein to Thaba Nchu. Anyway, changed all the colonial names from these places to time appropriate names. The names change when the republics rise.
-Changed kimberley (coal) RGO for Pretoria (grain) RGO 
-Added slaves for the south african nations that had them.
-Made uncivs without access to the sea unable to get some events regarding westernization and ships. In practice, uncivs without sea access have a higher chance of taking longer to civilize.
-Made pops in countries with the NV Liberty or Equality be more pro abolition
-Fixed Congress Poland borders
-Changed the name of Seattle to Fort Vancouver, Portland to Oregon City and Baker City to Grande Ronde. These cities weren't founded at the game start but Vancouver and Oregon City were. Gave Vancouver to the british ( In 1824, using this citation as source : He moved its regional headquarters to Fort Vancouver, which became the de facto political center of the Pacific Northwest.) Baker city is founded with the great migration.
-Added events for the great 1842 fire of hamburg and for germans to send help and for the great migration of 1843 for the USA to get oregon.
-Changed the goods of Klamath Falls from fish to timber and changed Portland (oregon city) from timber to fish. Changed the goods of Nitchequon from fish to timber and changed Fort Chimo from timber to fish. Changed Banja Luka (fish) to fruits and and Zadar (fruit) to fish. Changed Mao (fish) to cattle and Cotonou (cattle) to fish. Changed Velingara (fish) to grain and Bissau (grain) to fish. Changed Boras (fish) to grain and Frederiksstad (Grain) to fish. Changed Qaratal (fish) to grain and Kizil Arvat (grain) to fish. Changed Nagano (fish) to grain and Mito (grain) to fish. Changed Caribou (timber) to grain and Port Harrrison (grain) to timber. Changed Stikine (timber) to grain and Ross river (grain) to timber. Changed Fort Vermilion (timber) to grain and Inuvik (grain) to timber. Changed Dryden (timber) to cattle and Ungava (cattle) to timber. Whitehorse (fish) to timber and Prince Rupert (timber) to fish. Fort Rupert (fish) to Iron and Repulse Bay (iron) to fish. Changed Aruchukwu (fish) to grain and Calabar (grain) to fish. Changed Colima to Fish (iron), gualajara to timber (fish) and aguascalientes to iron (timber). So all fish RGOs are by the ocea, on a sea, near a great lake or the article circle.
-Reworked Canada's, Iceland and Greenland Life Ratings. Iceland and Greenland LR went down to 25 and 10 respectively. Most of Canada went down to 10 in the extreme north, then 15-20-25 in the middle with the 35 values kept in the border with the USA. Toronto, Ottawa and the line of cities nearby got up to 40. Hopefully, the country will be populated more historically.
-Added triggered modifiers for owning the Kiel, Suez and the Panama Canal. Adapted the british Raj one. Made a new modifier for small civilized countries, with less than a million people (300K pops) or less than 6 cities, to keep small countries like Lubeck afloat without loans. The modifier only applies to European countries though.
-Changed clergymen localization to intellectuals.
-Added Slaves and aristocrats to the dutch Antilles.
-Artisans can make fabric out of wool now.
-Made New York a coastal province.
-Removed the Jan Mayen Island and added the colony of Saint Barthelemy (St. Barths in the game), a swedish colony in the antilles.
-Fixed the Sahara western border in the terrain map.
-Changed the unused coastal desert vanilla terrain to Desert, made the old Desert terrain into Inhospitable Desert. You can't build infrastructure in inhospitable deserts, so you can't crisscross the Sahara with railways. Changed a few provinces from Inhospitable Desert to Desert, so you still can build railways crossing the mojave, potosi, around the arabian peninsula and cape to cairo, obviously.
-Removed Anglo African culture. The culture existed in the cultures files but had NO pops, country, nothing in the game files whatsoever.
-Gave Fascist Spain a decision to reclaim gibraltar, the french Pyrenees and Portugal according to the Falange doctrine. This decision gives a lot of infamy though.
-Renamed 339 Viipuri to Vyborg, 1019 Voronets to Voronezh, 1028 Vyatkha to Vyatka.
-A name changing decision to change St. Petersburg — Leningrad, Ekaterinburg — Sverdlovsk, Nizhni Novgorod — Gorky, Vyatka — Kirov, Tver — Kalinin, Samara — Kuybyshev, Tsaritsyn — Stalingrad, Yuzovka — Stalino, Luhansk — Voroshilovgrad, Mariupol — Zhdanov, Yekaterinoslav — Dnepropetrovsk, Luga - Petrogradsky, Tver Region to Kalinin Oblast and another one to change them back.
-Fixed the broken tax sliders from the social pyramid minimod. The rich taxes and poor taxes weren't inverted.
-Having the Gentry or Hereditary Bureaucracy will make it harder for the poor class to promote to bureaucrats and easier for the rich to "demote" to it.
-Reduced the Russian Fleet size so it's less of a drain on their coffers and added a port to Mariupol, as there was historically.
-You can create Argentina as a GP now, if you have the territories in our sphere or own them.
-Changed the localisation of Sikh parties and of the Mughal Empire to be a little more accurate. Corrected the Sikh Monarchy flag to be historically accurate.
-Anarcho liberals don't show in Unciv nations anymore.
-Changed so clerks (theoretically) earn double the salary of craftsmen.
-Changed Officers so they are demoted on migration, changed so the give less Leadership bonus (from up to 3 points to up to 2) (hopefully, this will make generals more significant and less spammy)
-Changed the way religious conversion works: Literacy no longer is a factor. Religious policy is the biggest factor in conversion. Pops in a occupied province will not convert, animists in africa will convert faster and Mormons/Jews will convert slower.
-Changed the name of La Plata to United Provinces.	
-Fixed Russian OOB. No more Fins and no more units in Finland or Congress Poland. Added 2 historical russian generals and 1 admiral.
-Stopped pops that are not from the state religion to be pro-moralism.
-Changed so the Second Great Awakening event of the USA gives moralism for pops of the state religion only.
-Made an event for Japan to lose cores on Korea after some time of not holding Seul while a civilized nation holds it.
-Made an event for the USA to pass child labor reforms.
-Changed the vanilla events to make it less likely that the AI will spend money when don't have any and bankrupt themselves.
-Changed some events like Authoritarianism to remove Pluralism besides the already established effects.
-Changed the NV modifiers to be more distinct.
-Renamed Walvis Bay to Ezorongondo, Port Arthur to Lüshun, Windhoek to Otjomuise, Swakopmund to Otjozondjii, Karasburg to Aixa-aibes. Made decisions to rename these places.
-Added a bunch of names to the Japanese and the Korean name list. Previously Koreans had about 10 names, now they have a lot. Inverted the name with the surname fields of the japanese and the koreans.
-Fixed a localization bug in the alaskan purchase.
-Made capitalsits a little more useful for factory input.
-Once a country loses a containment war, they also get their forts and naval bases destroyed.
-Unify America and the Austrian Empire requires a jingoistic party in power. Austria-Hungary can no longer use it.
-Added a genocide decision. You need the inventions Dogma of Violence and Rethoric of Hate nor be a signatory of the Geneva Convention. You need a fascisc/communist dictatorship or an absolute monarchy/presidential dictatorship with a reactionary/fascist/communist part in power. The decision sets a timer so you can continue. at the end, an event chain will guide through the options.
-Added a decision to retract from the Geneva Convention.
-Added an event for cleaning Japanese cores in Korea if they don't hold it after some time. A korean playtrhough is a little more possible now. I should get around to get the old finnbro decision to refute the manifest destiny as Mexico.
-Stopped the Rotten Boroughs crime to happen in countries with no voting.
-Added a new Hunger Riots crime for civs under severed hardship.
-Made events for the Rhine Crisis. It happens with a french declaration that starts enmity by the german states and France. If Prussia takes the Die Wacht am Rhein decision, any non germanic country will get a call to defend Germany by Prussia in a unification movement.
-Add event to rename the Namibia colonies and for the Luderitz expedition.
-The Springtime of Nations now should only happen in europe, like the description says.
-Conservatives are more likely in slave states (to avoid the whole Liberal CSA thing that was going on).
-Made an event for the abolition of slavery POST American Civil War. The ACW can happen before the abolition of slavery, and now the USA can abolish after the war ends, like it officially happened.
-Added 3 new NVs: Autocracy, Tradition and Productivity. They have their own unique bonuses and changes in POP ideology. Autocracy and Tradition make pops less likely to be liberal and more likely to be conservative. Productivity is completely neutral. Changed several countries NVs to reflect the new NVs. National values are not tiers like PDM, they are meant to represent the core values of a nation's people. And that almost doesn't change. Russia is the best example. Ever since the 19th (and before, actually) century they have a tradition of having a strong ruler.
-Fixed Prussian OOB so the organization of the starting armies is better. Didn't change the number of units, only their places.
-South Africa is not normally releasable anymore. You can form it and release it through a decision, like the United Baltic Provinces.
-Added a decision for the Mughal Empire to reclaim India, adding cores on all Indian cores.
-Changed "High and Low Pressure Steam Engine" to "Compound Steam Engine". Changed Water Wheel to Piston Steam Engine and Practical Steam Engine to High Pressure Steam Engine. Change their activation dates to make a little more sense. Changed the pictures.
-Corrected some small graphical errors in the file province_infra_strip.dds.
-Changed the way CSA cores spread: They need a neighbor CSA core before spreading. This means no more CSA exclaves.
-Changed the way EGO province modifiers from inventions work. Tractors now will only happen in provinces that produce a farm type RGO, and the mining related will appear only in provinces that produce a mining type RGO.
-Changed the Bonnie Blue Flag modifier so the CSA has a fighting chance.
-Integrated most flags from the Alternative Flag Pack V2 by Anon.

______________________
Hotfix E:
-Fixed Spain starting flag
-Fixed Wickedness Must be Stamped Out (Moral Crusaders) event so it's not spammed.
-Fixed a Vanilla event that mentioned a Politburo but didn't require a communist regime.
-Fixed French and Paris pops back to historical levels (they were too high, overall pop were almost at the 1856 census level).
-Gave Algeria its cores on the rest of Algeria.
-Fixed pops in Tangiers and West Sahara
-Changed a couple of regions and province names. Gave the Cherson province to the Zaporizhia region so the Crimea region has only the Crimean peninsula in it. Province 972 Ekaterinoslav changed to Yekaterinoslav, Province 969 from Pervomaisk to Olviopol, Province 1178 from Sana to Sana'a, province 1773 from Aaiun to Saguia el-Hamra and province 689 from Tesin to Teschen.
-Events for the French conquest of Algeria and the Hispano-Moroccan War (1859–60).
-Stopped election event spam from the NNM events, still need to make some adjustments for the vanilla ones.
-Start of the Crisis balancing, now increase tension NF is unlocked in 1870. I tried to make it tied to the research of Revolution and Counterrevolution, but the game didn't deal with that very well and that wasn't possible. One event will also clean province tensions in non colonial provinces in the old world until 1870. Also wanted to make this tied to tech. Maybe make another event to clean balkan tension until 1900.
-Fixed French borders in Algeria according to http://upload.wikimedia.org/wikipedia/commons/7/7b/French_Algeria_evolution_1830-1962_map-fr.svg
-Lots of tweaks, unique images and bug fixes of the mod, in vanilla and in NNM (including the Peru-Bolivia bug).
-Removed TAGs: PML - Pomerelia. Canditates for removal: BKV - Bukovina. RUT - Ruthenia.
-Integrated Faulty's rebel icons. Fixed one of the frames and removed another one. Integrated a lot more, totaling 17 rebel icons, almost one icon for every rebel and 11 more than vanilla's 6.
-Integrated flags from the Alternative Flag Pack mod by anonymous. Fixed his democratic flags from TAG_democracy to TAG_republic. Finished integrating parts of the mod "Flag Tweak Mod Pack Conversion... Thing". A lot of flags like the Israel ones, the french, swedish and norway fascist flags, El Salvador, Nicaragua, England and others were made by me and some by other anons. Most changes were made for south american fascist flags, most now have falangist symbols.
-Integrated the Italo-Turkish war for Lybia event chain by Anon. Made some images, made the localization and bugfixed it.
-Made decisions for Italy to claim the Adriatic and one for fascist Italy to claim Corfu, Malta, Savoy, and Corsica.
-Made the Japanese decision to claim Korea even with a foreign power holding it harder to do.
-Fixed old NNM flags that didn't have a tag: LNA, BEL, NPL, SCY, UAL, UAR, UFL, UGA, UIA, UIN, UKY, ULA, UMI, UMN, UMO, UMS, UNC, UNJ, UNY, UOH, UPA, USC, UTN, UVA, UWI, UWV.
-Fixed the starting flags to match the starting governments, fixed a few flags from NNM.

Hotfix D:
-Defines.lua restored to vanilla
-Adjusted Unciv malus to research
-Fixed missing italian cores on South Tirol
-Made NNM Germany and NGF formation decisions a little more vanilla
-Fixed Angoche being colonial.
-Fixed wrong Austrian core in the middle of transylvania
-Fixed some wrong argentina triggers that were causing weird behavior in two events
-Add a quick solution for the weird as fuck bug with Bolivia always puppeting Peru (still pinpointing that, but it seems to be a reload bug)
-Fixed some NNM events and a bunch of weird behavior in NNM events
-Fixed a wrong Omani core
-Fixed the Omani OOB, added a historical general
-Changed the Oriental Crisis - Egypt goes back to being a puppet if they lose the war. Ottomans inherit Hedjaz.
-Made a quick event to give the ottomans a conquest CB on North Yemen if they own Mecca and have nationalism and imperialism researched
-Reverted the unnoficial changes to RGOs in Africa back to what I did. The total number of RGOs is the same a vanilla per category, I just -changed fruit producing regions that are deserts to cattle/wool and exchanged some south african fruit/grain provinces with the coal producing provinces of Nigeria. This makes South Africa one of the biggest Coal producing regions in the world and make it more historical accurate. The coal was placed in the eastern side of South Africa according to maps of mines in South Africa.


Hotfix C:
A bunch of fixes made by an anon. Fixed supply and have some terrain changes and some OOB and core fixes. Expect further tweaks down the line and also deleted your defines.lua in the mod folder to guarantee everything is vanilla, as I need to review that file.
Kudos for that anon.
This does not contain any reform fixes or anything like that, and again, it was mostly done by an anon in the thread.
Anon's Changelog
- Fixed extra election event spam:
* Use vanilla's extra election events for major political issues
- Fixed Caucasian Wars
* Split Caucasian war into two separate wars
* Fix Circassia and Dagestan OOBs
* Remove Circassian units from Russian OOB
- Fixed war files
* Add end to Taiping rebellion
* Fix casus belli for Massina Jihad and Cochinchina campaign
- Reorganized terrain file
- Reworked populations
* Revert craftsmen POPs to vanilla levels
* Revert Russian clergy POPs to vanilla levels
* Clean up most files for better comparison with vanilla files
- Increased supply limit modifier for core province
* Supply limit for core provinces is now +3. This is a workaround until the revised terrain system is rolled out


Hotfix B:
Fixed and tweak some events to account for other actions/player actions.
Tweak pops in Argentina.

Hotfix A:
Fixed La Plata formation decision.
Added the post peace and clean up events to the aftermath of the uruguayan-argentine war.
Fixed colony spam in the start (protectorates that could be turned into colonies are now colonies).
Made tech research for Congress Poland way slower.
Fixed the event to reject the Paraguayan declaration of independence. Now you really get a conquest casus belli that you can use, even if they have more than one state. 
Fixed paraguayan starting OOB. They are way more scary to tackle early on. Added a huge tech penalty research for Paraguay from their initial isolationism. Added a historical general.

Notes:
I will fix event spam by pdm/nnm events in the next version. Theoretically, you just need to remove ExtraElectionEvents.txt but I don't have the time tot est it for this version. You can remove that yourself if you feel like risking it and see how it goes.
Into consideration for removal:
Korea to Japan Strait



Removed: Event cleanup 60160
Removed Tags: Iberia. Babylon. Hindustan (HDU). Maratha (MRT). Maghreb (MGH). Jan Mayen was already out.
Fixed shit: NNM/PDM general bugs 22 (missing images, wrong event composition, missing stuff, non existent commands. Not counting typos.)
definues.lua tweaks:
Non accepted are slightly more militant.
Increased the militancy gain when you conquer a province.
Made L-F bonus to output a little bigger.



Phase 1 - PDM barebones
-Removed Strait of Dover aka Wiz Strait
-Fixed Kingdom of Champasak, making it a vassal of Siam instead of being integrated in Siam.
-Fixed Aden region being English and Yemen already existing. The region is now divided into 4 OPMs: Lahej Sultanate (Aden), Fadhli Sultanate (Bayda), Kathiri (Mukalla), Mahra Sultanate (Ghayda)
-Fixed and added an Ethiopian state that was missing and fixed Ethiopian pop ethnicities
-Fixed bunch of references on city/buildings/railways positions in the middle of seas and sea provinces in positions.txt
-Fixed Oman not owning Zanzibar
-Made all RGOs from PDM match vanilla (that was some work).
-Made Circassia and Caucasian Imamate free in the 1836 start date.
-Congress Poland is a substate of Russia.


 
Phase 2 - General nation/pop fixing and start date adjustment
-Fixed Emirate of Afghanistan flags. Fixed Kokand flags. Fixed imperfections in XBI fascist flag. Fixed Nepal flag.
-Added Tatar and gypsies slaves to Moldavia and Wallachia instead of them enslaving their own kind.
-Added slaves to the sultanates of Aden. They are African Minors and animists, since the sharia forbids the slavery of other Muslims, and the slave trade of Oman of pagan Africans from near somalia was common.
-Added slaves to Bahrain, Nejd and Ha'il. They all were countries that allowed slaves in the game files (and historically) but didn't have a single slave.
-Added slaves to Trucial States. (Need to add a British decision to outlaw it in 1839).
-Added slaves to Zaydi and Ottoman holdings in the Arabian Peninsula.
-Added slaves to Persia. Made Persia have yes_slavery. Slaves are Afghans, North Caucasians, Indians and Africans. Compromising almost 6% of Persia's population, 90k slaves were added. Took some time to read and do the research, but it's over now. Slaves and their ethnicities are distributed through territory. In the Caucasus/southern Caucasus regions they are mostly Tatar, North Caucasian, Georgian and Armenians. In the Persian Gulf provinces they are africans and sometime indians. In central Persia they are africans, indians, georgian and armenians. In east persia they are indians and afghans. In most regions they are concentrated in the region capital for game speed sakes. Only in the heavily populated region of Tabriz they are more distributed.
The region of Khuzestan don't have any slaves, as the British established a seat of power in Bushehr to try to control the slave traffic in the persian gulf.
-Added slaves to Afghanistan, Kokand, Khiva, Bukkhara, Kalat and Makran.
-Added slaves to Morroco and Algiers.
-Fixed Esmereldas province name to Esmeraldas.
-Fixed South Peru capital location.
-Fixed The United States of Central America (USCA) to their real name Federal Republic of Central America (FRCA).
-Renamed afro caribeno to Afro Latino, to encompass all Latin American slaves, and added slaves to Argentina, Paraguay, Ecuador and Peru.
-Fixed British possessions and relations in India:
Source: India. (with) Delta Of The Ganges. Engraved by J. & W.W. Warr. Published by H.S. Tanner Philadelphia. (above neat line) Tanner's Universal Atlas. In:
http://www.davidrumsey.com/luna/servlet/detail/RUMSEY~8~1~596~60234:India---with--Delta-Of-The-Ganges--?sort=Pub_List_No_InitialSort
*Made Kolhapur and Bijapur Maharashtra territory. Added Maharashtra as a vassal of the UK.
-Slave population of Korea from 6% do 24% to better match sources claiming Korean slavery matched  one third to half of the population.
-Added Slaves to all states in India minus The Sikh Empire, totalizing 2M pops or 8 million people.
-Added Slaves to Sikk, Bhutan and Nepal.
-Fixed Burma monarchy flag, added slaves to Burma. Added more slaves to Siam. Changed Siam Absolute Monarchy name to Rattanakosin.
-Luang Prabang and Champassak were marked as yes slavery, but no slaves, added slaves to them. Changed name of Johore to Johor. Added more slaves to Dai Nam. Fixed some province names.
-Made Lanfang allied to China.
-Changed Atjeh to Aceh, fixed the flag and added slaves. Added slaves to Sulawesi, Siak, Sulu (yes_slavery but no slaves). Added slaves to Dutch, Spanish and  Portuguese East Indies colonies, bringing slavery to Borneo, Java, Philippines and Indonesia,
-Gave Api to Sulu, changed province 1464 from Sulu to Jolo.
Sources on slavery in this region:
http://www.kitlv.nl/home/Spotlight?subpage_id=422
http://researchrepository.murdoch.edu.au/18167/1/slave_markets.pdf
-Added slaves in the big Ottoman centers.
-Gave Tibet a core in Yazhou.
-Changed Changtang from Tibet to Xinjiang.
-Gave China cores on Pogobi and Otomari, since they were claimed by the Qing but not colonized.
-Changed Mongolia capital to Uliastai .
-Made Qinghai and XInjiang substates of China, on the basis they were ruled by Amban.
- Qinghai province of Díhuà changed to Tihwa. Added slaves to Tihwa and Kashgar, all of them are beifaren.
- Qinghai gained Mongol and Tibetan slaves on all provinces.
-Made Yunnan a substate of China, since it followed the Tusi system.
-Renamed Manchuko to Manchuria, gave it their possessions in the time, encompassing little more than Outer Manchuria.
-Gave Amami Islands from Ryukyu to Satsuma Daimyo.
-Changed Bonin island population from 15 to 29, from micronesian to yankee.
-Added slaves to China proper. Cleared out some China reforms.
-Fixed CHI and MCK OOB, renamed KOR from Korea to Kingdom of Joseon, made their communist government be named DPRK and fixed the Joseon flag. (Add tag for Korean Empire?)
-Fixed Yunnan and Qinghai starting parties names.

Phase 3 - NNM Integration and finishing touches on the 1836 start date
-Fixed some Vanilla bugs.
-Fixed Gonder, Tigray and Shewa primary and accepted pops. Fixed pop compositions for the Gonder territory. Fixed their OOB (they had hussars!).
-Removed Argentine/Paraguay from the Chaco region, added decision to claim it and fixed the pops in the region.
-Provinces 2353 - Trenque Lanquen, LR was 35, now is 15. 2393 - Telen, LR was 35, now is 15. 2395 - Curaco, LR was 35, now is 15. They were made empty and pops were corrected were needed. Changed Conquest of the Desert decision accordingly and made it have causalities on the natives. Made a similar decision for the Chaco region.
-Fixed rebel_types from NNM. Several errors were found (typos that made some trigger for rebels act in the wrong way. Examples are Separatists rebels missing independence trigger, native arab rebels, several missing entries, etc).
-Uruguay: Added Colorado rebels, fixed Uruguay and Chile starting government.
-Fixed Uruguay and Chile starting government and political reforms based on their constitutions. Added an argentine confederation tag, put them on the 1836 start and based their reforms on their constitutions.
-Add event to put money on the National Bank of the UK and Switzerland to avoid a lot of countries owing 2£ for dozens of countries.
-Made Montenegro a Russian satellite and changed their flag to match the historical one (needs some new fascist and democractic)
-Added Kumul Khanate with flags and everything. Made them a vassal of the Qing.
-Added a Corrientes tag. Made it, Entre Rios and Buenos Aires substates of the Argentine Confederation. Added OOB and historical generals.
-Fixed Paraguay start date control of the Chaco. Fixed Paraguay starting literacy, reforms and fixed party issues.
-Added Polish Organic Statute and Polish Uprising event chain.
-Added The Sultanate of Darfur, corrected the flag a little, changed Sokoto to Sokoto Caliphate. Added Borno, corrected the monarchy flag and the standard flag. Added Wadai.
-Made tags, flags, names and added cores for the Baguirmi Sultanate and the Adamawa Emirate, all near Lake Chad.
-Corrected Bornu Flag.
-RGO exchange in the deserts: Farafra lost fruit and got wool, Bangalore lost wool and got fruit. Changed Saurimo (cattle) to fruit and Baris (fruit) to cattle. Changed Lilongwe (cattle) to fruit and Bilma (fruit) to cattle. Changed Gweru (cattle) to fruit and Murzuk (fruit) to cattle. Changed San Fernado de Atabapo (wool) to fruit and Arlit (fruit) to wool. Changed Angostura (wool) to fruit and Tin Zawatene (fruit) to wool. Changed Yuncos (wool) to fruit and Tin Zawatene (fruit) to wool. Changed Bouar (cattle) to fruit and Zouar (fruit) to cattle. Changed Concepcion (cattle) to fruit and Kufra (fruit) to cattle.
-Added events for Paraguay, Uruguay and Argentina. Total amount to more or less 60.
-Add Shilluk Pops, Shilluk Kingdom Tag and stuff related to the 1836 start. Added their cores and made them start owning Fashoda, their capital. Egypt has a core in it.
-Added event for Bolivia to settle it's border with Argentina, to rename Chuquisaca to Sucre and to later in the game make its capital La Paz.
-Canals now take time to build and cost money.
-Added events for the conquest of Aden.
-Made most irredentist decisions need fascists in power. Made some give badboy for violating old treaties. Removed Mali Empire decision. Removed Greece joining Yugoslavia.  Made a free Congress Poland be able to turn into Poland. Removed some accept pops decisions from KUK and Danubian Federation. Canadian tags no longer apply to USA statehood. Removed Kobu Gattai decision from Japan, it appeared to be a leftover.
-Changed Moghulistan (?) to the Mughal Empire. Made it a puppet of the British and holding Delhi in 1836.
-Fixed Ethiopia and made the borders historical. Akordat and Asmara should belong to the kingdom of Medri Bahri, but to avoid using a tag they were given to Tigray. Move Tigray capital to Asmara to facilitate the unification of Ethiopia.
-USA states no longer ask to join Canada, Canada states no long join the USA.
-Added Warsangali Sultanate.
-Events: 96215 and 96216 and Indian pan nationalists were taken out. On the basis of "The Indian desire for complete independence, or Swaraj, was born with Bal Gangadhar Tilak, whose followers were the first to express the desire for complete independence, an idea that did not catch on until after World War I.
-Made the Eiffel Tower take time to build. Added the vanilla graphics to it. Made a decision to rebuild the Place of Westminster. Made it take time to build and add the Big Ben to the map. Made events for the destruction of the landmarks.
-Made event chains for the Krakow Uprising and the January Uprising.
-Event for the USA to lose their statue of liberty modifier if they ever stop being a democracy.
-Added events for the conquest of Lahej and adapted the protectorated of Aden and the formation of Yemen decisions
-Added events to enact the law of return as Israel. Made it so the NNM events for the return of the jews will happen faster if you enact the decision.
-Tweaked Haiti and Dominican Republic starting pops. Added images for 2 events regarding these nations and corrected their starting Upper Houses.
-Fixed the OOB of Chile and the PBC. Added a navy to these nations based on the battle of Casma. Added a historical general and a admiral for Chile. Add a historical admiral for the PBC.
-Changed kimberley (cattle) RGO for Awka (coal) RGO - changed Calabar (coal) RGO for Lydenburg (fruits) RGO
-Changed a bunch of wrong terrains.
-Fixed Haiti, Hawai and Chile starting stuff. Added the natives as accepted cultures for Peru and Bolivia.
-Made some events more likely, made the colonization techs be unlocked 10 years before NNM did.


General improvements:
Added custom pictures to several events, totalizing almost a 100 new pictures for events. Localized all ported events from NNM, checked them with the Validator, corrected a hundred typos, fixed bugs and misspellings on them. Changed and fixed a lot of tags.
The first release is just the amalgamation of the basic work. Porting events, adapting, making sure they work, correcting them, localizing them, making sure there are no bugs. It's was focused on fixing what I changed, so the events are most out of necessity than priority of work. Version 2 will have serfs if I get around to add them in a satisfactory way.
-Events for South America reach the eve of the war of the triple alliance