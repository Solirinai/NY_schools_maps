import matplotlib.pyplot as plt
from fuzzywuzzy import process
import fuzzywuzzy
import numpy as np

# Function to match names between dataframes
def match_name(name, list_names, min_score=0):
    max_score = -1
    max_name = ''
    for x in list_names:
        score = process.extractOne(name, [x], scorer=fuzzywuzzy.fuzz.token_sort_ratio)[1]
        if score > max_score and score >= min_score:
            max_name = x
            max_score = score
    return max_name, max_score

# Function that creates a bar chart
def create_plot(dataframe, name, columns_to_plot):
    plot_data = dataframe.set_index('Year')[columns_to_plot]
    plot_data.plot(kind='bar', stacked=True, figsize=(4,4))
    title = 'Results by years, ' + name
    plt.title(title)  # Set the title
    plt.xlabel('Year')  # X-axis label
    plt.ylabel('Share of students tested')  # Y-axis label
    plt.grid(axis='y')
    plt.legend(loc='lower left', fontsize=8)
    plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], ['0%', '20%', '40%', '60%', '80%', '100%'])  # Adjust y-ticks to percentage
    plt.tight_layout()
    # Return the figure object for further use
    return plt.gcf()  # gcf - Get Current Figure

# Function to process schools from text list into csv file
def process_schools(school_list, open_to):
    processed_schools = []
    pattern = re.compile(r"(.+?)\s+\((\d+[KMQ]\d{3})\)(.*)")
    for school in school_list:
        match = pattern.match(school)
        if match:
            school_name = match.group(1).strip()
            dbn = match.group(2).strip()
            comments = match.group(3).strip()
            processed_schools.append([dbn, school_name, open_to, comments])
    return processed_schools

# Function to create piechart
def create_chart(dataframe, name, columns_to_plot):

    columns = columns_to_plot
    sizes = dataframe[columns].values[0]
    num_categories = len(sizes)
    labels =  ['Asian', 'Black', 'Hispanic', 'Multi', 'Native American', 'White', 'Missing']

    # Use a colormap (e.g., Blues, Greens)
    cmap = plt.get_cmap('YlOrBr_r')

    # Generate colors from the colormap
    colors = [cmap(i) for i in np.linspace(0.4, 1, num_categories)]

    # Create a figure with a specified figure size
    plt.figure(figsize=(2.5,2.5))  #  inches wide,  inches tall

    plt.pie(sizes, labels = labels, colors = colors, autopct='%1.1f%%', startangle=0,
           textprops={'fontsize': 8},  # Adjust label sizes
            labeldistance=1.2,  # Increase label distance
            pctdistance=0.85,  # Adjust distance of percentage text
           )       

    # Add a title
    plt.title(name, fontsize=10, y=0.95)

    # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.axis('equal')
    
# Return the figure object for further use
    return plt.gcf()  # gcf - Get Current Figure