import matplotlib.pyplot as plt
from fuzzywuzzy import process
import fuzzywuzzy

# Function to match names between dataframes
def match_name(name, list_names, min_score=0):
    max_score = -1
    max_name = ''
    for x in list_names:
        score = process.extractOne(name, [x], scorer=fuzzywuzzy.fuzz.token_sort_ratio)[1]
        if score > max_score and score >= min_score:
            max_name = x
            max_score = score
    return max_name

# Function that creates a bar chart
def create_plot(dataframe, name):
    plot_data = dataframe.set_index('Year')[columns_to_plot]
    plot_data.plot(kind='bar', stacked=True, figsize=(4,4))
    title = 'Results by years, ' + name
    plt.title(title)  # Set the title
    plt.xlabel('Year')  # X-axis label
    plt.ylabel('Share of students tested')  # Y-axis label
    plt.grid(axis='y')
    plt.legend(loc='lower left')
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