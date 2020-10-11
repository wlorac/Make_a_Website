"""
Carol Wong
Penn ID:
I worked alone referencing to the following resources:
https://www.programiz.com/python-programming/methods/string/strip
"""


def detect_name(file):
    """
    Reads the resume file, and extracts the first line, i.e. the name.
    Raise a runtime error if the first character in the name is not an uppercase letter.
    Removes any leading or trailing whitespace in the first line.
    This function returns the first line.
    """

    # open the file.
    with open(file) as file:
        our_file = file

        # read the first line.
        file_first_line = our_file.readline()

        # raise a runtime error if first character in line is not uppercase.
        if file_first_line[0] != file_first_line[0].capitalize():
            raise RuntimeError("Error: " + file_first_line +
                               "is an invalid name as it does not begin with an uppercase letter.")

        # remove whitespace in the first line.
        file_first_line = file_first_line.strip()

    return file_first_line


def detect_email(file):
    """
    Look for the line in the file that contains the email address.
    This function returns the email address.
    """

    # open the file.
    with open(file) as file:
        our_file = file

        # read all the lines in the file.
        lines = our_file.readlines()

        # establishing the boolean conditions we are expecting to be true in the email address.
        has_at_symbol = False
        is_com_or_edu_address = False
        does_not_have_digits = False
        # establishing this boolean condition in case the email address is missing.
        file_email_line = None

        # look for the line with '@' symbol from all lines.
        for line in lines:
            # scan each character from the line.
            for character in line:
                # if there is a character equaled to '@' symbol, save that line and update True for the email condition.
                if character == '@':
                    file_email_line = line
                    has_at_symbol = True
                    break

        # if an email exists in the resume, eliminates email lines with digits in them.
        if file_email_line is not None:
            # scan each character from the line.
            for character in file_email_line:
                # if there are numeric characters in the line, return none.
                if character.isnumeric():
                    return None
                # otherwise, our current character is numeric, so return True for the no-digits condition.
                else:
                    does_not_have_digits = True

        # if an email exists in the resume, check that it is a .edu or .com address.
        if file_email_line is not None:
            # break up all the parts of the line with periods into a list
            dot_file_email_line = file_email_line.split('.')
            # get the length of the list we just created and minus 1 from said length
            length_dot_file_email_line = len(dot_file_email_line)
            last_index = length_dot_file_email_line - 1
            # identify that last index on the list and check if characters are 'edu' or 'com',
            # if so, set boolean variable to true
            if dot_file_email_line[last_index] == 'edu\n' or dot_file_email_line[last_index] == 'com\n':
                is_com_or_edu_address = True

        # if we all three conditions are met, return the email address line with all whitespace removed
        # otherwise, return None
        if is_com_or_edu_address and has_at_symbol and does_not_have_digits:
            return file_email_line.strip()
        else:
            return None


def detect_courses(file):
    """
    Looks for the word 'courses' in the file, filters out random symbols and whitespaces, and extract that line.
    This function returns that courses line.
    """

    # open the file.
    with open(file) as file:
        our_file = file

        # read all the lines in the file. For each line that contains courses, make a list.
        lines = our_file.readlines()
        courses = []

        # look for the word 'courses' in each line of the file.
        for courses_line in lines:
            # remove all the whitespace
            courses_line = courses_line.strip()
            # break up sentence into list of words.
            courses_words_list = courses_line.split(" ")
            # for each word in the list of words
            for word in courses_words_list:
                # if the word is 'Courses', append courses to the list
                if word == 'Courses':
                    courses.append(courses_words_list)

        # get all the sentences from the courses list, then make an empty list
        for sentence in courses:
            course_sentence = []
            # for each word in the sentence remove the whitespace
            for word in sentence:
                word = word.strip()
                # if the word is not some random characters, then append the word to the course sentence.
                if word != 'Courses' and word != ':' and word != '-' and word != '':
                    course_sentence.append(word)

        # make another empty list to filter once again
        course_sentence2 = []
        # for each word in our new sentence, split them on the comma
        for word in course_sentence:
            word = word.split("\t")
            # for each item, filter out all the random characters once again and append it to new list.
            for item in word:
                if item != 'Courses' and item != ':' and item != '-' and item != '' and item != ',':
                    course_sentence2.append(item)

        # combine the first course list with the second course list with no duplicates and a space separator
        course_sentence = ' '.join(course_sentence2)

        # remove all the white space and place everything on the same line
        course_sentence = course_sentence.strip()
        course_sentence = course_sentence.strip("\n")
        print(course_sentence)

        # return the courses
        return course_sentence


def detect_projects(file):
    """
    Looks for the word 'projects' in the file.
    Each subsequent line is a project until the separator is hit (>= ten minus signs).
    It filters out blank lines and whitespaces, and returns the project lines.
    """

    # open the file, read all the lines in the file and make a list.
    with open(file) as file:
        our_file = file
        lines = our_file.readlines()

        # establishing some variables for checking projects.
        found_projects = False
        project_line_count = 0

        # while we haven't come across the word 'Projects'.
        while not found_projects:
            # count each sentence and split the sentence into words
            for sentence in lines:
                project_line_count += 1
                sentence = sentence.split(' ')
                # but once we find the word 'Projects' in the sentence, break.
                if found_projects:
                    break
                # once we find the word 'Projects', break
                for word in sentence:
                    if found_projects:
                        break
                    # if the word 'Projects' or 'Projects' with a new line is found,
                    # set found_projects to True, minus 1 from the project_line_count, and break
                    if word == 'Projects' or word == 'Projects\n':
                        found_projects = True
                        project_line_count -= 1
                        break

        # establishing a list and some variables for testing
        project_lines = []
        ten_minus_signs = False
        minus_sign_count = 0

        # using the project_lines count, if we encounter ten minus signs, break.
        while not ten_minus_signs:
            for line in lines[project_line_count:]:
                if ten_minus_signs:
                    break
                for word in line:
                    # split up each word into characters. If the character is a minus sign,
                    # add to the count. If the minus count reaches 10,
                    # set the ten_minus_sign boolean to True, and break.
                    word = word.split()
                    for character in word:
                        if character == '-':
                            minus_sign_count += 1
                        if minus_sign_count == 10:
                            ten_minus_signs = True
                            break
                # as long as we have not encountered the ten minus signs,
                # remove all whitespace from the line and append the line to projects.
                if not ten_minus_signs:
                    line = line.strip()
                    project_lines.append(line)

        # combine the list of strings, make a list of separate projects
        project_lines = '\n'.join(project_lines)
        project_lines = project_lines.split("\n")

        # only take project lines that are not blank
        not_empty_project_lines = [line for line in project_lines if line.strip() != ""]

    # return all the project lines, which starts after the word 'projects' and ends before the minus signs
    return not_empty_project_lines


def surround_block(tag, text):
    """
    This helps us write proper HTML with the given text.
    It returns the text with the HTML.
    """

    # define the open tag and close tag
    open_tag = "<" + tag + ">"
    close_tag = "</" + tag + ">"
    # puts in all in a string
    text_with_tags = open_tag + text + close_tag

    return text_with_tags


def list_to_string(our_list):
    """
    Takes a given list and converts it to a string. Especially useful for rejoining separated words.
    """

    # Determine how we want to space each character, in this case no space.
    separator = ""

    # returns the joined list as a string. We need to assign a variable to hold the output of this function.
    return separator.join(our_list)


def create_email_link(email_address):
    """This function creates an email link in html format given the input email address."""

    # Create a new list that will contain each character in the email address.
    new_email = []
    # if the email address doesn't exist return None.
    if email_address is None:
        return None
    # for each character in the given email address.
    for character in email_address:
        # if the character we're looking at is equal to "@", then replace it with "aT"
        if character == "@":
            character = "[aT]"
            # add this new character to the list.
            new_email.append(character)
        else:
            # otherwise, add each character to the list we created.
            new_email.append(character)
    # join our new email from a list to a string.
    new_email = list_to_string(new_email)

    # return the result in html format for an active email address.
    return "<a href=\"mailto:" + email_address + "\">" + new_email + "</a>"


def write_intro_section(file):
    """Writes the introduction (basic information section) of our resume. First name and an active email link."""

    # create inner first by finding email.
    email = create_email_link(detect_email(file))
    # if email doesn't exist leave it blank.
    if email is None:
        email = ""
    # create next layer now
    email_surrounded = surround_block("p", "Email: " + email)
    # create the header with the name.
    header_with_name = surround_block("h1", detect_name(file))
    # put it all together within "div" now.
    intro = surround_block("div", "\n" + header_with_name + email_surrounded + "\n")

    return intro


def write_projects_section(file):
    """Writes the projects section of our resume. """

    # get the lines of the projects and assign to list variable.
    project_lines = detect_projects(file)
    # surround the word projects with the appropriate header.
    project_surrounded = surround_block("h2", "Projects")
    # initialize new list.
    projects_surrounded = []
    # for each line in the project list, surround the text with the appropriate headers and append to new list.
    for line in project_lines:
        projects_surrounded.append(surround_block("li", line))
    # rejoin the projects from a list to a single string on the newline command.
    projects_surrounded = "\n".join(projects_surrounded)
    # surround all projects with the appropriate header.
    projects_surrounded_final = surround_block("ul", "\n" + projects_surrounded + "\n")
    # concatenate the projects section into a single string.
    projects_section = surround_block("div", "\n" + project_surrounded + "\n" + projects_surrounded_final + "\n")

    return projects_section


def write_courses_section(file):
    """writes the courses section of our resume. Includes the necessary surrounding text."""

    # get the courses as string.
    courses = detect_courses(file)
    # surround the word Courses with the appropriate header.
    course_surrounded = surround_block("h3", "Courses")
    # Surround the projects with the appropriate header.
    courses_surrounded = surround_block("span", courses)
    # concatenate the courses section into a single string.
    courses_section = surround_block("div", "\n" + course_surrounded + "\n" + courses_surrounded + "\n")

    return courses_section


def remove_last_two_lines_in_html(file_lines):
    """Removes the last two lines in the given lines list from an html file. Makes sure that the last two lines
    contain </body> and </html> before removing them. This function also adds the </div id="page-wrap">."""

    # make sure that we have enough lines in our file_lines. We should, but just in case.
    if len(file_lines) >= 2:
        # delete last two lines from the file_lines.
        file_lines.pop()
        file_lines.pop()
        # now add the </div... line
        file_lines.append("</div id=\"page-wrap\">")

    # return file_lines
    return file_lines


def add_back_last_two_lines_in_html():
    """Adds back the last two lines in a given lines list from an html file,
    these lines will be: </body> and </html>."""

    # return the last three lines as a string.
    return "\n</div>" + "\n</body>" + "\n</html>"


def read_and_write_html_resume(html_file, new_resume_file, resume_file):
    """Programmatically opens an already defined html file, reads our resume from a text file and writes in our
    resume data into a second output file."""

    # now get the information we need from our resume_file and write it to our html file.
    # open our html file in read and write mode.
    resume_html_file = open(html_file, "r+")
    # read lines in file.
    resume_html_file_lines = resume_html_file.readlines()
    # remove last two lines in file and add the appropriate line back in.
    resume_html_file_lines = remove_last_two_lines_in_html(resume_html_file_lines)
    # write the introduction
    introduction = write_intro_section(resume_file)
    # write the projects section
    projects = write_projects_section(resume_file)
    # write the courses section
    courses = write_courses_section(resume_file)
    # append intro, projects and courses to resume_html_file_lines.
    resume_html_file_lines.append(introduction)
    resume_html_file_lines.append(projects)
    resume_html_file_lines.append(courses)
    # add the last three lines back in.
    resume_html_file_lines.append(add_back_last_two_lines_in_html())
    # make sure at the very end that we close template file.
    resume_html_file.close()
    # open our output file.
    read_new_resume_file = open(new_resume_file, "a")
    # add all of the lines into our new file.
    read_new_resume_file.writelines(resume_html_file_lines)
    # make sure at the very end that we close our new_resume_file.
    read_new_resume_file.close()


def main():
    """This is the main function that runs our code."""

    # read the resume template, get our resume information and then output new resume template with
    # updated info to a second html file.
    read_and_write_html_resume('resume_template.html', 'carol_resume.html', 'wong_resume.txt')


# entry point for our main function.
if __name__ == '__main__':
    main()