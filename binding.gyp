{
  "targets": [
    {
      "target_name": "rc522",
      "sources": [
        "src/spi.c",
	    "src/rc522.c",
        "src/rfid.c",
        "src/accessor.cc"
      ],
      "include_dirs" : ["<!(node -e \"require('nan')\")"],
      "libraries": [
      ]
    }
  ]
}
