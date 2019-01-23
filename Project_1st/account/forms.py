from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(label="ID", max_length=30)
    password = forms.CharField(label="PW", widget=forms.PasswordInput(), max_length=20)
    password_re = forms.CharField(label="confirm password", widget=forms.PasswordInput(), max_length=20)
    
    def is_valid(self):
        print(self['password'])
        valid = super(SignupForm, self).is_valid()
        if not valid:
            return valid
        if self['password'].data != self['password_re'].data:
            return False
        return True
