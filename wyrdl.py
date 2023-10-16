import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.font as font
import time

parks_list = {
    "Acadia National Park": {"The answer is Acadia National Park! It was established in 1919 and is located on the coast of Maine!", 
                             "Hint 1: This park was named after a region of Greece.", 
                             "Hint 2: It is the 5th smallest national park by land area in the US.", 
                             "Hint 3: It is the only park created solely from donations of private land.", 
                             "Hint 4: One of the park's peaks, Cadillac Mountain is the talles mountain on the East Coast!", 
                             "Hint 5: It's the only National Park in the Northeast!"}, 
                             
    "American Samoa National Park":["The answer is American Samoa National Park! It was established in 1988 and is located in American Samoa!", 
                                    "Hint 1: This park has a staff of only 25 employees!", 
                                    "Hint 2: This park covers 13,500 total acres of coral reefs, rainforests, and volcanic mountains!", 
                                    "Hint 3: The only native mammal species are three species of bats, including large fruit bats with 3-foot wingspans!",
                                    "Hint 4: The park is spread out across 3 islands." 
                                    "Hint 5: It is the only National Park in the US located South of the Equator!"], 

    "Arches National Park":["The answer is Arches National Park! It was established in 1929 and is located in Utah!", 
                            "Hint 1: The Old Spanish Trail went through this parks visitor center!", 
                            "Hint 2: At least 11 movies were filmed here including: Indiana Jones, Thelma and Louise, and The Hulk"
                            "Hint 3: There are cave and rock paintings in the park believed to be 1,500 - 4,000 years old!", 
                            "Hint 4: The park is known for its distinctive red rock formations and more than 2,000 natural sandstone features!", 
                            "Hint 5: This park used to be underwater and its magnificent sandstone features were formed by the Paradox Formation."], 

    "Badlands National Park":["The answer is Badlands National Park! It was established in 1978 and is located in South Dakota!", 
                              "Hint 1: This park is known for its rugged terrain, stunning views, and rich fossil history.", 
                              "Hint 2: The park was a part of the Louisianna Purchase in 1803.", 
                              "Hint 3: It was used as a practice bombing range during WW2.", 
                              "Hint 4: It is believed that this park was once covered by a shallow sea 75 million years ago!", 
                              "Hint 5: Many Native American tribes have used this area as their hunting grounds mainly hunting buffalo!"], 

    "Big Bend National Park":["The answer is Big Bend National Park! It was established in 1944 and is located in southwest Texas!", 
                              "Hint 1: This park has more species of birds than any other US National Park!", 
                              "Hint 2: This park is larger than the entire state of Rhode Island!", 
                              "Hint 3: It comes with its own natural jacuzzi known as the 'Langford Hot Springs'!", 
                              "Hint 4: In 1964, astronauts used this park to prepare for the legendary Lunar Landing!", 
                              "Hint 5: It is known as a land of geographic contrasts due to it containing vegetation belts along the Rio Grande, sparse deserts in the \
                                  Chihuahuan Desert, and entirety of the Chisos Mountain range!"], 

    "Biscayne National Park":["The answer is Biscayne National Park! It was established in 1980 and is located in Florida!", 
                              "Hint 1: This park was the headquarters for the notorious pirate Black Caesar in the early 18th century!", 
                              "Hint 2: The Maritime Heritage Trail offers an exciting opportunity to expolore at least 44 shipwreck remains in park waters!", 
                              "Hint 3: This park protects part of the only living coral reef in the continental US.", 
                              "Hint 4: 95 percent of the parks 173,000 acres are underwater!", 
                              "Hint 5: The park was used as a training area for Cuban exiles during the Cold War."], 

    "Black Canyon of the Gunnison National Park":["The answer is Black Canyon of the Gunnison National Park! It was established in 1999 and is located in Western Colorado!", 
                              "Hint 1: This park has a 'sister' park in Serbia named the Tara National Park.", 
                              "Hint 2: The ravine in this park is over 2,700 feet deep!", 
                              "Hint 3: Although Native American tribes called this area home for centuries, only the rims show evidence of human occupation, never in the gorge.", 
                              "Hint 4: The walls of the ravine are often shrouded in shadows, sometimes only recieving 33 total minutes of sunlight per day in some areas!", 
                              "Hint 5: The 'Painted Wall' is the tallest cliff in Colorado and 3rd tallest in the continential US!"], 

    "Bryce Canyon National Park":["The answer is Bryce Canyon National Park! It was established in 1928 and is located in southern Utah!", 
                                  "Hint 1: This park is known for towering weathered and unusually shaped rock spires and pinnacles known as 'Hoodoos'", 
                                  "Hint 2: Despite its name, this park is actually a series of about a dozen natural amphitheaters eroded into an escarpment of the Paunsaugunt Plateau.", 
                                  "Hint 3: This park has the longest running Night Sky program and hosts an annual Astronomy Festival!", 
                                  "Hint 4: According to Paiute Indian legend, ancient people known as the To-when-an-ung-wa were turned into the 'Hoodoo' rocks by the god Coyote for\
                                    their nefarious deeds.", 
                                    "Hint 5: It is the 12th smallest national park and the smallest national park in Utah."],

    "Canyonlands National Park":["The answer is Canyonlands National Park! It was established in 1964 and is located in Southeastern Utah!", 
                                 "Hint 1: Given the nickname 'Robbers Roost', the infamous outlaw Butch Cassidy would meet at this park with his 'Wild Bunch Gang' and hide out\
                                      after their big heists!", 
                                 "Hint 2: This park is considered to have one of the best 'Dark Sky Parks' and was designated a 'Gold-Tier International Dark Sky Park'!", 
                                 "Hint 3: Some of the most significant Rock Art is found at this park including the 'Great Gallery' with life-sized figures and intricate designs!", 
                                 "Hint 4: It hosts some incredible archaeological sites like Tower Ruin, a well-preserved cliff dwelling on cliff ledge in Horse Canyon!", 
                                 "Hint 5: in 1869, the legendary John Wesley Powell led the first known successful rafting expedition down Cataract Canyon in wooden boats!"], 

    "Capitol Reef National Park":["The answer is Capitol Reef National Park! It was established in 1971 and is located in South Central Utah!", 
                                  "Hint 1: This park was first known as 'Wayne's Wonderland' before Teddy Roosevelt changed the name in 1937.", 
                                  "Hint 2: The Fremont Petroglyphs found here are believed to be over 1,000 years old. Mormon Pioneers also left their own versons of\
                                      petroglyphs in the sandstone rock.", 
                                      "Hint 3: The park is home to the Fruita Orchads planted by mormom pioneers. Visitors can even pick the fruit and take it home!", 
                                      "Hint 4: Horseback riding is one of the most popular ways to see the park!", 
                                      "Hint 5: The white domes of Navajo sandstone are known to resemble a famous building in Washington DC!"], 

    "Carlsbad Caverns National Park":["The answer is Carlsbad Caverns National Park! It was established in 1930 and is located in southern New Mexico!", 
                                      "Hint 1: One of the main attractions of this park is its collection of stalactites, stalagmites, and helictites!", 
                                      "Hint 2: This park is one of over 300 limestone caves in a fossil reef believed to be about 265 million years old!", 
                                      "Hint 3: At over 145 miles long, Lechuguilla is one of the 10 longest caves in the world and second deepest limestone cave in the country!", 
                                      "Hint 4: The park has a wonderful Bat Flight Program where you can watch thousands of Mexican free-tailed bats emerge around sunset!", 
                                      "Hint 5: Although the cave systems are popular, there are also 50 miles of aboveground trails that explore the desert landscape!"], 

    "Channel Islands National Park":["The answer is Channel Islands National Park! It was established in 1980 and comprises 5 islands off the Southern California coast!", 
                                     "Hint 1: This park and its unique geography comprises 5 islands and has plants, animals, and resources found nowhere else on Earth!.", 
                                     "Hint 2: Two of the main islands have the highest concentration of prehistoric sites in North America.", 
                                     "Hint 3: The early natives at the park develeped an their own economy and the currency was 'Shell Money' which were actual shellfish!", 
                                     "Hint 4: Painted Cave and the other sea caves on Santa Cruz island were the inspiration for some of the sets on Pirates of the Caribbean!", 
                                     "Hint 5: San Miguel Island earned the name 'Graveyard of the pacific' due to the huge number of shipwrecks around the island!"], 

    "Congaree National Park":["The answer is Congaree National Park! It was established in 2003 and is located in South Carolina!", 
                              "Hint 1: The jungle-like floodplains and wilderness of this park served as a refuge for those that fled the cruelty of slavery.", 
                              "Hint 2: A newspaper editor by the name of Harry Hampton fought for the preservation of the cyprus trees that were being decimated by\
                                loggers. He succeeded and convinced the landowners to sell the land.", 
                                "Hint 3: In 1983 the park was given International Biosphere Reserve status as part of the South Atlantic Coastal Plain by UNESCO!", 
                                "Hint 4: Known as a floodplain, this park is only periodically covered in low lying water. Unlike a swamp which would be permanently covered.", 
                                "Hint 5: The area is known for having the largest area of Old Growth Bottomland Hardwood Forest in the US!"], 

    "Crater Lake National Park":["The answer is Crater Lake National Park! It was established in 1902 and is located in the Cascade Mountains of southern Oregon", 
                                 "Hint 1: This park has a caldera lake formed by a collapsed volcano that is over 1,900 feet deep and is the deepest lake in the United States!", 
                                 "Hint 2: The park has an annual average of 43 feet of snow and is one of the snowiest places in the US!", 
                                 "Hint 3: The parks main attraction is a massive lake that has no streams running in or out of it. All the water comes from rain or melted snow!", 
                                 "Hint 4: 'Wild' starring Reese Witherspoon was filmed here. The movie is about a troubled divorcee who leaves her old life behind\
                                    and decides to hike the Pacific Crest Trail.", 
                                    "Hint 5: Despite its name, the lake is inside a sleeping volcano and even has a smaller volcano in the middle of the lake named 'Wizards Hat'!"],   

    "Cuyahoga Valley National Park":["The answer is Cuyahoga Valley Naitonal Park! It was established in 1974 and is located between the Ohio cities of Cleveland and Akron!", 
                                     "Hint 1: You can take a tour of this park in an old-fashioned steam engine! It is a 2.5 hour ride and covers 26 miles.", 
                                     "Hint 2: This park is home to Brandywine Falls, Ohio's tallest waterfall!", 
                                     "Hint 3: This park includes 125 miles of hiking trails including a portion of Ohio's Buckeye Trail.", 
                                     "Hint 4: The 308-mile long Ohio and Erie Canal runs through the park and was dug by hand by Irish and German workers!", 
                                     "Hint 5: The name of this park is from the Mohawk Indian tribe and it means 'crooked river'."], 

    "Death Valley National Park":["The answer is Death Valley National Park! It was established in 1994 and it straddles eastern California and Nevada!", 
                                  "Hint 1: This park contains the Badwater Basin, which is the lowest point in North America at 282 feet below sea level!", 
                                  "Hint 2: This park has an area called 'Devil's Golf Course', which is a field of jagged salt crystals that rise up from the ground.", 
                                  "Hint 3: At a whopping 3.4 million acres, this park is the largest national park in the Continental US!", 
                                  "Hint 4: This park holds the record as being the hottest place on Earth! on July 10, 1913, the temperature was recorded at 134 degrees Farenheit!", 
                                  "Hint 5: The park is only 76 miles from the highest point in country, Mt. Whitney which has an elevation of 14,505 feet!"], 
    
    "Denali National Park and Preserve":["The answer is Denali National Park and Preserve! It was established in 1917 and it is located in Alaska!", 
                                         "Hint 1: This park was originally named after 1896 presidential candidate William McKinley before being changed to its current name.", 
                                         "Hint 2: This park has the higest elevation in North America!", 
                                         "Hint 3: The name of this park means 'The tall one' in Koyukon, a Native Alaskan language.", 
                                         "Hint 4: The famous mountain peak in this park is a member of 'The Seven Summits' which is a group of the highest mountains from each of the\
                                            seven traditional continents!", 
                                            "Hint 5: It is possible to see the 'Big 5' at this park. It is a group of the 5 largest mammals: caribou, Dall sheep, grizzly bears,\
                                                moose, and wolves!"], 

    "Dry Tortugas National Park":["The answer is Dry Tortugas National Park! It was established in 1935 and it is located in Florida!", 
                                  "Hint 1: This park is home to Fort Jefferson, a National Historical Landmark that is the largest brick fort in the US!", 
                                  "Hint 2: The famed explorer Ponce De Leon discovered this area in 1513 and named it 'The Islands of Turtles!", 
                                  "Hint 3: There are over 250 shipwrecks in within the vicinity of this park dating all the way back to the 16th century!",
                                  "Hint 4: This park comprises 7 islands and protected coral reefs in the Gulf of Mexico!", 
                                  "Hint 5: For over 300 years, pirates and privateers attacked and robbed treasure from merchant ships traveling in the area!"], 

    "Everglades National Park":["The answer is Everglades National Park! It was established in 1947 and it is located in Florida!", 
                                  "Hint 1: This park is home to one of the largest wetlands in the world! Visitors can experience 9 distinct habitats!", 
                                  "Hint 2: This park is the only subtropical wilderness in North America and protects endangered species like manatee, American crocodiles, and\
                                    the elusive Florida panther.", 
                                  "Hint 3: The are is composed of the largest contiguous stand of protected mangroves in the Northern Hemisphere!",
                                  "Hint 4: This park is the only place in the world where alligators and crocodiles coexist!", 
                                  "Hint 5: The water in this park provides drinking water for around 7-8 million Floridians!"], 
    
    "Gates of the Arctic National Park and Preserve":["The answer is Gates of the Arctic National Park and Preserve! It was established in 1980 and it is located in northern Alaska!", 
                                  "Hint 1: This park is the northern most National Park and is home to the largest contiguous wilderness in the US!", 
                                  "Hint 2: Snow falls 8-9 months of the year and it averages 45 inches of snow every year at the park!", 
                                  "Hint 3: It is believed that 10,000 years ago, the Inupiaq and Athabascan nomadic tribes were the first to explore this area!",
                                  "Hint 4: This park is known to be the least visited National Park even though it is the second-largest!", 
                                  "Hint 5: This park has no official hiking trails, in fact, there are no trails or roads into the park so you must fly or hike into the park!"], 

    "Glacier National Park":["The answer is Glacier National Park! It was established in 1910 and is located in Montana!", 
                              "Hint 1: This park is also known as the 'American Alps' due to the Swiss Chalet like chain of hotels in the park.", 
                              "Hint 2: The park contains one of the world's most dramatic roadways called the 'Going-to-the-Sun Road'.", 
                              "Hint 3: This park and Waterton Lakes National Park in Alberta Canada were combined to form the world's first International Peace Park!", 
                              "Hint 4: The Rocky Mountain Mountain Goat is the official symbol of this park", 
                              "Hint 5: There are 762 lakes in Glacier National Park, of these, 131 are named."], 

    "Glacier Bay National Park and Preserve":["The answer is Glacier Bay National Park! It was established in 1980 and is located in Southeast Alaska!", 
                             "Hint 1: There are over 1,000 glaciers in this park including the 40-mile-wide Grand Pacific Glacier!", 
                             "Hint 2: The 'Father of the National Parks' John Muir is credited as discovering the park when he visited the area in 1879!", 
                             "Hint 3: Pure glacial ice reflects blue colors of the light spectrum like sapphire, this makes the water in this park actually blue!", 
                             "Hint 4: The Fairweather Range is the highest coastal mountains in the world, they are also one of the least visited mountains at their elevation!", 
                             "Hint 5: This park covers 3,223,384 acres and is approximately four times the size of Rhode Island!"], 

    "Grand Canyon National Park":["The answer is Grand Canyon National Park! It was established in 1919 and is located in Arizona!", 
                             "Hint 1: In 1869, the legendary explorer John Wesley Powell set out to conquer this 'Final American Frontier'!", 
                             "Hint 2: This park has been affiliated with several mysteries and conspiracies including The Great Uncomformity, traces of an ancient Tibetan\
                                or Egyptian civilization underground, and its age ranging from six to seventy million years old!", 
                             "Hint 3: Plenty of fossils from the Precambian Time to the Paleozoic Era have been found throughout the park from top to bottom!", 
                             "Hint 4: River rafting down the Colorado River is huge at this park and the legendary Georgie White was the first woman to row the full length\
                                of the park! She was a true pioneer in the sport and in the park!", 
                             "Hint 5: This park is home to a massive, colorful, and deeply carved canyon that is one of the most iconic and breathtaking natural wonders in the world"], 

    "Grand Teton National Park":["The answer is Grand Teton National Park! It was established in 1929 and is located in northwest Wyoming!", 
                              "Hint 1: The park's centerpiece is a rugged mountain range that stretches approximately 40 miles from north to south. It's the youngest range in\
                                the Rocky Mountains!", 
                              "Hint 2: This park was formed by ancient glaciers and still contains eleven active glaciers, even though their size has diminished over the years.", 
                              "Hint 3: This park features some of the oldest rocks found on the planet.", 
                              "Hint 4: This park is the only National Park in the United States with an airport!", 
                              "Hint 5: Because of John D. Rockefeller, Jr's contributions, the National Park Service established a parkway in his name that connects this park\
                                to Yellowstone National Park!"], 

    "Great Basin National Park":["The answer is Great Basin National Park! It was established in 1986 and is located in eastern Nevada!", 
                             "Hint 1: One of the most notable features of this park is the Lehman Caves which is a series of underground chambers and passageways!", 
                             "Hint 2: This park is also home to Nevada's highest peak, Mount Wheeler!", 
                             "Hint 3: The Fremont Indians were among the first to inhabit this area and left plenty of petroglyphs in the caves of this park.", 
                             "Hint 4: This park was home to the famous Prometheus Tree which was once the oldest tree in the world (estimated 4,700-5,000 years old)!", 
                             "Hint 5: The park is home to at least 10 native Bat species and even a native trout species called the Bonneville Cutthroat."], 
    
    "Great Sand Dunes National Park and Preserve":["The answer is Great Sand Dunes National Park and Preserve! It was established in 1932 and is located in Colorado!", 
                             "Hint 1: The weather at this park can go to the extremes, the sand surfaces peak at 150 degrees Farenheit, and can drop to -20 degrees on a winters night!", 
                             "Hint 2: Some of the popular activites to do at this park is called 'sandboarding' and 'sand sledding!", 
                             "Hint 3: Fulgurites can be found in the park! This is a piece of dark glass left behind when lightning strikes the sand, vaporizes the area,\
                              and melts the surrounding sand!", 
                             "Hint 4: The tallest sand dune in North America can be found here, its called Star Dune.", 
                             "Hint 5: The National Park Service has deemed this park the quietest national park in the US due to the vast amount of sound absorbing sand."], 

    "Great Smoky Mountains National Park":["The answer is Great Smoky Mountains! It was established in 1934 and is located on the border of North Carolina and Tennessee!", 
                             "Hint 1: This park is known as the 'Salamander Capital of the World!", 
                             "Hint 2: During the many Spanish conquests for gold in the Americas, explorer Juan Padro found gold and silver in the vicinity of the park!", 
                             "Hint 3: The 'mother' of this park is Anne Davis, who was the third woman to serve in the Tennessee legislature!", 
                             "Hint 4: This park is America's most popular National Park. In 2021, the park had over 14 million visitors, the next park only had 5 million!", 
                             "Hint 5: Clingmans Dome is the highest point in the park and the highest in Tennessee. It is also the third highest mountain east of the Mississippi river!"], 
    
    "Guadalupe Mountains National Park":["The answer is Guadalupe Mountains National Park! It was established in 1972 and is located in western Texas!", 
                              "Hint 1: The earliest inhabitants of this park were the Mescalero Apaches who used this region as a sanctuary where they could harvest the agave plant!", 
                              "Hint 2: The Buffalo Soldiers were all-black regiments established by congress to halt the indian raids, they also became some of the first\
                                National Park Rangers!", 
                              "Hint 3: The highest point in Texas is in this park. It offers hikers an 8.5 mile round trip with 3,000 feet of elevation gain!", 
                              "Hint 4: My reports of gold have been reported at the park with many believing the park holds the richest gold mines in the western world.", 
                              "Hint 5: The salt flats near the park mountains are remnant of an ancient lake that is believed to have existed about 1.8 million years ago!"], 
    
    "Haleakalā National Park":["The answer is Haleakalā National Park! It was established in 1961 and is located on the Hawaiian island of Maui!", 
                             "Hint 1: This park is named after a massvie volcano that stands at an elevation of 10,023 feet and dominates the landscape!", 
                             "Hint 2: From the ocean floor, the volcano measures 20,704 feet! That's taller than Mount Everest, Mount Mckinley, and Kilamanjaro!", 
                             "Hint 3: This park was also designated an International Biosphere Reserve as it is a learning place for sustainable development.", 
                             "Hint 4: This park plays an important part in the protection of Hawaii's state bird, the Nēnē, and an endangered plant 'ahinaahina' or Silversword.", 
                             "Hint 5: The park contains many hikes including the Pīpīwai Trail where you can walk through vast and beautiful bamboo forests!"], 

    "Hawai'i Volcanoes National Park":["The answer is Hawai'i Volcanoes National Park! It was established in 1916 and is located on the island of Hawaii!", 
                             "Hint 1:  Legendary author Mark Twain spent four months at this park and wrote about his experience staying at the 'Volcano House'.", 
                             "Hint 2: This park is a UNESCO World Heritage Site as it preserves the intimate connection between the natural history of the region and the native culture.", 
                             "Hint 3: The park is easy to explore by car. Travelers can drive past many different craters, lookouts, and petroglyphs!", 
                             "Hint 4: Many lava tubes can be found here, one of which is the Thurston Lava Tube, a 450-foot tunnel east of the caldera!", 
                             "Hint 5: This park is named after its two main attractions, the Kilauea and Mauna Loa volcanoes, two of the largest and most active volcanoes in the world!"], 

    "Hot Springs National Park":["The answer is Hot Springs National Park! It was established in 1921 and is located in Arkansas!", 
                             "Hint 1: At 5,500 acres, this is the smallest national park in the United States!", 
                             "Hint 2: Thomas Jefferson sent William Dunbar and George Hunter to explore this area and they reported back their findings of the 'American Spa'.", 
                             "Hint 3: The incredible ecosystem of this park supports 47 naturally heated springs!", 
                             "Hint 4: This park has a Gangster Museum dedicated to the notorious mafiosos who spent time there including: Al Capone, Frank Castello, Meyer Lansky, and more!", 
                             "Hint 5: Surprisingly, the 4,000 year old spring water in this park is safe to drink due to the high tempertures killing the harmful bacteria!"], 

    "Indiana Dunes National Park":["The answer is Indiana Dunes National Park! It was established in 2019 and is located in northwestern Indiana!", 
                             "Hint 1: Although it was authorized as a 'Lakeshore' by Congress in 1966, it was re-designated as the nations 61st national park in 2019.", 
                             "Hint 2: This park is known as the birthplace for the science of ecology thanks to Henry C. Cowles.", 
                             "Hint 3: This park is fourth in biological diversity among the national parks despite having only 15,000 acres!", 
                             "Hint 4: With over 350 species of birds in the park, it is no surprise that there is an annual 'Birding Festival' held here.", 
                             "Hint 5: The most prominent ecosystem in the park is the beach and dune system, but it also contains marshes, swamps, savanna, woodland, and prairie ecosytems!"], 

    "Isle Royale National Park":["The answer is Isle Royale National Park! It was established in 1940 and is located on an island cluster in Lake Superior in Michigan!", 
                             "Hint 1: This park was known to be a 'Voyageurs Highway'. European-American missionaries, traders, and explorers canoed this area to trade goods!", 
                             "Hint 2: This park is one of the least visited parks due to it only being accessible by boat or seaplane. It is very isolated and full of primitive wilderness.", 
                             "Hint 3: This park is composed of not one, but many islands. In fact, its actually one large island surrounded by over 450 smaller islands!", 
                             "Hint 4: There have been more than 25 shipwrecks at the park. Ten of which have even been listed on the National Register!", 
                             "Hint 5: Another reason this park is one of the least visited is because it is actually closed from November unti mid-April due to weather."], 

    "Joshua Tree National Park":["The answer is Joshua Tree National Park! It was established in 1994 and is located in southern California!", 
                             "Hint 1: This park has a rich history in gold mining. The Desert Queen Mine was excavated and almost 4,000 ounces of gold was extracted!", 
                             "Hint 2: Due to its hot, dry climate, this area was actually considered beneficial to veterans of WW1 who were suffering from the effects of mustard gas.", 
                             "Hint 3: Unlike most mountain ranges in the U.S that run north to south, the mountain ranges in this park run from east to west!", 
                             "Hint 4: America's most famous earthquake fault line, the San Andreas Fault, runs through the southwest portion of this park!", 
                             "Hint 5: The park is named after its distinctive trees with their twisted and gnarled branches!"], 

    "Katmai National Park and Preserve":["The answer is Katmai National Park and Preserve! It was established in 1980 and is located in southern Alaska!", 
                             "Hint 1: The first settlers of this park included the Inuits, the Yupiks, and the Aleuts who were mistreated by early russian settlers over the fur trade.", 
                             "Hint 2: The largest volcanic eruption of the 20th century in 1912 created the parks most iconic landmarks: a stratovolcano with a crater lake, and\
                              the Valley of 10,000 Smokes!", 
                             "Hint 3: Robert Fiske Griggs was the first to explore the valley and document geologic and biological changes caused by the eruption.", 
                             "Hint 4: This park is one of the premier Brown Bear viewing areas in the world. Around 2,200 bears are estimated to inhabit the park!", 
                             "Hint 5: The park was expanded by Jimmy Carter as part of the larges single act of conservation in U.S History!"], 

    "Kenai Fjords National Park":["The answer is Kenai Fjords National Park! It was established in 1980 and is located in Alaska!", 
                             "Hint 1: Legendary English explorer Capatain James Cook was one of the first Europeans to see this area. He explored what is now known as 'Cook Inlet'\
                              in 1778.", 
                             "Hint 2: Approximately 51 percent of the park is covered with ice! The longest glacier in the park is Bear Glacier!", 
                             "Hint 3: The park is home to the Harding Icefield named after former President Warren G. Harding and it is the largest icefield in the United States!", 
                             "Hint 4: In 1989, the Exxon Valdez Oil Spill occurred in the once crystal-clean waters of the park killing hundreds of thousands of animals. It still\
                              affects the park today.", 
                             "Hint 5: This park is one of the only areas where visitors can kayak, paddleboard, and cautiously explore building-size icebergs in Bear Glacier Lagoon!"], 

    "Kings Canyon National Park":["The answer is Kings Canyon National Park! It was established in 1940 and is located on an island cluster in California's Sierra Nevada Mountains!", 
                             "Hint 1: This park is home to the largest remaining grove of sequoia trees in the world!", 
                             "Hint 2: The park is composed of two distict areas: Cedar Grove, and Grant Grove which is home to the 'General Giant tree' also known as 'The Nation's\
                              Christmas Tree'!", 
                             "Hint 3: This park was first made popular by the 'Father of the National Parks', John Muir! ", 
                             "Hint 4: Over 95 percent of this park is considered wilderness and is protected by the Wilderness Act signed by President Lyndon B. Johnson!", 
                             "Hint 5: This park contains the deepest canyon in the U.S, it drops 8,200 feet from high in the Sierra to San Joaquin Valley!"], 

    "Kobuk Valley National Park":["The answer is Kobuk Valley National Park! It was established in 1980 and is located in the Arctic Region of Alaska!", 
                             "Hint 1: At approximately 1.8 million acres, this is one of the largest national parks in the United States!", 
                             "Hint 2: This park is home to the largest active, high-altitude, dune field on Earth! They are believed to be a relic of the Ice Age!", 
                             "Hint 3: This park is a part of the Western Arctic Caribou Herd Migration that happens twice a year.", 
                             "Hint 4: An area called 'The Onion Portage' is known for the wild onions that grow along the river banks and abundance of animals.", 
                             "Hint 5: This is one of only two national parks that are north of the Arctic Circle!"], 

    "Lake Clark National Park and Preserve":["The answer is Lake Clark National Park! It was established in 1980 and is located in southwest Alaska!", 
                             "Hint 1: This park is considered an 'undiscovered jewel' and is one of the nations most remote national park units!", 
                             "Hint 2: Some of the earliest settlers of this area were the Athabascan people who were a Native American group who lived in subarctic regions.", 
                             "Hint 3: The highest point in the park is an active stratovolcano called Mount Redoubt!", 
                             "Hint 4: A wildlife photographer named Dick Proenneke made films and journals about his life living as a 'Survivor Man' in the wilderness alone!", 
                             "Hint 5: The park is named after a 50 mile long lake which is one of 3 lakes in the park that are designated as National Wild Rivers."], 

    "Lassen Volcanic National Park":["The answer is Lassen Volcanic National Park! It was established in 1916 and is located in northern California!", 
                             "Hint 1: Legendary explorer Jedediah Strong Smith was the first white man to traverse Utah, Nevada, and pars of California including this area.", 
                             "Hint 2: In 1915, an explosive volcanic eruption occurred at one of the vocanoes in the park and was seen as many as 150 miles away!", 
                             "Hint 3: The parks main road is 29 miles that takes your past many of the landmarks and it is the highest road in the Cascade Mountains!", 
                             "Hint 4: the 'Painted Dunes' can be found in the park. They are sand dunes near the mountains that contain many different minerals that\
                              leave a beautiful array of colors!", 
                             "Hint 5: All four types of vocanoes (shield, plug dome, cinder cone, and composite) found in the world can be found in this park!"], 

    "Mammoth Cave National Park":["The answer is Mammoth Cave National Park! It was established in 1941 and is located in Kentucky!", 
                             "Hint 1: This park is home to the world's longest known cave system with more than 400 miles of underground passageways!", 
                             "Hint 2: Native American tribes lived and inhabited the cave system miles back into the system unlike other caves where evidence of people are\
                              found only near the entrances!", 
                             "Hint 3: This park played a huge role in The War of 1812 due to its source of nitrates that were used to make gunpowder.", 
                             "Hint 4: In 1838, Stephen Bishop was a 17 year old slave that was sent to map out the caves. He made a complete map from memory and served as a tour guide.", 
                             "Hint 5: The first blind animal known in the world was a cave blindfish discovered in 1888 in a river that goes through the cave system!"], 

    "Mesa Verde National Park":["The answer is Mesa Verde National Park! It was established in 1906 and is located in southwest Colorado!", 
                             "Hint 1: This park is known for its well preserved Ancestral Puebloan cliff dwellings and is home to over 4,700 known archeological sites!!", 
                             "Hint 2: This park was protected from pillagers and overzealous tourists by a group of 10 Colorado women who fought to make the area a national park!", 
                             "Hint 3: This is the only park in the country where four states actually come together. Its known as the 'Four Corners'.", 
                             "Hint 4: This park is America's 7th oldest national park, its first cultural park, and the world's 100th International Dark Sky Park!", 
                             "Hint 5: One of the most famous structures in the park is called the 'Cliff Palace'. It contains 150 rooms, and had a population of around 100 people!"], 
    
    "Mount Rainier National Park":["The answer is Mount Rainier National Park! It was established in 1899 and is located in Washington State!", 
                             "Hint 1: This park is home to the tallest mountain in the state of Washington, its also the most heavily glaciated peak in the contiguous U.S!", 
                             "Hint 2: British Royal Navy Captain George Vancouver named this park after his friends, along with his other friends Baker and Hood.", 
                             "Hint 3: The primary feature of the park is a stratovolcano that thousands attempt to summit each year! It is one of the 16 'Decade' Volcanoes!", 
                             "Hint 4: This park features over 250 miles of hiking trails and 25 glaciers for park goers to experience!", 
                             "Hint 5: The park was also famous for being the honeymoon site of the legendary Walt Disney!"], 

    "New River Gorge National Park and Preserve":["The answer is New River Gorge National Park and Preserve! It was established in 1978 and is located in West Virginia!", 
                             "Hint 1: The river in this park is only one of a few rivers in the world that flow from South to North!", 
                             "Hint 2: Within the park there are over 1,400 established rock climbs, and its become on of the most popular climbing areas in the country!", 
                             "Hint 3: The park includes the fifth longest single-span arch bridge in the world! Its 876 feet tall, and spans over 3,000 feet in length!", 
                             "Hint 4: On the third Saturday of October, the park hosts 'Bridge Day' which is West Virginia's largest one-day festival and the largest\
                              extreme sports event in the world!", 
                             "Hint 5: The main feature of the park is a deep canyon carved out by one of the oldest rivers in the world geologically!"], 
    
    "North Cascades National Park":["The answer is North Cascades National Park! It was established in 1968 and is located in northern Washington State!", 
                             "Hint 1: David Brower aka the 'Father of the modern environmental movement' advocated and successfully led to the establishments of this park and\
                              several other famous parks in the U.S.", 
                             "Hint 2: Goode Mountin is the tallest mountain in the park and is one of ten non-volcanic peaks in Washington State above 9,000!", 
                             "Hint 3: This park is a shelter for three endangered species including: the gray wolf, grizzly bear, and Canada lynx.", 
                             "Hint 4: This park has more than 300 glaciers! That equals one third of the glaciers found in the lower 48 states!", 
                             "Hint 5: Because the park is renowned for its world class climbing terrain, it has been called the 'Alps of North America'."], 

    "Olympic National Park":["The answer is Olympic National Park! It was established in 1938 and is located in Washington State!", 
                             "Hint 1: This park includes three distinct ecosystems: subalpine forests, temperate rainforests, and rocky Pacific coastlines!", 
                             "Hint 2: When Franklin Roosevelt visited the park in 1937, he was met by 3,000 schoolchildren with banners asking for him to make the area a\
                              national park!", 
                             "Hint 3: This park is considered to have one of the most diverse wilderness areas in the U.S! It protects some of the most threatened and\
                              endangered species in the world!", 
                             "Hint 4: The Hoh rainforest recieves over 12 feet of rain per year! It's also one of the few remaining temperate rain forests in the U.S!", 
                             "Hint 5: In 1788, British sea captain John Meares named the park after a famous mountain in Greek Mythology after seeing the majestic peak!"], 
    
    "Petrified Forest National Park":["The answer is Petrified Forest National Park! It was established in 1899 and is located in Washington State!", 
                             "Hint 1: The Spanish were the earliest non-native explorers of this area and they named it 'The Painted Desert'", 
                             "Hint 2: This park features one of the largest fossilized wood forests in the world. The trees turned to stone and are filled with gems and minerals!", 
                             "Hint 3: Due to the easily accessble gems the forest provides, the area was turned into a national park to prevent theft!", 
                             "Hint 4: The park contains thousands of archaeological sites. Newspaper Rock contains more than 650 petroglyphs on its own!", 
                             "Hint 5: This is the only national park that actually closes every evening! There are no campgrounds here in order to prevent theft!"], 
    
    "Pinnacles National Park":["The answer is Pinnacles National Park! It was established in 2013 and is located central California!", 
                             "Hint 1: This park has a unique landscape of towering rock spires, deep canyons, and lush vegetation due to an ancient volcanic eruption!", 
                             "Hint 2: This park is a great example of tectonic plate movement and sits on the San Andreas Fault line!", 
                             "Hint 3: The park is home to the California Condor Recovery Program and manages a release site for captive-bred California condors.", 
                             "Hint 4: This park is the newest national park in the U.S after President Obama established it in 2013!", 
                             "Hint 5: Even though the park is only 42 square miles of land, more than 400 bee species live there! This makes it the largest concentration of bee\
                              species in the world!"], 

    "Redwood National and State Parks":["The answer is Redwood National and State Parks! It was established in 1968 and is located in northern California!", 
                             "Hint 1: The Native American tribes that resided in this area believed that the trees were living beings who served as guardians of their sacred place.", 
                             "Hint 2: There is a famous story of a cockroach that got stuck under the needle of a Chinese sailors compass and it led to their accidental arrival\
                              at this park!", 
                             "Hint 3: The trees in this park have the ability to create their own rain! They draw in moisture from the fog high in the air and it condenses\
                              into droplets!", 
                             "Hint 4: This park is home to the Hyperion tree that is the world's tallest known living tree at 380.3 feet tall!", 
                             "Hint 5: Star Wars: Return of the Jedi, Jurassic Park: The Lost World, and E.T.: The Extra Terrestrial were all filmed here for its otherworldy landscape."], 
    
    "Rocky Mountain National Park":["The answer is Rocky Mountain Forest National Park! It was established in 1915 and is located in northern Colorado!", 
                             "Hint 1: With over 4.5 million visitors every year, this is one of the most visited parks in the country!", 
                             "Hint 2: The highest point in the park is named after Stephen Harriman Long. He led an expedition in 1820 to explore the Front Range of the famous mountains!", 
                             "Hint 3: The park has over sixty mountain peaks, all of which are over 12,000 feet!", 
                             "Hint 4: The Trail Ridge Road is the highest continuous paved highway in the nation at 12,000 feet ", 
                             "Hint 5: Out of the parks 265,770 acres, nearly 95 percent of them are designated as wilderness in order to protect them from harmful human impact!"], 
    
    "Saguaro National Park":["The answer is Saguaro National Park! It was established in 1994 and is located in southern Arizona!", 
                             "Hint 1: This park contains 523 known archeological sites spanning more than 8,000 years of human occupation!", 
                             "Hint 2: The park is actually 2 parks in 1. The Western Tuscon Mountain District, and the Eastern Rincon Mountain District.", 
                             "Hint 3: The Madrean Sky Islands are home to 6,000 species of plants, second in biodiversity only to the Amazon Rainforest!", 
                             "Hint 4: The park is also known for its Gila Monsters! These are one of the only venomous lizards in the entire world!", 
                             "Hint 5: This park is named after a species of cactus that commonly reaches up to 40 feet in height!"], 

    "Sequoia National Park":["The answer is Sequoia National Park! It was established in 1962 and is located in northeastern Arizona!", 
                             "Hint 1: This park contains the highest point in the contiguous U.S, Mount Whitney at 14,505 feet above sea level!", 
                             "Hint 2: Thanks to George Stewart fighting for the protection of the area in 1890, this area became only the second established national park!", 
                             "Hint 3: Colonel Charles Young became the first African American superintendent of a national park at this park!", 
                             "Hint 4: This park was the first park created to protect a living organism.", 
                             "Hint 5: This park is home to the largest tree on Earth! The General Sherman Tree stands at 275 feet tall, and over 36 feet in diameter at the base!"], 
    
    "Shenandoah National Park":["The answer is Shenandoah National Park! It was established in 1935 and is located in Virginia!", 
                             "Hint 1: This is the first national park to be formed entirely from land that private owners have lived on and used!", 
                             "Hint 2: This is a park full of prehistoric creature remains. hundreds of mammoth and mastodon fossils have been found in the park!", 
                             "Hint 3: The Civilian Conservation Corps began at park and continued nationwide as they planted more than 3 billion trees, constructed trails, and\
                              shelters in more than 800 parks nationwide!", 
                             "Hint 4: Rocks that are believed to be older than 1 Billion years old can be found at this park. They are believed to be a part of Pangea!", 
                             "Hint 5: This park is comprised primarily of the Blue Ridge Mountains that get their name from the color they display when seen from a distance!"], 
    
    "Theodore Roosevelt National Park":["The answer is Theodore Roosevelt National Park! It was established in 1978 and is located in North Dakota!", 
                             "Hint 1: This park is divided into three units, the North Unit, the South Unit, and the Elkhorn Ranch Unit, each offering unique experiences!", 
                             "Hint 2: The park hosts thousands of Prairie Dogs! They are the parks most popular inhabitants.", 
                             "Hint 3: The Elkhorn ranch is still around today and is known to be the 'home ranch' of a famous former president!", 
                             "Hint 4: This is one of the only parks to feature wild horses! They are protected by the Wild Free-Roaming Horses and Burros Act of 1971.", 
                             "Hint 5: This is the only park to be named after a single person!"], 

    "Virgin Islands National Park":["The answer is Virgin Islands National Park! It was established in 1956 and is located in the U.S. Virgin Islands!", 
                             "Hint 1: This park was established in 1956 as a gift from Laurance Rockefeller.", 
                             "Hint 2: This park has an underwater snorkeling trail in Trunk Bay! You can read underwater signs to learn about the animals and coral!", 
                             "Hint 3: Fourty percent of the park is actually underwater!", 
                             "Hint 4: This park is also home to a few endangered turtle species such as the green turtle, leatherback turtle, and the hawksbill turtle.", 
                             "Hint 5: This park has many historical sites and plantations that teaches visitors about its history in the global sugar market."], 
    
    "Voyageurs National Park":["The answer is Voyageurs National Park! It was established in 1975 and is located in Minnesota!", 
                             "Hint 1: This park is known for its system of interconnected waterways and its network of hiking trails.", 
                             "Hint 2: The park is named after the French-Canadian fur traders who traveled through the area in the 18th and 19th centuries.", 
                             "Hint 3: Sigurd Olson was intstumental in the establshment of the park and also gave the park its name!", 
                             "Hint 4: This park is a water-based park. There are 4 large lakes, 84,000 acres of water, 655 miles of undeveloped shoreline, and more than 500 islands!", 
                             "Hint 5: This is a great park to see the Northern Lights!"], 
    
    "White Sands National Park":["The answer is White Sands National Park! It was established in 2019 and is located in New Mexico!", 
                             "Hint 1: The landscape of the park is made up of a vast expanse of gyspum deposits that were formed when an ancient sea evaporated!", 
                             "Hint 2: Large mounds that contain the remains of charcoal and ash were left behind by the prehistoric people that lived here are called Hearth Mounds.", 
                             "Hint 3: This park was part of a 'Salt War' between ranchers, farmers, and Native Americans that used a salt lake in the park for food preservation.", 
                             "Hint 4: This park has the largest gypsum dune field in the world! The sand also does not absorb heat from the sun making it pleasent to walk on!", 
                             "Hint 5: This park sits on one of the largest military bases in the United States. It is a missile range that the government uses year round!"], 

    "Wind Cave National Park":["The answer is Wind Cave National Park! It was established in 1903 and is located in South Dakota!", 
                             "Hint 1: The Lakota Indians were instrumental in early efforts to protect the area, they considered the area and underground system sacred.", 
                             "Hint 2: The park features an incredible 'complex maze' type cave that is one of the longest in the world at over 140 miles!", 
                             "Hint 3: The parks famous cave is the 6th longest mapped cave in the world because of its extensive network of passages and chambers!", 
                             "Hint 4: This park is also the site of a hunting practice called 'Buffalo Jumping' where the Native Americans would lure the bison to stamped over a cliff.", 
                             "Hint 5: The cave is filled with a natural formation called 'boxwork', a calcite deposit that forms honeycomb patters on the walls and ceilings."], 
    
    "Wrangell-St. Elias National Park and Preserve":["The answer is Wrangell-St. Elias National Park and Preserve! It was established in 1980 and is located in central Alaska!", 
                             "Hint 1: This is the largest national park in the country, covering over 13.2 million acres!", 
                             "Hint 2: The park contains several large glaciers including the Bering Glacier which is the largest glacier in the world!", 
                             "Hint 3: The park is also home to the second highest peak in North America at about 18,008 feet of elevation, it is also the parks namesake!", 
                             "Hint 4: This park is home to some of the worlds largest volcanoes including one of the largest active volcanoes in the world!", 
                             "Hint 5: The park was a popular site in the Alaskan Gold Rush in the late 19th and early 20th centuries."], 
    
    "Yellowstone National Park":["The answer is Yellowstone National Park! It was established in 1872 and is located in Wyoming and spreads to parts of Idaho and Montana!", 
                             "Hint 1: This park has the unique distinction of being America's oldest national park!", 
                             "Hint 2: This park is one of the world's largest active volcanic systems! It is believed to be a terrifying super-volcano!", 
                             "Hint 3: Since there was no National Park Service to provide rangers at the time, the parks first rangers were the U.S. Army!", 
                             "Hint 4: This park features the largest concentration of wildlife in the continental U.S.!", 
                             "Hint 5: The park is the site of America's greatest concentration of geysers and hot springs! it also features almost 300 waterfalls!"], 

    "Yosemite National Park":["The answer is Yosemite National Park! It was established in 1890 and is located in California's Sierra Nevada Mountains!", 
                             "Hint 1: Legendary writer and conservationalist John Muir called this park the 'grandest of all temples of nature'!", 
                             "Hint 2: Even though it's technically not the first national park, this park shaped the idea of how national parks would continue and be managed.", 
                             "Hint 3: This park is known for its waterfalls and its giant sequoia trees like those found in its Mariposa Grove!", 
                             "Hint 4: The park was formed by glaciers that can still be seen today such as the Lyell Glacier, and Maclure Glacier.!", 
                             "Hint 5: This park is also home to some of the best rock climbing in the world! Famous climbers like Tommy Caldwell have established hundreds\
                               of routes here!"], 
    
    "Zion National Park":["The answer is Zion National Park! It was established in 1919 and is located in Utah!", 
                             "Hint 1: This park is known for its towering sandstone cliffs, deep canyons, and unique rock formations like the 'Checkerboard Mesa'!", 
                             "Hint 2: Some of the first European settelers to inhabit the area were the Mormon pioneers.", 
                             "Hint 3: The Kolob Arch located in the park is the second largest arch rock formations in the world spanning 287 feet!", 
                             "Hint 4: The park features a 25 mile highway that connects it to 2 other famous national parks! There is also a tunnel that goes through a\
                               massive rock formation!", 
                             "Hint 5: This is the home of one of the most famous and dangerous hikes in the world: Angels Landing!"]
    }

daily_park = random.choice(list(parks_list.keys()))

def user_guess():
    counter = 1
    hint_counter = 1
    while counter < 6:
        print(parks_list[daily_park][hint_counter])
        guess = input(f"Guess #{counter}: ")

        if guess.upper() == "QUIT":
           break
        
        elif not 'NATIONAL PARK' in guess.upper():
            print("Please type the full name of the National Park!")
            continue

        if guess.upper() == daily_park.upper():
            print(f"You got it! Today's National Park is {parks_list[daily_park][0]}")
            return
        else:
            counter += 1
            hint_counter += 1
                
    print(f"Sorry {parks_list[daily_park][0]}")
   
def write():
  play_button.config(text=user_guess())   
 
root = tk.Tk()
root.title('Parkle')
root.geometry("800x600")
root.resizable(True, True)

root.columnconfigure(0, weight=2)

font.nametofont("TkDefaultFont").configure(size=13)

main = ttk.Frame(root, padding=(30, 15))
main.grid()
game_frame = ttk.Frame(root, padding=(20, 5))
game_frame.grid()

image = Image.open("/Users/jarmstrong/Desktop/Python Stuff/VSPYTHON/tkinterclass/Daco_1637362.png").resize((100,100))
photo = ImageTk.PhotoImage(image)
natlabel = ttk.Label(main, text="Welcome to Parkle!", image=photo, padding=5, compound="top", font=("Comic Sans MS", 20))
intro1 = ttk.Label(main, text="There are 63 disignated 'National Parks' in America")
intro2 = ttk.Label(main, text="Your job is to guess which one it is based on these 5 hints!")
play_button = ttk.Button(game_frame, text="Play", command=write)
label = ttk.Label(game_frame, text='')



natlabel.grid()
intro1.grid()
intro2.grid()
label.grid(column=1, row=3, sticky="ew", columnspan=3)
play_button.grid(column=0, row=2, sticky="ew", columnspan=3)

root.mainloop()
# user_guessas()