# External IP Check
Check external IP address of the host against the currently stored IP address and if these are not a match, update GoDaddy DNS Records with the current address.

I use a server in my house as a jumpbox with 2 Factor Authentication but occasionally the external IP address changes and locks me out until I manually update the records, this daily check should remove the need for this.
