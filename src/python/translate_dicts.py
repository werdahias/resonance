# translate_dicts.py
# SPDX-FileCopyrightText: 2023 nate-xyz
# SPDX-License-Identifier: GPL-3.0-or-later

id3_translate = {
    # In same sequence as defined at http://id3.org/id3v2.4.0-frames
    # 'TIT1': 'grouping', # Depends on itunes_compatible_grouping
    'TIT2': 'title',
    'TIT3': 'subtitle',
    'TALB': 'album',
    'TSST': 'discsubtitle',
    'TPE1': 'artist',
    'TPE2': 'albumartist',
    'TPE3': 'conductor',
    'TPE4': 'remixer',
    'TEXT': 'lyricist',
    'TCOM': 'composer',
    'TENC': 'encodedby',
    'TBPM': 'bpm',
    'TKEY': 'key',
    'TLAN': 'language',
    'TCON': 'genre',
    'TPUB': 'label',
    'TDOR': 'originaldate',
    'TDRC': 'date',
    'TSOA': 'albumsort',
    'TSOP': 'artistsort',
    'TSOT': 'titlesort',
    'TOAL': 'originalalbum',
    'TOPE': 'originalartist',
    'TOFN': 'originalfilename',

    'TRCK': 'tracknumber',
    'TPOS': 'discnumber',

    # The following are informal iTunes extensions to id3v2:
    'TCMP': 'compilation',
    'TSOC': 'composersort',
    'TSO2': 'albumartistsort',
    'MVNM': 'movement'
}

asf_translate = {'WM/AlbumTitle': 'album',
                 'Title': 'title',
                 'Author': 'artist',
                 'WM/AlbumArtist': 'albumartist',
                 'WM/Year': 'date',
                 'WM/OriginalAlbumTitle': 'originalalbum',
                 'WM/OriginalArtist': 'originalartist',
                 'WM/OriginalReleaseTime': 'originaldate',
                 'WM/OriginalReleaseYear': 'originalyear',
                 'WM/OriginalFilename': 'originalfilename',
                 'WM/Composer': 'composer',
                 'WM/Writer': 'lyricist',
                 'WM/Conductor': 'conductor',
                 'WM/ModifiedBy': 'remixer',
                 'WM/Producer': 'producer',
                 'WM/ContentGroupDescription': 'grouping',
                 'WM/SubTitle': 'subtitle',
                 'WM/SetSubTitle': 'discsubtitle',
                 'WM/TrackNumber': 'tracknumber',
                 'WM/PartOfSet': 'discnumber',
                 'Description': 'comment',
                 'WM/Genre': 'genre',
                 'WM/BeatsPerMinute': 'bpm',
                 'WM/InitialKey': 'key',
                 'WM/Script': 'script',
                 'WM/Language': 'language',
                 'WM/Mood': 'mood',
                 'WM/ISRC': 'isrc',
                 'Copyright': 'copyright',
                 'WM/Lyrics': 'lyrics',
                 'WM/SharedUserRating': '~rating',
                 'WM/Media': 'media',
                 'WM/Barcode': 'barcode',
                 'WM/CatalogNo': 'catalognumber',
                 'WM/Publisher': 'label',
                 'WM/EncodedBy': 'encodedby',
                 'WM/EncodingSettings': 'encodersettings',
                 'WM/AlbumSortOrder': 'albumsort',
                 'WM/AlbumArtistSortOrder': 'albumartistsort',
                 'WM/ArtistSortOrder': 'artistsort',
                 'WM/TitleSortOrder': 'titlesort',
                 'WM/ComposerSortOrder': 'composersort',
                 'MusicBrainz/Track Id': 'musicbrainz_recordingid',
                 'MusicBrainz/Release Track Id': 'musicbrainz_trackid',
                 'MusicBrainz/Album Id': 'musicbrainz_albumid',
                 'MusicBrainz/Artist Id': 'musicbrainz_artistid',
                 'MusicBrainz/Album Artist Id': 'musicbrainz_albumartistid',
                 'MusicBrainz/TRM Id': 'musicbrainz_trmid',
                 'MusicBrainz/Disc Id': 'musicbrainz_discid',
                 'MusicBrainz/Work Id': 'musicbrainz_workid',
                 'MusicBrainz/Release Group Id': 'musicbrainz_releasegroupid',
                 'MusicBrainz/Original Album Id': 'musicbrainz_originalalbumid',
                 'MusicBrainz/Original Artist Id': 'musicbrainz_originalartistid', 'MusicIP/PUID': 'musicip_puid', 'MusicBrainz/Album Status': 'releasestatus', 'MusicBrainz/Album Type': 'releasetype', 'MusicBrainz/Album Release Country': 'releasecountry', 'Acoustid/Id': 'acoustid_id', 'Acoustid/Fingerprint': 'acoustid_fingerprint', 'WM/IsCompilation': 'compilation', 'WM/Engineer': 'engineer', 'ASIN': 'asin', 'WM/DJMixer': 'djmixer', 'WM/Mixer': 'mixer', 'WM/ARTISTS': 'artists', 'WM/Director': 'director', 'WM/Work': 'work', 'WM/AuthorURL': 'website'}
mp4_translate = {
    "\xa9ART": "artist",
    "\xa9nam": "title",
    "\xa9alb": "album",
    "\xa9wrt": "composer",
    "aART": "albumartist",
    "\xa9grp": "grouping",
    "\xa9day": "date",
    "\xa9gen": "genre",
    "\xa9lyr": "lyrics",
    "\xa9cmt": "comment",
    "\xa9too": "encodedby",
    "\xa9dir": "director",
    "cprt": "copyright",
    "soal": "albumsort",
    "soaa": "albumartistsort",
    "soar": "artistsort",
    "sonm": "titlesort",
    "soco": "composersort",
    "sosn": "showsort",
    "tvsh": "show",
    "purl": "podcasturl",
    "\xa9mvn": "movement",
    "\xa9wrk": "work",
}

wav_translate = {
    # Minimal, as e.g. supported by Windows Explorer,
    # Audacity and foobar2000
    'IART': 'artist',
    'ICMT': 'comment',
    'ICOP': 'copyright',
    'ICRD': 'date',
    'IGNR': 'genre',
    'INAM': 'title',
    'IPRD': 'album',
    'ITRK': 'tracknumber',

    # Extended, not well supported by other tools
    'ICNT': 'releasecountry',
    'IENC': 'encodedby',
    'IENG': 'engineer',
    'ILNG': 'language',
    'IMED': 'media',
    'IMUS': 'composer',
    'IPRO': 'producer',
    'IWRI': 'writer',
}