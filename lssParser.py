import xml.etree.ElementTree as ET 
from Split import Split, Attempt, Segment
"""
A set of Functions designed to parse livesplit lss files to create a split object

Functions
---------
parse_lss(lss_file)
  Parses a passed lss file and generates a Splits object
"""

def parse_lss(lss_file):
  """Returns a Splits object from a lss file.

  Parameters
  ----------
    lss_file : str
      is an absolute path to the lss file.
  
  Returns
  -------
    Split
      A Split object that contains all useful data about that splits file.
  """
  #Grab the lss file as an xml
  tree = ET.parse(lss_file)
  root = tree.getroot()
  
  # Create a new empty Splits object
  temp_split = Split()

  # Find the game name
  temp_split.game_name = root.find("GameName").text

  # Find the Category name
  temp_split.category_name = root.find("CategoryName").text

  temp_split.attempt_count = root.find("AttemptCount").text
  attempt_dic = {}
  #  Parse through the Attempts to build each Attempt Objects
  for attempt in root.find("AttemptHistory").findall("Attempt"):
    # Create a new attempt object
    temp_attempt = Attempt()
    # Fill in date and live time starts
    temp_attempt.date_start, temp_attempt.ltime_start = attempt.attrib["started"].split(" ")
    # Fill in date and live time ends
    temp_attempt.date_end, temp_attempt.ltime_end = attempt.attrib["ended"].split(" ")
    
    # Check if run was completed, also set RealTime if it is
    if attempt.find("RealTime") != None:
      temp_attempt.rtime = attempt.find("RealTime").text
      temp_attempt.did_complete = True
    # Check if run was completed, also set GameTime if it is
    if attempt.find("GameTime") != None:
      temp_attempt.gtime = attempt.find("GameTime").text
      temp_attempt.did_complete = True

    # Later this attempt will be added to the split.
    attempt_dic[attempt.attrib["id"]] = temp_attempt

  for segs in root.find("Segments").findall("Segment"):
    #Create new segments for pb and best
    pb_seg = Segment()
    best_seg = Segment()

    seg_name = segs.find("Name").text
    
    # Fill in the segment names
    pb_seg.seg_name = seg_name
    best_seg.seg_name = seg_name

    # Grab pb data
    pb = segs.find("SplitTimes").find("SplitTime")
    pb_seg.real_time = pb.find("RealTime").text
    pb_seg.game_time = pb.find("GameTime").text
    temp_split.pb_segments.append(pb_seg) # Add this pb seg to the splits
    

    # Grab Best data
    best = segs.find("BestSegmentTime")
    best_seg.real_time = best.find("RealTime").text
    best_seg.game_time = best.find("GameTime").text
    temp_split.best_segments.append(best_seg) # Add this best seg to the splits

    # Parse through the segment history
    for seg_attempt in segs.find("SegmentHistory").findall("Time"):
      # Create a new segment
      temp_seg = Segment()
      # Fill name of the segment
      temp_seg.seg_name = seg_name
      
      # Grab the RealTime and GameTime
      temp_seg.real_time = seg_attempt.find("RealTime").text
      temp_seg.game_time = seg_attempt.find("GameTime").text

      # Assign this segment Attempt to its corresponding attempt. 
      attempt_dic[seg_attempt.attrib["id"]].segments.append(temp_seg)
  
  # Each Attempt should be fully populated my segments. So add them to the splits object
  for attempt in attempt_dic:
    temp_split.attempts.append(attempt_dic[attempt])

  # Finally return the splits object as we are finished parsing the data.
  return temp_split



