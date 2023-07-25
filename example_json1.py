import random
import json

electronics=['AC','Refrigerator','TV','Computer','Mobile','Laptop','Keyboard',
             'Fan','LCD','Bulb','Earphone','Headphone','Memory Card','Tabelts',
             'DSLR','Camera','Powerbanks','SmartWatches','Printers','Cooler',
             'Monitors','Desktop PCs','Speakers','Soundbars','DTH SetUp box',
             'Pendrives','Charger','Washing Machine','Water Purifiers','Lens',
             'Geysers','Table Fans','Immersion Rod','Iron','Vaccum Cleaners',
             'Inverter','Sewing Machine','Air Purifiers','Stabilizer','Modem',
             'Mouse','Phone','Routers','Electric Wires','Electric Kettle',
             'Switch','Heater','Toaster','Joystick','Scanner','Xbox','Drone',
             'Remote','Harddrive','USB Cable','Spy Camera','Microwaves','RAM',
             'UPS','Powerbank','Adapter','Socket','Induction','Juicer','Mixer',
             'Blender','Tablet','Processor','Motherboard','HDMI','Microphone',
             'TV Tuner','Graphic Card','DVD RW']
elec_comp=['LG','Whirlpool','Hitachi','Samsung','Lloyd','Panasonic','Micromaxc',
           'Nokia','Bajaj','Usha','Crompton','Havells','Anchor','HP','HCL',
           'Sony','Dell','Acer','Asus']
grocery=['Atta','Chana Dal','Ghee','Jaggery','Masalas','Oils','Rice','Salt',
         'Sugar','Detergent','Dry Fruits','Toothbrush','Toothpaste','Dishwash',
         'Household Cleaner','Handwash','Tissues','Freshners','Cereal','Methi',
         'Cumins','Ketchup','Soyachunks','Oats','Honey','Insect killer',
         'Peanut Butter','Pickle','Mosquito Vaporiser','Mong Dal','Vinegar',
         'Room Freshner','Milk','Butter','Paneer','Corn Flakes','Kabuli Chana',
         'Rajma','Urad Dal','Masoor Dal','Arhar Dal','Pepper','Turmeric',
         'Tamarind','Ajwain','Hing','Garlic Paste','Red Chilli','Saunf','Peas',
         'Black Salt','White Sesame','Black Sesame','Coriander Seed','Cloves',
         'Cardamom','Mustard seed','Olive Oil','Toothpeek','Ear Buds']
grcy_comp=['Ashirvaad','Tata','MDH','Everest']
furniture=['Sofa','Chair','Beds','Mattress','Wardrobes','Dressing Tables',
           'Recliners','Study Tables','Sofa Beds','Study Chairs','Bench',
           'Bean Bags','TV Units','Drawers','Storage Cabinet','Shoe Racks',
           'Side Table','Bookshelve','Wallshelve','Dining Set','Bar Cabinet',
           'Bar Stool','Kitchen Cabinet','Trolley','Center Tables','Rack']
fur_comp=['Godrej','Kosmo']
food=['Burger','Samosa','Biscuit','Chips','Namkeen','Sandwitch','Pasta','Idli',
      'Chhole Kulchhe','Biryani','Rolls','Pastry','Cakes','Rasgulla','Chowmin',
      'Chiken Roll','Kadhai Chiken','Pizza','Kulfi','Momo','Tikka','Soanpapdi',
      'Ice Cream','Cupcake','French Fries','Gulabjamun','Ladoo','Dosa','Maggi',
      'Taco','Dosa','Puri Sabzi','Kofta','Jalebi','Paneer Tikka','Litti Chokha'
      ]
fod_comp=['KFC','Pizza','Britania','Parle','Haldiram','Zomato','Swiggy']
beauty=['Deodorant','Face Wash','Face Masks','Facial Kit','Hair Colour','Soap',
        'Body Mist','Foundatoin','Eyeliner','Eyeshadow','Scrub','Kajal & Kohl',
        'Mascara','False Eyelashes','Eye Concealer','Lipstick','Makeup Brushes',
        'Sunscreen','Lotion','Nail Polish','Gel','Nail Remover','Face Powder',
        'CC Cream','Rosewater','Blusher','Shaving Foam','Moisturising','Comb',
        'Fairness Cream','Waxing Cream','Acne Cream','Conditioner','Perfume',
        'Anti-ageing Cream','Revitalizing Cream','Body Cream','Honey Gel',
        "Men's Cream",'Anti-wrinkle Cream','Pimple Facewash','Day Cream','Talc',
        'Night Cream','Cleanser','Toner','Hair Spray','Hair Cream','Razor',
        'Hair Wax','Straightner','Hair Color','Hair Serum','Hair Dryer','Serum',
        'False Eyelashes','Eyebrow Pencil','Trimmer','Blade','Nail Cutter',
        'Hair Brush','Hair Styler','Curler','Callus Remover','Facial Kit',
        'Massager','Hair Oils','Lip Balm','Epilator','Herbal Cream','Shampoo']
buty_comp=['Lakme','Garnier']
health=['Supplements','Whey Protein','Mass Gainer','Protein Bar','Vaporizer',
        'Health Drinks','Inhaler','Medicine','Thermometer','Antiseptic Band',
        'Sugarfree','Ointment','Painkiller','Mask','Nebulizer','Chyawanprash',
        'Wipes','Nicotex','Antiseptic Liquid','Pain Balm','First Aid','Cotton',
        'ORS','Eye Drop']
hlth_comp=['Abbott','Dabur','Himmalya','Patanjali','Lupin','Cipla','Mankind']
sports=['Sports Shoe','Cycle','Skates','Knee Pads','Elbow Pad','Stump','Net',
        'Skateboard','Racquets','Ball','Helmet','Pad','Protective Gloves',
        'Football','Sipper','Badminton','Shuttlecocks','Nets','String','Bat',
        'Shin Guard','Thigh Guard','Abdominal Guard','Batting Pads','Stand',
        'Tent','Sleeping Bag','Basketball','Backboard','Pump','Bells','Pedal',
        'Lock','Boxing Gloves','Arm Guard','Punching Bag']
sprt_comp=['Cosco','Addidas','Reebok','Nike','Puma']
fitness=['Yoga Mat','Treadmill','Dumbbell','Skipping Ropes','Hand Grip','Bars',
         'Lifting Bar','Ab Roller','Gym Ball','Knee Support','Tummy Trimmer',
         'Neck Belt','Kettlebell','Exercise Bike','Gym Bench','Flexband',
         'Balance Board','Gym Plate']
fit_comp=['Cosco','Nortus','Paramount','Steel Flex']
beverage=['Tea','Coffee','Soft Drink','Soup','Nimbupani','Juice','Lassi',
          'Whisky','Milk Shakes','Banana Shakes','Beer','Energy Drink','Wine',
          'Vodka','Mojito','Smoothie','Green Tea','Cocktail','Black Coffee']
bev_comp=['Nescafe','Pepsi','Knor','Coke','Kingfisher']
kitchen=['Pan','Tawa','Juicer','Mixer Grinder','Gas Stove','Caserole','Cooker',
         'Knife','Bottle','Cutlery','Lunch Box','Chopping Board','Gas Lighter',
         'Whisk','Strainer Filter','Rolling','Baking Tray','Kitchen Scissors',
         'Moulds','Utencil','Dinner Set','Gaslighter','Flask','Jars','Wok',
         'Container','Lids','Frying Pan','Spoon','Funnel','Slicer','Bowl',
         'Forks','Nutcracker','Skimmer','Sieve','Oil Pourer','Opener','Tray',
         'Scoop']
kchn_comp=['Prestige','Hawkins','Bajaj']
fashion=['Men Clothing','Women Clothing','Kids Clothing','Handbag','Jewellery',
         'Clutch','Shoe','Wallet','Watches','Belts','Tie','Caps & Hats','Stud',
         'Socks','Handkerchiefs','Cufflinks','Earrings','Bracelets','Rings',
         'Pendant','Chain','Eyewear','Gemstones','Bagpack','Luggage','Gym Bag',
         'Footwear','T-Shirt','Leggings','Short','Sling Bag','Trouser','Jeans',
         'Saree','Kurta','Salwar Suits','Dupattas','Scarves & Stoles','Jacket',
         'Sweaters','Sweatshirts','Swimwear','Bangles','Necklaces','Earcuff']
fshn_comp=['Sparky','PeterEngland','Killer','Reebok','Lee','Wrangler','Turtle']
stationary=['Crayon','Pencil','Book','Pen','Marker','Notebook','Paint Brushes',
            'Canvas','Highlighter','Planner','Calculator','Tape','Glue','Pin',
            'Stapler','Scissor','Paper','Dairy','Duster','File','Cardholder',
            'School Bag','Eraser','Sharpener','Glitter','Ink','Thread','Board',
            'Charms','Clay','Drawing Pads','Foam','Chart Paper','Pen Holder',
            'Scale','Compass','Protector','Scrapbook']
stn_comp=['Apsara','Classmate','Camel','Natraaj']
pet=["Pet's Clothing","Pet's Bed",'Serving Bowl','Pedigree','Coat Cleanser',
     'Cages','Starter Kit','Decorative Stone','Pump&Filter','Aquarium',
     "Bird's Feeder"]



products={'Electronics':
                    {68483:
                        {'Product Name': 'Computer',
                         'Company': 'Microsoft',
                         'MRP': 38000,
                         'Discount': 26,
                         'Rating': 5,
                         'Price': 28120
                          }
                       },
              'Grocery':
                  {1579:
                      {'Product Name': 'Salt',
                       'Company': 'Tata',
                       'MRP': 19,
                       'Discount': 0,
                       'Rating': 5,
                       'Price': 19
                        }
                     },
               'Sports':
                   {8907: 
                       {'Product Name': 'Pad',
                        'Company': 'Puma',
                        'MRP': 700,
                        'Discount': 11,
                        'Rating': 4,
                        'Price': 623
                        }
                      },
                 'Food':
                     {8436: 
                         {'Product Name': 'Sandwitch',
                          'Company': 'Parle',
                          'MRP': 71,
                          'Discount': 0,
                          'Rating': 4,
                          'Price': 71
                          },
                        },
             'Beverage':
                  {8589: 
                      {'Product Name': 'Wine',
                       'Company': 'Coke',
                       'MRP': 33,
                       'Discount': 0,
                       'Rating': 4,
                       'Price': 33
                       }
                    },
            'Furniture':
                {7169: 
                    {'Product Name': 'Kitchen Cabinet',
                     'Company': 'Godrej',
                     'MRP': 13700,
                     'Discount': 27,
                     'Rating': 5,
                     'Price': 10001
                     }
                  },
               'Beauty':
                   {2165: 
                       {'Product Name': 'Massager',
                        'Company': 'Lakme',
                        'MRP': 44780,
                        'Discount': 25,
                        'Rating': 5,
                        'Price': '  '
                        }
                      },
               'Health':
                   {7877: 
                       {'Product Name': 'Chyawanprash',
                        'Company': 'Dabur',
                        'MRP': 420,
                        'Discount': 5,
                        'Rating': 5,
                        'Price': 399
                        }
                      },
              'Fitness':
                  {62905: 
                      {'Product Name': 'Exercise Bike',
                       'Company': 'Cosco',
                       'MRP': 44800,
                       'Discount': 30,
                       'Rating': 5,
                       'Price': 31360
                       }
                     },
              'Fashion':
                  {9990: 
                      {'Product Name': 'Bangles',
                       'Company': 'Sparky',
                       'MRP': 1000,
                       'Discount': 22,
                       'Rating': 5,
                       'Price': 780
                       }
                     },
           'Stationary':
               {4232: 
                   {'Product Name': 'File',
                    'Company': 'Natraaj',
                    'MRP': 18,
                    'Discount': 0,
                    'Rating': 3,
                    'Price': 18
                    }
                  },
                  'Pet':{},
              'Kitchen':{}
             }


products1=products['Electronics']
for k in range(300):
    data={random.randint(10000,100000):{
                 'Product Name':random.choice(electronics),
                 'Company':random.choice(elec_comp),
                 'MRP':random.randint(10000,50000),
                 'Discount':random.randint(20,30),
                 'Rating':random.randint(3,5),
                 'Price':'  '
                 }
            }
products1.update(data)

def Groupitems(products,category):
        filtered_products={}
        product=products[category]
        for key,val in product.items():
            filtered_products[key]=val
        return filtered_products

filtered_products=Groupitems(products,'Electronics')

f=open('Product_Category1.json','w')
json.dump(products,f,indent=2)
f.close()
