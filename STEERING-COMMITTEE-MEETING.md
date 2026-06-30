# Open Device Partnership Steering Committee Meeting Process

A monthly Open Device Partnership (ODP) Steering Committee meeting is held to discuss and make decisions on important
matters related to the project. The meeting is scheduled on a monthly recurring basis and open to all members of the
Open Device Partnership community. The agenda is built in advance using pull requests to a markdown file in the
[`OpenDevicePartnership/governance`](https://github.com/OpenDevicePartnership/governance) repository.

Anyone is welcome to create pull requests to add items to the agenda. The committee is chaired by a designated Open
Device Partnership Steering Committee member. While the primary participants in the meeting are the members of the Open
Device Partnership Steering Committee, the meeting chair is responsible for ensuring that the meeting is inclusive and
that all voices are heard.

This meeting only discusses Open Device Partnership organizational and process matters. Technical discussions and
decisions are made in separate meetings that are focused on technical topics led by the appropriate project lead.

## Meeting Agenda Process

Note: The `governance` repository requires two approvals to merge a pull request. In cases below where only one approval
is required, the pull request may be merged by an admin by overriding the approval requirement in order to meet the
expected timelines for merging the pull request if necessary. If that is not required at the time, the pull request can
simply be merged with two approvals as usual.

1. An automated process creates a pull request to the [`OpenDevicePartnership/governance`](https://github.com/OpenDevicePartnership/governance)
   repository to add a new agenda markdown file in the `steering-committee-meetings` directory for the next meeting.
   The pull request is assigned to the meeting chair. The pull request includes all ODP Steering Committee members as
   reviewers.
   - This pull request must not add any content other than the new agenda markdown file with template fields customized
     for the next meeting.
2. Any ODP Steering Committee member can merge the file once at least one other ODP Steering Committee member has
   approved the pull request. The meeting chair is responsible for ensuring that the pull request is merged in a timely
   manner after it has received the necessary approvals, ideally within three business days of the pull request being
   created.
3. Once the upcoming meeting agenda file is merged, pull requests may be created to add items to the agenda.
    - The pull request should include a description of the agenda item(s) and any relevant links to documentation or
      discussions to support the item(s) in the markdown file.
    - The pull request should be assigned to the meeting chair and include all ODP Steering Committee members as
      reviewers.
    - At least two ODP Steering Committee members must approve the pull request for it to be merged. The meeting chair
      is responsible for ensuring that pull requests to add items to the agenda are merged in a timely manner after they
      have received the necessary approvals. The meeting chair should prioritize reviewing and approving pull requests,
      but their approval is not mandatory.
    - Reviewers should ensure that:
      - The agenda item is relevant to the Open Device Partnership organization and appropriate for discussion in the
        Steering Committee meeting.
        - In particular, that the item is not primarily technical in nature and would be more appropriate for
          discussion in a technical meeting led by the relevant project lead.
      - The description of the agenda item is clear and includes sufficient context or links to support the proposed
        discussion.
      - The agenda item requires a decision to be made by the Steering Committee or is otherwise important to discuss
        in the Steering Committee meeting and cannot be resolved through asynchronous discussion on GitHub.
        - Note: "Asynchronous discussion" refers to discussions that can be conducted through GitHub issues, pull
          requests, or other communication channels without requiring a real-time meeting.
4. At least two days prior to the scheduled meeting, the meeting chair should ensure that the agenda is finalized and
   published by merging any remaining open pull requests for agenda items for the upcoming meeting. The meeting chair
   should also ensure that any pull requests for agenda items that have not received the necessary approvals are closed
   and that the contributors to those pull requests are informed of the reason for closing the pull request.
   - The meeting chair is responsible for creating a pull request that updates the status in the agenda file to "Final".
     - This pull request only requires a single approval from an ODP Steering Committee member to be merged. The
       meeting chair should merge the pull request to finalize the agenda in a timely manner, ideally within one
       business day after all pull requests for agenda items have been merged and the agenda is finalized.
     - New items may not be added after the agenda is finalized, but existing items may be modified or removed as
       needed with the necessary approvals.

### Meeting Agenda Statuses

- **Draft:** The agenda is being built and is not yet finalized. New items may be added to the agenda through pull
  requests that receive the necessary approvals.
- **Final:** The agenda is finalized and published. No new items may be added to the agenda, but existing items may be
  modified or removed as needed with the necessary approvals.
- **Canceled:** The meeting has been canceled. No items may be added, modified, or removed from the agenda. The meeting
  chair should follow the process outlined in the [Meeting Cancellation](#meeting-cancellation) section below when
  canceling a meeting.

## Meeting Cancellation

The meeting chair may cancel an upcoming meeting at any time.

The meeting chair should cancel the meeting when:

- There are no agenda items, or there are not enough approved agenda items to support a meaningful discussion.

The meeting chair should also consider canceling the meeting when:

- There are not enough ODP Steering Committee members available to attend.
- Key stakeholders for a given agenda item are not available to attend.

When a meeting is canceled, the meeting chair is responsible for the following:

- Inform the ODP Steering Committee and the broader Open Device Partnership community of the cancellation and the reason
  for it in a timely manner.
- Update the agenda file for the canceled meeting to mark its status as "Canceled".
- Manually run the GitHub workflow to create the agenda file for the next meeting. That pull request follows the normal
  process for adding a new agenda file.
- Determine whether any agenda items planned for the canceled meeting should be carried over to the next meeting or can
  be resolved through asynchronous discussion on GitHub. If an item must be included in a future meeting, the chair
  creates a pull request to the next meeting's agenda file that adds the relevant items, following the normal process for
  adding agenda items, including obtaining the necessary approvals from ODP Steering Committee members.

## Meeting Process

During the meeting, the chair should follow the published agenda and facilitate discussion on each item. The primary
participants in the discussion should be the ODP Steering Committee members, but the chair should ensure that discussion
is inclusive. The submitter of an agenda item is not required to attend the meeting for the item to be discussed, but
they are welcome to attend and participate in the discussion.

For agenda items that require a decision to be made by the Steering Committee, the chair should facilitate discussion
until there is a clear consensus among the Steering Committee members on the decision. The chair may use a formal voting
process if needed to reach a decision, but the goal should be to reach consensus through discussion whenever possible.
The chair should ensure that all voices are heard during the discussion and that the decision is made in the best
interest of the Open Device Partnership project and community.

- Major new topic areas are not allowed to be added to the agenda in the meeting. They must be added to a future meeting
  agenda in a pull request.
- Non-Steering Committee members are welcome to attend the meeting and participate in the discussion, but they do not
  have voting rights in any decisions made by the Steering Committee. The chair should ensure that non-Steering Committee
  members have an opportunity to share their perspectives during the discussion, but the final decision on any agenda
  item is made by the Steering Committee members.

## Meeting Follow-Up

The meeting chair is responsible for ensuring that any decisions made during the meeting are documented in the meeting
minutes and that any action items resulting from the meeting are assigned to the appropriate individuals or teams for
follow-up. The meeting chair should also ensure that the meeting minutes are published and shared with the ODP Steering
Committee and the broader Open Device Partnership community in a timely manner after the meeting.

Meeting minutes may be recorded manually or through an automated process, but they should include a summary of the
discussion for each agenda item, the decisions made, and any action items assigned. In addition, all Open Device
Partnership Steering Committee meetings are recorded and the videos are published to the ODP YouTube channel.

The meeting chair should ensure that the meeting minutes are accurate and complete, and that they reflect the outcomes
of the meeting in a clear and concise manner.

Meeting minutes are added to the "Meeting Minutes" section of the agenda file for the meeting in a pull request created
by the meeting chair. This section also includes a link to the YouTube video recording of the meeting. This pull request
must be approved by at least one ODP Steering Committee member before it can be merged.
