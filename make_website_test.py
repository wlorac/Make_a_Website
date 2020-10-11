import unittest

from make_website import *

class MakeWebsite_Test(unittest.TestCase):

    def test_surround_block(self):

        # test surrounding html
        self.assertEqual(surround_block('h1', 'Eagles'), "<h1>Eagles</h1>")

        # test surrounding html
        self.assertEqual(surround_block('p', 'Lorem ipsum dolor sit amet, consectetur ' +
                                        'adipiscing elit. Sed ac felis sit amet ante porta ' +
                                        'hendrerit at at urna. Donec in vehicula ex. Aenean ' +
                                        'scelerisque accumsan augue, vitae cursus sapien venenatis ' +
                                        'ac. Quisque dui tellus, rutrum hendrerit nisl vitae, ' +
                                        'pretium mollis lorem. Pellentesque eget quam a justo ' +
                                        'egestas vehicula in eu justo. Nulla cursus, metus vitae ' +
                                        'tincidunt luctus, turpis lectus bibendum purus, eget ' +
                                        'consequat est lacus ac nibh. In interdum metus vel est ' +
                                        'posuere aliquet. Maecenas et euismod arcu, eu auctor ' +
                                        'libero. Phasellus lectus magna, auctor ac auctor in, ' +
                                        'suscipit id turpis. Maecenas dignissim enim ac justo ' +
                                        'tincidunt viverra. Sed interdum molestie tincidunt. Etiam ' +
                                        'vitae justo tincidunt, blandit augue id, volutpat ligula. ' +
                                        'Aenean ut aliquet mi. Suspendisse consequat blandit posuere.'),
                                        '<p>Lorem ipsum dolor sit amet, consectetur ' +
                                        'adipiscing elit. Sed ac felis sit amet ante porta ' +
                                        'hendrerit at at urna. Donec in vehicula ex. Aenean ' +
                                        'scelerisque accumsan augue, vitae cursus sapien venenatis ' +
                                        'ac. Quisque dui tellus, rutrum hendrerit nisl vitae, ' +
                                        'pretium mollis lorem. Pellentesque eget quam a justo ' +
                                        'egestas vehicula in eu justo. Nulla cursus, metus vitae ' +
                                        'tincidunt luctus, turpis lectus bibendum purus, eget ' +
                                        'consequat est lacus ac nibh. In interdum metus vel est ' +
                                        'posuere aliquet. Maecenas et euismod arcu, eu auctor ' +
                                        'libero. Phasellus lectus magna, auctor ac auctor in, ' +
                                        'suscipit id turpis. Maecenas dignissim enim ac justo ' +
                                        'tincidunt viverra. Sed interdum molestie tincidunt. Etiam ' +
                                        'vitae justo tincidunt, blandit augue id, volutpat ligula. ' +
                                        'Aenean ut aliquet mi. Suspendisse consequat blandit posuere.</p>')

    def test_create_email_link(self):

        # test created email
        self.assertEqual(
            create_email_link('lbrandon@wharton.upenn.edu'),
            '<a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>')

        # test created email
        self.assertEqual(
            create_email_link('lbrandon.at.wharton.upenn.edu'),
            '<a href="mailto:lbrandon.at.wharton.upenn.edu">lbrandon.at.wharton.upenn.edu</a>')

    def test_detect_name(self):
    """
    Check whether we can get a name from a resume.
    """

        some_name = test_detect_name('resume.txt')

        # if the test is a pass, this is what we should expect
        self.assertEqual(some_name, 'Brandon Krakowsky')

        # checking a different resume
        some_other_name = test_detect_name('wong_resume.txt')

        # if the test is a pass, this is what we should expect
        self.assertEqual(some_other_name, 'Carol Wong')

    def test_detect_email(self):
    """
    Check whether we can get an email address from a resume.
    """
        self.assertEqual("cliw@seas.upenn.edu", test_detect_email('wong_resume.txt'))

    def test_detect_courses(self):
    """
    Check whether we can get courses from a resume.
    """
        self.assertEqual("Introduction to Software Development, Mathematical Foundations of Computer Science",
                         detect_courses('wong_resume.txt'))

    def test_detect_projects(self):
    """
    Check whether we can get projects from a resume, and ensure that a list is returned.
    """

        expected_projects = [] # defines an empty list
        self.assertEqual(type(expected_projects), type(detect_projects('wong_resume.txt')))


    def test_convert_list_to_string(self):
    """
    Check whether the return is actually a string by comparing it to another string.
    """

        sample_string = "Sample string"
        sample_string_list = ["Sample", "string"]

        self.assertEqual(sample_string, convert_list_to_string(sample_string_list))



    def test_write_basic_info(self):
    """
    Check whether the expected output from basic info matches what the function actually outputs
    Also check whether they are the same data type.
    """

        expected_intro = "<div>\n<h1>Carol Wong</h1><p>Email: <a href=\"mailto:cliw@seas.upenn.edu\"" \
                          ">cliw[aT]seas.upenn.edu</a></p>\n</div>"

        self.assertEqual(expected_intro, write_basic_info('wong_resume.txt'))

        self.assertEqual(type(expected_intro), type(write_basic_info('wong_resume.txt')))

    def test_write_projects(self):
    """
    Check whether the expected output from projects matches what the function actually outputs.
    Also check whether they are the same data type.
    """

        expected_projects = "<div>\n<h2>Projects</h2>\n<ul>\n<li>PwC - Owned product development from conception to MVP launch, of B2B SaaS middleware that connects corporate procurement systems to the central bank’s trade finance platform</li>\n<li>PwC - Led 10-week development ceremony employing Agile methodology to roll out a scalable prototype release with 5 well-scoped features; groomed backlog, facilitated sprint planning (using Jira), daily standups, iteration reviews, and retrospectives</li>\n<li>EY - Created baseline IT strategy for a leading retail bank, with a three-year roadmap and its quarterly iterations</li>\n</ul>\n</div>"

        self.assertEqual(expected_projects, write_projects('wong_resume.txt'))

        self.assertEqual(type(expected_projects), type(write_projects('wong_resume.txt')))

    def test_write_courses(self):
        """
        Check whether the expected output from courses matches what the function actually outputs.
        Also check whether they are the same data type.
        """

        expected_courses = "<div>\n<h3>Courses</h3>\n<span>Introduction to Software Development, Mathematical Foundations of Computer Science</span>\n</div>"

        self.assertEqual(expected_courses, write_courses('wong_resume.txt'))

        self.assertEqual(type(expected_courses), type(write_courses('carol_resume.txt')))

    def test_add_end_lines_in_html(self):
        """
        Check whether the expected output is equal to the function's actual output
        """
        correct_list = "\n</div>" + "\n</body>" + "\n</html>"

        self.assertEqual(correct_list, add_end_lines_in_html())




# entry point.
if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()
