import solitaire as sol
import datetime
import smtplib
import variables as vars

soli = sol.Solitaire() # Solitaire object
result = 0 # For results

sender = vars.email
receivers = [vars.email]
print "Run started at "  + datetime.datetime.now().time().isoformat()

for i in xrange(1000000000):
  result = soli.solve()
  if result < 5:
    print "Run #" + repr(i) + ": " + repr(result) + " cards left."

    if result = 0: # Solved

      message = "From: Kristoffer <" + vars.email + """>
To: Kristoffer Lorentsen <""" + vars.email + """>
Subject: Solitaire solved!

The Solitaire was solved on run #""" + repr(i) + " at " + datetime.datetime.now().time().isoformat()

      try:
        smtpObj = smtplib.SMTP('smtp.gmail.com',587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.ehlo()
        smtpObj.login(sender,vars.password)
        smtpObj.sendmail(sender, receivers, message)
        smtpObj.quit()
        print "Successfully sent email"
      except smtplib.SMTPException:
        print "Error: unable to send email"


  soli.reset()
