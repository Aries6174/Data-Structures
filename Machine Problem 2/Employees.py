# IMPORT THIS FILE TO BE USED IN MACHINE PROBLEM 2 NO. 3

# Employee Object Class
class Employee:
    def __init__(self,fName="Juan", lName="Dela Cruz", addr="Iloilo City", years=1, desc="N/A", joblist=[]):
        self.fName = fName
        self.lName = lName
        self.addr = addr
        self.years = years
        self.desc = desc
        self.joblist = joblist

    def getFullName(self):
        if "South Korea" in self.addr or "China" in self.addr:
            return (self.lName + " " + self.fName)

        elif self.fName and self.lName:
            return (self.fName + " " + self.lName)

        else:
            raise Exception("No First or Last Name")

    def getFName(self):
        if self.fName:
            return self.fName
        else:
            raise Exception("No First Name")

    def getLName(self):
        if self.lName:
            return self.lName
        else:
            raise Exception("No Last Name")

    def getAddress(self):
        if self.addr:
            return self.addr
        else:
            raise Exception("No Known Address")
        
    def getYears(self):
        if self.years:
            return str(self.years)
        else:
            raise Exception("No Known Number Of Years in Industry")

    def getDesc(self):
        if self.desc:
            return self.desc
        else:
            raise Exception("No Description Available")
        
    def getJobs(self):
        if self.joblist:
            jobs = ""
            count = 1
            for job in self.joblist:
                jobs += "\nJob " + str(count) + ": " + job
                count += 1
            return jobs
        else:
            raise Exception("No Jobs Assigned")


# List Of Employees
# Note: Please use this list accordingly. You are not allowed to modify this list.
# Note: There should be a total of 100 employees.

# Jobs Available
# 1. Singer
# 2. Rapper
# 3. Belter
# 4. Songwriter
# 5. Actor
# 6. Dancer
# 7. Producer
# 8. Band Member

employee_list = [
    Employee("Taylor Alison", "Swift", "Pennsylvania, USA", 13, "Thirteen Starbucks Lovers",["Singer","Songwriter","Actor","Producer"]),
    Employee("Ariana", "Grande-Butera", "Florida, USA", 12, "High Pitched and High-Heeled",["Singer","Belter","Songwriter","Actor","Dancer"]),
    Employee("Adele Laurie", "Adkins", "London, UK", 10, "Hello, is it me you're looking for?",["Singer","Belter","Songwriter","Producer"]),
    Employee("Dua", "Lipa", "London, UK", 4, "One-and-Only Dula Peep",["Singer","Songwriter","Dancer"]),
    Employee("Katherine Elizabeth", "Hudson", "California, USA", 6, "You and IIIIIIIIIII ayayayay!!!",["Singer","Belter","Songwriter","Dancer","Producer"]),
    Employee("Stefani Joanne Angelina", "Germanotta", "New York, USA", 15, "Meat Dress Aesthetics",["Singer","Belter","Songwriter","Actor","Dancer"]),
    Employee("Belcalis", "Almanzar", "New York, USA", 1, "Eeaaawwww!!!",["Rapper","Dancer"]),
    Employee("Robyn Rihanna", "Fenty", "Saint Michael, Barbados", 9, "Thou shall not date Chris Brown",["Singer","Belter","Songwriter","Actor","Dancer"]),
    Employee("Megan Jovon Ruth", "Pete", "Texas, USA", 9, "Stallion >>> Red Horse",["Rapper","Songwriter","Dancer"]),
    Employee("Meghan Elizabeth", "Trainor", "Massachusetts, USA", 12, "Shoobeedoobap Doobeedapdap",["Singer","Belter","Songwriter","Dancer"]),
    Employee("Selena Marie", "Gomez", "Texas, USA", 11, "Are you re-e-ea-dy?",["Singer","Songwriter","Dancer","Actor"]),
    Employee("Miley Ray", "Cyrus", "Tennessee, USA", 14, "Hannah Montana Lookalike",["Singer","Songwriter","Belter","Dancer","Actor"]),
    Employee("Karla Camila", "Cabello-Estrabao", "Cojimar, Cuba", 15, "Bam bam bam bam bam bam",["Singer","Dancer","Belter","Producer","Actor","Band Member"]),
    Employee("Ashley Nicolette", "Frangipane", "New Jersey, USA", 5, "Not so eazy",["Singer","Belter","Songwriter"]),
    Employee("Anne-Marie Rose", "Nicholson", "East Tilbury, UK", 6, "Born before 2002",["Singer","Belter"]),
    Employee("Sia Kate Isobelle", "Furler", "Adelaide, Australia", 8, "Chandelier swinger",["Singer","Belter","Songwriter"]),
    Employee("Victoria Loren", "Kelly", "California, USA", 10, "Underrated AF",["Singer","Belter","Songwriter"]),
    Employee("Onika Tanya", "Maraj", "Saint James, Trinidad and Tobago", 20, "Barbie without the Queue",["Singer","Rapper","Songwriter"]),
    Employee("Demetria Devonne", "Lovato", "New Mexico, USA", 16, "Sorry not sorry for your loss",["Singer","Belter","Songwriter","Actor"]),
    Employee("Rita Sahatciu", "Ora", "Pristina, Kosovo", 17, "That's how do you do?",["Singer","Dancer"]),
    Employee("Cheryl Ann", "Tweedy", "Newcastle upon Tyne, UK", 19, "Tweedy Birdie",["Singer","Dancer"]),
    Employee("Jessica", "Cornish", "London, UK", 11, "Putting price tags on expensive items",["Singer","Belter","Songwriter","Dancer","Producer"]),
    Employee("Alecia Beth", "Moore-Hart", "Pennsylvania, USA", 12, "Let's start the parttyyy",["Singer","Songwriter"]),
    Employee("Kesha Rose", "Sebert", "California, USA", 16, "#REBORN",["Singer","Belter","Songwriter","Dancer"]),
    Employee("Amala Ratna Zandile", "Dlamini", "California, USA", 2, "Snoop Dogg's Evil Counterpart",["Singer","Rapper","Songwriter"]),
    Employee("Billie Eilish", "Baird O'Connell", "California, USA", 8, "happier forever",["Singer","Songwriter"]),
    Employee("Amethyst Amelia", "Kelly", "Sydney, Australia", 1, "Extravaganza",["Rapper","Songwriter"]),
    Employee("Elizabeth", "Grant", "New York, USA", 3, "Mellow than yellow",["Singer","Songwriter"]),
    Employee("Ella Marija Lani", "Yelich-O'Connor", "Auckland, New Zealand", 5, "Lorde and saviour",["Singer","Songwriter","Producer"]),
    Employee("Sabrina Annlynn", "Carpenter", "Pennsylvania, USA", 6, "You want me? No duh!",["Singer","Songwriter","Dancer","Actor"]),
    Employee("Elena Jane", "Goulding", "Hereford, UK", 11, "Raspy is everything!",["Singer","Songwriter","Dancer"]),
    Employee("Beyonce Giselle", "Knowles-Carter", "Texas, USA", 22, "Uh oh uh oh uh oh oh no no",["Singer","Belter","Songwriter","Dancer","Producer","Band Member"]),
    Employee("Christina Maria", "Aguilera", "New York, USA", 30, "Traps genies in bottles",["Singer","Belter","Dancer"]),
    Employee("Britney Jean", "Spears", "Mississippi, USA", 32, "Dancing Until The World End",["Singer","Dancer"]),
    Employee("Jennifer Lynn", "Lopez-Affleck", "New York, USA", 29, "Dancing Again And Again",["Singer","Dancer","Actor"]),
    Employee("Mariah", "Carey", "New York, USA", 25, "Queen Of Christmas",["Singer","Belter"]),
    Employee("Jessica Louise", "Nelson", "Romford, UK", 9, "Little Mix Member",["Singer","Rapper","Songwriter","Dancer","Band Member"]),
    Employee("Perrie Louise", "Edwards", "South Shields, UK", 9, "Little Mix Member",["Singer","Belter","Dancer","Band Member"]),
    Employee("Leigh-Anne", "Pinnock", "High Wycombe, UK", 9, "Little Mix Member",["Singer","Belter","Dancer","Band Member"]),
    Employee("Jade Amelia", "Thirlwall", "South Shields, UK", 9, "Little Mix Member",["Singer","Belter","Songwriter","Band Member"]),
    Employee("Cher", "Lloyd", "Malvern, UK", 4, "X Factor winner winner chicken zayner",["Singer","Songwriter"]),
    Employee("Bridgit Claire", "Mendler", "Washington, USA", 1, "Lemonade Disney",["Singer","Songwriter"]),
    Employee("Olivia Isabel", "Rodrigo", "California, USA", 3, "failed the driver's test",["Singer","Belter","Songwriter","Producer"]),
    Employee("Phoebe Lucille", "Bridgers", "California, USA", 5, "Bo Burnham's wife",["Singer","Belter","Songwriter"]),
    Employee("Nicole", "Zefanya", "Jakarta, Indonesia", 7, "A little spunk, a little gumption",["Singer","Songwriter"]),
    Employee("John Roger", "Stephens", "Ohio, USA", 10, "The Legend of Weddings",["Singer","Belter","Songwriter"]),
    Employee("Edward Christopher", "Sheeran", "Halifax, UK", 13, "Ginger Rapper",["Singer","Rapper","Belter","Songwriter"]),
    Employee("Shawn Peter Raul", "Mendes", "Pickering, Canada", 8, "Bieber Wannabe",["Singer","Belter","Songwriter"]),
    Employee("Charlie Otto", "Puth", "New Jersey, USA", 8, "Won't see you again",["Singer","Belter","Rapper","Songwriter","Producer"]),
    Employee("Justin Drew", "Bieber", "London, Canada", 16, "Mendes Wannabe",["Singer","Songwriter","Producer"]),
    Employee("Adam Richard", "Wiles", "Dumfries, UK", 6, "Swift's Less Famous Ex",["Songwriter","Producer"]),
    Employee("Peter Gene", "Hernandez", "Hawaii, USA", 14, "If you ever leave me baby...",["Singer","Belter","Songwriter","Producer"]),
    Employee("Pierre David", "Guetta", "Paris, France", 20, "Tugs tugs tugs",["Songwriter","Producer"]),
    Employee("Tim", "Bergling", "Stockholm, Sweden", 8, "Rest In Peace",["Songwriter","Producer"]),
    Employee("Jason Joel", "Desrouleaux", "Florida, USA", 11, "JSon Format Deroooohlooooo",["Singer","Belter","Songwriter","Producer"]),
    Employee("Usher Terry", "Raymond", "Texas, USA", 11, "My last name is Raymond",["Singer","Belter"]),
    Employee("William James", "Adams", "California, USA", 23, "Black Eyed Peas Member",["Songwriter","Rapper","Producer"]),
    Employee("Shawn Corey", "Carter", "New York, USA", 24, "Jay-Z",["Rapper","Songwriter","Producer"]),
    Employee("Marshall Bruce", "Mathers", "Missouri, USA", 29, "Better than the chocolate candy",["Rapper","Songwriter","Producer"]),
    Employee("Tramar", "Dillard", "Florida, USA", 17, "Here we go!",["Rapper","Producer"]),
    Employee("Benjamin", "Haggerty", "Washington, USA", 3, "Buying cheap clothes",["Rapper","Producer"]),
    Employee("Michael Ray", "Nguyen-Stevenson", "California, USA", 14, "Thank You God Always",["Rapper","Songwriter","Producer"]),
    Employee("Timothy", "McKenzie", "London, England", 6, "The Maze Runner",["Singer","Rapper"]),
    Employee("Shaffer Chimere", "Smith", "Arkansas, USA", 18, "Yo yo yo",["Singer","Belter","Producer","Actor"]),
    Employee("Troye Sivan", "Mellet", "Johannesburg, South Africa", 7, "Timothee Chalamet Lookalike",["Singer","Songwriter","Actor"]),
    Employee("Aubrey Drake", "Graham", "Toronto, Canada", 9, "I am God's Plan",["Rapper","Songwriter"]),
    Employee("Oliver Stanley", "Murs", "Witham, UK", 4, "Nowhere to go but UP",["Singer","Belter","Songwriter"]),
    Employee("Samuel Frederick", "Smith", "London, UK", 7, "Mummie don't know daddy's getting HOT",["Singer","Belter","Songwriter","Producer"]),
    Employee("Faheem Rasheed", "Najm", "Florida, USA", 16, "T-PAIN",["Singer","Belter","Songwriter","Producer"]),
    Employee("Calvin Cordozar", "Broadus", "California, USA", 19, "Doja Cat's Male Counterpart",["Rapper","Producer"]),
    Employee("Harry Edward", "Styles", "Redditch, UK", 12, "That One Direction Member Who Dresses Differently",["Singer","Belter","Songwriter","Band Member"]),
    Employee("Zain Javadd", "Malik", "Bradford, UK", 12, "That One Direction Member Who Left Earlier Than Everyone Else",["Singer","Belter","Songwriter","Band Member"]),
    Employee("Niall James", "Horan", "Mullingar, Ireland", 12, "That One Direction Member Who Writes Better Songs",["Singer","Songwriter","Band Member"]),
    Employee("Louis William", "Tomlinson", "Doncaster, UK", 12, "That One Direction Member Who Went EDM",["Singer","Songwriter","Band Member"]),
    Employee("Liam James", "Payne", "Wolverhampton, UK", 12, "That One Direction Member Who's Just An A**Hole",["Singer","Songwriter","Band Member"]),
    Employee("Jung-kook", "Jeon", "Busan, South Korea", 10, "Behind The Scenes Member",["Singer","Belter","Dancer","Band Member"]),
    Employee("Tae-hyung", "Kim", "Daegu, South Korea", 10, "Behind The Scenes Member",["Singer","Dancer","Band Member"]),
    Employee("Ji-min", "Park", "Busan, South Korea", 10, "Behind The Scenes Member",["Singer","Dancer","Band Member"]),
    Employee("Yoon-gi", "Min", "Daegu, South Korea", 10, "Behind The Scenes Member",["Rapper","Dancer","Band Member"]),
    Employee("Seok-jin", "Kim", "Anyang-si, South Korea", 10, "Behind The Scenes Member",["Singer","Dancer","Band Member"]),
    Employee("Nam-joon", "Kim", "Seoul, South Korea", 10, "Behind The Scenes Member",["Rapper","Dancer","Band Member"]),
    Employee("Ho-seok", "Jung", "Gwangju, South Korea", 10, "Behind The Scenes Member",["Rapper","Dancer","Band Member"]),
    Employee("Sunwoo", "Kim", "South Korea", 8, "The Boyz Member",["Singer","Songwriter","Rapper","Dancer","Band Member"]),
    Employee("Juyeon", "Lee", "Gwangju-si, South Korea", 8, "The Boyz Member",["Dancer","Singer","Rapper","Band Member"]),
    Employee("Jaehyun", "Lee", "Incheon, South Korea", 8, "The Boyz Member",["Singer","Dancer","Band Member"]),
    Employee("Younghoon", "Kim", "Seoul, South Korea", 8, "The Boyz Member",["Singer","Dancer","Band Member"]),
    Employee("Sangyeon", "Lee", "Seoul, South Korea", 8, "The Boyz Member",["Singer","Belter","Band Member"]),
    Employee("Hak-Nyeon", "Ju", "Seogwipo-si, South Korea", 8, "The Boyz Member",["Singer","Dancer","Band Member"]),
    Employee("Young Jae (Eric)", "Son", "Seoul, South Korea", 8, "The Boyz Member",["Rapper","Dancer","Band Member"]),
    Employee("Chang Min", "Ji", "Cheongju-si, South Korea", 8, "The Boyz Member",["Singer","Dancer","Band Member"]),
    Employee("Chan-hee", "Choi", "Jeonju-si, South Korea", 8, "The Boyz Member",["Singer","Belter","Band Member"]),
    Employee("Hyung-seo (Kevin)", "Moon", "Gwangju, South Korea", 8, "The Boyz Member",["Singer","Dancer","Band Member"]),
    Employee("Joon Young (Jacob)", "Bae", "Toronto, Canada", 8, "The Boyz Member",["Singer","Belter","Dancer","Band Member"]),
    Employee("Jae-min", "Na", "Jeonju-si, South Korea", 7, "NCT Dream Member",["Singer","Rapper","Dancer","Band Member"]),
    Employee("Je-no", "Lee", "Incheon, South Korea", 7, "NCT Dream Member",["Singer","Rapper","Dancer","Band Member"]),
    Employee("Ren Jun", "Huang", "Jilin City, China", 7, "NCT Dream Member",["Singer","Belter","Dancer","Band Member"]),
    Employee("Chenle", "Zhong", "Shanghai, China", 7, "NCT Dream Member",["Singer","Belter","Dancer","Band Member"]),
    Employee("Dong-hyuck", "Lee", "Seoul, South Korea", 7, "NCT Dream Member",["Singer","Belter","Dancer","Band Member"]),
    Employee("Mark", "Lee", "Toronto, Canada", 7, "NCT Dream Member",["Singer","Rapper","Dancer","Band Member"]),
    Employee("Ji-sung", "Park", "Seoul, South Korea", 7, "NCT Dream Member",["Singer","Dancer","Band Member"]),
]

def display_employees():
# Displays Employee List Elements
# Note: You may use this method or not
    count = 0
    for employee in employee_list:
        count += 1
        print("\n===========| Employee No.", count, "|===========")
        print("Name:",employee.getFullName())
        print("Address:",employee.getAddress())
        print("Years In Industry:",employee.getYears())
        print("Description:",employee.getDesc())
        print("\n--------| List Of Assigned Jobs |--------",employee.getJobs())
        print("==========================================")

# Call Function
display_employees()