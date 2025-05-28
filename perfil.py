import pandas as pd

personal_info = {
    "Name":           ["Sanyer Duque Hoyos"],
    "Profession":     ["Systems and Telecommunications Engineer"],
    "Specialization": ["Big Data and Data Analytics"],
    "Role":           ["Data Engineer"]
}

skills = {
    "Languages":      ["Python", "SQL", "Scala", "R"],
    "Big Data Tools": ["Spark", "Kafka", "Hadoop"],
    "Visualization":  ["Power BI", "Looker Studio", "Excel"],
    "Dev Tools":      ["VS Code", "Jupyter Notebook", "Git", "Docker"]
}

profile_df = pd.DataFrame(personal_info)
skills_df  = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in skills.items()]))

print(profile_df)
print("\n💡 Technical Skills:")
print(skills_df.fillna(""))
