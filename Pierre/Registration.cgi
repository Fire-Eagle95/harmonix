#!/usr/bin/perl

	local ($buffer, @

print "Content-type:text/html\r\n\r\n";
print '<html>';
print '<head>';
print '<title>Registration was successful</title>';
print '</head>';
print '<body bgcolor="A9F5F2" text="#08088A"><h2>Your registration was successful! Congratulations</h2>';
print '<a href="http://cgi.cs.mcgill.ca/~pgianf/Welcome.html">Go back to Home page</a>';
print '</body>';
print '</html>';
my $filename = 'members.csv';
open(my $fh, '>>', $filename);
close $fh;


exit 0;

