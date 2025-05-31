import sgqlc.types
import sgqlc.types.datetime
import sgqlc.types.relay


schema = sgqlc.types.Schema()


# Unexport Node/PageInfo, let schema re-declare them
schema -= sgqlc.types.relay.Node
schema -= sgqlc.types.relay.PageInfo



########################################################################
# Scalars and Enumerations
########################################################################
class AuthenticationSessionType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('android', 'desktop', 'ios', 'web')


Boolean = sgqlc.types.Boolean

class ContextViewType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('activeCycle', 'activeIssues', 'backlog', 'triage', 'upcomingCycle')


class CustomerStatusType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('active', 'inactive')


class CyclePeriod(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('after', 'before', 'during')


class DateResolutionType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('halfYear', 'month', 'quarter', 'year')


DateTime = sgqlc.types.datetime.DateTime

class DateTimeOrDuration(sgqlc.types.Scalar):
    __schema__ = schema


class Day(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday')


class Duration(sgqlc.types.Scalar):
    __schema__ = schema


class ExternalSyncService(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('github', 'jira', 'slack')


class FacetPageSource(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('feed', 'projects', 'teamIssues')


class FeedSummarySchedule(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('daily', 'never', 'weekly')


Float = sgqlc.types.Float

class FrequencyResolutionType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('daily', 'weekly')


class GitAutomationStates(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('draft', 'merge', 'mergeable', 'review', 'start')


class GitLinkKind(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('closes', 'contributes', 'links')


class GithubOrgType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('organization', 'user')


ID = sgqlc.types.ID

class InitiativeStatus(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('Active', 'Completed', 'Planned')


class InitiativeTab(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('overview', 'projects')


class InitiativeUpdateHealthType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('atRisk', 'offTrack', 'onTrack')


Int = sgqlc.types.Int

class IntegrationService(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('airbyte', 'discord', 'email', 'figma', 'figmaPlugin', 'front', 'github', 'githubCommit', 'githubEnterpriseServer', 'githubImport', 'githubPersonal', 'gitlab', 'googleCalendarPersonal', 'googleSheets', 'intercom', 'jira', 'jiraPersonal', 'launchDarkly', 'launchDarklyPersonal', 'loom', 'notion', 'opsgenie', 'pagerDuty', 'salesforce', 'sentry', 'slack', 'slackAsks', 'slackCustomViewNotifications', 'slackInitiativePost', 'slackOrgInitiativeUpdatesPost', 'slackOrgProjectUpdatesPost', 'slackPersonal', 'slackPost', 'slackProjectPost', 'slackProjectUpdatesPost', 'zendesk')


class IssueRelationType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('blocks', 'duplicate', 'related', 'similar')


class IssueSuggestionState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('accepted', 'active', 'dismissed', 'stale')


class IssueSuggestionType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('assignee', 'label', 'project', 'relatedIssue', 'similarIssue', 'team')


class JSON(sgqlc.types.Scalar):
    __schema__ = schema


class JSONObject(sgqlc.types.Scalar):
    __schema__ = schema


class NotificationCategory(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('appsAndIntegrations', 'assignments', 'commentsAndReplies', 'customers', 'documentChanges', 'mentions', 'postsAndUpdates', 'reactions', 'reminders', 'reviews', 'statusChanges', 'subscriptions', 'system', 'triage')


class NotificationChannel(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('desktop', 'email', 'mobile', 'slack')


class OAuthClientApprovalStatus(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('approved', 'denied', 'requested')


class OrganizationDomainAuthType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('general', 'saml')


class OrganizationInviteStatus(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('accepted', 'expired', 'pending')


class PaginationNulls(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('first', 'last')


class PaginationOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('createdAt', 'updatedAt')


class PaginationSortOrder(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('Ascending', 'Descending')


class PostType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('summary', 'update')


class ProductIntelligenceScope(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('none', 'team', 'teamHierarchy', 'workspace')


class ProjectMilestoneStatus(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('done', 'next', 'overdue', 'unstarted')


class ProjectStatusType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('backlog', 'canceled', 'completed', 'paused', 'planned', 'started')


class ProjectTab(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('customers', 'documents', 'issues')


class ProjectUpdateHealthType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('atRisk', 'offTrack', 'onTrack')


class ProjectUpdateReminderFrequency(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('month', 'never', 'twoWeeks', 'week')


class PullRequestReviewTool(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('graphite', 'source')


class PullRequestStatus(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('approved', 'closed', 'draft', 'inReview', 'merged', 'open')


class PushSubscriptionType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('apple', 'appleDevelopment', 'firebase', 'web')


class ReleaseChannel(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('beta', 'development', 'internal', 'preRelease', 'public')


class SLADayCountType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('all', 'onlyBusinessDays')


class SemanticSearchResultType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('document', 'initiative', 'issue', 'project')


class SendStrategy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('desktop', 'desktopAndPush', 'desktopThenPush', 'push')


class SlaStatus(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('Breached', 'Completed', 'Failed', 'HighRisk', 'LowRisk', 'MediumRisk')


class SlackChannelType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DirectMessage', 'MultiPersonDirectMessage', 'Private', 'Public')


String = sgqlc.types.String

class TimelessDate(sgqlc.types.Scalar):
    __schema__ = schema


class TimelessDateOrDuration(sgqlc.types.Scalar):
    __schema__ = schema


class TriageResponsibilityAction(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('assign', 'notify')


class UUID(sgqlc.types.Scalar):
    __schema__ = schema


class UserContextViewType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('assigned',)


class UserFlagType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('all', 'analyticsWelcomeDismissed', 'canPlaySnake', 'canPlayTetris', 'commandMenuClearShortcutTip', 'completedOnboarding', 'cycleWelcomeDismissed', 'desktopDownloadToastDismissed', 'desktopInstalled', 'desktopTabsOnboardingDismissed', 'dueDateShortcutMigration', 'editorSlashCommandUsed', 'emptyActiveIssuesDismissed', 'emptyBacklogDismissed', 'emptyCustomViewsDismissed', 'emptyMyIssuesDismissed', 'emptyParagraphSlashCommandTip', 'figmaPluginBannerDismissed', 'figmaPromptDismissed', 'helpIslandFeatureInsightsDismissed', 'importBannerDismissed', 'initiativesBannerDismissed', 'insightsHelpDismissed', 'insightsWelcomeDismissed', 'issueLabelSuggestionUsed', 'issueMovePromptCompleted', 'joinTeamIntroductionDismissed', 'listSelectionTip', 'migrateThemePreference', 'milestoneOnboardingIsSeenAndDismissed', 'projectBacklogWelcomeDismissed', 'projectBoardOnboardingIsSeenAndDismissed', 'projectUpdatesWelcomeDismissed', 'projectWelcomeDismissed', 'pulseWelcomeDismissed', 'rewindBannerDismissed', 'slackCommentReactionTipShown', 'teamsPageIntroductionDismissed', 'threadedCommentsNudgeIsSeen', 'triageWelcomeDismissed', 'tryCyclesDismissed', 'tryGithubDismissed', 'tryInvitePeopleDismissed', 'tryRoadmapsDismissed', 'tryTriageDismissed', 'updatedSlackThreadSyncIntegration')


class UserFlagUpdateOperation(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('clear', 'decr', 'incr', 'lock')


class UserRoleType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('admin', 'app', 'guest', 'user')


class ViewPreferencesType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('organization', 'user')


class ViewType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('activeIssues', 'allIssues', 'archive', 'backlog', 'board', 'completedCycle', 'customRoadmap', 'customView', 'customViews', 'customer', 'customers', 'cycle', 'dashboards', 'embeddedCustomerNeeds', 'feedAll', 'feedCreated', 'feedFollowing', 'feedPopular', 'inbox', 'initiative', 'initiativeOverview', 'initiativeOverviewSubInitiatives', 'initiatives', 'initiativesCompleted', 'initiativesPlanned', 'issueIdentifiers', 'label', 'myIssues', 'myIssuesActivity', 'myIssuesCreatedByMe', 'myIssuesSubscribedTo', 'myReviews', 'project', 'projectCustomerNeeds', 'projectDocuments', 'projectLabel', 'projects', 'projectsAll', 'projectsBacklog', 'projectsClosed', 'quickView', 'reviews', 'roadmap', 'roadmapAll', 'roadmapBacklog', 'roadmapClosed', 'roadmaps', 'search', 'splitSearch', 'subIssues', 'teams', 'triage', 'userProfile', 'userProfileCreatedByUser', 'workspaceMembers')



########################################################################
# Input Objects
########################################################################
class AirbyteConfigurationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('api_key',)
    api_key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='apiKey')


class ApiKeyCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'label', 'key', 'team_ids', 'scope')
    id = sgqlc.types.Field(String, graphql_name='id')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    team_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='teamIds')
    scope = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='scope')


class ApiKeyUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('label', 'team_ids', 'scope')
    label = sgqlc.types.Field(String, graphql_name='label')
    team_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='teamIds')
    scope = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='scope')


class ApproximateNeedCountSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class AssigneeSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class AttachmentCollectionFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'title', 'subtitle', 'url', 'creator', 'source_type', 'and_', 'or_', 'some', 'every', 'length')
    id = sgqlc.types.Field('IDComparator', graphql_name='id')
    created_at = sgqlc.types.Field('DateComparator', graphql_name='createdAt')
    updated_at = sgqlc.types.Field('DateComparator', graphql_name='updatedAt')
    title = sgqlc.types.Field('StringComparator', graphql_name='title')
    subtitle = sgqlc.types.Field('NullableStringComparator', graphql_name='subtitle')
    url = sgqlc.types.Field('StringComparator', graphql_name='url')
    creator = sgqlc.types.Field('NullableUserFilter', graphql_name='creator')
    source_type = sgqlc.types.Field('SourceTypeComparator', graphql_name='sourceType')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('AttachmentCollectionFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('AttachmentCollectionFilter')), graphql_name='or')
    some = sgqlc.types.Field('AttachmentFilter', graphql_name='some')
    every = sgqlc.types.Field('AttachmentFilter', graphql_name='every')
    length = sgqlc.types.Field('NumberComparator', graphql_name='length')


class AttachmentCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'title', 'subtitle', 'url', 'issue_id', 'icon_url', 'metadata', 'group_by_source', 'comment_body', 'comment_body_data', 'create_as_user')
    id = sgqlc.types.Field(String, graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    subtitle = sgqlc.types.Field(String, graphql_name='subtitle')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='issueId')
    icon_url = sgqlc.types.Field(String, graphql_name='iconUrl')
    metadata = sgqlc.types.Field(JSONObject, graphql_name='metadata')
    group_by_source = sgqlc.types.Field(Boolean, graphql_name='groupBySource')
    comment_body = sgqlc.types.Field(String, graphql_name='commentBody')
    comment_body_data = sgqlc.types.Field(JSONObject, graphql_name='commentBodyData')
    create_as_user = sgqlc.types.Field(String, graphql_name='createAsUser')


class AttachmentFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'title', 'subtitle', 'url', 'creator', 'source_type', 'and_', 'or_')
    id = sgqlc.types.Field('IDComparator', graphql_name='id')
    created_at = sgqlc.types.Field('DateComparator', graphql_name='createdAt')
    updated_at = sgqlc.types.Field('DateComparator', graphql_name='updatedAt')
    title = sgqlc.types.Field('StringComparator', graphql_name='title')
    subtitle = sgqlc.types.Field('NullableStringComparator', graphql_name='subtitle')
    url = sgqlc.types.Field('StringComparator', graphql_name='url')
    creator = sgqlc.types.Field('NullableUserFilter', graphql_name='creator')
    source_type = sgqlc.types.Field('SourceTypeComparator', graphql_name='sourceType')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('AttachmentFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('AttachmentFilter')), graphql_name='or')


class AttachmentUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('title', 'subtitle', 'metadata', 'icon_url')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    subtitle = sgqlc.types.Field(String, graphql_name='subtitle')
    metadata = sgqlc.types.Field(JSONObject, graphql_name='metadata')
    icon_url = sgqlc.types.Field(String, graphql_name='iconUrl')


class AuditEntryFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'type', 'ip', 'country_code', 'actor', 'and_', 'or_')
    id = sgqlc.types.Field('IDComparator', graphql_name='id')
    created_at = sgqlc.types.Field('DateComparator', graphql_name='createdAt')
    updated_at = sgqlc.types.Field('DateComparator', graphql_name='updatedAt')
    type = sgqlc.types.Field('StringComparator', graphql_name='type')
    ip = sgqlc.types.Field('StringComparator', graphql_name='ip')
    country_code = sgqlc.types.Field('StringComparator', graphql_name='countryCode')
    actor = sgqlc.types.Field('NullableUserFilter', graphql_name='actor')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('AuditEntryFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('AuditEntryFilter')), graphql_name='or')


class BooleanComparator(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('eq', 'neq')
    eq = sgqlc.types.Field(Boolean, graphql_name='eq')
    neq = sgqlc.types.Field(Boolean, graphql_name='neq')


class CommentCollectionFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'body', 'user', 'issue', 'project_update', 'parent', 'document_content', 'reactions', 'needs', 'and_', 'or_', 'some', 'every', 'length')
    id = sgqlc.types.Field('IDComparator', graphql_name='id')
    created_at = sgqlc.types.Field('DateComparator', graphql_name='createdAt')
    updated_at = sgqlc.types.Field('DateComparator', graphql_name='updatedAt')
    body = sgqlc.types.Field('StringComparator', graphql_name='body')
    user = sgqlc.types.Field('UserFilter', graphql_name='user')
    issue = sgqlc.types.Field('NullableIssueFilter', graphql_name='issue')
    project_update = sgqlc.types.Field('NullableProjectUpdateFilter', graphql_name='projectUpdate')
    parent = sgqlc.types.Field('NullableCommentFilter', graphql_name='parent')
    document_content = sgqlc.types.Field('NullableDocumentContentFilter', graphql_name='documentContent')
    reactions = sgqlc.types.Field('ReactionCollectionFilter', graphql_name='reactions')
    needs = sgqlc.types.Field('CustomerNeedCollectionFilter', graphql_name='needs')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CommentCollectionFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CommentCollectionFilter')), graphql_name='or')
    some = sgqlc.types.Field('CommentFilter', graphql_name='some')
    every = sgqlc.types.Field('CommentFilter', graphql_name='every')
    length = sgqlc.types.Field('NumberComparator', graphql_name='length')


class CommentCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'body', 'body_data', 'issue_id', 'project_update_id', 'initiative_update_id', 'post_id', 'document_content_id', 'parent_id', 'create_as_user', 'display_icon_url', 'created_at', 'do_not_subscribe_to_issue', 'create_on_synced_slack_thread', 'quoted_text', 'subscriber_ids')
    id = sgqlc.types.Field(String, graphql_name='id')
    body = sgqlc.types.Field(String, graphql_name='body')
    body_data = sgqlc.types.Field(JSON, graphql_name='bodyData')
    issue_id = sgqlc.types.Field(String, graphql_name='issueId')
    project_update_id = sgqlc.types.Field(String, graphql_name='projectUpdateId')
    initiative_update_id = sgqlc.types.Field(String, graphql_name='initiativeUpdateId')
    post_id = sgqlc.types.Field(String, graphql_name='postId')
    document_content_id = sgqlc.types.Field(String, graphql_name='documentContentId')
    parent_id = sgqlc.types.Field(String, graphql_name='parentId')
    create_as_user = sgqlc.types.Field(String, graphql_name='createAsUser')
    display_icon_url = sgqlc.types.Field(String, graphql_name='displayIconUrl')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    do_not_subscribe_to_issue = sgqlc.types.Field(Boolean, graphql_name='doNotSubscribeToIssue')
    create_on_synced_slack_thread = sgqlc.types.Field(Boolean, graphql_name='createOnSyncedSlackThread')
    quoted_text = sgqlc.types.Field(String, graphql_name='quotedText')
    subscriber_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='subscriberIds')


class CommentFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'body', 'user', 'issue', 'project_update', 'parent', 'document_content', 'reactions', 'needs', 'and_', 'or_')
    id = sgqlc.types.Field('IDComparator', graphql_name='id')
    created_at = sgqlc.types.Field('DateComparator', graphql_name='createdAt')
    updated_at = sgqlc.types.Field('DateComparator', graphql_name='updatedAt')
    body = sgqlc.types.Field('StringComparator', graphql_name='body')
    user = sgqlc.types.Field('UserFilter', graphql_name='user')
    issue = sgqlc.types.Field('NullableIssueFilter', graphql_name='issue')
    project_update = sgqlc.types.Field('NullableProjectUpdateFilter', graphql_name='projectUpdate')
    parent = sgqlc.types.Field('NullableCommentFilter', graphql_name='parent')
    document_content = sgqlc.types.Field('NullableDocumentContentFilter', graphql_name='documentContent')
    reactions = sgqlc.types.Field('ReactionCollectionFilter', graphql_name='reactions')
    needs = sgqlc.types.Field('CustomerNeedCollectionFilter', graphql_name='needs')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CommentFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CommentFilter')), graphql_name='or')


class CommentUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('body', 'body_data', 'resolving_user_id', 'resolving_comment_id', 'quoted_text', 'subscriber_ids', 'do_not_subscribe_to_issue')
    body = sgqlc.types.Field(String, graphql_name='body')
    body_data = sgqlc.types.Field(JSON, graphql_name='bodyData')
    resolving_user_id = sgqlc.types.Field(String, graphql_name='resolvingUserId')
    resolving_comment_id = sgqlc.types.Field(String, graphql_name='resolvingCommentId')
    quoted_text = sgqlc.types.Field(String, graphql_name='quotedText')
    subscriber_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='subscriberIds')
    do_not_subscribe_to_issue = sgqlc.types.Field(Boolean, graphql_name='doNotSubscribeToIssue')


class CompletedAtSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class ContactCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('type', 'message', 'operating_system', 'browser', 'device', 'client_version', 'disappointment_rating')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')
    operating_system = sgqlc.types.Field(String, graphql_name='operatingSystem')
    browser = sgqlc.types.Field(String, graphql_name='browser')
    device = sgqlc.types.Field(String, graphql_name='device')
    client_version = sgqlc.types.Field(String, graphql_name='clientVersion')
    disappointment_rating = sgqlc.types.Field(Int, graphql_name='disappointmentRating')


class ContactSalesCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'email', 'company_size', 'message')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    company_size = sgqlc.types.Field(String, graphql_name='companySize')
    message = sgqlc.types.Field(String, graphql_name='message')


class ContentComparator(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('contains', 'not_contains')
    contains = sgqlc.types.Field(String, graphql_name='contains')
    not_contains = sgqlc.types.Field(String, graphql_name='notContains')


class CreateOrganizationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'url_key', 'domain_access', 'timezone', 'utm')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url_key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='urlKey')
    domain_access = sgqlc.types.Field(Boolean, graphql_name='domainAccess')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    utm = sgqlc.types.Field(String, graphql_name='utm')


class CreatedAtSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class CustomViewCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'description', 'icon', 'color', 'team_id', 'project_id', 'initiative_id', 'owner_id', 'filter_data', 'project_filter_data', 'feed_item_filter_data', 'shared')
    id = sgqlc.types.Field(String, graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    icon = sgqlc.types.Field(String, graphql_name='icon')
    color = sgqlc.types.Field(String, graphql_name='color')
    team_id = sgqlc.types.Field(String, graphql_name='teamId')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    initiative_id = sgqlc.types.Field(String, graphql_name='initiativeId')
    owner_id = sgqlc.types.Field(String, graphql_name='ownerId')
    filter_data = sgqlc.types.Field('IssueFilter', graphql_name='filterData')
    project_filter_data = sgqlc.types.Field('ProjectFilter', graphql_name='projectFilterData')
    feed_item_filter_data = sgqlc.types.Field('FeedItemFilter', graphql_name='feedItemFilterData')
    shared = sgqlc.types.Field(Boolean, graphql_name='shared')


class CustomViewUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'description', 'icon', 'color', 'team_id', 'project_id', 'initiative_id', 'owner_id', 'filter_data', 'project_filter_data', 'feed_item_filter_data', 'shared')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    icon = sgqlc.types.Field(String, graphql_name='icon')
    color = sgqlc.types.Field(String, graphql_name='color')
    team_id = sgqlc.types.Field(String, graphql_name='teamId')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    initiative_id = sgqlc.types.Field(String, graphql_name='initiativeId')
    owner_id = sgqlc.types.Field(String, graphql_name='ownerId')
    filter_data = sgqlc.types.Field('IssueFilter', graphql_name='filterData')
    project_filter_data = sgqlc.types.Field('ProjectFilter', graphql_name='projectFilterData')
    feed_item_filter_data = sgqlc.types.Field('FeedItemFilter', graphql_name='feedItemFilterData')
    shared = sgqlc.types.Field(Boolean, graphql_name='shared')


class CustomerCountSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class CustomerCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'domains', 'external_ids', 'slack_channel_id', 'owner_id', 'status_id', 'revenue', 'size', 'tier_id', 'logo_url', 'main_source_id')
    id = sgqlc.types.Field(String, graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    domains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='domains')
    external_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='externalIds')
    slack_channel_id = sgqlc.types.Field(String, graphql_name='slackChannelId')
    owner_id = sgqlc.types.Field(String, graphql_name='ownerId')
    status_id = sgqlc.types.Field(String, graphql_name='statusId')
    revenue = sgqlc.types.Field(Int, graphql_name='revenue')
    size = sgqlc.types.Field(Int, graphql_name='size')
    tier_id = sgqlc.types.Field(String, graphql_name='tierId')
    logo_url = sgqlc.types.Field(String, graphql_name='logoUrl')
    main_source_id = sgqlc.types.Field(String, graphql_name='mainSourceId')


class CustomerCreatedAtSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class CustomerFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'slack_channel_id', 'domains', 'external_ids', 'owner', 'needs', 'revenue', 'size', 'status', 'tier', 'and_', 'or_')
    id = sgqlc.types.Field('IDComparator', graphql_name='id')
    created_at = sgqlc.types.Field('DateComparator', graphql_name='createdAt')
    updated_at = sgqlc.types.Field('DateComparator', graphql_name='updatedAt')
    name = sgqlc.types.Field('StringComparator', graphql_name='name')
    slack_channel_id = sgqlc.types.Field('StringComparator', graphql_name='slackChannelId')
    domains = sgqlc.types.Field('StringArrayComparator', graphql_name='domains')
    external_ids = sgqlc.types.Field('StringArrayComparator', graphql_name='externalIds')
    owner = sgqlc.types.Field('NullableUserFilter', graphql_name='owner')
    needs = sgqlc.types.Field('CustomerNeedCollectionFilter', graphql_name='needs')
    revenue = sgqlc.types.Field('NumberComparator', graphql_name='revenue')
    size = sgqlc.types.Field('NumberComparator', graphql_name='size')
    status = sgqlc.types.Field('CustomerStatusFilter', graphql_name='status')
    tier = sgqlc.types.Field('CustomerTierFilter', graphql_name='tier')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CustomerFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CustomerFilter')), graphql_name='or')


class CustomerImportantCountSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class CustomerNeedCollectionFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'priority', 'project', 'issue', 'comment', 'customer', 'and_', 'or_', 'some', 'every', 'length')
    id = sgqlc.types.Field('IDComparator', graphql_name='id')
    created_at = sgqlc.types.Field('DateComparator', graphql_name='createdAt')
    updated_at = sgqlc.types.Field('DateComparator', graphql_name='updatedAt')
    priority = sgqlc.types.Field('NumberComparator', graphql_name='priority')
    project = sgqlc.types.Field('NullableProjectFilter', graphql_name='project')
    issue = sgqlc.types.Field('NullableIssueFilter', graphql_name='issue')
    comment = sgqlc.types.Field('NullableCommentFilter', graphql_name='comment')
    customer = sgqlc.types.Field('NullableCustomerFilter', graphql_name='customer')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CustomerNeedCollectionFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CustomerNeedCollectionFilter')), graphql_name='or')
    some = sgqlc.types.Field('CustomerNeedFilter', graphql_name='some')
    every = sgqlc.types.Field('CustomerNeedFilter', graphql_name='every')
    length = sgqlc.types.Field('NumberComparator', graphql_name='length')


class CustomerNeedCreateFromAttachmentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('attachment_id',)
    attachment_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='attachmentId')


class CustomerNeedCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'customer_id', 'customer_external_id', 'issue_id', 'project_id', 'comment_id', 'attachment_id', 'priority', 'body', 'body_data', 'attachment_url', 'create_as_user', 'display_icon_url')
    id = sgqlc.types.Field(String, graphql_name='id')
    customer_id = sgqlc.types.Field(String, graphql_name='customerId')
    customer_external_id = sgqlc.types.Field(String, graphql_name='customerExternalId')
    issue_id = sgqlc.types.Field(String, graphql_name='issueId')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    comment_id = sgqlc.types.Field(String, graphql_name='commentId')
    attachment_id = sgqlc.types.Field(String, graphql_name='attachmentId')
    priority = sgqlc.types.Field(Float, graphql_name='priority')
    body = sgqlc.types.Field(String, graphql_name='body')
    body_data = sgqlc.types.Field(JSON, graphql_name='bodyData')
    attachment_url = sgqlc.types.Field(String, graphql_name='attachmentUrl')
    create_as_user = sgqlc.types.Field(String, graphql_name='createAsUser')
    display_icon_url = sgqlc.types.Field(String, graphql_name='displayIconUrl')


class CustomerNeedFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'priority', 'project', 'issue', 'comment', 'customer', 'and_', 'or_')
    id = sgqlc.types.Field('IDComparator', graphql_name='id')
    created_at = sgqlc.types.Field('DateComparator', graphql_name='createdAt')
    updated_at = sgqlc.types.Field('DateComparator', graphql_name='updatedAt')
    priority = sgqlc.types.Field('NumberComparator', graphql_name='priority')
    project = sgqlc.types.Field('NullableProjectFilter', graphql_name='project')
    issue = sgqlc.types.Field('NullableIssueFilter', graphql_name='issue')
    comment = sgqlc.types.Field('NullableCommentFilter', graphql_name='comment')
    customer = sgqlc.types.Field('NullableCustomerFilter', graphql_name='customer')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CustomerNeedFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CustomerNeedFilter')), graphql_name='or')


class CustomerNeedUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'customer_id', 'customer_external_id', 'issue_id', 'project_id', 'priority', 'apply_priority_to_related_needs', 'body', 'body_data', 'attachment_url')
    id = sgqlc.types.Field(String, graphql_name='id')
    customer_id = sgqlc.types.Field(String, graphql_name='customerId')
    customer_external_id = sgqlc.types.Field(String, graphql_name='customerExternalId')
    issue_id = sgqlc.types.Field(String, graphql_name='issueId')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    priority = sgqlc.types.Field(Float, graphql_name='priority')
    apply_priority_to_related_needs = sgqlc.types.Field(Boolean, graphql_name='applyPriorityToRelatedNeeds')
    body = sgqlc.types.Field(String, graphql_name='body')
    body_data = sgqlc.types.Field(JSON, graphql_name='bodyData')
    attachment_url = sgqlc.types.Field(String, graphql_name='attachmentUrl')


class CustomerRevenueSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class CustomerSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class CustomerSortInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'created_at', 'owner', 'status', 'revenue', 'size', 'tier', 'approximate_need_count')
    name = sgqlc.types.Field('NameSort', graphql_name='name')
    created_at = sgqlc.types.Field(CustomerCreatedAtSort, graphql_name='createdAt')
    owner = sgqlc.types.Field('OwnerSort', graphql_name='owner')
    status = sgqlc.types.Field('CustomerStatusSort', graphql_name='status')
    revenue = sgqlc.types.Field('RevenueSort', graphql_name='revenue')
    size = sgqlc.types.Field('SizeSort', graphql_name='size')
    tier = sgqlc.types.Field('TierSort', graphql_name='tier')
    approximate_need_count = sgqlc.types.Field(ApproximateNeedCountSort, graphql_name='approximateNeedCount')


class CustomerStatusCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'color', 'description', 'position')
    id = sgqlc.types.Field(String, graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='color')
    description = sgqlc.types.Field(String, graphql_name='description')
    position = sgqlc.types.Field(Float, graphql_name='position')


class CustomerStatusFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'description', 'position', 'type', 'color', 'and_', 'or_')
    id = sgqlc.types.Field('IDComparator', graphql_name='id')
    created_at = sgqlc.types.Field('DateComparator', graphql_name='createdAt')
    updated_at = sgqlc.types.Field('DateComparator', graphql_name='updatedAt')
    name = sgqlc.types.Field('StringComparator', graphql_name='name')
    description = sgqlc.types.Field('StringComparator', graphql_name='description')
    position = sgqlc.types.Field('NumberComparator', graphql_name='position')
    type = sgqlc.types.Field('StringComparator', graphql_name='type')
    color = sgqlc.types.Field('StringComparator', graphql_name='color')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CustomerStatusFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CustomerStatusFilter')), graphql_name='or')


class CustomerStatusSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class CustomerStatusUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'color', 'description', 'position')
    name = sgqlc.types.Field(String, graphql_name='name')
    color = sgqlc.types.Field(String, graphql_name='color')
    description = sgqlc.types.Field(String, graphql_name='description')
    position = sgqlc.types.Field(Float, graphql_name='position')


class CustomerTierCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'color', 'description', 'position', 'display_name')
    id = sgqlc.types.Field(String, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='color')
    description = sgqlc.types.Field(String, graphql_name='description')
    position = sgqlc.types.Field(Float, graphql_name='position')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')


class CustomerTierFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'description', 'position', 'color', 'and_', 'or_')
    id = sgqlc.types.Field('IDComparator', graphql_name='id')
    created_at = sgqlc.types.Field('DateComparator', graphql_name='createdAt')
    updated_at = sgqlc.types.Field('DateComparator', graphql_name='updatedAt')
    name = sgqlc.types.Field('StringComparator', graphql_name='name')
    description = sgqlc.types.Field('StringComparator', graphql_name='description')
    position = sgqlc.types.Field('NumberComparator', graphql_name='position')
    color = sgqlc.types.Field('StringComparator', graphql_name='color')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CustomerTierFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CustomerTierFilter')), graphql_name='or')


class CustomerTierUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'color', 'description', 'position', 'display_name')
    name = sgqlc.types.Field(String, graphql_name='name')
    color = sgqlc.types.Field(String, graphql_name='color')
    description = sgqlc.types.Field(String, graphql_name='description')
    position = sgqlc.types.Field(Float, graphql_name='position')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')


class CustomerUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'domains', 'external_ids', 'slack_channel_id', 'owner_id', 'status_id', 'revenue', 'size', 'tier_id', 'logo_url', 'main_source_id')
    name = sgqlc.types.Field(String, graphql_name='name')
    domains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='domains')
    external_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='externalIds')
    slack_channel_id = sgqlc.types.Field(String, graphql_name='slackChannelId')
    owner_id = sgqlc.types.Field(String, graphql_name='ownerId')
    status_id = sgqlc.types.Field(String, graphql_name='statusId')
    revenue = sgqlc.types.Field(Int, graphql_name='revenue')
    size = sgqlc.types.Field(Int, graphql_name='size')
    tier_id = sgqlc.types.Field(String, graphql_name='tierId')
    logo_url = sgqlc.types.Field(String, graphql_name='logoUrl')
    main_source_id = sgqlc.types.Field(String, graphql_name='mainSourceId')


class CustomerUpsertInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'domains', 'external_id', 'slack_channel_id', 'owner_id', 'status_id', 'revenue', 'size', 'tier_id', 'logo_url', 'tier_name')
    id = sgqlc.types.Field(String, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    domains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='domains')
    external_id = sgqlc.types.Field(String, graphql_name='externalId')
    slack_channel_id = sgqlc.types.Field(String, graphql_name='slackChannelId')
    owner_id = sgqlc.types.Field(String, graphql_name='ownerId')
    status_id = sgqlc.types.Field(String, graphql_name='statusId')
    revenue = sgqlc.types.Field(Int, graphql_name='revenue')
    size = sgqlc.types.Field(Int, graphql_name='size')
    tier_id = sgqlc.types.Field(String, graphql_name='tierId')
    logo_url = sgqlc.types.Field(String, graphql_name='logoUrl')
    tier_name = sgqlc.types.Field(String, graphql_name='tierName')


class CycleCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'description', 'team_id', 'starts_at', 'ends_at', 'completed_at')
    id = sgqlc.types.Field(String, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    team_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='teamId')
    starts_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startsAt')
    ends_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='endsAt')
    completed_at = sgqlc.types.Field(DateTime, graphql_name='completedAt')


class CycleFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'number', 'name', 'starts_at', 'ends_at', 'completed_at', 'is_active', 'is_in_cooldown', 'is_next', 'is_previous', 'is_future', 'is_past', 'team', 'issues', 'and_', 'or_')
    id = sgqlc.types.Field('IDComparator', graphql_name='id')
    created_at = sgqlc.types.Field('DateComparator', graphql_name='createdAt')
    updated_at = sgqlc.types.Field('DateComparator', graphql_name='updatedAt')
    number = sgqlc.types.Field('NumberComparator', graphql_name='number')
    name = sgqlc.types.Field('StringComparator', graphql_name='name')
    starts_at = sgqlc.types.Field('DateComparator', graphql_name='startsAt')
    ends_at = sgqlc.types.Field('DateComparator', graphql_name='endsAt')
    completed_at = sgqlc.types.Field('DateComparator', graphql_name='completedAt')
    is_active = sgqlc.types.Field(BooleanComparator, graphql_name='isActive')
    is_in_cooldown = sgqlc.types.Field(BooleanComparator, graphql_name='isInCooldown')
    is_next = sgqlc.types.Field(BooleanComparator, graphql_name='isNext')
    is_previous = sgqlc.types.Field(BooleanComparator, graphql_name='isPrevious')
    is_future = sgqlc.types.Field(BooleanComparator, graphql_name='isFuture')
    is_past = sgqlc.types.Field(BooleanComparator, graphql_name='isPast')
    team = sgqlc.types.Field('TeamFilter', graphql_name='team')
    issues = sgqlc.types.Field('IssueCollectionFilter', graphql_name='issues')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CycleFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CycleFilter')), graphql_name='or')


class CyclePeriodComparator(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('eq', 'neq', 'in_', 'nin', 'null')
    eq = sgqlc.types.Field(CyclePeriod, graphql_name='eq')
    neq = sgqlc.types.Field(CyclePeriod, graphql_name='neq')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CyclePeriod)), graphql_name='in')
    nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CyclePeriod)), graphql_name='nin')
    null = sgqlc.types.Field(Boolean, graphql_name='null')


class CycleShiftAllInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'days_to_shift')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    days_to_shift = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='daysToShift')


class CycleSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order', 'current_cycle_first')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')
    current_cycle_first = sgqlc.types.Field(Boolean, graphql_name='currentCycleFirst')


class CycleUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'description', 'starts_at', 'ends_at', 'completed_at')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    starts_at = sgqlc.types.Field(DateTime, graphql_name='startsAt')
    ends_at = sgqlc.types.Field(DateTime, graphql_name='endsAt')
    completed_at = sgqlc.types.Field(DateTime, graphql_name='completedAt')


class DateComparator(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('eq', 'neq', 'in_', 'nin', 'lt', 'lte', 'gt', 'gte')
    eq = sgqlc.types.Field(DateTimeOrDuration, graphql_name='eq')
    neq = sgqlc.types.Field(DateTimeOrDuration, graphql_name='neq')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DateTimeOrDuration)), graphql_name='in')
    nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DateTimeOrDuration)), graphql_name='nin')
    lt = sgqlc.types.Field(DateTimeOrDuration, graphql_name='lt')
    lte = sgqlc.types.Field(DateTimeOrDuration, graphql_name='lte')
    gt = sgqlc.types.Field(DateTimeOrDuration, graphql_name='gt')
    gte = sgqlc.types.Field(DateTimeOrDuration, graphql_name='gte')


class DeleteOrganizationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('deletion_code',)
    deletion_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deletionCode')


class DocumentCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'title', 'icon', 'color', 'content', 'project_id', 'initiative_id', 'team_id', 'resource_folder_id', 'last_applied_template_id', 'sort_order', 'subscriber_ids')
    id = sgqlc.types.Field(String, graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    icon = sgqlc.types.Field(String, graphql_name='icon')
    color = sgqlc.types.Field(String, graphql_name='color')
    content = sgqlc.types.Field(String, graphql_name='content')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    initiative_id = sgqlc.types.Field(String, graphql_name='initiativeId')
    team_id = sgqlc.types.Field(String, graphql_name='teamId')
    resource_folder_id = sgqlc.types.Field(String, graphql_name='resourceFolderId')
    last_applied_template_id = sgqlc.types.Field(String, graphql_name='lastAppliedTemplateId')
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')
    subscriber_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='subscriberIds')


class DocumentFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'title', 'slug_id', 'creator', 'project', 'initiative', 'and_', 'or_')
    id = sgqlc.types.Field('IDComparator', graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    title = sgqlc.types.Field('StringComparator', graphql_name='title')
    slug_id = sgqlc.types.Field('StringComparator', graphql_name='slugId')
    creator = sgqlc.types.Field('UserFilter', graphql_name='creator')
    project = sgqlc.types.Field('ProjectFilter', graphql_name='project')
    initiative = sgqlc.types.Field('InitiativeFilter', graphql_name='initiative')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DocumentFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DocumentFilter')), graphql_name='or')


class DocumentUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('title', 'icon', 'color', 'content', 'project_id', 'initiative_id', 'team_id', 'resource_folder_id', 'last_applied_template_id', 'hidden_at', 'sort_order', 'trashed', 'subscriber_ids')
    title = sgqlc.types.Field(String, graphql_name='title')
    icon = sgqlc.types.Field(String, graphql_name='icon')
    color = sgqlc.types.Field(String, graphql_name='color')
    content = sgqlc.types.Field(String, graphql_name='content')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    initiative_id = sgqlc.types.Field(String, graphql_name='initiativeId')
    team_id = sgqlc.types.Field(String, graphql_name='teamId')
    resource_folder_id = sgqlc.types.Field(String, graphql_name='resourceFolderId')
    last_applied_template_id = sgqlc.types.Field(String, graphql_name='lastAppliedTemplateId')
    hidden_at = sgqlc.types.Field(DateTime, graphql_name='hiddenAt')
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')
    trashed = sgqlc.types.Field(Boolean, graphql_name='trashed')
    subscriber_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='subscriberIds')


class DueDateSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class EmailIntakeAddressCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'team_id', 'template_id')
    id = sgqlc.types.Field(String, graphql_name='id')
    team_id = sgqlc.types.Field(String, graphql_name='teamId')
    template_id = sgqlc.types.Field(String, graphql_name='templateId')


class EmailIntakeAddressUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('enabled', 'replies_enabled', 'customer_requests_enabled')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    replies_enabled = sgqlc.types.Field(Boolean, graphql_name='repliesEnabled')
    customer_requests_enabled = sgqlc.types.Field(Boolean, graphql_name='customerRequestsEnabled')


class EmailUnsubscribeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('type', 'token', 'user_id')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    token = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='token')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userId')


class EmailUserAccountAuthChallengeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('email', 'is_desktop', 'client_auth_code', 'invite_link', 'login_code_only')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    is_desktop = sgqlc.types.Field(Boolean, graphql_name='isDesktop')
    client_auth_code = sgqlc.types.Field(String, graphql_name='clientAuthCode')
    invite_link = sgqlc.types.Field(String, graphql_name='inviteLink')
    login_code_only = sgqlc.types.Field(Boolean, graphql_name='loginCodeOnly')


class EmojiCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'url')
    id = sgqlc.types.Field(String, graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class EntityExternalLinkCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'url', 'label', 'initiative_id', 'project_id', 'team_id', 'resource_folder_id', 'sort_order')
    id = sgqlc.types.Field(String, graphql_name='id')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    initiative_id = sgqlc.types.Field(String, graphql_name='initiativeId')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    team_id = sgqlc.types.Field(String, graphql_name='teamId')
    resource_folder_id = sgqlc.types.Field(String, graphql_name='resourceFolderId')
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')


class EntityExternalLinkUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('url', 'label', 'sort_order', 'resource_folder_id')
    url = sgqlc.types.Field(String, graphql_name='url')
    label = sgqlc.types.Field(String, graphql_name='label')
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')
    resource_folder_id = sgqlc.types.Field(String, graphql_name='resourceFolderId')


class EstimateComparator(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('eq', 'neq', 'in_', 'nin', 'null', 'lt', 'lte', 'gt', 'gte', 'or_', 'and_')
    eq = sgqlc.types.Field(Float, graphql_name='eq')
    neq = sgqlc.types.Field(Float, graphql_name='neq')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Float)), graphql_name='in')
    nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Float)), graphql_name='nin')
    null = sgqlc.types.Field(Boolean, graphql_name='null')
    lt = sgqlc.types.Field(Float, graphql_name='lt')
    lte = sgqlc.types.Field(Float, graphql_name='lte')
    gt = sgqlc.types.Field(Float, graphql_name='gt')
    gte = sgqlc.types.Field(Float, graphql_name='gte')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NullableNumberComparator')), graphql_name='or')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NullableNumberComparator')), graphql_name='and')


class EstimateSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class FavoriteCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'folder_name', 'parent_id', 'issue_id', 'facet_id', 'project_id', 'project_tab', 'predefined_view_type', 'predefined_view_team_id', 'cycle_id', 'custom_view_id', 'document_id', 'roadmap_id', 'initiative_id', 'initiative_tab', 'label_id', 'project_label_id', 'user_id', 'sort_order', 'customer_id', 'dashboard_id')
    id = sgqlc.types.Field(String, graphql_name='id')
    folder_name = sgqlc.types.Field(String, graphql_name='folderName')
    parent_id = sgqlc.types.Field(String, graphql_name='parentId')
    issue_id = sgqlc.types.Field(String, graphql_name='issueId')
    facet_id = sgqlc.types.Field(String, graphql_name='facetId')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    project_tab = sgqlc.types.Field(ProjectTab, graphql_name='projectTab')
    predefined_view_type = sgqlc.types.Field(String, graphql_name='predefinedViewType')
    predefined_view_team_id = sgqlc.types.Field(String, graphql_name='predefinedViewTeamId')
    cycle_id = sgqlc.types.Field(String, graphql_name='cycleId')
    custom_view_id = sgqlc.types.Field(String, graphql_name='customViewId')
    document_id = sgqlc.types.Field(String, graphql_name='documentId')
    roadmap_id = sgqlc.types.Field(String, graphql_name='roadmapId')
    initiative_id = sgqlc.types.Field(String, graphql_name='initiativeId')
    initiative_tab = sgqlc.types.Field(InitiativeTab, graphql_name='initiativeTab')
    label_id = sgqlc.types.Field(String, graphql_name='labelId')
    project_label_id = sgqlc.types.Field(String, graphql_name='projectLabelId')
    user_id = sgqlc.types.Field(String, graphql_name='userId')
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')
    customer_id = sgqlc.types.Field(String, graphql_name='customerId')
    dashboard_id = sgqlc.types.Field(String, graphql_name='dashboardId')


class FavoriteUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('sort_order', 'parent_id', 'folder_name')
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')
    parent_id = sgqlc.types.Field(String, graphql_name='parentId')
    folder_name = sgqlc.types.Field(String, graphql_name='folderName')


class FeedItemFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'author', 'update_type', 'update_health', 'project_update', 'related_initiatives', 'related_teams', 'and_', 'or_')
    id = sgqlc.types.Field('IDComparator', graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    author = sgqlc.types.Field('UserFilter', graphql_name='author')
    update_type = sgqlc.types.Field('StringComparator', graphql_name='updateType')
    update_health = sgqlc.types.Field('StringComparator', graphql_name='updateHealth')
    project_update = sgqlc.types.Field('ProjectUpdateFilter', graphql_name='projectUpdate')
    related_initiatives = sgqlc.types.Field('InitiativeCollectionFilter', graphql_name='relatedInitiatives')
    related_teams = sgqlc.types.Field('TeamCollectionFilter', graphql_name='relatedTeams')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('FeedItemFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('FeedItemFilter')), graphql_name='or')


class FrontSettingsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('send_note_on_status_change', 'send_note_on_comment', 'automate_ticket_reopening_on_completion', 'automate_ticket_reopening_on_cancellation', 'automate_ticket_reopening_on_comment')
    send_note_on_status_change = sgqlc.types.Field(Boolean, graphql_name='sendNoteOnStatusChange')
    send_note_on_comment = sgqlc.types.Field(Boolean, graphql_name='sendNoteOnComment')
    automate_ticket_reopening_on_completion = sgqlc.types.Field(Boolean, graphql_name='automateTicketReopeningOnCompletion')
    automate_ticket_reopening_on_cancellation = sgqlc.types.Field(Boolean, graphql_name='automateTicketReopeningOnCancellation')
    automate_ticket_reopening_on_comment = sgqlc.types.Field(Boolean, graphql_name='automateTicketReopeningOnComment')


class GitAutomationStateCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'team_id', 'state_id', 'target_branch_id', 'event')
    id = sgqlc.types.Field(String, graphql_name='id')
    team_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='teamId')
    state_id = sgqlc.types.Field(String, graphql_name='stateId')
    target_branch_id = sgqlc.types.Field(String, graphql_name='targetBranchId')
    event = sgqlc.types.Field(sgqlc.types.non_null(GitAutomationStates), graphql_name='event')


class GitAutomationStateUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('state_id', 'target_branch_id', 'event')
    state_id = sgqlc.types.Field(String, graphql_name='stateId')
    target_branch_id = sgqlc.types.Field(String, graphql_name='targetBranchId')
    event = sgqlc.types.Field(GitAutomationStates, graphql_name='event')


class GitAutomationTargetBranchCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'team_id', 'branch_pattern', 'is_regex')
    id = sgqlc.types.Field(String, graphql_name='id')
    team_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='teamId')
    branch_pattern = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='branchPattern')
    is_regex = sgqlc.types.Field(Boolean, graphql_name='isRegex')


class GitAutomationTargetBranchUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('branch_pattern', 'is_regex')
    branch_pattern = sgqlc.types.Field(String, graphql_name='branchPattern')
    is_regex = sgqlc.types.Field(Boolean, graphql_name='isRegex')


class GitHubImportSettingsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('org_login', 'org_avatar_url', 'repositories', 'labels', 'org_type')
    org_login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='orgLogin')
    org_avatar_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='orgAvatarUrl')
    repositories = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GitHubRepoInput'))), graphql_name='repositories')
    labels = sgqlc.types.Field(JSONObject, graphql_name='labels')
    org_type = sgqlc.types.Field(sgqlc.types.non_null(GithubOrgType), graphql_name='orgType')


class GitHubPersonalSettingsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('login',)
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')


class GitHubRepoInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'full_name', 'archived')
    id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='id')
    full_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fullName')
    archived = sgqlc.types.Field(Boolean, graphql_name='archived')


class GitHubRepoMappingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'linear_team_id', 'git_hub_repo_id', 'git_hub_labels', 'bidirectional', 'default')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    linear_team_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='linearTeamId')
    git_hub_repo_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='gitHubRepoId')
    git_hub_labels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='gitHubLabels')
    bidirectional = sgqlc.types.Field(Boolean, graphql_name='bidirectional')
    default = sgqlc.types.Field(Boolean, graphql_name='default')


class GitHubSettingsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('pull_request_review_tool', 'org_avatar_url', 'org_login', 'repositories', 'repositories_mapping', 'org_type')
    pull_request_review_tool = sgqlc.types.Field(PullRequestReviewTool, graphql_name='pullRequestReviewTool')
    org_avatar_url = sgqlc.types.Field(String, graphql_name='orgAvatarUrl')
    org_login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='orgLogin')
    repositories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GitHubRepoInput)), graphql_name='repositories')
    repositories_mapping = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GitHubRepoMappingInput)), graphql_name='repositoriesMapping')
    org_type = sgqlc.types.Field(GithubOrgType, graphql_name='orgType')


class GitLabSettingsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('url', 'readonly', 'expires_at')
    url = sgqlc.types.Field(String, graphql_name='url')
    readonly = sgqlc.types.Field(Boolean, graphql_name='readonly')
    expires_at = sgqlc.types.Field(String, graphql_name='expiresAt')


class GoogleSheetsExportSettings(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('enabled', 'spreadsheet_id', 'spreadsheet_url', 'sheet_id', 'updated_at')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    spreadsheet_id = sgqlc.types.Field(String, graphql_name='spreadsheetId')
    spreadsheet_url = sgqlc.types.Field(String, graphql_name='spreadsheetUrl')
    sheet_id = sgqlc.types.Field(Float, graphql_name='sheetId')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')


class GoogleSheetsSettingsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('spreadsheet_id', 'spreadsheet_url', 'sheet_id', 'updated_issues_at', 'issue', 'project')
    spreadsheet_id = sgqlc.types.Field(String, graphql_name='spreadsheetId')
    spreadsheet_url = sgqlc.types.Field(String, graphql_name='spreadsheetUrl')
    sheet_id = sgqlc.types.Field(Float, graphql_name='sheetId')
    updated_issues_at = sgqlc.types.Field(DateTime, graphql_name='updatedIssuesAt')
    issue = sgqlc.types.Field(GoogleSheetsExportSettings, graphql_name='issue')
    project = sgqlc.types.Field(GoogleSheetsExportSettings, graphql_name='project')


class GoogleUserAccountAuthInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('code', 'redirect_uri', 'timezone', 'invite_link', 'disallow_signup')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    redirect_uri = sgqlc.types.Field(String, graphql_name='redirectUri')
    timezone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='timezone')
    invite_link = sgqlc.types.Field(String, graphql_name='inviteLink')
    disallow_signup = sgqlc.types.Field(Boolean, graphql_name='disallowSignup')


class IDComparator(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('eq', 'neq', 'in_', 'nin')
    eq = sgqlc.types.Field(ID, graphql_name='eq')
    neq = sgqlc.types.Field(ID, graphql_name='neq')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='in')
    nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='nin')


class InheritanceEntityMapping(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('workflow_states', 'issue_labels')
    workflow_states = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='workflowStates')
    issue_labels = sgqlc.types.Field(JSONObject, graphql_name='issueLabels')


class InitiativeCollectionFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'slug_id', 'status', 'creator', 'owner', 'health', 'health_with_age', 'ancestors', 'and_', 'or_', 'some', 'every', 'length')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    name = sgqlc.types.Field('StringComparator', graphql_name='name')
    slug_id = sgqlc.types.Field('StringComparator', graphql_name='slugId')
    status = sgqlc.types.Field('StringComparator', graphql_name='status')
    creator = sgqlc.types.Field('UserFilter', graphql_name='creator')
    owner = sgqlc.types.Field('UserFilter', graphql_name='owner')
    health = sgqlc.types.Field('StringComparator', graphql_name='health')
    health_with_age = sgqlc.types.Field('StringComparator', graphql_name='healthWithAge')
    ancestors = sgqlc.types.Field('InitiativeCollectionFilter', graphql_name='ancestors')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('InitiativeCollectionFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('InitiativeCollectionFilter')), graphql_name='or')
    some = sgqlc.types.Field('InitiativeFilter', graphql_name='some')
    every = sgqlc.types.Field('InitiativeFilter', graphql_name='every')
    length = sgqlc.types.Field('NumberComparator', graphql_name='length')


class InitiativeCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'description', 'owner_id', 'sort_order', 'color', 'icon', 'status', 'target_date', 'target_date_resolution', 'content')
    id = sgqlc.types.Field(String, graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    owner_id = sgqlc.types.Field(String, graphql_name='ownerId')
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')
    color = sgqlc.types.Field(String, graphql_name='color')
    icon = sgqlc.types.Field(String, graphql_name='icon')
    status = sgqlc.types.Field(InitiativeStatus, graphql_name='status')
    target_date = sgqlc.types.Field(TimelessDate, graphql_name='targetDate')
    target_date_resolution = sgqlc.types.Field(DateResolutionType, graphql_name='targetDateResolution')
    content = sgqlc.types.Field(String, graphql_name='content')


class InitiativeFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'slug_id', 'status', 'creator', 'owner', 'health', 'health_with_age', 'ancestors', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    name = sgqlc.types.Field('StringComparator', graphql_name='name')
    slug_id = sgqlc.types.Field('StringComparator', graphql_name='slugId')
    status = sgqlc.types.Field('StringComparator', graphql_name='status')
    creator = sgqlc.types.Field('UserFilter', graphql_name='creator')
    owner = sgqlc.types.Field('UserFilter', graphql_name='owner')
    health = sgqlc.types.Field('StringComparator', graphql_name='health')
    health_with_age = sgqlc.types.Field('StringComparator', graphql_name='healthWithAge')
    ancestors = sgqlc.types.Field(InitiativeCollectionFilter, graphql_name='ancestors')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('InitiativeFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('InitiativeFilter')), graphql_name='or')


class InitiativeRelationCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'initiative_id', 'related_initiative_id', 'sort_order')
    id = sgqlc.types.Field(String, graphql_name='id')
    initiative_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='initiativeId')
    related_initiative_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='relatedInitiativeId')
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')


class InitiativeRelationUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('sort_order',)
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')


class InitiativeToProjectCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'project_id', 'initiative_id', 'sort_order')
    id = sgqlc.types.Field(String, graphql_name='id')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')
    initiative_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='initiativeId')
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')


class InitiativeToProjectUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('sort_order',)
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')


class InitiativeUpdateCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'body', 'body_data', 'health', 'initiative_id', 'is_diff_hidden')
    id = sgqlc.types.Field(String, graphql_name='id')
    body = sgqlc.types.Field(String, graphql_name='body')
    body_data = sgqlc.types.Field(JSON, graphql_name='bodyData')
    health = sgqlc.types.Field(InitiativeUpdateHealthType, graphql_name='health')
    initiative_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='initiativeId')
    is_diff_hidden = sgqlc.types.Field(Boolean, graphql_name='isDiffHidden')


class InitiativeUpdateFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'user', 'initiative', 'reactions', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    user = sgqlc.types.Field('UserFilter', graphql_name='user')
    initiative = sgqlc.types.Field(InitiativeFilter, graphql_name='initiative')
    reactions = sgqlc.types.Field('ReactionCollectionFilter', graphql_name='reactions')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('InitiativeUpdateFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('InitiativeUpdateFilter')), graphql_name='or')


class InitiativeUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'description', 'owner_id', 'sort_order', 'color', 'icon', 'target_date', 'status', 'target_date_resolution', 'trashed', 'content', 'update_reminder_frequency_in_weeks', 'update_reminder_frequency', 'frequency_resolution', 'update_reminders_day', 'update_reminders_hour')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    owner_id = sgqlc.types.Field(String, graphql_name='ownerId')
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')
    color = sgqlc.types.Field(String, graphql_name='color')
    icon = sgqlc.types.Field(String, graphql_name='icon')
    target_date = sgqlc.types.Field(TimelessDate, graphql_name='targetDate')
    status = sgqlc.types.Field(InitiativeStatus, graphql_name='status')
    target_date_resolution = sgqlc.types.Field(DateResolutionType, graphql_name='targetDateResolution')
    trashed = sgqlc.types.Field(Boolean, graphql_name='trashed')
    content = sgqlc.types.Field(String, graphql_name='content')
    update_reminder_frequency_in_weeks = sgqlc.types.Field(Float, graphql_name='updateReminderFrequencyInWeeks')
    update_reminder_frequency = sgqlc.types.Field(Float, graphql_name='updateReminderFrequency')
    frequency_resolution = sgqlc.types.Field(FrequencyResolutionType, graphql_name='frequencyResolution')
    update_reminders_day = sgqlc.types.Field(Day, graphql_name='updateRemindersDay')
    update_reminders_hour = sgqlc.types.Field(Int, graphql_name='updateRemindersHour')


class InitiativeUpdateUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('body', 'body_data', 'health', 'is_diff_hidden')
    body = sgqlc.types.Field(String, graphql_name='body')
    body_data = sgqlc.types.Field(JSON, graphql_name='bodyData')
    health = sgqlc.types.Field(InitiativeUpdateHealthType, graphql_name='health')
    is_diff_hidden = sgqlc.types.Field(Boolean, graphql_name='isDiffHidden')


class IntegrationRequestInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('email', 'name')
    email = sgqlc.types.Field(String, graphql_name='email')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IntegrationSettingsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('slack', 'slack_asks', 'slack_post', 'slack_project_post', 'slack_initiative_post', 'slack_custom_view_notifications', 'slack_org_project_updates_post', 'slack_org_initiative_updates_post', 'google_sheets', 'git_hub', 'git_hub_import', 'git_hub_personal', 'git_lab', 'sentry', 'zendesk', 'intercom', 'front', 'jira', 'notion', 'opsgenie', 'pager_duty', 'launch_darkly', 'jira_personal', 'salesforce')
    slack = sgqlc.types.Field('SlackSettingsInput', graphql_name='slack')
    slack_asks = sgqlc.types.Field('SlackAsksSettingsInput', graphql_name='slackAsks')
    slack_post = sgqlc.types.Field('SlackPostSettingsInput', graphql_name='slackPost')
    slack_project_post = sgqlc.types.Field('SlackPostSettingsInput', graphql_name='slackProjectPost')
    slack_initiative_post = sgqlc.types.Field('SlackPostSettingsInput', graphql_name='slackInitiativePost')
    slack_custom_view_notifications = sgqlc.types.Field('SlackPostSettingsInput', graphql_name='slackCustomViewNotifications')
    slack_org_project_updates_post = sgqlc.types.Field('SlackPostSettingsInput', graphql_name='slackOrgProjectUpdatesPost')
    slack_org_initiative_updates_post = sgqlc.types.Field('SlackPostSettingsInput', graphql_name='slackOrgInitiativeUpdatesPost')
    google_sheets = sgqlc.types.Field(GoogleSheetsSettingsInput, graphql_name='googleSheets')
    git_hub = sgqlc.types.Field(GitHubSettingsInput, graphql_name='gitHub')
    git_hub_import = sgqlc.types.Field(GitHubImportSettingsInput, graphql_name='gitHubImport')
    git_hub_personal = sgqlc.types.Field(GitHubPersonalSettingsInput, graphql_name='gitHubPersonal')
    git_lab = sgqlc.types.Field(GitLabSettingsInput, graphql_name='gitLab')
    sentry = sgqlc.types.Field('SentrySettingsInput', graphql_name='sentry')
    zendesk = sgqlc.types.Field('ZendeskSettingsInput', graphql_name='zendesk')
    intercom = sgqlc.types.Field('IntercomSettingsInput', graphql_name='intercom')
    front = sgqlc.types.Field(FrontSettingsInput, graphql_name='front')
    jira = sgqlc.types.Field('JiraSettingsInput', graphql_name='jira')
    notion = sgqlc.types.Field('NotionSettingsInput', graphql_name='notion')
    opsgenie = sgqlc.types.Field('OpsgenieInput', graphql_name='opsgenie')
    pager_duty = sgqlc.types.Field('PagerDutyInput', graphql_name='pagerDuty')
    launch_darkly = sgqlc.types.Field('LaunchDarklySettingsInput', graphql_name='launchDarkly')
    jira_personal = sgqlc.types.Field('JiraPersonalSettingsInput', graphql_name='jiraPersonal')
    salesforce = sgqlc.types.Field('SalesforceSettingsInput', graphql_name='salesforce')


class IntegrationTemplateCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'integration_id', 'template_id', 'foreign_entity_id')
    id = sgqlc.types.Field(String, graphql_name='id')
    integration_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='integrationId')
    template_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='templateId')
    foreign_entity_id = sgqlc.types.Field(String, graphql_name='foreignEntityId')


class IntegrationUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('settings',)
    settings = sgqlc.types.Field(IntegrationSettingsInput, graphql_name='settings')


class IntegrationsSettingsCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('slack_issue_created', 'slack_issue_added_to_view', 'slack_issue_new_comment', 'slack_issue_status_changed_done', 'slack_issue_status_changed_all', 'slack_project_update_created', 'slack_project_update_created_to_team', 'slack_project_update_created_to_workspace', 'slack_initiative_update_created', 'slack_issue_added_to_triage', 'slack_issue_sla_high_risk', 'slack_issue_sla_breached', 'id', 'team_id', 'project_id', 'initiative_id', 'custom_view_id', 'context_view_type')
    slack_issue_created = sgqlc.types.Field(Boolean, graphql_name='slackIssueCreated')
    slack_issue_added_to_view = sgqlc.types.Field(Boolean, graphql_name='slackIssueAddedToView')
    slack_issue_new_comment = sgqlc.types.Field(Boolean, graphql_name='slackIssueNewComment')
    slack_issue_status_changed_done = sgqlc.types.Field(Boolean, graphql_name='slackIssueStatusChangedDone')
    slack_issue_status_changed_all = sgqlc.types.Field(Boolean, graphql_name='slackIssueStatusChangedAll')
    slack_project_update_created = sgqlc.types.Field(Boolean, graphql_name='slackProjectUpdateCreated')
    slack_project_update_created_to_team = sgqlc.types.Field(Boolean, graphql_name='slackProjectUpdateCreatedToTeam')
    slack_project_update_created_to_workspace = sgqlc.types.Field(Boolean, graphql_name='slackProjectUpdateCreatedToWorkspace')
    slack_initiative_update_created = sgqlc.types.Field(Boolean, graphql_name='slackInitiativeUpdateCreated')
    slack_issue_added_to_triage = sgqlc.types.Field(Boolean, graphql_name='slackIssueAddedToTriage')
    slack_issue_sla_high_risk = sgqlc.types.Field(Boolean, graphql_name='slackIssueSlaHighRisk')
    slack_issue_sla_breached = sgqlc.types.Field(Boolean, graphql_name='slackIssueSlaBreached')
    id = sgqlc.types.Field(String, graphql_name='id')
    team_id = sgqlc.types.Field(String, graphql_name='teamId')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    initiative_id = sgqlc.types.Field(String, graphql_name='initiativeId')
    custom_view_id = sgqlc.types.Field(String, graphql_name='customViewId')
    context_view_type = sgqlc.types.Field(ContextViewType, graphql_name='contextViewType')


class IntegrationsSettingsUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('slack_issue_created', 'slack_issue_added_to_view', 'slack_issue_new_comment', 'slack_issue_status_changed_done', 'slack_issue_status_changed_all', 'slack_project_update_created', 'slack_project_update_created_to_team', 'slack_project_update_created_to_workspace', 'slack_initiative_update_created', 'slack_issue_added_to_triage', 'slack_issue_sla_high_risk', 'slack_issue_sla_breached')
    slack_issue_created = sgqlc.types.Field(Boolean, graphql_name='slackIssueCreated')
    slack_issue_added_to_view = sgqlc.types.Field(Boolean, graphql_name='slackIssueAddedToView')
    slack_issue_new_comment = sgqlc.types.Field(Boolean, graphql_name='slackIssueNewComment')
    slack_issue_status_changed_done = sgqlc.types.Field(Boolean, graphql_name='slackIssueStatusChangedDone')
    slack_issue_status_changed_all = sgqlc.types.Field(Boolean, graphql_name='slackIssueStatusChangedAll')
    slack_project_update_created = sgqlc.types.Field(Boolean, graphql_name='slackProjectUpdateCreated')
    slack_project_update_created_to_team = sgqlc.types.Field(Boolean, graphql_name='slackProjectUpdateCreatedToTeam')
    slack_project_update_created_to_workspace = sgqlc.types.Field(Boolean, graphql_name='slackProjectUpdateCreatedToWorkspace')
    slack_initiative_update_created = sgqlc.types.Field(Boolean, graphql_name='slackInitiativeUpdateCreated')
    slack_issue_added_to_triage = sgqlc.types.Field(Boolean, graphql_name='slackIssueAddedToTriage')
    slack_issue_sla_high_risk = sgqlc.types.Field(Boolean, graphql_name='slackIssueSlaHighRisk')
    slack_issue_sla_breached = sgqlc.types.Field(Boolean, graphql_name='slackIssueSlaBreached')


class IntercomSettingsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('send_note_on_status_change', 'send_note_on_comment', 'automate_ticket_reopening_on_completion', 'automate_ticket_reopening_on_cancellation', 'automate_ticket_reopening_on_comment')
    send_note_on_status_change = sgqlc.types.Field(Boolean, graphql_name='sendNoteOnStatusChange')
    send_note_on_comment = sgqlc.types.Field(Boolean, graphql_name='sendNoteOnComment')
    automate_ticket_reopening_on_completion = sgqlc.types.Field(Boolean, graphql_name='automateTicketReopeningOnCompletion')
    automate_ticket_reopening_on_cancellation = sgqlc.types.Field(Boolean, graphql_name='automateTicketReopeningOnCancellation')
    automate_ticket_reopening_on_comment = sgqlc.types.Field(Boolean, graphql_name='automateTicketReopeningOnComment')


class IssueBatchCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('issues',)
    issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueCreateInput'))), graphql_name='issues')


class IssueCollectionFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'number', 'title', 'description', 'priority', 'estimate', 'started_at', 'triaged_at', 'completed_at', 'canceled_at', 'archived_at', 'auto_closed_at', 'auto_archived_at', 'added_to_cycle_at', 'added_to_cycle_period', 'due_date', 'snoozed_until_at', 'assignee', 'last_applied_template', 'recurring_issue_template', 'source_metadata', 'creator', 'parent', 'snoozed_by', 'labels', 'subscribers', 'team', 'project_milestone', 'comments', 'cycle', 'project', 'state', 'children', 'attachments', 'searchable_content', 'has_related_relations', 'has_duplicate_relations', 'has_blocked_by_relations', 'has_blocking_relations', 'sla_status', 'reactions', 'needs', 'customer_count', 'lead_time', 'cycle_time', 'age_time', 'triage_time', 'and_', 'or_', 'some', 'every', 'length')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    number = sgqlc.types.Field('NumberComparator', graphql_name='number')
    title = sgqlc.types.Field('StringComparator', graphql_name='title')
    description = sgqlc.types.Field('NullableStringComparator', graphql_name='description')
    priority = sgqlc.types.Field('NullableNumberComparator', graphql_name='priority')
    estimate = sgqlc.types.Field(EstimateComparator, graphql_name='estimate')
    started_at = sgqlc.types.Field('NullableDateComparator', graphql_name='startedAt')
    triaged_at = sgqlc.types.Field('NullableDateComparator', graphql_name='triagedAt')
    completed_at = sgqlc.types.Field('NullableDateComparator', graphql_name='completedAt')
    canceled_at = sgqlc.types.Field('NullableDateComparator', graphql_name='canceledAt')
    archived_at = sgqlc.types.Field('NullableDateComparator', graphql_name='archivedAt')
    auto_closed_at = sgqlc.types.Field('NullableDateComparator', graphql_name='autoClosedAt')
    auto_archived_at = sgqlc.types.Field('NullableDateComparator', graphql_name='autoArchivedAt')
    added_to_cycle_at = sgqlc.types.Field('NullableDateComparator', graphql_name='addedToCycleAt')
    added_to_cycle_period = sgqlc.types.Field(CyclePeriodComparator, graphql_name='addedToCyclePeriod')
    due_date = sgqlc.types.Field('NullableTimelessDateComparator', graphql_name='dueDate')
    snoozed_until_at = sgqlc.types.Field('NullableDateComparator', graphql_name='snoozedUntilAt')
    assignee = sgqlc.types.Field('NullableUserFilter', graphql_name='assignee')
    last_applied_template = sgqlc.types.Field('NullableTemplateFilter', graphql_name='lastAppliedTemplate')
    recurring_issue_template = sgqlc.types.Field('NullableTemplateFilter', graphql_name='recurringIssueTemplate')
    source_metadata = sgqlc.types.Field('SourceMetadataComparator', graphql_name='sourceMetadata')
    creator = sgqlc.types.Field('NullableUserFilter', graphql_name='creator')
    parent = sgqlc.types.Field('NullableIssueFilter', graphql_name='parent')
    snoozed_by = sgqlc.types.Field('NullableUserFilter', graphql_name='snoozedBy')
    labels = sgqlc.types.Field('IssueLabelCollectionFilter', graphql_name='labels')
    subscribers = sgqlc.types.Field('UserCollectionFilter', graphql_name='subscribers')
    team = sgqlc.types.Field('TeamFilter', graphql_name='team')
    project_milestone = sgqlc.types.Field('NullableProjectMilestoneFilter', graphql_name='projectMilestone')
    comments = sgqlc.types.Field(CommentCollectionFilter, graphql_name='comments')
    cycle = sgqlc.types.Field('NullableCycleFilter', graphql_name='cycle')
    project = sgqlc.types.Field('NullableProjectFilter', graphql_name='project')
    state = sgqlc.types.Field('WorkflowStateFilter', graphql_name='state')
    children = sgqlc.types.Field('IssueCollectionFilter', graphql_name='children')
    attachments = sgqlc.types.Field(AttachmentCollectionFilter, graphql_name='attachments')
    searchable_content = sgqlc.types.Field(ContentComparator, graphql_name='searchableContent')
    has_related_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasRelatedRelations')
    has_duplicate_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasDuplicateRelations')
    has_blocked_by_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasBlockedByRelations')
    has_blocking_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasBlockingRelations')
    sla_status = sgqlc.types.Field('SlaStatusComparator', graphql_name='slaStatus')
    reactions = sgqlc.types.Field('ReactionCollectionFilter', graphql_name='reactions')
    needs = sgqlc.types.Field(CustomerNeedCollectionFilter, graphql_name='needs')
    customer_count = sgqlc.types.Field('NumberComparator', graphql_name='customerCount')
    lead_time = sgqlc.types.Field('NullableDurationComparator', graphql_name='leadTime')
    cycle_time = sgqlc.types.Field('NullableDurationComparator', graphql_name='cycleTime')
    age_time = sgqlc.types.Field('NullableDurationComparator', graphql_name='ageTime')
    triage_time = sgqlc.types.Field('NullableDurationComparator', graphql_name='triageTime')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IssueCollectionFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IssueCollectionFilter')), graphql_name='or')
    some = sgqlc.types.Field('IssueFilter', graphql_name='some')
    every = sgqlc.types.Field('IssueFilter', graphql_name='every')
    length = sgqlc.types.Field('NumberComparator', graphql_name='length')


class IssueCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'title', 'description', 'description_data', 'assignee_id', 'parent_id', 'priority', 'estimate', 'subscriber_ids', 'label_ids', 'team_id', 'cycle_id', 'project_id', 'project_milestone_id', 'last_applied_template_id', 'state_id', 'reference_comment_id', 'source_comment_id', 'source_pull_request_comment_id', 'sort_order', 'priority_sort_order', 'sub_issue_sort_order', 'due_date', 'create_as_user', 'display_icon_url', 'preserve_sort_order_on_create', 'created_at', 'sla_breaches_at', 'sla_started_at', 'template_id', 'completed_at', 'sla_type')
    id = sgqlc.types.Field(String, graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')
    description_data = sgqlc.types.Field(JSON, graphql_name='descriptionData')
    assignee_id = sgqlc.types.Field(String, graphql_name='assigneeId')
    parent_id = sgqlc.types.Field(String, graphql_name='parentId')
    priority = sgqlc.types.Field(Int, graphql_name='priority')
    estimate = sgqlc.types.Field(Int, graphql_name='estimate')
    subscriber_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='subscriberIds')
    label_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labelIds')
    team_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='teamId')
    cycle_id = sgqlc.types.Field(String, graphql_name='cycleId')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    project_milestone_id = sgqlc.types.Field(String, graphql_name='projectMilestoneId')
    last_applied_template_id = sgqlc.types.Field(String, graphql_name='lastAppliedTemplateId')
    state_id = sgqlc.types.Field(String, graphql_name='stateId')
    reference_comment_id = sgqlc.types.Field(String, graphql_name='referenceCommentId')
    source_comment_id = sgqlc.types.Field(String, graphql_name='sourceCommentId')
    source_pull_request_comment_id = sgqlc.types.Field(String, graphql_name='sourcePullRequestCommentId')
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')
    priority_sort_order = sgqlc.types.Field(Float, graphql_name='prioritySortOrder')
    sub_issue_sort_order = sgqlc.types.Field(Float, graphql_name='subIssueSortOrder')
    due_date = sgqlc.types.Field(TimelessDate, graphql_name='dueDate')
    create_as_user = sgqlc.types.Field(String, graphql_name='createAsUser')
    display_icon_url = sgqlc.types.Field(String, graphql_name='displayIconUrl')
    preserve_sort_order_on_create = sgqlc.types.Field(Boolean, graphql_name='preserveSortOrderOnCreate')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    sla_breaches_at = sgqlc.types.Field(DateTime, graphql_name='slaBreachesAt')
    sla_started_at = sgqlc.types.Field(DateTime, graphql_name='slaStartedAt')
    template_id = sgqlc.types.Field(String, graphql_name='templateId')
    completed_at = sgqlc.types.Field(DateTime, graphql_name='completedAt')
    sla_type = sgqlc.types.Field(SLADayCountType, graphql_name='slaType')


class IssueFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'number', 'title', 'description', 'priority', 'estimate', 'started_at', 'triaged_at', 'completed_at', 'canceled_at', 'archived_at', 'auto_closed_at', 'auto_archived_at', 'added_to_cycle_at', 'added_to_cycle_period', 'due_date', 'snoozed_until_at', 'assignee', 'last_applied_template', 'recurring_issue_template', 'source_metadata', 'creator', 'parent', 'snoozed_by', 'labels', 'subscribers', 'team', 'project_milestone', 'comments', 'cycle', 'project', 'state', 'children', 'attachments', 'searchable_content', 'has_related_relations', 'has_duplicate_relations', 'has_blocked_by_relations', 'has_blocking_relations', 'sla_status', 'reactions', 'needs', 'customer_count', 'lead_time', 'cycle_time', 'age_time', 'triage_time', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    number = sgqlc.types.Field('NumberComparator', graphql_name='number')
    title = sgqlc.types.Field('StringComparator', graphql_name='title')
    description = sgqlc.types.Field('NullableStringComparator', graphql_name='description')
    priority = sgqlc.types.Field('NullableNumberComparator', graphql_name='priority')
    estimate = sgqlc.types.Field(EstimateComparator, graphql_name='estimate')
    started_at = sgqlc.types.Field('NullableDateComparator', graphql_name='startedAt')
    triaged_at = sgqlc.types.Field('NullableDateComparator', graphql_name='triagedAt')
    completed_at = sgqlc.types.Field('NullableDateComparator', graphql_name='completedAt')
    canceled_at = sgqlc.types.Field('NullableDateComparator', graphql_name='canceledAt')
    archived_at = sgqlc.types.Field('NullableDateComparator', graphql_name='archivedAt')
    auto_closed_at = sgqlc.types.Field('NullableDateComparator', graphql_name='autoClosedAt')
    auto_archived_at = sgqlc.types.Field('NullableDateComparator', graphql_name='autoArchivedAt')
    added_to_cycle_at = sgqlc.types.Field('NullableDateComparator', graphql_name='addedToCycleAt')
    added_to_cycle_period = sgqlc.types.Field(CyclePeriodComparator, graphql_name='addedToCyclePeriod')
    due_date = sgqlc.types.Field('NullableTimelessDateComparator', graphql_name='dueDate')
    snoozed_until_at = sgqlc.types.Field('NullableDateComparator', graphql_name='snoozedUntilAt')
    assignee = sgqlc.types.Field('NullableUserFilter', graphql_name='assignee')
    last_applied_template = sgqlc.types.Field('NullableTemplateFilter', graphql_name='lastAppliedTemplate')
    recurring_issue_template = sgqlc.types.Field('NullableTemplateFilter', graphql_name='recurringIssueTemplate')
    source_metadata = sgqlc.types.Field('SourceMetadataComparator', graphql_name='sourceMetadata')
    creator = sgqlc.types.Field('NullableUserFilter', graphql_name='creator')
    parent = sgqlc.types.Field('NullableIssueFilter', graphql_name='parent')
    snoozed_by = sgqlc.types.Field('NullableUserFilter', graphql_name='snoozedBy')
    labels = sgqlc.types.Field('IssueLabelCollectionFilter', graphql_name='labels')
    subscribers = sgqlc.types.Field('UserCollectionFilter', graphql_name='subscribers')
    team = sgqlc.types.Field('TeamFilter', graphql_name='team')
    project_milestone = sgqlc.types.Field('NullableProjectMilestoneFilter', graphql_name='projectMilestone')
    comments = sgqlc.types.Field(CommentCollectionFilter, graphql_name='comments')
    cycle = sgqlc.types.Field('NullableCycleFilter', graphql_name='cycle')
    project = sgqlc.types.Field('NullableProjectFilter', graphql_name='project')
    state = sgqlc.types.Field('WorkflowStateFilter', graphql_name='state')
    children = sgqlc.types.Field(IssueCollectionFilter, graphql_name='children')
    attachments = sgqlc.types.Field(AttachmentCollectionFilter, graphql_name='attachments')
    searchable_content = sgqlc.types.Field(ContentComparator, graphql_name='searchableContent')
    has_related_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasRelatedRelations')
    has_duplicate_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasDuplicateRelations')
    has_blocked_by_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasBlockedByRelations')
    has_blocking_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasBlockingRelations')
    sla_status = sgqlc.types.Field('SlaStatusComparator', graphql_name='slaStatus')
    reactions = sgqlc.types.Field('ReactionCollectionFilter', graphql_name='reactions')
    needs = sgqlc.types.Field(CustomerNeedCollectionFilter, graphql_name='needs')
    customer_count = sgqlc.types.Field('NumberComparator', graphql_name='customerCount')
    lead_time = sgqlc.types.Field('NullableDurationComparator', graphql_name='leadTime')
    cycle_time = sgqlc.types.Field('NullableDurationComparator', graphql_name='cycleTime')
    age_time = sgqlc.types.Field('NullableDurationComparator', graphql_name='ageTime')
    triage_time = sgqlc.types.Field('NullableDurationComparator', graphql_name='triageTime')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IssueFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IssueFilter')), graphql_name='or')


class IssueImportUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('mapping',)
    mapping = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='mapping')


class IssueLabelCollectionFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'is_group', 'creator', 'team', 'parent', 'and_', 'or_', 'some', 'every', 'length')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    name = sgqlc.types.Field('StringComparator', graphql_name='name')
    is_group = sgqlc.types.Field(BooleanComparator, graphql_name='isGroup')
    creator = sgqlc.types.Field('NullableUserFilter', graphql_name='creator')
    team = sgqlc.types.Field('NullableTeamFilter', graphql_name='team')
    parent = sgqlc.types.Field('IssueLabelFilter', graphql_name='parent')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IssueLabelCollectionFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IssueLabelCollectionFilter')), graphql_name='or')
    some = sgqlc.types.Field('IssueLabelFilter', graphql_name='some')
    every = sgqlc.types.Field('IssueLabelFilter', graphql_name='every')
    length = sgqlc.types.Field('NumberComparator', graphql_name='length')


class IssueLabelCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'description', 'color', 'parent_id', 'team_id', 'is_group')
    id = sgqlc.types.Field(String, graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    color = sgqlc.types.Field(String, graphql_name='color')
    parent_id = sgqlc.types.Field(String, graphql_name='parentId')
    team_id = sgqlc.types.Field(String, graphql_name='teamId')
    is_group = sgqlc.types.Field(Boolean, graphql_name='isGroup')


class IssueLabelFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'is_group', 'creator', 'team', 'parent', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    name = sgqlc.types.Field('StringComparator', graphql_name='name')
    is_group = sgqlc.types.Field(BooleanComparator, graphql_name='isGroup')
    creator = sgqlc.types.Field('NullableUserFilter', graphql_name='creator')
    team = sgqlc.types.Field('NullableTeamFilter', graphql_name='team')
    parent = sgqlc.types.Field('IssueLabelFilter', graphql_name='parent')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IssueLabelFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IssueLabelFilter')), graphql_name='or')


class IssueLabelUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'description', 'parent_id', 'color')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    parent_id = sgqlc.types.Field(String, graphql_name='parentId')
    color = sgqlc.types.Field(String, graphql_name='color')


class IssueRelationCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'type', 'issue_id', 'related_issue_id')
    id = sgqlc.types.Field(String, graphql_name='id')
    type = sgqlc.types.Field(sgqlc.types.non_null(IssueRelationType), graphql_name='type')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='issueId')
    related_issue_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='relatedIssueId')


class IssueRelationUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('type', 'issue_id', 'related_issue_id')
    type = sgqlc.types.Field(String, graphql_name='type')
    issue_id = sgqlc.types.Field(String, graphql_name='issueId')
    related_issue_id = sgqlc.types.Field(String, graphql_name='relatedIssueId')


class IssueSortInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('priority', 'estimate', 'title', 'label', 'label_group', 'sla_status', 'created_at', 'updated_at', 'completed_at', 'due_date', 'cycle', 'milestone', 'assignee', 'project', 'team', 'manual', 'workflow_state', 'customer', 'customer_revenue', 'customer_count', 'customer_important_count', 'root_issue', 'link_count')
    priority = sgqlc.types.Field('PrioritySort', graphql_name='priority')
    estimate = sgqlc.types.Field(EstimateSort, graphql_name='estimate')
    title = sgqlc.types.Field('TitleSort', graphql_name='title')
    label = sgqlc.types.Field('LabelSort', graphql_name='label')
    label_group = sgqlc.types.Field('LabelGroupSort', graphql_name='labelGroup')
    sla_status = sgqlc.types.Field('SlaStatusSort', graphql_name='slaStatus')
    created_at = sgqlc.types.Field(CreatedAtSort, graphql_name='createdAt')
    updated_at = sgqlc.types.Field('UpdatedAtSort', graphql_name='updatedAt')
    completed_at = sgqlc.types.Field(CompletedAtSort, graphql_name='completedAt')
    due_date = sgqlc.types.Field(DueDateSort, graphql_name='dueDate')
    cycle = sgqlc.types.Field(CycleSort, graphql_name='cycle')
    milestone = sgqlc.types.Field('MilestoneSort', graphql_name='milestone')
    assignee = sgqlc.types.Field(AssigneeSort, graphql_name='assignee')
    project = sgqlc.types.Field('ProjectSort', graphql_name='project')
    team = sgqlc.types.Field('TeamSort', graphql_name='team')
    manual = sgqlc.types.Field('ManualSort', graphql_name='manual')
    workflow_state = sgqlc.types.Field('WorkflowStateSort', graphql_name='workflowState')
    customer = sgqlc.types.Field(CustomerSort, graphql_name='customer')
    customer_revenue = sgqlc.types.Field(CustomerRevenueSort, graphql_name='customerRevenue')
    customer_count = sgqlc.types.Field(CustomerCountSort, graphql_name='customerCount')
    customer_important_count = sgqlc.types.Field(CustomerImportantCountSort, graphql_name='customerImportantCount')
    root_issue = sgqlc.types.Field('RootIssueSort', graphql_name='rootIssue')
    link_count = sgqlc.types.Field('LinkCountSort', graphql_name='linkCount')


class IssueUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('title', 'description', 'description_data', 'assignee_id', 'parent_id', 'priority', 'estimate', 'subscriber_ids', 'label_ids', 'added_label_ids', 'removed_label_ids', 'team_id', 'cycle_id', 'project_id', 'project_milestone_id', 'last_applied_template_id', 'state_id', 'sort_order', 'priority_sort_order', 'sub_issue_sort_order', 'due_date', 'trashed', 'sla_breaches_at', 'sla_started_at', 'snoozed_until_at', 'snoozed_by_id', 'sla_type', 'auto_closed_by_parent_closing')
    title = sgqlc.types.Field(String, graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')
    description_data = sgqlc.types.Field(JSON, graphql_name='descriptionData')
    assignee_id = sgqlc.types.Field(String, graphql_name='assigneeId')
    parent_id = sgqlc.types.Field(String, graphql_name='parentId')
    priority = sgqlc.types.Field(Int, graphql_name='priority')
    estimate = sgqlc.types.Field(Int, graphql_name='estimate')
    subscriber_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='subscriberIds')
    label_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labelIds')
    added_label_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='addedLabelIds')
    removed_label_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='removedLabelIds')
    team_id = sgqlc.types.Field(String, graphql_name='teamId')
    cycle_id = sgqlc.types.Field(String, graphql_name='cycleId')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    project_milestone_id = sgqlc.types.Field(String, graphql_name='projectMilestoneId')
    last_applied_template_id = sgqlc.types.Field(String, graphql_name='lastAppliedTemplateId')
    state_id = sgqlc.types.Field(String, graphql_name='stateId')
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')
    priority_sort_order = sgqlc.types.Field(Float, graphql_name='prioritySortOrder')
    sub_issue_sort_order = sgqlc.types.Field(Float, graphql_name='subIssueSortOrder')
    due_date = sgqlc.types.Field(TimelessDate, graphql_name='dueDate')
    trashed = sgqlc.types.Field(Boolean, graphql_name='trashed')
    sla_breaches_at = sgqlc.types.Field(DateTime, graphql_name='slaBreachesAt')
    sla_started_at = sgqlc.types.Field(DateTime, graphql_name='slaStartedAt')
    snoozed_until_at = sgqlc.types.Field(DateTime, graphql_name='snoozedUntilAt')
    snoozed_by_id = sgqlc.types.Field(String, graphql_name='snoozedById')
    sla_type = sgqlc.types.Field(SLADayCountType, graphql_name='slaType')
    auto_closed_by_parent_closing = sgqlc.types.Field(Boolean, graphql_name='autoClosedByParentClosing')


class JiraConfigurationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('access_token', 'email', 'hostname', 'manual_setup')
    access_token = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='accessToken')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    hostname = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='hostname')
    manual_setup = sgqlc.types.Field(Boolean, graphql_name='manualSetup')


class JiraLinearMappingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('jira_project_id', 'linear_team_id', 'bidirectional', 'default')
    jira_project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='jiraProjectId')
    linear_team_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='linearTeamId')
    bidirectional = sgqlc.types.Field(Boolean, graphql_name='bidirectional')
    default = sgqlc.types.Field(Boolean, graphql_name='default')


class JiraPersonalSettingsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('site_name',)
    site_name = sgqlc.types.Field(String, graphql_name='siteName')


class JiraProjectDataInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'key', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class JiraSettingsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('project_mapping', 'projects', 'is_jira_server', 'setup_pending', 'manual_setup', 'label')
    project_mapping = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(JiraLinearMappingInput)), graphql_name='projectMapping')
    projects = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JiraProjectDataInput))), graphql_name='projects')
    is_jira_server = sgqlc.types.Field(Boolean, graphql_name='isJiraServer')
    setup_pending = sgqlc.types.Field(Boolean, graphql_name='setupPending')
    manual_setup = sgqlc.types.Field(Boolean, graphql_name='manualSetup')
    label = sgqlc.types.Field(String, graphql_name='label')


class JiraUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'update_projects', 'update_metadata', 'delete_webhook', 'webhook_secret', 'access_token', 'email')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    update_projects = sgqlc.types.Field(Boolean, graphql_name='updateProjects')
    update_metadata = sgqlc.types.Field(Boolean, graphql_name='updateMetadata')
    delete_webhook = sgqlc.types.Field(Boolean, graphql_name='deleteWebhook')
    webhook_secret = sgqlc.types.Field(String, graphql_name='webhookSecret')
    access_token = sgqlc.types.Field(String, graphql_name='accessToken')
    email = sgqlc.types.Field(String, graphql_name='email')


class JoinOrganizationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('organization_id', 'invite_link')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='organizationId')
    invite_link = sgqlc.types.Field(String, graphql_name='inviteLink')


class LabelGroupSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order', 'label_group_id')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')
    label_group_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='labelGroupId')


class LabelSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class LaunchDarklySettingsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('project_key', 'environment')
    project_key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectKey')
    environment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='environment')


class LinkCountSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class ManualSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class MilestoneSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class NameSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class NotificationCategoryPreferencesInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('assignments', 'status_changes', 'comments_and_replies', 'mentions', 'reactions', 'subscriptions', 'document_changes', 'posts_and_updates', 'reminders', 'reviews', 'apps_and_integrations', 'triage', 'customers')
    assignments = sgqlc.types.Field('PartialNotificationChannelPreferencesInput', graphql_name='assignments')
    status_changes = sgqlc.types.Field('PartialNotificationChannelPreferencesInput', graphql_name='statusChanges')
    comments_and_replies = sgqlc.types.Field('PartialNotificationChannelPreferencesInput', graphql_name='commentsAndReplies')
    mentions = sgqlc.types.Field('PartialNotificationChannelPreferencesInput', graphql_name='mentions')
    reactions = sgqlc.types.Field('PartialNotificationChannelPreferencesInput', graphql_name='reactions')
    subscriptions = sgqlc.types.Field('PartialNotificationChannelPreferencesInput', graphql_name='subscriptions')
    document_changes = sgqlc.types.Field('PartialNotificationChannelPreferencesInput', graphql_name='documentChanges')
    posts_and_updates = sgqlc.types.Field('PartialNotificationChannelPreferencesInput', graphql_name='postsAndUpdates')
    reminders = sgqlc.types.Field('PartialNotificationChannelPreferencesInput', graphql_name='reminders')
    reviews = sgqlc.types.Field('PartialNotificationChannelPreferencesInput', graphql_name='reviews')
    apps_and_integrations = sgqlc.types.Field('PartialNotificationChannelPreferencesInput', graphql_name='appsAndIntegrations')
    triage = sgqlc.types.Field('PartialNotificationChannelPreferencesInput', graphql_name='triage')
    customers = sgqlc.types.Field('PartialNotificationChannelPreferencesInput', graphql_name='customers')


class NotificationDeliveryPreferencesChannelInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('schedule',)
    schedule = sgqlc.types.Field('NotificationDeliveryPreferencesScheduleInput', graphql_name='schedule')


class NotificationDeliveryPreferencesDayInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(String, graphql_name='start')
    end = sgqlc.types.Field(String, graphql_name='end')


class NotificationDeliveryPreferencesInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('mobile',)
    mobile = sgqlc.types.Field(NotificationDeliveryPreferencesChannelInput, graphql_name='mobile')


class NotificationDeliveryPreferencesScheduleInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('disabled', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
    disabled = sgqlc.types.Field(Boolean, graphql_name='disabled')
    sunday = sgqlc.types.Field(sgqlc.types.non_null(NotificationDeliveryPreferencesDayInput), graphql_name='sunday')
    monday = sgqlc.types.Field(sgqlc.types.non_null(NotificationDeliveryPreferencesDayInput), graphql_name='monday')
    tuesday = sgqlc.types.Field(sgqlc.types.non_null(NotificationDeliveryPreferencesDayInput), graphql_name='tuesday')
    wednesday = sgqlc.types.Field(sgqlc.types.non_null(NotificationDeliveryPreferencesDayInput), graphql_name='wednesday')
    thursday = sgqlc.types.Field(sgqlc.types.non_null(NotificationDeliveryPreferencesDayInput), graphql_name='thursday')
    friday = sgqlc.types.Field(sgqlc.types.non_null(NotificationDeliveryPreferencesDayInput), graphql_name='friday')
    saturday = sgqlc.types.Field(sgqlc.types.non_null(NotificationDeliveryPreferencesDayInput), graphql_name='saturday')


class NotificationEntityInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('issue_id', 'project_id', 'initiative_id', 'project_update_id', 'initiative_update_id', 'oauth_client_approval_id', 'id')
    issue_id = sgqlc.types.Field(String, graphql_name='issueId')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    initiative_id = sgqlc.types.Field(String, graphql_name='initiativeId')
    project_update_id = sgqlc.types.Field(String, graphql_name='projectUpdateId')
    initiative_update_id = sgqlc.types.Field(String, graphql_name='initiativeUpdateId')
    oauth_client_approval_id = sgqlc.types.Field(String, graphql_name='oauthClientApprovalId')
    id = sgqlc.types.Field(String, graphql_name='id')


class NotificationFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'type', 'archived_at', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    type = sgqlc.types.Field('StringComparator', graphql_name='type')
    archived_at = sgqlc.types.Field(DateComparator, graphql_name='archivedAt')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NotificationFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NotificationFilter')), graphql_name='or')


class NotificationSubscriptionCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'customer_id', 'custom_view_id', 'cycle_id', 'initiative_id', 'label_id', 'project_id', 'team_id', 'user_id', 'context_view_type', 'user_context_view_type', 'notification_subscription_types', 'active')
    id = sgqlc.types.Field(String, graphql_name='id')
    customer_id = sgqlc.types.Field(String, graphql_name='customerId')
    custom_view_id = sgqlc.types.Field(String, graphql_name='customViewId')
    cycle_id = sgqlc.types.Field(String, graphql_name='cycleId')
    initiative_id = sgqlc.types.Field(String, graphql_name='initiativeId')
    label_id = sgqlc.types.Field(String, graphql_name='labelId')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    team_id = sgqlc.types.Field(String, graphql_name='teamId')
    user_id = sgqlc.types.Field(String, graphql_name='userId')
    context_view_type = sgqlc.types.Field(ContextViewType, graphql_name='contextViewType')
    user_context_view_type = sgqlc.types.Field(UserContextViewType, graphql_name='userContextViewType')
    notification_subscription_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='notificationSubscriptionTypes')
    active = sgqlc.types.Field(Boolean, graphql_name='active')


class NotificationSubscriptionUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('notification_subscription_types', 'active')
    notification_subscription_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='notificationSubscriptionTypes')
    active = sgqlc.types.Field(Boolean, graphql_name='active')


class NotificationUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('read_at', 'snoozed_until_at', 'project_update_id', 'initiative_update_id')
    read_at = sgqlc.types.Field(DateTime, graphql_name='readAt')
    snoozed_until_at = sgqlc.types.Field(DateTime, graphql_name='snoozedUntilAt')
    project_update_id = sgqlc.types.Field(String, graphql_name='projectUpdateId')
    initiative_update_id = sgqlc.types.Field(String, graphql_name='initiativeUpdateId')


class NotionSettingsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('workspace_id', 'workspace_name')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='workspaceId')
    workspace_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='workspaceName')


class NullableCommentFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'body', 'user', 'issue', 'project_update', 'parent', 'document_content', 'reactions', 'needs', 'null', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    body = sgqlc.types.Field('StringComparator', graphql_name='body')
    user = sgqlc.types.Field('UserFilter', graphql_name='user')
    issue = sgqlc.types.Field('NullableIssueFilter', graphql_name='issue')
    project_update = sgqlc.types.Field('NullableProjectUpdateFilter', graphql_name='projectUpdate')
    parent = sgqlc.types.Field('NullableCommentFilter', graphql_name='parent')
    document_content = sgqlc.types.Field('NullableDocumentContentFilter', graphql_name='documentContent')
    reactions = sgqlc.types.Field('ReactionCollectionFilter', graphql_name='reactions')
    needs = sgqlc.types.Field(CustomerNeedCollectionFilter, graphql_name='needs')
    null = sgqlc.types.Field(Boolean, graphql_name='null')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NullableCommentFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NullableCommentFilter')), graphql_name='or')


class NullableCustomerFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'slack_channel_id', 'domains', 'external_ids', 'owner', 'needs', 'revenue', 'size', 'status', 'tier', 'null', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    name = sgqlc.types.Field('StringComparator', graphql_name='name')
    slack_channel_id = sgqlc.types.Field('StringComparator', graphql_name='slackChannelId')
    domains = sgqlc.types.Field('StringArrayComparator', graphql_name='domains')
    external_ids = sgqlc.types.Field('StringArrayComparator', graphql_name='externalIds')
    owner = sgqlc.types.Field('NullableUserFilter', graphql_name='owner')
    needs = sgqlc.types.Field(CustomerNeedCollectionFilter, graphql_name='needs')
    revenue = sgqlc.types.Field('NumberComparator', graphql_name='revenue')
    size = sgqlc.types.Field('NumberComparator', graphql_name='size')
    status = sgqlc.types.Field(CustomerStatusFilter, graphql_name='status')
    tier = sgqlc.types.Field(CustomerTierFilter, graphql_name='tier')
    null = sgqlc.types.Field(Boolean, graphql_name='null')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NullableCustomerFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NullableCustomerFilter')), graphql_name='or')


class NullableCycleFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'number', 'name', 'starts_at', 'ends_at', 'completed_at', 'is_active', 'is_in_cooldown', 'is_next', 'is_previous', 'is_future', 'is_past', 'team', 'issues', 'null', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    number = sgqlc.types.Field('NumberComparator', graphql_name='number')
    name = sgqlc.types.Field('StringComparator', graphql_name='name')
    starts_at = sgqlc.types.Field(DateComparator, graphql_name='startsAt')
    ends_at = sgqlc.types.Field(DateComparator, graphql_name='endsAt')
    completed_at = sgqlc.types.Field(DateComparator, graphql_name='completedAt')
    is_active = sgqlc.types.Field(BooleanComparator, graphql_name='isActive')
    is_in_cooldown = sgqlc.types.Field(BooleanComparator, graphql_name='isInCooldown')
    is_next = sgqlc.types.Field(BooleanComparator, graphql_name='isNext')
    is_previous = sgqlc.types.Field(BooleanComparator, graphql_name='isPrevious')
    is_future = sgqlc.types.Field(BooleanComparator, graphql_name='isFuture')
    is_past = sgqlc.types.Field(BooleanComparator, graphql_name='isPast')
    team = sgqlc.types.Field('TeamFilter', graphql_name='team')
    issues = sgqlc.types.Field(IssueCollectionFilter, graphql_name='issues')
    null = sgqlc.types.Field(Boolean, graphql_name='null')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NullableCycleFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NullableCycleFilter')), graphql_name='or')


class NullableDateComparator(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('eq', 'neq', 'in_', 'nin', 'null', 'lt', 'lte', 'gt', 'gte')
    eq = sgqlc.types.Field(DateTimeOrDuration, graphql_name='eq')
    neq = sgqlc.types.Field(DateTimeOrDuration, graphql_name='neq')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DateTimeOrDuration)), graphql_name='in')
    nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DateTimeOrDuration)), graphql_name='nin')
    null = sgqlc.types.Field(Boolean, graphql_name='null')
    lt = sgqlc.types.Field(DateTimeOrDuration, graphql_name='lt')
    lte = sgqlc.types.Field(DateTimeOrDuration, graphql_name='lte')
    gt = sgqlc.types.Field(DateTimeOrDuration, graphql_name='gt')
    gte = sgqlc.types.Field(DateTimeOrDuration, graphql_name='gte')


class NullableDocumentContentFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'project', 'document', 'null', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    project = sgqlc.types.Field('ProjectFilter', graphql_name='project')
    document = sgqlc.types.Field(DocumentFilter, graphql_name='document')
    null = sgqlc.types.Field(Boolean, graphql_name='null')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NullableDocumentContentFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NullableDocumentContentFilter')), graphql_name='or')


class NullableDurationComparator(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('eq', 'neq', 'in_', 'nin', 'null', 'lt', 'lte', 'gt', 'gte')
    eq = sgqlc.types.Field(Duration, graphql_name='eq')
    neq = sgqlc.types.Field(Duration, graphql_name='neq')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Duration)), graphql_name='in')
    nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Duration)), graphql_name='nin')
    null = sgqlc.types.Field(Boolean, graphql_name='null')
    lt = sgqlc.types.Field(Duration, graphql_name='lt')
    lte = sgqlc.types.Field(Duration, graphql_name='lte')
    gt = sgqlc.types.Field(Duration, graphql_name='gt')
    gte = sgqlc.types.Field(Duration, graphql_name='gte')


class NullableIssueFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'number', 'title', 'description', 'priority', 'estimate', 'started_at', 'triaged_at', 'completed_at', 'canceled_at', 'archived_at', 'auto_closed_at', 'auto_archived_at', 'added_to_cycle_at', 'added_to_cycle_period', 'due_date', 'snoozed_until_at', 'assignee', 'last_applied_template', 'recurring_issue_template', 'source_metadata', 'creator', 'parent', 'snoozed_by', 'labels', 'subscribers', 'team', 'project_milestone', 'comments', 'cycle', 'project', 'state', 'children', 'attachments', 'searchable_content', 'has_related_relations', 'has_duplicate_relations', 'has_blocked_by_relations', 'has_blocking_relations', 'sla_status', 'reactions', 'needs', 'customer_count', 'lead_time', 'cycle_time', 'age_time', 'triage_time', 'null', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    number = sgqlc.types.Field('NumberComparator', graphql_name='number')
    title = sgqlc.types.Field('StringComparator', graphql_name='title')
    description = sgqlc.types.Field('NullableStringComparator', graphql_name='description')
    priority = sgqlc.types.Field('NullableNumberComparator', graphql_name='priority')
    estimate = sgqlc.types.Field(EstimateComparator, graphql_name='estimate')
    started_at = sgqlc.types.Field(NullableDateComparator, graphql_name='startedAt')
    triaged_at = sgqlc.types.Field(NullableDateComparator, graphql_name='triagedAt')
    completed_at = sgqlc.types.Field(NullableDateComparator, graphql_name='completedAt')
    canceled_at = sgqlc.types.Field(NullableDateComparator, graphql_name='canceledAt')
    archived_at = sgqlc.types.Field(NullableDateComparator, graphql_name='archivedAt')
    auto_closed_at = sgqlc.types.Field(NullableDateComparator, graphql_name='autoClosedAt')
    auto_archived_at = sgqlc.types.Field(NullableDateComparator, graphql_name='autoArchivedAt')
    added_to_cycle_at = sgqlc.types.Field(NullableDateComparator, graphql_name='addedToCycleAt')
    added_to_cycle_period = sgqlc.types.Field(CyclePeriodComparator, graphql_name='addedToCyclePeriod')
    due_date = sgqlc.types.Field('NullableTimelessDateComparator', graphql_name='dueDate')
    snoozed_until_at = sgqlc.types.Field(NullableDateComparator, graphql_name='snoozedUntilAt')
    assignee = sgqlc.types.Field('NullableUserFilter', graphql_name='assignee')
    last_applied_template = sgqlc.types.Field('NullableTemplateFilter', graphql_name='lastAppliedTemplate')
    recurring_issue_template = sgqlc.types.Field('NullableTemplateFilter', graphql_name='recurringIssueTemplate')
    source_metadata = sgqlc.types.Field('SourceMetadataComparator', graphql_name='sourceMetadata')
    creator = sgqlc.types.Field('NullableUserFilter', graphql_name='creator')
    parent = sgqlc.types.Field('NullableIssueFilter', graphql_name='parent')
    snoozed_by = sgqlc.types.Field('NullableUserFilter', graphql_name='snoozedBy')
    labels = sgqlc.types.Field(IssueLabelCollectionFilter, graphql_name='labels')
    subscribers = sgqlc.types.Field('UserCollectionFilter', graphql_name='subscribers')
    team = sgqlc.types.Field('TeamFilter', graphql_name='team')
    project_milestone = sgqlc.types.Field('NullableProjectMilestoneFilter', graphql_name='projectMilestone')
    comments = sgqlc.types.Field(CommentCollectionFilter, graphql_name='comments')
    cycle = sgqlc.types.Field(NullableCycleFilter, graphql_name='cycle')
    project = sgqlc.types.Field('NullableProjectFilter', graphql_name='project')
    state = sgqlc.types.Field('WorkflowStateFilter', graphql_name='state')
    children = sgqlc.types.Field(IssueCollectionFilter, graphql_name='children')
    attachments = sgqlc.types.Field(AttachmentCollectionFilter, graphql_name='attachments')
    searchable_content = sgqlc.types.Field(ContentComparator, graphql_name='searchableContent')
    has_related_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasRelatedRelations')
    has_duplicate_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasDuplicateRelations')
    has_blocked_by_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasBlockedByRelations')
    has_blocking_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasBlockingRelations')
    sla_status = sgqlc.types.Field('SlaStatusComparator', graphql_name='slaStatus')
    reactions = sgqlc.types.Field('ReactionCollectionFilter', graphql_name='reactions')
    needs = sgqlc.types.Field(CustomerNeedCollectionFilter, graphql_name='needs')
    customer_count = sgqlc.types.Field('NumberComparator', graphql_name='customerCount')
    lead_time = sgqlc.types.Field(NullableDurationComparator, graphql_name='leadTime')
    cycle_time = sgqlc.types.Field(NullableDurationComparator, graphql_name='cycleTime')
    age_time = sgqlc.types.Field(NullableDurationComparator, graphql_name='ageTime')
    triage_time = sgqlc.types.Field(NullableDurationComparator, graphql_name='triageTime')
    null = sgqlc.types.Field(Boolean, graphql_name='null')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NullableIssueFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NullableIssueFilter')), graphql_name='or')


class NullableNumberComparator(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('eq', 'neq', 'in_', 'nin', 'null', 'lt', 'lte', 'gt', 'gte')
    eq = sgqlc.types.Field(Float, graphql_name='eq')
    neq = sgqlc.types.Field(Float, graphql_name='neq')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Float)), graphql_name='in')
    nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Float)), graphql_name='nin')
    null = sgqlc.types.Field(Boolean, graphql_name='null')
    lt = sgqlc.types.Field(Float, graphql_name='lt')
    lte = sgqlc.types.Field(Float, graphql_name='lte')
    gt = sgqlc.types.Field(Float, graphql_name='gt')
    gte = sgqlc.types.Field(Float, graphql_name='gte')


class NullableProjectFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'slug_id', 'state', 'status', 'priority', 'labels', 'searchable_content', 'completed_at', 'canceled_at', 'start_date', 'target_date', 'health', 'health_with_age', 'activity_type', 'has_related_relations', 'has_depended_on_by_relations', 'has_depends_on_relations', 'has_blocked_by_relations', 'has_blocking_relations', 'has_violated_relations', 'project_updates', 'creator', 'lead', 'members', 'issues', 'roadmaps', 'initiatives', 'project_milestones', 'completed_project_milestones', 'next_project_milestone', 'accessible_teams', 'last_applied_template', 'needs', 'customer_count', 'null', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    name = sgqlc.types.Field('StringComparator', graphql_name='name')
    slug_id = sgqlc.types.Field('StringComparator', graphql_name='slugId')
    state = sgqlc.types.Field('StringComparator', graphql_name='state')
    status = sgqlc.types.Field('ProjectStatusFilter', graphql_name='status')
    priority = sgqlc.types.Field(NullableNumberComparator, graphql_name='priority')
    labels = sgqlc.types.Field('ProjectLabelCollectionFilter', graphql_name='labels')
    searchable_content = sgqlc.types.Field(ContentComparator, graphql_name='searchableContent')
    completed_at = sgqlc.types.Field(NullableDateComparator, graphql_name='completedAt')
    canceled_at = sgqlc.types.Field(NullableDateComparator, graphql_name='canceledAt')
    start_date = sgqlc.types.Field(NullableDateComparator, graphql_name='startDate')
    target_date = sgqlc.types.Field(NullableDateComparator, graphql_name='targetDate')
    health = sgqlc.types.Field('StringComparator', graphql_name='health')
    health_with_age = sgqlc.types.Field('StringComparator', graphql_name='healthWithAge')
    activity_type = sgqlc.types.Field('StringComparator', graphql_name='activityType')
    has_related_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasRelatedRelations')
    has_depended_on_by_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasDependedOnByRelations')
    has_depends_on_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasDependsOnRelations')
    has_blocked_by_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasBlockedByRelations')
    has_blocking_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasBlockingRelations')
    has_violated_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasViolatedRelations')
    project_updates = sgqlc.types.Field('ProjectUpdatesCollectionFilter', graphql_name='projectUpdates')
    creator = sgqlc.types.Field('UserFilter', graphql_name='creator')
    lead = sgqlc.types.Field('NullableUserFilter', graphql_name='lead')
    members = sgqlc.types.Field('UserCollectionFilter', graphql_name='members')
    issues = sgqlc.types.Field(IssueCollectionFilter, graphql_name='issues')
    roadmaps = sgqlc.types.Field('RoadmapCollectionFilter', graphql_name='roadmaps')
    initiatives = sgqlc.types.Field(InitiativeCollectionFilter, graphql_name='initiatives')
    project_milestones = sgqlc.types.Field('ProjectMilestoneCollectionFilter', graphql_name='projectMilestones')
    completed_project_milestones = sgqlc.types.Field('ProjectMilestoneCollectionFilter', graphql_name='completedProjectMilestones')
    next_project_milestone = sgqlc.types.Field('ProjectMilestoneFilter', graphql_name='nextProjectMilestone')
    accessible_teams = sgqlc.types.Field('TeamCollectionFilter', graphql_name='accessibleTeams')
    last_applied_template = sgqlc.types.Field('NullableTemplateFilter', graphql_name='lastAppliedTemplate')
    needs = sgqlc.types.Field(CustomerNeedCollectionFilter, graphql_name='needs')
    customer_count = sgqlc.types.Field('NumberComparator', graphql_name='customerCount')
    null = sgqlc.types.Field(Boolean, graphql_name='null')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NullableProjectFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NullableProjectFilter')), graphql_name='or')


class NullableProjectMilestoneFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'target_date', 'null', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    name = sgqlc.types.Field('NullableStringComparator', graphql_name='name')
    target_date = sgqlc.types.Field(NullableDateComparator, graphql_name='targetDate')
    null = sgqlc.types.Field(Boolean, graphql_name='null')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NullableProjectMilestoneFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NullableProjectMilestoneFilter')), graphql_name='or')


class NullableProjectUpdateFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'user', 'project', 'reactions', 'null', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    user = sgqlc.types.Field('UserFilter', graphql_name='user')
    project = sgqlc.types.Field('ProjectFilter', graphql_name='project')
    reactions = sgqlc.types.Field('ReactionCollectionFilter', graphql_name='reactions')
    null = sgqlc.types.Field(Boolean, graphql_name='null')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NullableProjectUpdateFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NullableProjectUpdateFilter')), graphql_name='or')


class NullableStringComparator(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('eq', 'neq', 'in_', 'nin', 'null', 'eq_ignore_case', 'neq_ignore_case', 'starts_with', 'starts_with_ignore_case', 'not_starts_with', 'ends_with', 'not_ends_with', 'contains', 'contains_ignore_case', 'not_contains', 'not_contains_ignore_case', 'contains_ignore_case_and_accent')
    eq = sgqlc.types.Field(String, graphql_name='eq')
    neq = sgqlc.types.Field(String, graphql_name='neq')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='in')
    nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='nin')
    null = sgqlc.types.Field(Boolean, graphql_name='null')
    eq_ignore_case = sgqlc.types.Field(String, graphql_name='eqIgnoreCase')
    neq_ignore_case = sgqlc.types.Field(String, graphql_name='neqIgnoreCase')
    starts_with = sgqlc.types.Field(String, graphql_name='startsWith')
    starts_with_ignore_case = sgqlc.types.Field(String, graphql_name='startsWithIgnoreCase')
    not_starts_with = sgqlc.types.Field(String, graphql_name='notStartsWith')
    ends_with = sgqlc.types.Field(String, graphql_name='endsWith')
    not_ends_with = sgqlc.types.Field(String, graphql_name='notEndsWith')
    contains = sgqlc.types.Field(String, graphql_name='contains')
    contains_ignore_case = sgqlc.types.Field(String, graphql_name='containsIgnoreCase')
    not_contains = sgqlc.types.Field(String, graphql_name='notContains')
    not_contains_ignore_case = sgqlc.types.Field(String, graphql_name='notContainsIgnoreCase')
    contains_ignore_case_and_accent = sgqlc.types.Field(String, graphql_name='containsIgnoreCaseAndAccent')


class NullableTeamFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'key', 'description', 'issues', 'parent', 'null', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    name = sgqlc.types.Field('StringComparator', graphql_name='name')
    key = sgqlc.types.Field('StringComparator', graphql_name='key')
    description = sgqlc.types.Field(NullableStringComparator, graphql_name='description')
    issues = sgqlc.types.Field(IssueCollectionFilter, graphql_name='issues')
    parent = sgqlc.types.Field('NullableTeamFilter', graphql_name='parent')
    null = sgqlc.types.Field(Boolean, graphql_name='null')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NullableTeamFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NullableTeamFilter')), graphql_name='or')


class NullableTemplateFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'type', 'null', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    name = sgqlc.types.Field('StringComparator', graphql_name='name')
    type = sgqlc.types.Field('StringComparator', graphql_name='type')
    null = sgqlc.types.Field(Boolean, graphql_name='null')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NullableTemplateFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NullableTemplateFilter')), graphql_name='or')


class NullableTimelessDateComparator(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('eq', 'neq', 'in_', 'nin', 'null', 'lt', 'lte', 'gt', 'gte')
    eq = sgqlc.types.Field(TimelessDateOrDuration, graphql_name='eq')
    neq = sgqlc.types.Field(TimelessDateOrDuration, graphql_name='neq')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TimelessDateOrDuration)), graphql_name='in')
    nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TimelessDateOrDuration)), graphql_name='nin')
    null = sgqlc.types.Field(Boolean, graphql_name='null')
    lt = sgqlc.types.Field(TimelessDateOrDuration, graphql_name='lt')
    lte = sgqlc.types.Field(TimelessDateOrDuration, graphql_name='lte')
    gt = sgqlc.types.Field(TimelessDateOrDuration, graphql_name='gt')
    gte = sgqlc.types.Field(TimelessDateOrDuration, graphql_name='gte')


class NullableUserFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'display_name', 'email', 'active', 'assigned_issues', 'admin', 'invited', 'app', 'is_me', 'null', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    name = sgqlc.types.Field('StringComparator', graphql_name='name')
    display_name = sgqlc.types.Field('StringComparator', graphql_name='displayName')
    email = sgqlc.types.Field('StringComparator', graphql_name='email')
    active = sgqlc.types.Field(BooleanComparator, graphql_name='active')
    assigned_issues = sgqlc.types.Field(IssueCollectionFilter, graphql_name='assignedIssues')
    admin = sgqlc.types.Field(BooleanComparator, graphql_name='admin')
    invited = sgqlc.types.Field(BooleanComparator, graphql_name='invited')
    app = sgqlc.types.Field(BooleanComparator, graphql_name='app')
    is_me = sgqlc.types.Field(BooleanComparator, graphql_name='isMe')
    null = sgqlc.types.Field(Boolean, graphql_name='null')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NullableUserFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NullableUserFilter')), graphql_name='or')


class NumberComparator(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('eq', 'neq', 'in_', 'nin', 'lt', 'lte', 'gt', 'gte')
    eq = sgqlc.types.Field(Float, graphql_name='eq')
    neq = sgqlc.types.Field(Float, graphql_name='neq')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Float)), graphql_name='in')
    nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Float)), graphql_name='nin')
    lt = sgqlc.types.Field(Float, graphql_name='lt')
    lte = sgqlc.types.Field(Float, graphql_name='lte')
    gt = sgqlc.types.Field(Float, graphql_name='gt')
    gte = sgqlc.types.Field(Float, graphql_name='gte')


class OnboardingCustomerSurvey(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('company_role', 'company_size')
    company_role = sgqlc.types.Field(String, graphql_name='companyRole')
    company_size = sgqlc.types.Field(String, graphql_name='companySize')


class OpsgenieInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('api_failed_with_unauthorized_error_at',)
    api_failed_with_unauthorized_error_at = sgqlc.types.Field(DateTime, graphql_name='apiFailedWithUnauthorizedErrorAt')


class OrganizationDomainCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'verification_email', 'auth_type')
    id = sgqlc.types.Field(String, graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    verification_email = sgqlc.types.Field(String, graphql_name='verificationEmail')
    auth_type = sgqlc.types.Field(String, graphql_name='authType')


class OrganizationDomainUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('disable_organization_creation',)
    disable_organization_creation = sgqlc.types.Field(Boolean, graphql_name='disableOrganizationCreation')


class OrganizationDomainVerificationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('organization_domain_id', 'verification_code')
    organization_domain_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='organizationDomainId')
    verification_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='verificationCode')


class OrganizationInviteCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'email', 'role', 'team_ids', 'metadata')
    id = sgqlc.types.Field(String, graphql_name='id')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    role = sgqlc.types.Field(UserRoleType, graphql_name='role')
    team_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='teamIds')
    metadata = sgqlc.types.Field(JSONObject, graphql_name='metadata')


class OrganizationInviteUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('team_ids',)
    team_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='teamIds')


class OrganizationIpRestrictionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('range', 'type', 'description', 'enabled')
    range = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='range')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    description = sgqlc.types.Field(String, graphql_name='description')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')


class OrganizationStartTrialInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('plan_type',)
    plan_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='planType')


class OrganizationUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'logo_url', 'url_key', 'git_branch_format', 'git_linkback_messages_enabled', 'git_public_linkback_messages_enabled', 'roadmap_enabled', 'project_update_reminder_frequency_in_weeks', 'project_update_reminders_day', 'project_update_reminders_hour', 'initiative_update_reminder_frequency_in_weeks', 'initiative_update_reminders_day', 'initiative_update_reminders_hour', 'fiscal_year_start_month', 'working_days', 'reduced_personal_information', 'oauth_app_review', 'allowed_auth_services', 'sla_enabled', 'allow_members_to_invite', 'restrict_team_creation_to_admins', 'restrict_label_management_to_admins', 'ip_restrictions', 'theme_settings', 'customers_enabled', 'customers_configuration', 'feed_enabled', 'default_feed_summary_schedule', 'ai_addon_enabled', 'personal_api_keys_enabled')
    name = sgqlc.types.Field(String, graphql_name='name')
    logo_url = sgqlc.types.Field(String, graphql_name='logoUrl')
    url_key = sgqlc.types.Field(String, graphql_name='urlKey')
    git_branch_format = sgqlc.types.Field(String, graphql_name='gitBranchFormat')
    git_linkback_messages_enabled = sgqlc.types.Field(Boolean, graphql_name='gitLinkbackMessagesEnabled')
    git_public_linkback_messages_enabled = sgqlc.types.Field(Boolean, graphql_name='gitPublicLinkbackMessagesEnabled')
    roadmap_enabled = sgqlc.types.Field(Boolean, graphql_name='roadmapEnabled')
    project_update_reminder_frequency_in_weeks = sgqlc.types.Field(Float, graphql_name='projectUpdateReminderFrequencyInWeeks')
    project_update_reminders_day = sgqlc.types.Field(Day, graphql_name='projectUpdateRemindersDay')
    project_update_reminders_hour = sgqlc.types.Field(Float, graphql_name='projectUpdateRemindersHour')
    initiative_update_reminder_frequency_in_weeks = sgqlc.types.Field(Float, graphql_name='initiativeUpdateReminderFrequencyInWeeks')
    initiative_update_reminders_day = sgqlc.types.Field(Day, graphql_name='initiativeUpdateRemindersDay')
    initiative_update_reminders_hour = sgqlc.types.Field(Float, graphql_name='initiativeUpdateRemindersHour')
    fiscal_year_start_month = sgqlc.types.Field(Float, graphql_name='fiscalYearStartMonth')
    working_days = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Float)), graphql_name='workingDays')
    reduced_personal_information = sgqlc.types.Field(Boolean, graphql_name='reducedPersonalInformation')
    oauth_app_review = sgqlc.types.Field(Boolean, graphql_name='oauthAppReview')
    allowed_auth_services = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='allowedAuthServices')
    sla_enabled = sgqlc.types.Field(Boolean, graphql_name='slaEnabled')
    allow_members_to_invite = sgqlc.types.Field(Boolean, graphql_name='allowMembersToInvite')
    restrict_team_creation_to_admins = sgqlc.types.Field(Boolean, graphql_name='restrictTeamCreationToAdmins')
    restrict_label_management_to_admins = sgqlc.types.Field(Boolean, graphql_name='restrictLabelManagementToAdmins')
    ip_restrictions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(OrganizationIpRestrictionInput)), graphql_name='ipRestrictions')
    theme_settings = sgqlc.types.Field(JSONObject, graphql_name='themeSettings')
    customers_enabled = sgqlc.types.Field(Boolean, graphql_name='customersEnabled')
    customers_configuration = sgqlc.types.Field(JSONObject, graphql_name='customersConfiguration')
    feed_enabled = sgqlc.types.Field(Boolean, graphql_name='feedEnabled')
    default_feed_summary_schedule = sgqlc.types.Field(FeedSummarySchedule, graphql_name='defaultFeedSummarySchedule')
    ai_addon_enabled = sgqlc.types.Field(Boolean, graphql_name='aiAddonEnabled')
    personal_api_keys_enabled = sgqlc.types.Field(Boolean, graphql_name='personalApiKeysEnabled')


class OwnerSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class PagerDutyInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('api_failed_with_unauthorized_error_at',)
    api_failed_with_unauthorized_error_at = sgqlc.types.Field(DateTime, graphql_name='apiFailedWithUnauthorizedErrorAt')


class PartialNotificationChannelPreferencesInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('mobile', 'desktop', 'email', 'slack')
    mobile = sgqlc.types.Field(Boolean, graphql_name='mobile')
    desktop = sgqlc.types.Field(Boolean, graphql_name='desktop')
    email = sgqlc.types.Field(Boolean, graphql_name='email')
    slack = sgqlc.types.Field(Boolean, graphql_name='slack')


class PrioritySort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order', 'no_priority_first')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')
    no_priority_first = sgqlc.types.Field(Boolean, graphql_name='noPriorityFirst')


class ProjectCollectionFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'slug_id', 'state', 'status', 'priority', 'labels', 'searchable_content', 'completed_at', 'canceled_at', 'start_date', 'target_date', 'health', 'health_with_age', 'activity_type', 'has_related_relations', 'has_depended_on_by_relations', 'has_depends_on_relations', 'has_blocked_by_relations', 'has_blocking_relations', 'has_violated_relations', 'project_updates', 'creator', 'lead', 'members', 'issues', 'roadmaps', 'initiatives', 'project_milestones', 'completed_project_milestones', 'next_project_milestone', 'accessible_teams', 'last_applied_template', 'needs', 'customer_count', 'and_', 'or_', 'some', 'every', 'length')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    name = sgqlc.types.Field('StringComparator', graphql_name='name')
    slug_id = sgqlc.types.Field('StringComparator', graphql_name='slugId')
    state = sgqlc.types.Field('StringComparator', graphql_name='state')
    status = sgqlc.types.Field('ProjectStatusFilter', graphql_name='status')
    priority = sgqlc.types.Field(NullableNumberComparator, graphql_name='priority')
    labels = sgqlc.types.Field('ProjectLabelCollectionFilter', graphql_name='labels')
    searchable_content = sgqlc.types.Field(ContentComparator, graphql_name='searchableContent')
    completed_at = sgqlc.types.Field(NullableDateComparator, graphql_name='completedAt')
    canceled_at = sgqlc.types.Field(NullableDateComparator, graphql_name='canceledAt')
    start_date = sgqlc.types.Field(NullableDateComparator, graphql_name='startDate')
    target_date = sgqlc.types.Field(NullableDateComparator, graphql_name='targetDate')
    health = sgqlc.types.Field('StringComparator', graphql_name='health')
    health_with_age = sgqlc.types.Field('StringComparator', graphql_name='healthWithAge')
    activity_type = sgqlc.types.Field('StringComparator', graphql_name='activityType')
    has_related_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasRelatedRelations')
    has_depended_on_by_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasDependedOnByRelations')
    has_depends_on_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasDependsOnRelations')
    has_blocked_by_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasBlockedByRelations')
    has_blocking_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasBlockingRelations')
    has_violated_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasViolatedRelations')
    project_updates = sgqlc.types.Field('ProjectUpdatesCollectionFilter', graphql_name='projectUpdates')
    creator = sgqlc.types.Field('UserFilter', graphql_name='creator')
    lead = sgqlc.types.Field(NullableUserFilter, graphql_name='lead')
    members = sgqlc.types.Field('UserCollectionFilter', graphql_name='members')
    issues = sgqlc.types.Field(IssueCollectionFilter, graphql_name='issues')
    roadmaps = sgqlc.types.Field('RoadmapCollectionFilter', graphql_name='roadmaps')
    initiatives = sgqlc.types.Field(InitiativeCollectionFilter, graphql_name='initiatives')
    project_milestones = sgqlc.types.Field('ProjectMilestoneCollectionFilter', graphql_name='projectMilestones')
    completed_project_milestones = sgqlc.types.Field('ProjectMilestoneCollectionFilter', graphql_name='completedProjectMilestones')
    next_project_milestone = sgqlc.types.Field('ProjectMilestoneFilter', graphql_name='nextProjectMilestone')
    accessible_teams = sgqlc.types.Field('TeamCollectionFilter', graphql_name='accessibleTeams')
    last_applied_template = sgqlc.types.Field(NullableTemplateFilter, graphql_name='lastAppliedTemplate')
    needs = sgqlc.types.Field(CustomerNeedCollectionFilter, graphql_name='needs')
    customer_count = sgqlc.types.Field(NumberComparator, graphql_name='customerCount')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProjectCollectionFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProjectCollectionFilter')), graphql_name='or')
    some = sgqlc.types.Field('ProjectFilter', graphql_name='some')
    every = sgqlc.types.Field('ProjectFilter', graphql_name='every')
    length = sgqlc.types.Field(NumberComparator, graphql_name='length')


class ProjectCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'icon', 'color', 'status_id', 'description', 'content', 'team_ids', 'converted_from_issue_id', 'last_applied_template_id', 'lead_id', 'member_ids', 'start_date', 'start_date_resolution', 'target_date', 'target_date_resolution', 'sort_order', 'priority_sort_order', 'priority', 'label_ids')
    id = sgqlc.types.Field(String, graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    icon = sgqlc.types.Field(String, graphql_name='icon')
    color = sgqlc.types.Field(String, graphql_name='color')
    status_id = sgqlc.types.Field(String, graphql_name='statusId')
    description = sgqlc.types.Field(String, graphql_name='description')
    content = sgqlc.types.Field(String, graphql_name='content')
    team_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='teamIds')
    converted_from_issue_id = sgqlc.types.Field(String, graphql_name='convertedFromIssueId')
    last_applied_template_id = sgqlc.types.Field(String, graphql_name='lastAppliedTemplateId')
    lead_id = sgqlc.types.Field(String, graphql_name='leadId')
    member_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='memberIds')
    start_date = sgqlc.types.Field(TimelessDate, graphql_name='startDate')
    start_date_resolution = sgqlc.types.Field(DateResolutionType, graphql_name='startDateResolution')
    target_date = sgqlc.types.Field(TimelessDate, graphql_name='targetDate')
    target_date_resolution = sgqlc.types.Field(DateResolutionType, graphql_name='targetDateResolution')
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')
    priority_sort_order = sgqlc.types.Field(Float, graphql_name='prioritySortOrder')
    priority = sgqlc.types.Field(Int, graphql_name='priority')
    label_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labelIds')


class ProjectFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'slug_id', 'state', 'status', 'priority', 'labels', 'searchable_content', 'completed_at', 'canceled_at', 'start_date', 'target_date', 'health', 'health_with_age', 'activity_type', 'has_related_relations', 'has_depended_on_by_relations', 'has_depends_on_relations', 'has_blocked_by_relations', 'has_blocking_relations', 'has_violated_relations', 'project_updates', 'creator', 'lead', 'members', 'issues', 'roadmaps', 'initiatives', 'project_milestones', 'completed_project_milestones', 'next_project_milestone', 'accessible_teams', 'last_applied_template', 'needs', 'customer_count', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    name = sgqlc.types.Field('StringComparator', graphql_name='name')
    slug_id = sgqlc.types.Field('StringComparator', graphql_name='slugId')
    state = sgqlc.types.Field('StringComparator', graphql_name='state')
    status = sgqlc.types.Field('ProjectStatusFilter', graphql_name='status')
    priority = sgqlc.types.Field(NullableNumberComparator, graphql_name='priority')
    labels = sgqlc.types.Field('ProjectLabelCollectionFilter', graphql_name='labels')
    searchable_content = sgqlc.types.Field(ContentComparator, graphql_name='searchableContent')
    completed_at = sgqlc.types.Field(NullableDateComparator, graphql_name='completedAt')
    canceled_at = sgqlc.types.Field(NullableDateComparator, graphql_name='canceledAt')
    start_date = sgqlc.types.Field(NullableDateComparator, graphql_name='startDate')
    target_date = sgqlc.types.Field(NullableDateComparator, graphql_name='targetDate')
    health = sgqlc.types.Field('StringComparator', graphql_name='health')
    health_with_age = sgqlc.types.Field('StringComparator', graphql_name='healthWithAge')
    activity_type = sgqlc.types.Field('StringComparator', graphql_name='activityType')
    has_related_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasRelatedRelations')
    has_depended_on_by_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasDependedOnByRelations')
    has_depends_on_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasDependsOnRelations')
    has_blocked_by_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasBlockedByRelations')
    has_blocking_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasBlockingRelations')
    has_violated_relations = sgqlc.types.Field('RelationExistsComparator', graphql_name='hasViolatedRelations')
    project_updates = sgqlc.types.Field('ProjectUpdatesCollectionFilter', graphql_name='projectUpdates')
    creator = sgqlc.types.Field('UserFilter', graphql_name='creator')
    lead = sgqlc.types.Field(NullableUserFilter, graphql_name='lead')
    members = sgqlc.types.Field('UserCollectionFilter', graphql_name='members')
    issues = sgqlc.types.Field(IssueCollectionFilter, graphql_name='issues')
    roadmaps = sgqlc.types.Field('RoadmapCollectionFilter', graphql_name='roadmaps')
    initiatives = sgqlc.types.Field(InitiativeCollectionFilter, graphql_name='initiatives')
    project_milestones = sgqlc.types.Field('ProjectMilestoneCollectionFilter', graphql_name='projectMilestones')
    completed_project_milestones = sgqlc.types.Field('ProjectMilestoneCollectionFilter', graphql_name='completedProjectMilestones')
    next_project_milestone = sgqlc.types.Field('ProjectMilestoneFilter', graphql_name='nextProjectMilestone')
    accessible_teams = sgqlc.types.Field('TeamCollectionFilter', graphql_name='accessibleTeams')
    last_applied_template = sgqlc.types.Field(NullableTemplateFilter, graphql_name='lastAppliedTemplate')
    needs = sgqlc.types.Field(CustomerNeedCollectionFilter, graphql_name='needs')
    customer_count = sgqlc.types.Field(NumberComparator, graphql_name='customerCount')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProjectFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProjectFilter')), graphql_name='or')


class ProjectLabelCollectionFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'is_group', 'creator', 'parent', 'and_', 'or_', 'some', 'every', 'length')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    name = sgqlc.types.Field('StringComparator', graphql_name='name')
    is_group = sgqlc.types.Field(BooleanComparator, graphql_name='isGroup')
    creator = sgqlc.types.Field(NullableUserFilter, graphql_name='creator')
    parent = sgqlc.types.Field('ProjectLabelFilter', graphql_name='parent')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProjectLabelCollectionFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProjectLabelCollectionFilter')), graphql_name='or')
    some = sgqlc.types.Field('ProjectLabelCollectionFilter', graphql_name='some')
    every = sgqlc.types.Field('ProjectLabelFilter', graphql_name='every')
    length = sgqlc.types.Field(NumberComparator, graphql_name='length')


class ProjectLabelFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'is_group', 'creator', 'parent', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    name = sgqlc.types.Field('StringComparator', graphql_name='name')
    is_group = sgqlc.types.Field(BooleanComparator, graphql_name='isGroup')
    creator = sgqlc.types.Field(NullableUserFilter, graphql_name='creator')
    parent = sgqlc.types.Field('ProjectLabelFilter', graphql_name='parent')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProjectLabelFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProjectLabelFilter')), graphql_name='or')


class ProjectMilestoneCollectionFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'target_date', 'and_', 'or_', 'some', 'every', 'length')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    name = sgqlc.types.Field(NullableStringComparator, graphql_name='name')
    target_date = sgqlc.types.Field(NullableDateComparator, graphql_name='targetDate')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProjectMilestoneCollectionFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProjectMilestoneCollectionFilter')), graphql_name='or')
    some = sgqlc.types.Field('ProjectMilestoneFilter', graphql_name='some')
    every = sgqlc.types.Field('ProjectMilestoneFilter', graphql_name='every')
    length = sgqlc.types.Field(NumberComparator, graphql_name='length')


class ProjectMilestoneCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'description', 'description_data', 'target_date', 'project_id', 'sort_order')
    id = sgqlc.types.Field(String, graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    description_data = sgqlc.types.Field(JSONObject, graphql_name='descriptionData')
    target_date = sgqlc.types.Field(TimelessDate, graphql_name='targetDate')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')


class ProjectMilestoneFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'target_date', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    name = sgqlc.types.Field(NullableStringComparator, graphql_name='name')
    target_date = sgqlc.types.Field(NullableDateComparator, graphql_name='targetDate')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProjectMilestoneFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProjectMilestoneFilter')), graphql_name='or')


class ProjectMilestoneMoveInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('project_id', 'new_issue_team_id', 'add_issue_team_to_project', 'undo_issue_team_ids', 'undo_project_team_ids')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')
    new_issue_team_id = sgqlc.types.Field(String, graphql_name='newIssueTeamId')
    add_issue_team_to_project = sgqlc.types.Field(Boolean, graphql_name='addIssueTeamToProject')
    undo_issue_team_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProjectMilestoneMoveIssueToTeamInput')), graphql_name='undoIssueTeamIds')
    undo_project_team_ids = sgqlc.types.Field('ProjectMilestoneMoveProjectTeamsInput', graphql_name='undoProjectTeamIds')


class ProjectMilestoneMoveIssueToTeamInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('issue_id', 'team_id')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='issueId')
    team_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='teamId')


class ProjectMilestoneMoveProjectTeamsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('project_id', 'team_ids')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')
    team_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='teamIds')


class ProjectMilestoneUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'description', 'description_data', 'target_date', 'sort_order', 'project_id')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    description_data = sgqlc.types.Field(JSONObject, graphql_name='descriptionData')
    target_date = sgqlc.types.Field(TimelessDate, graphql_name='targetDate')
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')


class ProjectRelationCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'type', 'project_id', 'project_milestone_id', 'anchor_type', 'related_project_id', 'related_project_milestone_id', 'related_anchor_type')
    id = sgqlc.types.Field(String, graphql_name='id')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')
    project_milestone_id = sgqlc.types.Field(String, graphql_name='projectMilestoneId')
    anchor_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='anchorType')
    related_project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='relatedProjectId')
    related_project_milestone_id = sgqlc.types.Field(String, graphql_name='relatedProjectMilestoneId')
    related_anchor_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='relatedAnchorType')


class ProjectRelationUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('type', 'project_id', 'project_milestone_id', 'anchor_type', 'related_project_id', 'related_project_milestone_id', 'related_anchor_type')
    type = sgqlc.types.Field(String, graphql_name='type')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    project_milestone_id = sgqlc.types.Field(String, graphql_name='projectMilestoneId')
    anchor_type = sgqlc.types.Field(String, graphql_name='anchorType')
    related_project_id = sgqlc.types.Field(String, graphql_name='relatedProjectId')
    related_project_milestone_id = sgqlc.types.Field(String, graphql_name='relatedProjectMilestoneId')
    related_anchor_type = sgqlc.types.Field(String, graphql_name='relatedAnchorType')


class ProjectSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class ProjectStatusCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'color', 'description', 'position', 'type', 'indefinite')
    id = sgqlc.types.Field(String, graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='color')
    description = sgqlc.types.Field(String, graphql_name='description')
    position = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='position')
    type = sgqlc.types.Field(sgqlc.types.non_null(ProjectStatusType), graphql_name='type')
    indefinite = sgqlc.types.Field(Boolean, graphql_name='indefinite')


class ProjectStatusFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'description', 'position', 'type', 'projects', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    name = sgqlc.types.Field('StringComparator', graphql_name='name')
    description = sgqlc.types.Field('StringComparator', graphql_name='description')
    position = sgqlc.types.Field(NumberComparator, graphql_name='position')
    type = sgqlc.types.Field('StringComparator', graphql_name='type')
    projects = sgqlc.types.Field(ProjectCollectionFilter, graphql_name='projects')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProjectStatusFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProjectStatusFilter')), graphql_name='or')


class ProjectStatusUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'color', 'description', 'position', 'type', 'indefinite')
    name = sgqlc.types.Field(String, graphql_name='name')
    color = sgqlc.types.Field(String, graphql_name='color')
    description = sgqlc.types.Field(String, graphql_name='description')
    position = sgqlc.types.Field(Float, graphql_name='position')
    type = sgqlc.types.Field(ProjectStatusType, graphql_name='type')
    indefinite = sgqlc.types.Field(Boolean, graphql_name='indefinite')


class ProjectUpdateCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'body', 'body_data', 'project_id', 'health', 'is_diff_hidden')
    id = sgqlc.types.Field(String, graphql_name='id')
    body = sgqlc.types.Field(String, graphql_name='body')
    body_data = sgqlc.types.Field(JSON, graphql_name='bodyData')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')
    health = sgqlc.types.Field(ProjectUpdateHealthType, graphql_name='health')
    is_diff_hidden = sgqlc.types.Field(Boolean, graphql_name='isDiffHidden')


class ProjectUpdateFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'user', 'project', 'reactions', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    user = sgqlc.types.Field('UserFilter', graphql_name='user')
    project = sgqlc.types.Field(ProjectFilter, graphql_name='project')
    reactions = sgqlc.types.Field('ReactionCollectionFilter', graphql_name='reactions')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProjectUpdateFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProjectUpdateFilter')), graphql_name='or')


class ProjectUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('status_id', 'name', 'description', 'content', 'converted_from_issue_id', 'last_applied_template_id', 'icon', 'color', 'team_ids', 'project_update_reminders_paused_until_at', 'update_reminder_frequency_in_weeks', 'update_reminder_frequency', 'frequency_resolution', 'update_reminders_day', 'update_reminders_hour', 'lead_id', 'member_ids', 'start_date', 'start_date_resolution', 'target_date', 'target_date_resolution', 'completed_at', 'canceled_at', 'slack_new_issue', 'slack_issue_comments', 'slack_issue_statuses', 'sort_order', 'priority_sort_order', 'trashed', 'priority', 'label_ids')
    status_id = sgqlc.types.Field(String, graphql_name='statusId')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    content = sgqlc.types.Field(String, graphql_name='content')
    converted_from_issue_id = sgqlc.types.Field(String, graphql_name='convertedFromIssueId')
    last_applied_template_id = sgqlc.types.Field(String, graphql_name='lastAppliedTemplateId')
    icon = sgqlc.types.Field(String, graphql_name='icon')
    color = sgqlc.types.Field(String, graphql_name='color')
    team_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='teamIds')
    project_update_reminders_paused_until_at = sgqlc.types.Field(DateTime, graphql_name='projectUpdateRemindersPausedUntilAt')
    update_reminder_frequency_in_weeks = sgqlc.types.Field(Float, graphql_name='updateReminderFrequencyInWeeks')
    update_reminder_frequency = sgqlc.types.Field(Float, graphql_name='updateReminderFrequency')
    frequency_resolution = sgqlc.types.Field(FrequencyResolutionType, graphql_name='frequencyResolution')
    update_reminders_day = sgqlc.types.Field(Day, graphql_name='updateRemindersDay')
    update_reminders_hour = sgqlc.types.Field(Int, graphql_name='updateRemindersHour')
    lead_id = sgqlc.types.Field(String, graphql_name='leadId')
    member_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='memberIds')
    start_date = sgqlc.types.Field(TimelessDate, graphql_name='startDate')
    start_date_resolution = sgqlc.types.Field(DateResolutionType, graphql_name='startDateResolution')
    target_date = sgqlc.types.Field(TimelessDate, graphql_name='targetDate')
    target_date_resolution = sgqlc.types.Field(DateResolutionType, graphql_name='targetDateResolution')
    completed_at = sgqlc.types.Field(DateTime, graphql_name='completedAt')
    canceled_at = sgqlc.types.Field(DateTime, graphql_name='canceledAt')
    slack_new_issue = sgqlc.types.Field(Boolean, graphql_name='slackNewIssue')
    slack_issue_comments = sgqlc.types.Field(Boolean, graphql_name='slackIssueComments')
    slack_issue_statuses = sgqlc.types.Field(Boolean, graphql_name='slackIssueStatuses')
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')
    priority_sort_order = sgqlc.types.Field(Float, graphql_name='prioritySortOrder')
    trashed = sgqlc.types.Field(Boolean, graphql_name='trashed')
    priority = sgqlc.types.Field(Int, graphql_name='priority')
    label_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labelIds')


class ProjectUpdateUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('body', 'body_data', 'health', 'is_diff_hidden')
    body = sgqlc.types.Field(String, graphql_name='body')
    body_data = sgqlc.types.Field(JSON, graphql_name='bodyData')
    health = sgqlc.types.Field(ProjectUpdateHealthType, graphql_name='health')
    is_diff_hidden = sgqlc.types.Field(Boolean, graphql_name='isDiffHidden')


class ProjectUpdatesCollectionFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'health', 'and_', 'or_', 'some', 'every', 'length')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    health = sgqlc.types.Field('StringComparator', graphql_name='health')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProjectUpdatesCollectionFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProjectUpdatesCollectionFilter')), graphql_name='or')
    some = sgqlc.types.Field('ProjectUpdatesFilter', graphql_name='some')
    every = sgqlc.types.Field('ProjectUpdatesFilter', graphql_name='every')
    length = sgqlc.types.Field(NumberComparator, graphql_name='length')


class ProjectUpdatesFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'health', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    health = sgqlc.types.Field('StringComparator', graphql_name='health')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProjectUpdatesFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProjectUpdatesFilter')), graphql_name='or')


class PushSubscriptionCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'data', 'type')
    id = sgqlc.types.Field(String, graphql_name='id')
    data = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='data')
    type = sgqlc.types.Field(PushSubscriptionType, graphql_name='type')


class ReactionCollectionFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'emoji', 'custom_emoji_id', 'and_', 'or_', 'some', 'every', 'length')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    emoji = sgqlc.types.Field('StringComparator', graphql_name='emoji')
    custom_emoji_id = sgqlc.types.Field(IDComparator, graphql_name='customEmojiId')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ReactionCollectionFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ReactionCollectionFilter')), graphql_name='or')
    some = sgqlc.types.Field('ReactionFilter', graphql_name='some')
    every = sgqlc.types.Field('ReactionFilter', graphql_name='every')
    length = sgqlc.types.Field(NumberComparator, graphql_name='length')


class ReactionCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'emoji', 'comment_id', 'project_update_id', 'initiative_update_id', 'issue_id', 'post_id', 'pull_request_id', 'pull_request_comment_id')
    id = sgqlc.types.Field(String, graphql_name='id')
    emoji = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='emoji')
    comment_id = sgqlc.types.Field(String, graphql_name='commentId')
    project_update_id = sgqlc.types.Field(String, graphql_name='projectUpdateId')
    initiative_update_id = sgqlc.types.Field(String, graphql_name='initiativeUpdateId')
    issue_id = sgqlc.types.Field(String, graphql_name='issueId')
    post_id = sgqlc.types.Field(String, graphql_name='postId')
    pull_request_id = sgqlc.types.Field(String, graphql_name='pullRequestId')
    pull_request_comment_id = sgqlc.types.Field(String, graphql_name='pullRequestCommentId')


class ReactionFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'emoji', 'custom_emoji_id', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    emoji = sgqlc.types.Field('StringComparator', graphql_name='emoji')
    custom_emoji_id = sgqlc.types.Field(IDComparator, graphql_name='customEmojiId')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ReactionFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ReactionFilter')), graphql_name='or')


class RelationExistsComparator(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('eq', 'neq')
    eq = sgqlc.types.Field(Boolean, graphql_name='eq')
    neq = sgqlc.types.Field(Boolean, graphql_name='neq')


class RevenueSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class RoadmapCollectionFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'slug_id', 'creator', 'and_', 'or_', 'some', 'every', 'length')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    name = sgqlc.types.Field('StringComparator', graphql_name='name')
    slug_id = sgqlc.types.Field('StringComparator', graphql_name='slugId')
    creator = sgqlc.types.Field('UserFilter', graphql_name='creator')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RoadmapCollectionFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RoadmapCollectionFilter')), graphql_name='or')
    some = sgqlc.types.Field('RoadmapFilter', graphql_name='some')
    every = sgqlc.types.Field('RoadmapFilter', graphql_name='every')
    length = sgqlc.types.Field(NumberComparator, graphql_name='length')


class RoadmapCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'description', 'owner_id', 'sort_order', 'color')
    id = sgqlc.types.Field(String, graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    owner_id = sgqlc.types.Field(String, graphql_name='ownerId')
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')
    color = sgqlc.types.Field(String, graphql_name='color')


class RoadmapFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'slug_id', 'creator', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    name = sgqlc.types.Field('StringComparator', graphql_name='name')
    slug_id = sgqlc.types.Field('StringComparator', graphql_name='slugId')
    creator = sgqlc.types.Field('UserFilter', graphql_name='creator')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RoadmapFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RoadmapFilter')), graphql_name='or')


class RoadmapToProjectCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'project_id', 'roadmap_id', 'sort_order')
    id = sgqlc.types.Field(String, graphql_name='id')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')
    roadmap_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='roadmapId')
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')


class RoadmapToProjectUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('sort_order',)
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')


class RoadmapUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'description', 'owner_id', 'sort_order', 'color')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    owner_id = sgqlc.types.Field(String, graphql_name='ownerId')
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')
    color = sgqlc.types.Field(String, graphql_name='color')


class RootIssueSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order', 'sort')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')
    sort = sgqlc.types.Field(sgqlc.types.non_null(IssueSortInput), graphql_name='sort')


class SalesforceSettingsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('send_note_on_status_change', 'send_note_on_comment', 'automate_ticket_reopening_on_completion', 'automate_ticket_reopening_on_cancellation', 'automate_ticket_reopening_on_comment', 'subdomain', 'url')
    send_note_on_status_change = sgqlc.types.Field(Boolean, graphql_name='sendNoteOnStatusChange')
    send_note_on_comment = sgqlc.types.Field(Boolean, graphql_name='sendNoteOnComment')
    automate_ticket_reopening_on_completion = sgqlc.types.Field(Boolean, graphql_name='automateTicketReopeningOnCompletion')
    automate_ticket_reopening_on_cancellation = sgqlc.types.Field(Boolean, graphql_name='automateTicketReopeningOnCancellation')
    automate_ticket_reopening_on_comment = sgqlc.types.Field(Boolean, graphql_name='automateTicketReopeningOnComment')
    subdomain = sgqlc.types.Field(String, graphql_name='subdomain')
    url = sgqlc.types.Field(String, graphql_name='url')


class SentrySettingsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('organization_slug', 'organization_id', 'resolving_completes_issues', 'unresolving_reopens_issues')
    organization_slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='organizationSlug')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='organizationId')
    resolving_completes_issues = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='resolvingCompletesIssues')
    unresolving_reopens_issues = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='unresolvingReopensIssues')


class SizeSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class SlaStatusComparator(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('eq', 'neq', 'in_', 'nin', 'null')
    eq = sgqlc.types.Field(SlaStatus, graphql_name='eq')
    neq = sgqlc.types.Field(SlaStatus, graphql_name='neq')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SlaStatus)), graphql_name='in')
    nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SlaStatus)), graphql_name='nin')
    null = sgqlc.types.Field(Boolean, graphql_name='null')


class SlaStatusSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class SlackAsksSettingsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('team_name', 'team_id', 'enterprise_name', 'enterprise_id', 'should_unfurl', 'slack_channel_mapping', 'can_administrate')
    team_name = sgqlc.types.Field(String, graphql_name='teamName')
    team_id = sgqlc.types.Field(String, graphql_name='teamId')
    enterprise_name = sgqlc.types.Field(String, graphql_name='enterpriseName')
    enterprise_id = sgqlc.types.Field(String, graphql_name='enterpriseId')
    should_unfurl = sgqlc.types.Field(Boolean, graphql_name='shouldUnfurl')
    slack_channel_mapping = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SlackChannelNameMappingInput')), graphql_name='slackChannelMapping')
    can_administrate = sgqlc.types.Field(sgqlc.types.non_null(UserRoleType), graphql_name='canAdministrate')


class SlackAsksTeamSettingsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'has_default_ask')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    has_default_ask = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasDefaultAsk')


class SlackChannelNameMappingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'is_private', 'is_shared', 'bot_added', 'teams', 'auto_create_on_message', 'auto_create_on_emoji', 'auto_create_on_bot_mention', 'auto_create_template_id', 'post_cancellation_updates', 'post_completion_updates', 'post_accepted_from_triage_updates', 'ai_titles')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    is_private = sgqlc.types.Field(Boolean, graphql_name='isPrivate')
    is_shared = sgqlc.types.Field(Boolean, graphql_name='isShared')
    bot_added = sgqlc.types.Field(Boolean, graphql_name='botAdded')
    teams = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SlackAsksTeamSettingsInput))), graphql_name='teams')
    auto_create_on_message = sgqlc.types.Field(Boolean, graphql_name='autoCreateOnMessage')
    auto_create_on_emoji = sgqlc.types.Field(Boolean, graphql_name='autoCreateOnEmoji')
    auto_create_on_bot_mention = sgqlc.types.Field(Boolean, graphql_name='autoCreateOnBotMention')
    auto_create_template_id = sgqlc.types.Field(String, graphql_name='autoCreateTemplateId')
    post_cancellation_updates = sgqlc.types.Field(Boolean, graphql_name='postCancellationUpdates')
    post_completion_updates = sgqlc.types.Field(Boolean, graphql_name='postCompletionUpdates')
    post_accepted_from_triage_updates = sgqlc.types.Field(Boolean, graphql_name='postAcceptedFromTriageUpdates')
    ai_titles = sgqlc.types.Field(Boolean, graphql_name='aiTitles')


class SlackPostSettingsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('channel', 'channel_id', 'configuration_url', 'team_id', 'channel_type')
    channel = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='channel')
    channel_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='channelId')
    configuration_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='configurationUrl')
    team_id = sgqlc.types.Field(String, graphql_name='teamId')
    channel_type = sgqlc.types.Field(SlackChannelType, graphql_name='channelType')


class SlackSettingsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('team_name', 'team_id', 'enterprise_name', 'enterprise_id', 'should_unfurl', 'link_on_issue_id_mention')
    team_name = sgqlc.types.Field(String, graphql_name='teamName')
    team_id = sgqlc.types.Field(String, graphql_name='teamId')
    enterprise_name = sgqlc.types.Field(String, graphql_name='enterpriseName')
    enterprise_id = sgqlc.types.Field(String, graphql_name='enterpriseId')
    should_unfurl = sgqlc.types.Field(Boolean, graphql_name='shouldUnfurl')
    link_on_issue_id_mention = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='linkOnIssueIdMention')


class SourceMetadataComparator(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('eq', 'neq', 'in_', 'nin', 'null', 'sub_type')
    eq = sgqlc.types.Field(String, graphql_name='eq')
    neq = sgqlc.types.Field(String, graphql_name='neq')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='in')
    nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='nin')
    null = sgqlc.types.Field(Boolean, graphql_name='null')
    sub_type = sgqlc.types.Field('SubTypeComparator', graphql_name='subType')


class SourceTypeComparator(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('eq', 'neq', 'in_', 'nin', 'eq_ignore_case', 'neq_ignore_case', 'starts_with', 'starts_with_ignore_case', 'not_starts_with', 'ends_with', 'not_ends_with', 'contains', 'contains_ignore_case', 'not_contains', 'not_contains_ignore_case', 'contains_ignore_case_and_accent')
    eq = sgqlc.types.Field(String, graphql_name='eq')
    neq = sgqlc.types.Field(String, graphql_name='neq')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='in')
    nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='nin')
    eq_ignore_case = sgqlc.types.Field(String, graphql_name='eqIgnoreCase')
    neq_ignore_case = sgqlc.types.Field(String, graphql_name='neqIgnoreCase')
    starts_with = sgqlc.types.Field(String, graphql_name='startsWith')
    starts_with_ignore_case = sgqlc.types.Field(String, graphql_name='startsWithIgnoreCase')
    not_starts_with = sgqlc.types.Field(String, graphql_name='notStartsWith')
    ends_with = sgqlc.types.Field(String, graphql_name='endsWith')
    not_ends_with = sgqlc.types.Field(String, graphql_name='notEndsWith')
    contains = sgqlc.types.Field(String, graphql_name='contains')
    contains_ignore_case = sgqlc.types.Field(String, graphql_name='containsIgnoreCase')
    not_contains = sgqlc.types.Field(String, graphql_name='notContains')
    not_contains_ignore_case = sgqlc.types.Field(String, graphql_name='notContainsIgnoreCase')
    contains_ignore_case_and_accent = sgqlc.types.Field(String, graphql_name='containsIgnoreCaseAndAccent')


class StringArrayComparator(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('length', 'every', 'some')
    length = sgqlc.types.Field(NumberComparator, graphql_name='length')
    every = sgqlc.types.Field('StringItemComparator', graphql_name='every')
    some = sgqlc.types.Field('StringItemComparator', graphql_name='some')


class StringComparator(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('eq', 'neq', 'in_', 'nin', 'eq_ignore_case', 'neq_ignore_case', 'starts_with', 'starts_with_ignore_case', 'not_starts_with', 'ends_with', 'not_ends_with', 'contains', 'contains_ignore_case', 'not_contains', 'not_contains_ignore_case', 'contains_ignore_case_and_accent')
    eq = sgqlc.types.Field(String, graphql_name='eq')
    neq = sgqlc.types.Field(String, graphql_name='neq')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='in')
    nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='nin')
    eq_ignore_case = sgqlc.types.Field(String, graphql_name='eqIgnoreCase')
    neq_ignore_case = sgqlc.types.Field(String, graphql_name='neqIgnoreCase')
    starts_with = sgqlc.types.Field(String, graphql_name='startsWith')
    starts_with_ignore_case = sgqlc.types.Field(String, graphql_name='startsWithIgnoreCase')
    not_starts_with = sgqlc.types.Field(String, graphql_name='notStartsWith')
    ends_with = sgqlc.types.Field(String, graphql_name='endsWith')
    not_ends_with = sgqlc.types.Field(String, graphql_name='notEndsWith')
    contains = sgqlc.types.Field(String, graphql_name='contains')
    contains_ignore_case = sgqlc.types.Field(String, graphql_name='containsIgnoreCase')
    not_contains = sgqlc.types.Field(String, graphql_name='notContains')
    not_contains_ignore_case = sgqlc.types.Field(String, graphql_name='notContainsIgnoreCase')
    contains_ignore_case_and_accent = sgqlc.types.Field(String, graphql_name='containsIgnoreCaseAndAccent')


class StringItemComparator(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('eq', 'neq', 'in_', 'nin', 'eq_ignore_case', 'neq_ignore_case', 'starts_with', 'starts_with_ignore_case', 'not_starts_with', 'ends_with', 'not_ends_with', 'contains', 'contains_ignore_case', 'not_contains', 'not_contains_ignore_case', 'contains_ignore_case_and_accent')
    eq = sgqlc.types.Field(String, graphql_name='eq')
    neq = sgqlc.types.Field(String, graphql_name='neq')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='in')
    nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='nin')
    eq_ignore_case = sgqlc.types.Field(String, graphql_name='eqIgnoreCase')
    neq_ignore_case = sgqlc.types.Field(String, graphql_name='neqIgnoreCase')
    starts_with = sgqlc.types.Field(String, graphql_name='startsWith')
    starts_with_ignore_case = sgqlc.types.Field(String, graphql_name='startsWithIgnoreCase')
    not_starts_with = sgqlc.types.Field(String, graphql_name='notStartsWith')
    ends_with = sgqlc.types.Field(String, graphql_name='endsWith')
    not_ends_with = sgqlc.types.Field(String, graphql_name='notEndsWith')
    contains = sgqlc.types.Field(String, graphql_name='contains')
    contains_ignore_case = sgqlc.types.Field(String, graphql_name='containsIgnoreCase')
    not_contains = sgqlc.types.Field(String, graphql_name='notContains')
    not_contains_ignore_case = sgqlc.types.Field(String, graphql_name='notContainsIgnoreCase')
    contains_ignore_case_and_accent = sgqlc.types.Field(String, graphql_name='containsIgnoreCaseAndAccent')


class SubTypeComparator(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('eq', 'neq', 'in_', 'nin', 'null')
    eq = sgqlc.types.Field(String, graphql_name='eq')
    neq = sgqlc.types.Field(String, graphql_name='neq')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='in')
    nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='nin')
    null = sgqlc.types.Field(Boolean, graphql_name='null')


class TeamCollectionFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'and_', 'or_', 'some', 'every', 'length')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TeamCollectionFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TeamCollectionFilter')), graphql_name='or')
    some = sgqlc.types.Field('TeamFilter', graphql_name='some')
    every = sgqlc.types.Field('TeamFilter', graphql_name='every')
    length = sgqlc.types.Field(NumberComparator, graphql_name='length')


class TeamCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'description', 'key', 'icon', 'color', 'cycles_enabled', 'cycle_start_day', 'cycle_duration', 'cycle_cooldown_time', 'cycle_issue_auto_assign_started', 'cycle_issue_auto_assign_completed', 'cycle_lock_to_active', 'upcoming_cycle_count', 'triage_enabled', 'require_priority_to_leave_triage', 'timezone', 'inherit_issue_estimation', 'inherit_workflow_statuses', 'issue_estimation_type', 'issue_estimation_allow_zero', 'set_issue_sort_order_on_state_change', 'issue_estimation_extended', 'default_issue_estimate', 'group_issue_history', 'default_template_for_members_id', 'default_template_for_non_members_id', 'default_project_template_id', 'private', 'auto_close_period', 'auto_close_state_id', 'auto_archive_period', 'marked_as_duplicate_workflow_state_id', 'parent_id', 'inherit_product_intelligence_scope', 'product_intelligence_scope')
    id = sgqlc.types.Field(String, graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    key = sgqlc.types.Field(String, graphql_name='key')
    icon = sgqlc.types.Field(String, graphql_name='icon')
    color = sgqlc.types.Field(String, graphql_name='color')
    cycles_enabled = sgqlc.types.Field(Boolean, graphql_name='cyclesEnabled')
    cycle_start_day = sgqlc.types.Field(Float, graphql_name='cycleStartDay')
    cycle_duration = sgqlc.types.Field(Int, graphql_name='cycleDuration')
    cycle_cooldown_time = sgqlc.types.Field(Int, graphql_name='cycleCooldownTime')
    cycle_issue_auto_assign_started = sgqlc.types.Field(Boolean, graphql_name='cycleIssueAutoAssignStarted')
    cycle_issue_auto_assign_completed = sgqlc.types.Field(Boolean, graphql_name='cycleIssueAutoAssignCompleted')
    cycle_lock_to_active = sgqlc.types.Field(Boolean, graphql_name='cycleLockToActive')
    upcoming_cycle_count = sgqlc.types.Field(Float, graphql_name='upcomingCycleCount')
    triage_enabled = sgqlc.types.Field(Boolean, graphql_name='triageEnabled')
    require_priority_to_leave_triage = sgqlc.types.Field(Boolean, graphql_name='requirePriorityToLeaveTriage')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    inherit_issue_estimation = sgqlc.types.Field(Boolean, graphql_name='inheritIssueEstimation')
    inherit_workflow_statuses = sgqlc.types.Field(Boolean, graphql_name='inheritWorkflowStatuses')
    issue_estimation_type = sgqlc.types.Field(String, graphql_name='issueEstimationType')
    issue_estimation_allow_zero = sgqlc.types.Field(Boolean, graphql_name='issueEstimationAllowZero')
    set_issue_sort_order_on_state_change = sgqlc.types.Field(String, graphql_name='setIssueSortOrderOnStateChange')
    issue_estimation_extended = sgqlc.types.Field(Boolean, graphql_name='issueEstimationExtended')
    default_issue_estimate = sgqlc.types.Field(Float, graphql_name='defaultIssueEstimate')
    group_issue_history = sgqlc.types.Field(Boolean, graphql_name='groupIssueHistory')
    default_template_for_members_id = sgqlc.types.Field(String, graphql_name='defaultTemplateForMembersId')
    default_template_for_non_members_id = sgqlc.types.Field(String, graphql_name='defaultTemplateForNonMembersId')
    default_project_template_id = sgqlc.types.Field(String, graphql_name='defaultProjectTemplateId')
    private = sgqlc.types.Field(Boolean, graphql_name='private')
    auto_close_period = sgqlc.types.Field(Float, graphql_name='autoClosePeriod')
    auto_close_state_id = sgqlc.types.Field(String, graphql_name='autoCloseStateId')
    auto_archive_period = sgqlc.types.Field(Float, graphql_name='autoArchivePeriod')
    marked_as_duplicate_workflow_state_id = sgqlc.types.Field(String, graphql_name='markedAsDuplicateWorkflowStateId')
    parent_id = sgqlc.types.Field(String, graphql_name='parentId')
    inherit_product_intelligence_scope = sgqlc.types.Field(Boolean, graphql_name='inheritProductIntelligenceScope')
    product_intelligence_scope = sgqlc.types.Field(ProductIntelligenceScope, graphql_name='productIntelligenceScope')


class TeamFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'key', 'description', 'issues', 'parent', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    name = sgqlc.types.Field(StringComparator, graphql_name='name')
    key = sgqlc.types.Field(StringComparator, graphql_name='key')
    description = sgqlc.types.Field(NullableStringComparator, graphql_name='description')
    issues = sgqlc.types.Field(IssueCollectionFilter, graphql_name='issues')
    parent = sgqlc.types.Field(NullableTeamFilter, graphql_name='parent')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TeamFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TeamFilter')), graphql_name='or')


class TeamMembershipCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'user_id', 'team_id', 'owner', 'sort_order')
    id = sgqlc.types.Field(String, graphql_name='id')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userId')
    team_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='teamId')
    owner = sgqlc.types.Field(Boolean, graphql_name='owner')
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')


class TeamMembershipUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('owner', 'sort_order')
    owner = sgqlc.types.Field(Boolean, graphql_name='owner')
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')


class TeamSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class TeamUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'description', 'key', 'icon', 'color', 'cycles_enabled', 'cycle_start_day', 'cycle_duration', 'cycle_cooldown_time', 'cycle_issue_auto_assign_started', 'cycle_issue_auto_assign_completed', 'cycle_lock_to_active', 'cycle_enabled_start_date', 'upcoming_cycle_count', 'timezone', 'inherit_issue_estimation', 'issue_estimation_type', 'issue_estimation_allow_zero', 'set_issue_sort_order_on_state_change', 'issue_estimation_extended', 'default_issue_estimate', 'slack_new_issue', 'slack_issue_comments', 'slack_issue_statuses', 'group_issue_history', 'ai_thread_summaries_enabled', 'default_template_for_members_id', 'default_template_for_non_members_id', 'default_project_template_id', 'private', 'triage_enabled', 'require_priority_to_leave_triage', 'default_issue_state_id', 'auto_close_period', 'auto_close_state_id', 'auto_close_parent_issues', 'auto_close_child_issues', 'auto_archive_period', 'marked_as_duplicate_workflow_state_id', 'join_by_default', 'scim_managed', 'parent_id', 'inherit_workflow_statuses', 'inherit_product_intelligence_scope', 'product_intelligence_scope')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    key = sgqlc.types.Field(String, graphql_name='key')
    icon = sgqlc.types.Field(String, graphql_name='icon')
    color = sgqlc.types.Field(String, graphql_name='color')
    cycles_enabled = sgqlc.types.Field(Boolean, graphql_name='cyclesEnabled')
    cycle_start_day = sgqlc.types.Field(Float, graphql_name='cycleStartDay')
    cycle_duration = sgqlc.types.Field(Int, graphql_name='cycleDuration')
    cycle_cooldown_time = sgqlc.types.Field(Int, graphql_name='cycleCooldownTime')
    cycle_issue_auto_assign_started = sgqlc.types.Field(Boolean, graphql_name='cycleIssueAutoAssignStarted')
    cycle_issue_auto_assign_completed = sgqlc.types.Field(Boolean, graphql_name='cycleIssueAutoAssignCompleted')
    cycle_lock_to_active = sgqlc.types.Field(Boolean, graphql_name='cycleLockToActive')
    cycle_enabled_start_date = sgqlc.types.Field(DateTime, graphql_name='cycleEnabledStartDate')
    upcoming_cycle_count = sgqlc.types.Field(Float, graphql_name='upcomingCycleCount')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    inherit_issue_estimation = sgqlc.types.Field(Boolean, graphql_name='inheritIssueEstimation')
    issue_estimation_type = sgqlc.types.Field(String, graphql_name='issueEstimationType')
    issue_estimation_allow_zero = sgqlc.types.Field(Boolean, graphql_name='issueEstimationAllowZero')
    set_issue_sort_order_on_state_change = sgqlc.types.Field(String, graphql_name='setIssueSortOrderOnStateChange')
    issue_estimation_extended = sgqlc.types.Field(Boolean, graphql_name='issueEstimationExtended')
    default_issue_estimate = sgqlc.types.Field(Float, graphql_name='defaultIssueEstimate')
    slack_new_issue = sgqlc.types.Field(Boolean, graphql_name='slackNewIssue')
    slack_issue_comments = sgqlc.types.Field(Boolean, graphql_name='slackIssueComments')
    slack_issue_statuses = sgqlc.types.Field(Boolean, graphql_name='slackIssueStatuses')
    group_issue_history = sgqlc.types.Field(Boolean, graphql_name='groupIssueHistory')
    ai_thread_summaries_enabled = sgqlc.types.Field(Boolean, graphql_name='aiThreadSummariesEnabled')
    default_template_for_members_id = sgqlc.types.Field(String, graphql_name='defaultTemplateForMembersId')
    default_template_for_non_members_id = sgqlc.types.Field(String, graphql_name='defaultTemplateForNonMembersId')
    default_project_template_id = sgqlc.types.Field(String, graphql_name='defaultProjectTemplateId')
    private = sgqlc.types.Field(Boolean, graphql_name='private')
    triage_enabled = sgqlc.types.Field(Boolean, graphql_name='triageEnabled')
    require_priority_to_leave_triage = sgqlc.types.Field(Boolean, graphql_name='requirePriorityToLeaveTriage')
    default_issue_state_id = sgqlc.types.Field(String, graphql_name='defaultIssueStateId')
    auto_close_period = sgqlc.types.Field(Float, graphql_name='autoClosePeriod')
    auto_close_state_id = sgqlc.types.Field(String, graphql_name='autoCloseStateId')
    auto_close_parent_issues = sgqlc.types.Field(Boolean, graphql_name='autoCloseParentIssues')
    auto_close_child_issues = sgqlc.types.Field(Boolean, graphql_name='autoCloseChildIssues')
    auto_archive_period = sgqlc.types.Field(Float, graphql_name='autoArchivePeriod')
    marked_as_duplicate_workflow_state_id = sgqlc.types.Field(String, graphql_name='markedAsDuplicateWorkflowStateId')
    join_by_default = sgqlc.types.Field(Boolean, graphql_name='joinByDefault')
    scim_managed = sgqlc.types.Field(Boolean, graphql_name='scimManaged')
    parent_id = sgqlc.types.Field(String, graphql_name='parentId')
    inherit_workflow_statuses = sgqlc.types.Field(Boolean, graphql_name='inheritWorkflowStatuses')
    inherit_product_intelligence_scope = sgqlc.types.Field(Boolean, graphql_name='inheritProductIntelligenceScope')
    product_intelligence_scope = sgqlc.types.Field(ProductIntelligenceScope, graphql_name='productIntelligenceScope')


class TemplateCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'type', 'team_id', 'name', 'description', 'template_data', 'sort_order')
    id = sgqlc.types.Field(String, graphql_name='id')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    team_id = sgqlc.types.Field(String, graphql_name='teamId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    template_data = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='templateData')
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')


class TemplateUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'description', 'team_id', 'template_data', 'sort_order')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    team_id = sgqlc.types.Field(String, graphql_name='teamId')
    template_data = sgqlc.types.Field(JSON, graphql_name='templateData')
    sort_order = sgqlc.types.Field(Float, graphql_name='sortOrder')


class TierSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class TimeScheduleCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'entries', 'external_id', 'external_url')
    id = sgqlc.types.Field(String, graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    entries = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TimeScheduleEntryInput'))), graphql_name='entries')
    external_id = sgqlc.types.Field(String, graphql_name='externalId')
    external_url = sgqlc.types.Field(String, graphql_name='externalUrl')


class TimeScheduleEntryInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('starts_at', 'ends_at', 'user_id', 'user_email')
    starts_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startsAt')
    ends_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='endsAt')
    user_id = sgqlc.types.Field(String, graphql_name='userId')
    user_email = sgqlc.types.Field(String, graphql_name='userEmail')


class TimeScheduleUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'entries', 'external_id', 'external_url')
    name = sgqlc.types.Field(String, graphql_name='name')
    entries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TimeScheduleEntryInput)), graphql_name='entries')
    external_id = sgqlc.types.Field(String, graphql_name='externalId')
    external_url = sgqlc.types.Field(String, graphql_name='externalUrl')


class TitleSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class TokenUserAccountAuthInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('email', 'token', 'timezone', 'invite_link')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    token = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='token')
    timezone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='timezone')
    invite_link = sgqlc.types.Field(String, graphql_name='inviteLink')


class TriageResponsibilityCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'team_id', 'action', 'manual_selection', 'time_schedule_id')
    id = sgqlc.types.Field(String, graphql_name='id')
    team_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='teamId')
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    manual_selection = sgqlc.types.Field('TriageResponsibilityManualSelectionInput', graphql_name='manualSelection')
    time_schedule_id = sgqlc.types.Field(String, graphql_name='timeScheduleId')


class TriageResponsibilityManualSelectionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('user_ids', 'assignment_index')
    user_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='userIds')
    assignment_index = sgqlc.types.Field(Int, graphql_name='assignmentIndex')


class TriageResponsibilityUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('action', 'manual_selection', 'time_schedule_id')
    action = sgqlc.types.Field(String, graphql_name='action')
    manual_selection = sgqlc.types.Field(TriageResponsibilityManualSelectionInput, graphql_name='manualSelection')
    time_schedule_id = sgqlc.types.Field(String, graphql_name='timeScheduleId')


class UpdatedAtSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')


class UserCollectionFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'display_name', 'email', 'active', 'assigned_issues', 'admin', 'invited', 'app', 'is_me', 'and_', 'or_', 'some', 'every', 'length')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    name = sgqlc.types.Field(StringComparator, graphql_name='name')
    display_name = sgqlc.types.Field(StringComparator, graphql_name='displayName')
    email = sgqlc.types.Field(StringComparator, graphql_name='email')
    active = sgqlc.types.Field(BooleanComparator, graphql_name='active')
    assigned_issues = sgqlc.types.Field(IssueCollectionFilter, graphql_name='assignedIssues')
    admin = sgqlc.types.Field(BooleanComparator, graphql_name='admin')
    invited = sgqlc.types.Field(BooleanComparator, graphql_name='invited')
    app = sgqlc.types.Field(BooleanComparator, graphql_name='app')
    is_me = sgqlc.types.Field(BooleanComparator, graphql_name='isMe')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('UserCollectionFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('UserCollectionFilter')), graphql_name='or')
    some = sgqlc.types.Field('UserFilter', graphql_name='some')
    every = sgqlc.types.Field('UserFilter', graphql_name='every')
    length = sgqlc.types.Field(NumberComparator, graphql_name='length')


class UserFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'display_name', 'email', 'active', 'assigned_issues', 'admin', 'invited', 'app', 'is_me', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    name = sgqlc.types.Field(StringComparator, graphql_name='name')
    display_name = sgqlc.types.Field(StringComparator, graphql_name='displayName')
    email = sgqlc.types.Field(StringComparator, graphql_name='email')
    active = sgqlc.types.Field(BooleanComparator, graphql_name='active')
    assigned_issues = sgqlc.types.Field(IssueCollectionFilter, graphql_name='assignedIssues')
    admin = sgqlc.types.Field(BooleanComparator, graphql_name='admin')
    invited = sgqlc.types.Field(BooleanComparator, graphql_name='invited')
    app = sgqlc.types.Field(BooleanComparator, graphql_name='app')
    is_me = sgqlc.types.Field(BooleanComparator, graphql_name='isMe')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('UserFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('UserFilter')), graphql_name='or')


class UserSettingsUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('settings', 'subscribed_to_changelog', 'subscribed_to_dpa', 'subscribed_to_invite_accepted', 'subscribed_to_privacy_legal_updates', 'notification_category_preferences', 'notification_channel_preferences', 'notification_delivery_preferences', 'usage_warning_history', 'feed_summary_schedule')
    settings = sgqlc.types.Field(JSONObject, graphql_name='settings')
    subscribed_to_changelog = sgqlc.types.Field(Boolean, graphql_name='subscribedToChangelog')
    subscribed_to_dpa = sgqlc.types.Field(Boolean, graphql_name='subscribedToDPA')
    subscribed_to_invite_accepted = sgqlc.types.Field(Boolean, graphql_name='subscribedToInviteAccepted')
    subscribed_to_privacy_legal_updates = sgqlc.types.Field(Boolean, graphql_name='subscribedToPrivacyLegalUpdates')
    notification_category_preferences = sgqlc.types.Field(NotificationCategoryPreferencesInput, graphql_name='notificationCategoryPreferences')
    notification_channel_preferences = sgqlc.types.Field(PartialNotificationChannelPreferencesInput, graphql_name='notificationChannelPreferences')
    notification_delivery_preferences = sgqlc.types.Field(NotificationDeliveryPreferencesInput, graphql_name='notificationDeliveryPreferences')
    usage_warning_history = sgqlc.types.Field(JSONObject, graphql_name='usageWarningHistory')
    feed_summary_schedule = sgqlc.types.Field(FeedSummarySchedule, graphql_name='feedSummarySchedule')


class UserUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'display_name', 'avatar_url', 'description', 'status_emoji', 'status_label', 'status_until_at', 'timezone')
    name = sgqlc.types.Field(String, graphql_name='name')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    avatar_url = sgqlc.types.Field(String, graphql_name='avatarUrl')
    description = sgqlc.types.Field(String, graphql_name='description')
    status_emoji = sgqlc.types.Field(String, graphql_name='statusEmoji')
    status_label = sgqlc.types.Field(String, graphql_name='statusLabel')
    status_until_at = sgqlc.types.Field(DateTime, graphql_name='statusUntilAt')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')


class ViewPreferencesCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'type', 'view_type', 'preferences', 'insights', 'team_id', 'project_id', 'roadmap_id', 'initiative_id', 'label_id', 'project_label_id', 'custom_view_id', 'user_id')
    id = sgqlc.types.Field(String, graphql_name='id')
    type = sgqlc.types.Field(sgqlc.types.non_null(ViewPreferencesType), graphql_name='type')
    view_type = sgqlc.types.Field(sgqlc.types.non_null(ViewType), graphql_name='viewType')
    preferences = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='preferences')
    insights = sgqlc.types.Field(JSONObject, graphql_name='insights')
    team_id = sgqlc.types.Field(String, graphql_name='teamId')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    roadmap_id = sgqlc.types.Field(String, graphql_name='roadmapId')
    initiative_id = sgqlc.types.Field(String, graphql_name='initiativeId')
    label_id = sgqlc.types.Field(String, graphql_name='labelId')
    project_label_id = sgqlc.types.Field(String, graphql_name='projectLabelId')
    custom_view_id = sgqlc.types.Field(String, graphql_name='customViewId')
    user_id = sgqlc.types.Field(String, graphql_name='userId')


class ViewPreferencesUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('preferences', 'insights')
    preferences = sgqlc.types.Field(JSONObject, graphql_name='preferences')
    insights = sgqlc.types.Field(JSONObject, graphql_name='insights')


class WebhookCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('label', 'id', 'enabled', 'secret', 'url', 'resource_types', 'team_id', 'all_public_teams')
    label = sgqlc.types.Field(String, graphql_name='label')
    id = sgqlc.types.Field(String, graphql_name='id')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    secret = sgqlc.types.Field(String, graphql_name='secret')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    resource_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='resourceTypes')
    team_id = sgqlc.types.Field(String, graphql_name='teamId')
    all_public_teams = sgqlc.types.Field(Boolean, graphql_name='allPublicTeams')


class WebhookUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('label', 'secret', 'enabled', 'url', 'resource_types')
    label = sgqlc.types.Field(String, graphql_name='label')
    secret = sgqlc.types.Field(String, graphql_name='secret')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    url = sgqlc.types.Field(String, graphql_name='url')
    resource_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='resourceTypes')


class WorkflowStateCreateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'type', 'name', 'color', 'description', 'position', 'team_id')
    id = sgqlc.types.Field(String, graphql_name='id')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='color')
    description = sgqlc.types.Field(String, graphql_name='description')
    position = sgqlc.types.Field(Float, graphql_name='position')
    team_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='teamId')


class WorkflowStateFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'description', 'position', 'type', 'team', 'issues', 'and_', 'or_')
    id = sgqlc.types.Field(IDComparator, graphql_name='id')
    created_at = sgqlc.types.Field(DateComparator, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(DateComparator, graphql_name='updatedAt')
    name = sgqlc.types.Field(StringComparator, graphql_name='name')
    description = sgqlc.types.Field(StringComparator, graphql_name='description')
    position = sgqlc.types.Field(NumberComparator, graphql_name='position')
    type = sgqlc.types.Field(StringComparator, graphql_name='type')
    team = sgqlc.types.Field(TeamFilter, graphql_name='team')
    issues = sgqlc.types.Field(IssueCollectionFilter, graphql_name='issues')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('WorkflowStateFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('WorkflowStateFilter')), graphql_name='or')


class WorkflowStateSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('nulls', 'order', 'closed_issues_ordered_by_recency')
    nulls = sgqlc.types.Field(PaginationNulls, graphql_name='nulls')
    order = sgqlc.types.Field(PaginationSortOrder, graphql_name='order')
    closed_issues_ordered_by_recency = sgqlc.types.Field(Boolean, graphql_name='closedIssuesOrderedByRecency')


class WorkflowStateUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'color', 'description', 'position')
    name = sgqlc.types.Field(String, graphql_name='name')
    color = sgqlc.types.Field(String, graphql_name='color')
    description = sgqlc.types.Field(String, graphql_name='description')
    position = sgqlc.types.Field(Float, graphql_name='position')


class ZendeskSettingsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('send_note_on_status_change', 'send_note_on_comment', 'automate_ticket_reopening_on_completion', 'automate_ticket_reopening_on_cancellation', 'automate_ticket_reopening_on_comment', 'subdomain', 'url', 'bot_user_id', 'can_read_customers')
    send_note_on_status_change = sgqlc.types.Field(Boolean, graphql_name='sendNoteOnStatusChange')
    send_note_on_comment = sgqlc.types.Field(Boolean, graphql_name='sendNoteOnComment')
    automate_ticket_reopening_on_completion = sgqlc.types.Field(Boolean, graphql_name='automateTicketReopeningOnCompletion')
    automate_ticket_reopening_on_cancellation = sgqlc.types.Field(Boolean, graphql_name='automateTicketReopeningOnCancellation')
    automate_ticket_reopening_on_comment = sgqlc.types.Field(Boolean, graphql_name='automateTicketReopeningOnComment')
    subdomain = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='subdomain')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    bot_user_id = sgqlc.types.Field(String, graphql_name='botUserId')
    can_read_customers = sgqlc.types.Field(Boolean, graphql_name='canReadCustomers')



########################################################################
# Output Objects and Interfaces
########################################################################
class ArchivePayload(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class Node(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class Entity(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'archived_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')


class Notification(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'archived_at', 'type', 'actor', 'external_user_actor', 'user', 'read_at', 'emailed_at', 'snoozed_until_at', 'unsnoozed_at', 'url', 'inbox_url', 'title', 'subtitle', 'is_linear_actor', 'actor_avatar_url', 'actor_initials', 'actor_avatar_color', 'issue_status_type', 'project_update_health', 'grouping_key', 'grouping_priority', 'bot_actor')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    actor = sgqlc.types.Field('User', graphql_name='actor')
    external_user_actor = sgqlc.types.Field('ExternalUser', graphql_name='externalUserActor')
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')
    read_at = sgqlc.types.Field(DateTime, graphql_name='readAt')
    emailed_at = sgqlc.types.Field(DateTime, graphql_name='emailedAt')
    snoozed_until_at = sgqlc.types.Field(DateTime, graphql_name='snoozedUntilAt')
    unsnoozed_at = sgqlc.types.Field(DateTime, graphql_name='unsnoozedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    inbox_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='inboxUrl')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    subtitle = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='subtitle')
    is_linear_actor = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isLinearActor')
    actor_avatar_url = sgqlc.types.Field(String, graphql_name='actorAvatarUrl')
    actor_initials = sgqlc.types.Field(String, graphql_name='actorInitials')
    actor_avatar_color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='actorAvatarColor')
    issue_status_type = sgqlc.types.Field(String, graphql_name='issueStatusType')
    project_update_health = sgqlc.types.Field(String, graphql_name='projectUpdateHealth')
    grouping_key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='groupingKey')
    grouping_priority = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='groupingPriority')
    bot_actor = sgqlc.types.Field('ActorBot', graphql_name='botActor')


class NotificationSubscription(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'archived_at', 'subscriber', 'customer', 'custom_view', 'cycle', 'label', 'project', 'initiative', 'team', 'user', 'context_view_type', 'user_context_view_type', 'active')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    subscriber = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='subscriber')
    customer = sgqlc.types.Field('Customer', graphql_name='customer')
    custom_view = sgqlc.types.Field('CustomView', graphql_name='customView')
    cycle = sgqlc.types.Field('Cycle', graphql_name='cycle')
    label = sgqlc.types.Field('IssueLabel', graphql_name='label')
    project = sgqlc.types.Field('Project', graphql_name='project')
    initiative = sgqlc.types.Field('Initiative', graphql_name='initiative')
    team = sgqlc.types.Field('Team', graphql_name='team')
    user = sgqlc.types.Field('User', graphql_name='user')
    context_view_type = sgqlc.types.Field(ContextViewType, graphql_name='contextViewType')
    user_context_view_type = sgqlc.types.Field(UserContextViewType, graphql_name='userContextViewType')
    active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='active')


class ActorBot(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'type', 'sub_type', 'name', 'user_display_name', 'avatar_url')
    id = sgqlc.types.Field(ID, graphql_name='id')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    sub_type = sgqlc.types.Field(String, graphql_name='subType')
    name = sgqlc.types.Field(String, graphql_name='name')
    user_display_name = sgqlc.types.Field(String, graphql_name='userDisplayName')
    avatar_url = sgqlc.types.Field(String, graphql_name='avatarUrl')


class ApiKeyConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ApiKeyEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ApiKey'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class ApiKeyEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('ApiKey'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class ApiKeyPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'api_key', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    api_key = sgqlc.types.Field(sgqlc.types.non_null('ApiKey'), graphql_name='apiKey')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class AppUserAuthentication(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('created_at', 'scope', 'requested_sync_groups', 'authorizing_user')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    scope = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='scope')
    requested_sync_groups = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requestedSyncGroups')
    authorizing_user = sgqlc.types.Field('AuthorizingUser', graphql_name='authorizingUser')


class Application(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'client_id', 'name', 'description', 'developer', 'developer_url', 'image_url')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    client_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    developer = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='developer')
    developer_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='developerUrl')
    image_url = sgqlc.types.Field(String, graphql_name='imageUrl')


class ArchiveResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('archive', 'total_count', 'database_version', 'includes_dependencies')
    archive = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='archive')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='totalCount')
    database_version = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='databaseVersion')
    includes_dependencies = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='includesDependencies')


class AsksChannelConnectPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'integration', 'success', 'mapping', 'add_bot')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    integration = sgqlc.types.Field('Integration', graphql_name='integration')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')
    mapping = sgqlc.types.Field(sgqlc.types.non_null('SlackChannelNameMapping'), graphql_name='mapping')
    add_bot = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='addBot')


class AttachmentConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AttachmentEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Attachment'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class AttachmentEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Attachment'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class AttachmentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'attachment', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    attachment = sgqlc.types.Field(sgqlc.types.non_null('Attachment'), graphql_name='attachment')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class AttachmentSourcesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('sources',)
    sources = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='sources')


class AuditEntryConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AuditEntryEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AuditEntry'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class AuditEntryEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('AuditEntry'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class AuditEntryType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('type', 'description')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')


class AuthMembership(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('user_id', 'authorizing_user_id', 'created_at')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userId')
    authorizing_user_id = sgqlc.types.Field(String, graphql_name='authorizingUserId')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')


class AuthOrganization(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'enabled', 'url_key', 'previous_url_keys', 'logo_url', 'deletion_requested_at', 'release_channel', 'saml_enabled', 'saml_settings', 'allowed_auth_services', 'scim_enabled', 'service_id', 'region', 'user_count')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    url_key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='urlKey')
    previous_url_keys = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='previousUrlKeys')
    logo_url = sgqlc.types.Field(String, graphql_name='logoUrl')
    deletion_requested_at = sgqlc.types.Field(DateTime, graphql_name='deletionRequestedAt')
    release_channel = sgqlc.types.Field(sgqlc.types.non_null(ReleaseChannel), graphql_name='releaseChannel')
    saml_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='samlEnabled')
    saml_settings = sgqlc.types.Field(JSONObject, graphql_name='samlSettings')
    allowed_auth_services = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='allowedAuthServices')
    scim_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='scimEnabled')
    service_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='serviceId')
    region = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='region')
    user_count = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='userCount')


class AuthResolverResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'email', 'allow_domain_access', 'users', 'locked_users', 'available_organizations', 'locked_organizations', 'last_used_organization_id', 'token')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    allow_domain_access = sgqlc.types.Field(Boolean, graphql_name='allowDomainAccess')
    users = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AuthUser'))), graphql_name='users')
    locked_users = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AuthUser'))), graphql_name='lockedUsers')
    available_organizations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AuthOrganization)), graphql_name='availableOrganizations')
    locked_organizations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AuthOrganization)), graphql_name='lockedOrganizations')
    last_used_organization_id = sgqlc.types.Field(String, graphql_name='lastUsedOrganizationId')
    token = sgqlc.types.Field(String, graphql_name='token')


class AuthUser(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'display_name', 'email', 'avatar_url', 'role', 'active', 'user_account_id', 'organization')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    display_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='displayName')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    avatar_url = sgqlc.types.Field(String, graphql_name='avatarUrl')
    role = sgqlc.types.Field(sgqlc.types.non_null(UserRoleType), graphql_name='role')
    active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='active')
    user_account_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userAccountId')
    organization = sgqlc.types.Field(sgqlc.types.non_null(AuthOrganization), graphql_name='organization')


class AuthenticationSessionResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'type', 'ip', 'location_country', 'location_country_code', 'country_codes', 'location_region_code', 'location_city', 'user_agent', 'browser_type', 'service', 'last_active_at', 'created_at', 'updated_at', 'location', 'operating_system', 'client', 'name', 'is_current_session')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    type = sgqlc.types.Field(sgqlc.types.non_null(AuthenticationSessionType), graphql_name='type')
    ip = sgqlc.types.Field(String, graphql_name='ip')
    location_country = sgqlc.types.Field(String, graphql_name='locationCountry')
    location_country_code = sgqlc.types.Field(String, graphql_name='locationCountryCode')
    country_codes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='countryCodes')
    location_region_code = sgqlc.types.Field(String, graphql_name='locationRegionCode')
    location_city = sgqlc.types.Field(String, graphql_name='locationCity')
    user_agent = sgqlc.types.Field(String, graphql_name='userAgent')
    browser_type = sgqlc.types.Field(String, graphql_name='browserType')
    service = sgqlc.types.Field(String, graphql_name='service')
    last_active_at = sgqlc.types.Field(DateTime, graphql_name='lastActiveAt')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    location = sgqlc.types.Field(String, graphql_name='location')
    operating_system = sgqlc.types.Field(String, graphql_name='operatingSystem')
    client = sgqlc.types.Field(String, graphql_name='client')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    is_current_session = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCurrentSession')


class AuthorizedApplication(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'description', 'developer', 'developer_url', 'image_url', 'scope', 'app_id', 'client_id', 'webhooks_enabled')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    developer = sgqlc.types.Field(String, graphql_name='developer')
    developer_url = sgqlc.types.Field(String, graphql_name='developerUrl')
    image_url = sgqlc.types.Field(String, graphql_name='imageUrl')
    scope = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='scope')
    app_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='appId')
    client_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientId')
    webhooks_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='webhooksEnabled')


class AuthorizingUser(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'display_name')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    display_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='displayName')


class CommentConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CommentEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Comment'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class CommentEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Comment'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class CommentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'comment', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    comment = sgqlc.types.Field(sgqlc.types.non_null('Comment'), graphql_name='comment')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class ContactPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class CreateCsvExportReportPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class CreateOrJoinOrganizationResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('organization', 'user')
    organization = sgqlc.types.Field(sgqlc.types.non_null(AuthOrganization), graphql_name='organization')
    user = sgqlc.types.Field(sgqlc.types.non_null(AuthUser), graphql_name='user')


class CustomViewConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CustomViewEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CustomView'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class CustomViewEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('CustomView'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class CustomViewHasSubscribersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('has_subscribers',)
    has_subscribers = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasSubscribers')


class CustomViewPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'custom_view', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    custom_view = sgqlc.types.Field(sgqlc.types.non_null('CustomView'), graphql_name='customView')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class CustomViewSuggestionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'description', 'icon')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    icon = sgqlc.types.Field(String, graphql_name='icon')


class CustomerConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CustomerEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Customer'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class CustomerEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Customer'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class CustomerNeedConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CustomerNeedEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CustomerNeed'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class CustomerNeedEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('CustomerNeed'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class CustomerNeedPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'need', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    need = sgqlc.types.Field(sgqlc.types.non_null('CustomerNeed'), graphql_name='need')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class CustomerNeedUpdatePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'need', 'success', 'updated_related_needs')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    need = sgqlc.types.Field(sgqlc.types.non_null('CustomerNeed'), graphql_name='need')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')
    updated_related_needs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CustomerNeed'))), graphql_name='updatedRelatedNeeds')


class CustomerPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'customer', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    customer = sgqlc.types.Field(sgqlc.types.non_null('Customer'), graphql_name='customer')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class CustomerStatusConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CustomerStatusEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CustomerStatus'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class CustomerStatusEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('CustomerStatus'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class CustomerStatusPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'status', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    status = sgqlc.types.Field(sgqlc.types.non_null('CustomerStatus'), graphql_name='status')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class CustomerTierConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CustomerTierEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CustomerTier'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class CustomerTierEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('CustomerTier'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class CustomerTierPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'tier', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    tier = sgqlc.types.Field(sgqlc.types.non_null('CustomerTier'), graphql_name='tier')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class CycleConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CycleEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Cycle'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class CycleEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Cycle'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class CyclePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'cycle', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    cycle = sgqlc.types.Field('Cycle', graphql_name='cycle')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class DocumentConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DocumentEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Document'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class DocumentContentHistoryPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('history', 'success')
    history = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DocumentContentHistoryType'))), graphql_name='history')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class DocumentContentHistoryType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'content_data_snapshot_at', 'content_data', 'actor_ids')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    content_data_snapshot_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='contentDataSnapshotAt')
    content_data = sgqlc.types.Field(JSON, graphql_name='contentData')
    actor_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='actorIds')


class DocumentEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Document'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class DocumentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'document', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    document = sgqlc.types.Field(sgqlc.types.non_null('Document'), graphql_name='document')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class DocumentSearchPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'archive_payload', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DocumentSearchResultEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DocumentSearchResult'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    archive_payload = sgqlc.types.Field(sgqlc.types.non_null(ArchiveResponse), graphql_name='archivePayload')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='totalCount')


class DocumentSearchResultEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('DocumentSearchResult'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class DraftConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DraftEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Draft'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class DraftEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Draft'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class EmailIntakeAddressPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'email_intake_address', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    email_intake_address = sgqlc.types.Field(sgqlc.types.non_null('EmailIntakeAddress'), graphql_name='emailIntakeAddress')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class EmailUnsubscribePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class EmailUserAccountAuthChallengeResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success', 'auth_type')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')
    auth_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='authType')


class EmojiConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EmojiEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Emoji'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class EmojiEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Emoji'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class EmojiPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'emoji', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    emoji = sgqlc.types.Field(sgqlc.types.non_null('Emoji'), graphql_name='emoji')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class EntityExternalLinkConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EntityExternalLinkEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EntityExternalLink'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class EntityExternalLinkEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('EntityExternalLink'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class EntityExternalLinkPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'entity_external_link', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    entity_external_link = sgqlc.types.Field(sgqlc.types.non_null('EntityExternalLink'), graphql_name='entityExternalLink')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class ExternalEntityInfo(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'service', 'metadata')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    service = sgqlc.types.Field(sgqlc.types.non_null(ExternalSyncService), graphql_name='service')
    metadata = sgqlc.types.Field('ExternalEntityInfoMetadata', graphql_name='metadata')


class ExternalEntityInfoGithubMetadata(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('repo', 'owner', 'number')
    repo = sgqlc.types.Field(String, graphql_name='repo')
    owner = sgqlc.types.Field(String, graphql_name='owner')
    number = sgqlc.types.Field(Float, graphql_name='number')


class ExternalEntityInfoJiraMetadata(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('issue_key', 'project_id', 'issue_type_id')
    issue_key = sgqlc.types.Field(String, graphql_name='issueKey')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    issue_type_id = sgqlc.types.Field(String, graphql_name='issueTypeId')


class ExternalEntitySlackMetadata(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('is_from_slack', 'channel_id', 'channel_name', 'message_url')
    is_from_slack = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFromSlack')
    channel_id = sgqlc.types.Field(String, graphql_name='channelId')
    channel_name = sgqlc.types.Field(String, graphql_name='channelName')
    message_url = sgqlc.types.Field(String, graphql_name='messageUrl')


class ExternalUserConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ExternalUserEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ExternalUser'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class ExternalUserEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('ExternalUser'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class FavoriteConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FavoriteEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Favorite'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class FavoriteEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Favorite'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class FavoritePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'favorite', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    favorite = sgqlc.types.Field(sgqlc.types.non_null('Favorite'), graphql_name='favorite')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class FrontAttachmentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'attachment', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    attachment = sgqlc.types.Field(sgqlc.types.non_null('Attachment'), graphql_name='attachment')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class GitAutomationStateConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GitAutomationStateEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GitAutomationState'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class GitAutomationStateEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('GitAutomationState'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class GitAutomationStatePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'git_automation_state', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    git_automation_state = sgqlc.types.Field(sgqlc.types.non_null('GitAutomationState'), graphql_name='gitAutomationState')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class GitAutomationTargetBranchPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'target_branch', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    target_branch = sgqlc.types.Field(sgqlc.types.non_null('GitAutomationTargetBranch'), graphql_name='targetBranch')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class GitHubCommitIntegrationPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'integration', 'success', 'webhook_secret')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    integration = sgqlc.types.Field('Integration', graphql_name='integration')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')
    webhook_secret = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='webhookSecret')


class GitHubEnterpriseServerInstallVerificationPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class GitHubEnterpriseServerPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'integration', 'success', 'setup_url', 'install_url', 'webhook_secret')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    integration = sgqlc.types.Field('Integration', graphql_name='integration')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')
    setup_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='setupUrl')
    install_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='installUrl')
    webhook_secret = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='webhookSecret')


class GitLabIntegrationCreatePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'integration', 'success', 'webhook_secret')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    integration = sgqlc.types.Field('Integration', graphql_name='integration')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')
    webhook_secret = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='webhookSecret')


class ImageUploadFromUrlPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'url', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    url = sgqlc.types.Field(String, graphql_name='url')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class InitiativeConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('InitiativeEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Initiative'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class InitiativeEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Initiative'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class InitiativeHistoryConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('InitiativeHistoryEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('InitiativeHistory'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class InitiativeHistoryEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('InitiativeHistory'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class InitiativePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'initiative', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    initiative = sgqlc.types.Field(sgqlc.types.non_null('Initiative'), graphql_name='initiative')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class InitiativeRelationConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('InitiativeRelationEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('InitiativeRelation'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class InitiativeRelationEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('InitiativeRelation'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class InitiativeRelationPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'initiative_relation', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    initiative_relation = sgqlc.types.Field(sgqlc.types.non_null('InitiativeRelation'), graphql_name='initiativeRelation')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class InitiativeToProjectConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('InitiativeToProjectEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('InitiativeToProject'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class InitiativeToProjectEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('InitiativeToProject'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class InitiativeToProjectPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'initiative_to_project', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    initiative_to_project = sgqlc.types.Field(sgqlc.types.non_null('InitiativeToProject'), graphql_name='initiativeToProject')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class InitiativeUpdateConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('InitiativeUpdateEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('InitiativeUpdate'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class InitiativeUpdateEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('InitiativeUpdate'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class InitiativeUpdatePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'initiative_update', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    initiative_update = sgqlc.types.Field(sgqlc.types.non_null('InitiativeUpdate'), graphql_name='initiativeUpdate')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class InitiativeUpdateReminderPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class IntegrationConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IntegrationEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Integration'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class IntegrationEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Integration'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class IntegrationHasScopesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('has_all_scopes', 'missing_scopes')
    has_all_scopes = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasAllScopes')
    missing_scopes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='missingScopes')


class IntegrationPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'integration', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    integration = sgqlc.types.Field('Integration', graphql_name='integration')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class IntegrationRequestPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class IntegrationTemplateConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IntegrationTemplateEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IntegrationTemplate'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class IntegrationTemplateEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('IntegrationTemplate'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class IntegrationTemplatePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'integration_template', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    integration_template = sgqlc.types.Field(sgqlc.types.non_null('IntegrationTemplate'), graphql_name='integrationTemplate')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class IntegrationsSettingsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'integrations_settings', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    integrations_settings = sgqlc.types.Field(sgqlc.types.non_null('IntegrationsSettings'), graphql_name='integrationsSettings')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class IssueBatchPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'issues', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Issue'))), graphql_name='issues')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class IssueConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Issue'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class IssueDraftConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueDraftEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueDraft'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class IssueDraftEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('IssueDraft'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class IssueEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class IssueFilterSuggestionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('filter', 'log_id')
    filter = sgqlc.types.Field(JSONObject, graphql_name='filter')
    log_id = sgqlc.types.Field(String, graphql_name='logId')


class IssueHistoryConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueHistoryEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueHistory'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class IssueHistoryEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('IssueHistory'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class IssueImportCheckPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class IssueImportDeletePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'issue_import', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    issue_import = sgqlc.types.Field('IssueImport', graphql_name='issueImport')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class IssueImportJqlCheckPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success', 'count', 'error')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')
    count = sgqlc.types.Field(Float, graphql_name='count')
    error = sgqlc.types.Field(String, graphql_name='error')


class IssueImportPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'issue_import', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    issue_import = sgqlc.types.Field('IssueImport', graphql_name='issueImport')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class IssueImportSyncCheckPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('can_sync', 'error')
    can_sync = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canSync')
    error = sgqlc.types.Field(String, graphql_name='error')


class IssueLabelConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueLabelEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueLabel'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class IssueLabelEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('IssueLabel'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class IssueLabelPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'issue_label', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    issue_label = sgqlc.types.Field(sgqlc.types.non_null('IssueLabel'), graphql_name='issueLabel')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class IssuePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'issue', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    issue = sgqlc.types.Field('Issue', graphql_name='issue')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class IssuePriorityValue(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('priority', 'label')
    priority = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='priority')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')


class IssueRelationConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueRelationEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueRelation'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class IssueRelationEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('IssueRelation'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class IssueRelationHistoryPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('identifier', 'type')
    identifier = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='identifier')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')


class IssueRelationPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'issue_relation', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    issue_relation = sgqlc.types.Field(sgqlc.types.non_null('IssueRelation'), graphql_name='issueRelation')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class IssueSearchPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'archive_payload', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueSearchResultEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueSearchResult'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    archive_payload = sgqlc.types.Field(sgqlc.types.non_null(ArchiveResponse), graphql_name='archivePayload')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='totalCount')


class IssueSearchResultEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('IssueSearchResult'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class IssueSuggestionConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueSuggestionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueSuggestion'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class IssueSuggestionEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('IssueSuggestion'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class IssueSuggestionMetadata(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('score', 'classification', 'reasons', 'eval_log_id')
    score = sgqlc.types.Field(Float, graphql_name='score')
    classification = sgqlc.types.Field(String, graphql_name='classification')
    reasons = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='reasons')
    eval_log_id = sgqlc.types.Field(String, graphql_name='evalLogId')


class IssueTitleSuggestionFromCustomerRequestPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'title', 'log_id')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    log_id = sgqlc.types.Field(String, graphql_name='logId')


class LogoutResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class Mutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('workflow_state_create', 'workflow_state_update', 'workflow_state_archive', 'webhook_create', 'webhook_update', 'webhook_delete', 'view_preferences_create', 'view_preferences_update', 'view_preferences_delete', 'user_settings_update', 'user_settings_flags_reset', 'user_flag_update', 'notification_category_channel_subscription_update', 'user_update', 'user_discord_connect', 'user_external_user_disconnect', 'user_promote_admin', 'user_demote_admin', 'user_promote_member', 'user_demote_member', 'user_suspend', 'user_unsuspend', 'triage_responsibility_create', 'triage_responsibility_update', 'triage_responsibility_delete', 'time_schedule_create', 'time_schedule_update', 'time_schedule_upsert_external', 'time_schedule_delete', 'time_schedule_refresh_integration_schedule', 'template_create', 'template_update', 'template_delete', 'team_create', 'team_update', 'team_delete', 'team_unarchive', 'team_cycles_delete', 'team_membership_create', 'team_membership_update', 'team_membership_delete', 'team_key_delete', 'roadmap_to_project_create', 'roadmap_to_project_update', 'roadmap_to_project_delete', 'roadmap_create', 'roadmap_update', 'roadmap_archive', 'roadmap_unarchive', 'roadmap_delete', 'create_csv_export_report', 'reaction_create', 'reaction_delete', 'push_subscription_create', 'push_subscription_delete', 'project_update_create', 'project_update_update', 'project_update_archive', 'project_update_unarchive', 'project_update_delete', 'create_project_update_reminder', 'project_status_create', 'project_status_update', 'project_status_archive', 'project_status_unarchive', 'project_create', 'project_update', 'project_reassign_status', 'project_delete', 'project_archive', 'project_unarchive', 'project_add_label', 'project_remove_label', 'project_relation_create', 'project_relation_update', 'project_relation_delete', 'project_milestone_create', 'project_milestone_update', 'project_milestone_delete', 'project_milestone_move', 'organization_update', 'organization_delete_challenge', 'organization_delete', 'organization_cancel_delete', 'organization_start_trial_for_plan', 'organization_start_trial', 'organization_invite_create', 'organization_invite_update', 'resend_organization_invite', 'resend_organization_invite_by_email', 'organization_invite_delete', 'organization_domain_claim', 'organization_domain_verify', 'organization_domain_create', 'organization_domain_update', 'organization_domain_delete', 'notification_subscription_create', 'notification_subscription_update', 'notification_subscription_delete', 'notification_update', 'notification_mark_read_all', 'notification_mark_unread_all', 'notification_snooze_all', 'notification_unsnooze_all', 'notification_archive', 'notification_archive_all', 'notification_unarchive', 'issue_create', 'issue_batch_create', 'issue_update', 'issue_batch_update', 'issue_archive', 'issue_unarchive', 'issue_delete', 'issue_add_label', 'issue_remove_label', 'issue_reminder', 'issue_subscribe', 'issue_unsubscribe', 'issue_description_update_from_front', 'update_issue_summary', 'issue_relation_create', 'issue_relation_update', 'issue_relation_delete', 'issue_label_create', 'issue_label_update', 'issue_label_delete', 'issue_import_create_github', 'issue_import_create_jira', 'issue_import_create_csvjira', 'issue_import_create_clubhouse', 'issue_import_create_asana', 'issue_import_create_linear_v2', 'issue_import_delete', 'issue_import_process', 'issue_import_update', 'integrations_settings_create', 'integrations_settings_update', 'integration_template_create', 'integration_template_delete', 'integration_update', 'integration_settings_update', 'integration_github_commit_create', 'integration_github_connect', 'integration_github_import_connect', 'integration_github_import_refresh', 'integration_git_hub_enterprise_server_connect', 'integration_gitlab_connect', 'airbyte_integration_connect', 'integration_google_calendar_personal_connect', 'integration_launch_darkly_connect', 'integration_launch_darkly_personal_connect', 'jira_integration_connect', 'integration_jira_update', 'integration_jira_personal', 'integration_git_hub_personal', 'integration_intercom', 'integration_intercom_delete', 'integration_intercom_customer_data_attributes_refresh', 'integration_intercom_settings_update', 'integration_discord', 'integration_opsgenie_connect', 'integration_opsgenie_refresh_schedule_mappings', 'integration_pager_duty_connect', 'integration_pager_duty_refresh_schedule_mappings', 'update_integration_slack_scopes', 'integration_slack', 'integration_slack_asks', 'integration_slack_personal', 'integration_asks_connect_channel', 'integration_slack_post', 'integration_slack_project_post', 'integration_slack_initiative_post', 'integration_slack_custom_view_notifications', 'integration_slack_customer_channel_link', 'integration_slack_org_project_updates_post', 'integration_slack_org_initiative_updates_post', 'integration_slack_import_emojis', 'integration_figma', 'integration_google_sheets', 'refresh_google_sheets_data', 'integration_sentry_connect', 'integration_front', 'integration_zendesk', 'integration_loom', 'integration_salesforce', 'integration_delete', 'integration_archive', 'integration_request', 'initiative_update_create', 'initiative_update_update', 'initiative_update_archive', 'create_initiative_update_reminder', 'initiative_update_unarchive', 'initiative_to_project_create', 'initiative_to_project_update', 'initiative_to_project_delete', 'initiative_create', 'initiative_update', 'initiative_archive', 'initiative_unarchive', 'initiative_delete', 'initiative_relation_create', 'initiative_relation_update', 'initiative_relation_delete', 'git_automation_target_branch_create', 'git_automation_target_branch_update', 'git_automation_target_branch_delete', 'git_automation_state_create', 'git_automation_state_update', 'git_automation_state_delete', 'file_upload', 'import_file_upload', 'image_upload_from_url', 'favorite_create', 'favorite_update', 'favorite_delete', 'entity_external_link_create', 'entity_external_link_update', 'entity_external_link_delete', 'emoji_create', 'emoji_delete', 'email_unsubscribe', 'email_intake_address_create', 'email_intake_address_rotate', 'email_intake_address_update', 'email_intake_address_delete', 'document_create', 'document_update', 'document_delete', 'document_unarchive', 'cycle_create', 'cycle_update', 'cycle_archive', 'cycle_shift_all', 'cycle_start_upcoming_cycle_today', 'customer_tier_create', 'customer_tier_update', 'customer_tier_delete', 'customer_status_create', 'customer_status_update', 'customer_status_delete', 'customer_create', 'customer_update', 'customer_delete', 'customer_merge', 'customer_upsert', 'customer_need_create', 'customer_need_create_from_attachment', 'customer_need_update', 'customer_need_delete', 'customer_need_archive', 'customer_need_unarchive', 'custom_view_create', 'custom_view_update', 'custom_view_delete', 'contact_create', 'contact_sales_create', 'comment_create', 'comment_update', 'comment_delete', 'comment_resolve', 'comment_unresolve', 'email_user_account_auth_challenge', 'email_token_user_account_auth', 'saml_token_user_account_auth', 'google_user_account_auth', 'passkey_login_start', 'passkey_login_finish', 'create_organization_from_onboarding', 'join_organization_from_onboarding', 'leave_organization', 'logout', 'logout_session', 'logout_all_sessions', 'logout_other_sessions', 'attachment_create', 'attachment_update', 'attachment_link_url', 'attachment_link_git_lab_mr', 'attachment_link_git_hub_issue', 'attachment_link_git_hub_pr', 'attachment_link_zendesk', 'attachment_link_discord', 'attachment_sync_to_slack', 'attachment_link_slack', 'attachment_link_front', 'attachment_link_intercom', 'attachment_link_jira_issue', 'attachment_delete', 'api_key_create', 'api_key_delete', 'api_key_update')
    workflow_state_create = sgqlc.types.Field(sgqlc.types.non_null('WorkflowStatePayload'), graphql_name='workflowStateCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(WorkflowStateCreateInput), graphql_name='input', default=None)),
))
    )
    workflow_state_update = sgqlc.types.Field(sgqlc.types.non_null('WorkflowStatePayload'), graphql_name='workflowStateUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(WorkflowStateUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    workflow_state_archive = sgqlc.types.Field(sgqlc.types.non_null('WorkflowStateArchivePayload'), graphql_name='workflowStateArchive', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    webhook_create = sgqlc.types.Field(sgqlc.types.non_null('WebhookPayload'), graphql_name='webhookCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(WebhookCreateInput), graphql_name='input', default=None)),
))
    )
    webhook_update = sgqlc.types.Field(sgqlc.types.non_null('WebhookPayload'), graphql_name='webhookUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(WebhookUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    webhook_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='webhookDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    view_preferences_create = sgqlc.types.Field(sgqlc.types.non_null('ViewPreferencesPayload'), graphql_name='viewPreferencesCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ViewPreferencesCreateInput), graphql_name='input', default=None)),
))
    )
    view_preferences_update = sgqlc.types.Field(sgqlc.types.non_null('ViewPreferencesPayload'), graphql_name='viewPreferencesUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ViewPreferencesUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    view_preferences_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='viewPreferencesDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    user_settings_update = sgqlc.types.Field(sgqlc.types.non_null('UserSettingsPayload'), graphql_name='userSettingsUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UserSettingsUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    user_settings_flags_reset = sgqlc.types.Field(sgqlc.types.non_null('UserSettingsFlagsResetPayload'), graphql_name='userSettingsFlagsReset', args=sgqlc.types.ArgDict((
        ('flags', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(UserFlagType)), graphql_name='flags', default=None)),
))
    )
    user_flag_update = sgqlc.types.Field(sgqlc.types.non_null('UserSettingsFlagPayload'), graphql_name='userFlagUpdate', args=sgqlc.types.ArgDict((
        ('operation', sgqlc.types.Arg(sgqlc.types.non_null(UserFlagUpdateOperation), graphql_name='operation', default=None)),
        ('flag', sgqlc.types.Arg(sgqlc.types.non_null(UserFlagType), graphql_name='flag', default=None)),
))
    )
    notification_category_channel_subscription_update = sgqlc.types.Field(sgqlc.types.non_null('UserSettingsPayload'), graphql_name='notificationCategoryChannelSubscriptionUpdate', args=sgqlc.types.ArgDict((
        ('channel', sgqlc.types.Arg(sgqlc.types.non_null(NotificationChannel), graphql_name='channel', default=None)),
        ('category', sgqlc.types.Arg(sgqlc.types.non_null(NotificationCategory), graphql_name='category', default=None)),
        ('subscribe', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='subscribe', default=None)),
))
    )
    user_update = sgqlc.types.Field(sgqlc.types.non_null('UserPayload'), graphql_name='userUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UserUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    user_discord_connect = sgqlc.types.Field(sgqlc.types.non_null('UserPayload'), graphql_name='userDiscordConnect', args=sgqlc.types.ArgDict((
        ('redirect_uri', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='redirectUri', default=None)),
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    user_external_user_disconnect = sgqlc.types.Field(sgqlc.types.non_null('UserPayload'), graphql_name='userExternalUserDisconnect', args=sgqlc.types.ArgDict((
        ('service', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='service', default=None)),
))
    )
    user_promote_admin = sgqlc.types.Field(sgqlc.types.non_null('UserAdminPayload'), graphql_name='userPromoteAdmin', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    user_demote_admin = sgqlc.types.Field(sgqlc.types.non_null('UserAdminPayload'), graphql_name='userDemoteAdmin', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    user_promote_member = sgqlc.types.Field(sgqlc.types.non_null('UserAdminPayload'), graphql_name='userPromoteMember', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    user_demote_member = sgqlc.types.Field(sgqlc.types.non_null('UserAdminPayload'), graphql_name='userDemoteMember', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    user_suspend = sgqlc.types.Field(sgqlc.types.non_null('UserAdminPayload'), graphql_name='userSuspend', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    user_unsuspend = sgqlc.types.Field(sgqlc.types.non_null('UserAdminPayload'), graphql_name='userUnsuspend', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    triage_responsibility_create = sgqlc.types.Field(sgqlc.types.non_null('TriageResponsibilityPayload'), graphql_name='triageResponsibilityCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TriageResponsibilityCreateInput), graphql_name='input', default=None)),
))
    )
    triage_responsibility_update = sgqlc.types.Field(sgqlc.types.non_null('TriageResponsibilityPayload'), graphql_name='triageResponsibilityUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TriageResponsibilityUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    triage_responsibility_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='triageResponsibilityDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    time_schedule_create = sgqlc.types.Field(sgqlc.types.non_null('TimeSchedulePayload'), graphql_name='timeScheduleCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TimeScheduleCreateInput), graphql_name='input', default=None)),
))
    )
    time_schedule_update = sgqlc.types.Field(sgqlc.types.non_null('TimeSchedulePayload'), graphql_name='timeScheduleUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TimeScheduleUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    time_schedule_upsert_external = sgqlc.types.Field(sgqlc.types.non_null('TimeSchedulePayload'), graphql_name='timeScheduleUpsertExternal', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TimeScheduleUpdateInput), graphql_name='input', default=None)),
        ('external_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='externalId', default=None)),
))
    )
    time_schedule_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='timeScheduleDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    time_schedule_refresh_integration_schedule = sgqlc.types.Field(sgqlc.types.non_null('TimeSchedulePayload'), graphql_name='timeScheduleRefreshIntegrationSchedule', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    template_create = sgqlc.types.Field(sgqlc.types.non_null('TemplatePayload'), graphql_name='templateCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TemplateCreateInput), graphql_name='input', default=None)),
))
    )
    template_update = sgqlc.types.Field(sgqlc.types.non_null('TemplatePayload'), graphql_name='templateUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TemplateUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    template_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='templateDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    team_create = sgqlc.types.Field(sgqlc.types.non_null('TeamPayload'), graphql_name='teamCreate', args=sgqlc.types.ArgDict((
        ('copy_settings_from_team_id', sgqlc.types.Arg(String, graphql_name='copySettingsFromTeamId', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TeamCreateInput), graphql_name='input', default=None)),
))
    )
    team_update = sgqlc.types.Field(sgqlc.types.non_null('TeamPayload'), graphql_name='teamUpdate', args=sgqlc.types.ArgDict((
        ('mapping', sgqlc.types.Arg(InheritanceEntityMapping, graphql_name='mapping', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TeamUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    team_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='teamDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    team_unarchive = sgqlc.types.Field(sgqlc.types.non_null('TeamArchivePayload'), graphql_name='teamUnarchive', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    team_cycles_delete = sgqlc.types.Field(sgqlc.types.non_null('TeamPayload'), graphql_name='teamCyclesDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    team_membership_create = sgqlc.types.Field(sgqlc.types.non_null('TeamMembershipPayload'), graphql_name='teamMembershipCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TeamMembershipCreateInput), graphql_name='input', default=None)),
))
    )
    team_membership_update = sgqlc.types.Field(sgqlc.types.non_null('TeamMembershipPayload'), graphql_name='teamMembershipUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TeamMembershipUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    team_membership_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='teamMembershipDelete', args=sgqlc.types.ArgDict((
        ('also_leave_parent_teams', sgqlc.types.Arg(Boolean, graphql_name='alsoLeaveParentTeams', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    team_key_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='teamKeyDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    roadmap_to_project_create = sgqlc.types.Field(sgqlc.types.non_null('RoadmapToProjectPayload'), graphql_name='roadmapToProjectCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RoadmapToProjectCreateInput), graphql_name='input', default=None)),
))
    )
    roadmap_to_project_update = sgqlc.types.Field(sgqlc.types.non_null('RoadmapToProjectPayload'), graphql_name='roadmapToProjectUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RoadmapToProjectUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    roadmap_to_project_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='roadmapToProjectDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    roadmap_create = sgqlc.types.Field(sgqlc.types.non_null('RoadmapPayload'), graphql_name='roadmapCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RoadmapCreateInput), graphql_name='input', default=None)),
))
    )
    roadmap_update = sgqlc.types.Field(sgqlc.types.non_null('RoadmapPayload'), graphql_name='roadmapUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RoadmapUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    roadmap_archive = sgqlc.types.Field(sgqlc.types.non_null('RoadmapArchivePayload'), graphql_name='roadmapArchive', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    roadmap_unarchive = sgqlc.types.Field(sgqlc.types.non_null('RoadmapArchivePayload'), graphql_name='roadmapUnarchive', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    roadmap_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='roadmapDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    create_csv_export_report = sgqlc.types.Field(sgqlc.types.non_null(CreateCsvExportReportPayload), graphql_name='createCsvExportReport', args=sgqlc.types.ArgDict((
        ('include_private_team_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='includePrivateTeamIds', default=None)),
))
    )
    reaction_create = sgqlc.types.Field(sgqlc.types.non_null('ReactionPayload'), graphql_name='reactionCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ReactionCreateInput), graphql_name='input', default=None)),
))
    )
    reaction_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='reactionDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    push_subscription_create = sgqlc.types.Field(sgqlc.types.non_null('PushSubscriptionPayload'), graphql_name='pushSubscriptionCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(PushSubscriptionCreateInput), graphql_name='input', default=None)),
))
    )
    push_subscription_delete = sgqlc.types.Field(sgqlc.types.non_null('PushSubscriptionPayload'), graphql_name='pushSubscriptionDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    project_update_create = sgqlc.types.Field(sgqlc.types.non_null('ProjectUpdatePayload'), graphql_name='projectUpdateCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ProjectUpdateCreateInput), graphql_name='input', default=None)),
))
    )
    project_update_update = sgqlc.types.Field(sgqlc.types.non_null('ProjectUpdatePayload'), graphql_name='projectUpdateUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ProjectUpdateUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    project_update_archive = sgqlc.types.Field(sgqlc.types.non_null('ProjectUpdateArchivePayload'), graphql_name='projectUpdateArchive', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    project_update_unarchive = sgqlc.types.Field(sgqlc.types.non_null('ProjectUpdateArchivePayload'), graphql_name='projectUpdateUnarchive', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    project_update_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='projectUpdateDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    create_project_update_reminder = sgqlc.types.Field(sgqlc.types.non_null('ProjectUpdateReminderPayload'), graphql_name='createProjectUpdateReminder', args=sgqlc.types.ArgDict((
        ('user_id', sgqlc.types.Arg(String, graphql_name='userId', default=None)),
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='projectId', default=None)),
))
    )
    project_status_create = sgqlc.types.Field(sgqlc.types.non_null('ProjectStatusPayload'), graphql_name='projectStatusCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ProjectStatusCreateInput), graphql_name='input', default=None)),
))
    )
    project_status_update = sgqlc.types.Field(sgqlc.types.non_null('ProjectStatusPayload'), graphql_name='projectStatusUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ProjectStatusUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    project_status_archive = sgqlc.types.Field(sgqlc.types.non_null('ProjectStatusArchivePayload'), graphql_name='projectStatusArchive', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    project_status_unarchive = sgqlc.types.Field(sgqlc.types.non_null('ProjectStatusArchivePayload'), graphql_name='projectStatusUnarchive', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    project_create = sgqlc.types.Field(sgqlc.types.non_null('ProjectPayload'), graphql_name='projectCreate', args=sgqlc.types.ArgDict((
        ('connect_slack_channel', sgqlc.types.Arg(Boolean, graphql_name='connectSlackChannel', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ProjectCreateInput), graphql_name='input', default=None)),
))
    )
    project_update = sgqlc.types.Field(sgqlc.types.non_null('ProjectPayload'), graphql_name='projectUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ProjectUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    project_reassign_status = sgqlc.types.Field(sgqlc.types.non_null('SuccessPayload'), graphql_name='projectReassignStatus', args=sgqlc.types.ArgDict((
        ('new_project_status_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='newProjectStatusId', default=None)),
        ('original_project_status_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='originalProjectStatusId', default=None)),
))
    )
    project_delete = sgqlc.types.Field(sgqlc.types.non_null('ProjectArchivePayload'), graphql_name='projectDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    project_archive = sgqlc.types.Field(sgqlc.types.non_null('ProjectArchivePayload'), graphql_name='projectArchive', args=sgqlc.types.ArgDict((
        ('trash', sgqlc.types.Arg(Boolean, graphql_name='trash', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    project_unarchive = sgqlc.types.Field(sgqlc.types.non_null('ProjectArchivePayload'), graphql_name='projectUnarchive', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    project_add_label = sgqlc.types.Field(sgqlc.types.non_null('ProjectPayload'), graphql_name='projectAddLabel', args=sgqlc.types.ArgDict((
        ('label_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='labelId', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    project_remove_label = sgqlc.types.Field(sgqlc.types.non_null('ProjectPayload'), graphql_name='projectRemoveLabel', args=sgqlc.types.ArgDict((
        ('label_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='labelId', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    project_relation_create = sgqlc.types.Field(sgqlc.types.non_null('ProjectRelationPayload'), graphql_name='projectRelationCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ProjectRelationCreateInput), graphql_name='input', default=None)),
))
    )
    project_relation_update = sgqlc.types.Field(sgqlc.types.non_null('ProjectRelationPayload'), graphql_name='projectRelationUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ProjectRelationUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    project_relation_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='projectRelationDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    project_milestone_create = sgqlc.types.Field(sgqlc.types.non_null('ProjectMilestonePayload'), graphql_name='projectMilestoneCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ProjectMilestoneCreateInput), graphql_name='input', default=None)),
))
    )
    project_milestone_update = sgqlc.types.Field(sgqlc.types.non_null('ProjectMilestonePayload'), graphql_name='projectMilestoneUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ProjectMilestoneUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    project_milestone_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='projectMilestoneDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    project_milestone_move = sgqlc.types.Field(sgqlc.types.non_null('ProjectMilestoneMovePayload'), graphql_name='projectMilestoneMove', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ProjectMilestoneMoveInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    organization_update = sgqlc.types.Field(sgqlc.types.non_null('OrganizationPayload'), graphql_name='organizationUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(OrganizationUpdateInput), graphql_name='input', default=None)),
))
    )
    organization_delete_challenge = sgqlc.types.Field(sgqlc.types.non_null('OrganizationDeletePayload'), graphql_name='organizationDeleteChallenge')
    organization_delete = sgqlc.types.Field(sgqlc.types.non_null('OrganizationDeletePayload'), graphql_name='organizationDelete', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteOrganizationInput), graphql_name='input', default=None)),
))
    )
    organization_cancel_delete = sgqlc.types.Field(sgqlc.types.non_null('OrganizationCancelDeletePayload'), graphql_name='organizationCancelDelete')
    organization_start_trial_for_plan = sgqlc.types.Field(sgqlc.types.non_null('OrganizationStartTrialPayload'), graphql_name='organizationStartTrialForPlan', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(OrganizationStartTrialInput), graphql_name='input', default=None)),
))
    )
    organization_start_trial = sgqlc.types.Field(sgqlc.types.non_null('OrganizationStartTrialPayload'), graphql_name='organizationStartTrial')
    organization_invite_create = sgqlc.types.Field(sgqlc.types.non_null('OrganizationInvitePayload'), graphql_name='organizationInviteCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(OrganizationInviteCreateInput), graphql_name='input', default=None)),
))
    )
    organization_invite_update = sgqlc.types.Field(sgqlc.types.non_null('OrganizationInvitePayload'), graphql_name='organizationInviteUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(OrganizationInviteUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    resend_organization_invite = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='resendOrganizationInvite', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    resend_organization_invite_by_email = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='resendOrganizationInviteByEmail', args=sgqlc.types.ArgDict((
        ('email', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='email', default=None)),
))
    )
    organization_invite_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='organizationInviteDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    organization_domain_claim = sgqlc.types.Field(sgqlc.types.non_null('OrganizationDomainSimplePayload'), graphql_name='organizationDomainClaim', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    organization_domain_verify = sgqlc.types.Field(sgqlc.types.non_null('OrganizationDomainPayload'), graphql_name='organizationDomainVerify', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(OrganizationDomainVerificationInput), graphql_name='input', default=None)),
))
    )
    organization_domain_create = sgqlc.types.Field(sgqlc.types.non_null('OrganizationDomainPayload'), graphql_name='organizationDomainCreate', args=sgqlc.types.ArgDict((
        ('trigger_email_verification', sgqlc.types.Arg(Boolean, graphql_name='triggerEmailVerification', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(OrganizationDomainCreateInput), graphql_name='input', default=None)),
))
    )
    organization_domain_update = sgqlc.types.Field(sgqlc.types.non_null('OrganizationDomainPayload'), graphql_name='organizationDomainUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(OrganizationDomainUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    organization_domain_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='organizationDomainDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    notification_subscription_create = sgqlc.types.Field(sgqlc.types.non_null('NotificationSubscriptionPayload'), graphql_name='notificationSubscriptionCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(NotificationSubscriptionCreateInput), graphql_name='input', default=None)),
))
    )
    notification_subscription_update = sgqlc.types.Field(sgqlc.types.non_null('NotificationSubscriptionPayload'), graphql_name='notificationSubscriptionUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(NotificationSubscriptionUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    notification_subscription_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='notificationSubscriptionDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    notification_update = sgqlc.types.Field(sgqlc.types.non_null('NotificationPayload'), graphql_name='notificationUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(NotificationUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    notification_mark_read_all = sgqlc.types.Field(sgqlc.types.non_null('NotificationBatchActionPayload'), graphql_name='notificationMarkReadAll', args=sgqlc.types.ArgDict((
        ('read_at', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='readAt', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(NotificationEntityInput), graphql_name='input', default=None)),
))
    )
    notification_mark_unread_all = sgqlc.types.Field(sgqlc.types.non_null('NotificationBatchActionPayload'), graphql_name='notificationMarkUnreadAll', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(NotificationEntityInput), graphql_name='input', default=None)),
))
    )
    notification_snooze_all = sgqlc.types.Field(sgqlc.types.non_null('NotificationBatchActionPayload'), graphql_name='notificationSnoozeAll', args=sgqlc.types.ArgDict((
        ('snoozed_until_at', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='snoozedUntilAt', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(NotificationEntityInput), graphql_name='input', default=None)),
))
    )
    notification_unsnooze_all = sgqlc.types.Field(sgqlc.types.non_null('NotificationBatchActionPayload'), graphql_name='notificationUnsnoozeAll', args=sgqlc.types.ArgDict((
        ('unsnoozed_at', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='unsnoozedAt', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(NotificationEntityInput), graphql_name='input', default=None)),
))
    )
    notification_archive = sgqlc.types.Field(sgqlc.types.non_null('NotificationArchivePayload'), graphql_name='notificationArchive', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    notification_archive_all = sgqlc.types.Field(sgqlc.types.non_null('NotificationBatchActionPayload'), graphql_name='notificationArchiveAll', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(NotificationEntityInput), graphql_name='input', default=None)),
))
    )
    notification_unarchive = sgqlc.types.Field(sgqlc.types.non_null('NotificationArchivePayload'), graphql_name='notificationUnarchive', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    issue_create = sgqlc.types.Field(sgqlc.types.non_null(IssuePayload), graphql_name='issueCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IssueCreateInput), graphql_name='input', default=None)),
))
    )
    issue_batch_create = sgqlc.types.Field(sgqlc.types.non_null(IssueBatchPayload), graphql_name='issueBatchCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IssueBatchCreateInput), graphql_name='input', default=None)),
))
    )
    issue_update = sgqlc.types.Field(sgqlc.types.non_null(IssuePayload), graphql_name='issueUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IssueUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    issue_batch_update = sgqlc.types.Field(sgqlc.types.non_null(IssueBatchPayload), graphql_name='issueBatchUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IssueUpdateInput), graphql_name='input', default=None)),
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(UUID))), graphql_name='ids', default=None)),
))
    )
    issue_archive = sgqlc.types.Field(sgqlc.types.non_null('IssueArchivePayload'), graphql_name='issueArchive', args=sgqlc.types.ArgDict((
        ('trash', sgqlc.types.Arg(Boolean, graphql_name='trash', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    issue_unarchive = sgqlc.types.Field(sgqlc.types.non_null('IssueArchivePayload'), graphql_name='issueUnarchive', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    issue_delete = sgqlc.types.Field(sgqlc.types.non_null('IssueArchivePayload'), graphql_name='issueDelete', args=sgqlc.types.ArgDict((
        ('permanently_delete', sgqlc.types.Arg(Boolean, graphql_name='permanentlyDelete', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    issue_add_label = sgqlc.types.Field(sgqlc.types.non_null(IssuePayload), graphql_name='issueAddLabel', args=sgqlc.types.ArgDict((
        ('label_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='labelId', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    issue_remove_label = sgqlc.types.Field(sgqlc.types.non_null(IssuePayload), graphql_name='issueRemoveLabel', args=sgqlc.types.ArgDict((
        ('label_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='labelId', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    issue_reminder = sgqlc.types.Field(sgqlc.types.non_null(IssuePayload), graphql_name='issueReminder', args=sgqlc.types.ArgDict((
        ('reminder_at', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='reminderAt', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    issue_subscribe = sgqlc.types.Field(sgqlc.types.non_null(IssuePayload), graphql_name='issueSubscribe', args=sgqlc.types.ArgDict((
        ('user_id', sgqlc.types.Arg(String, graphql_name='userId', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    issue_unsubscribe = sgqlc.types.Field(sgqlc.types.non_null(IssuePayload), graphql_name='issueUnsubscribe', args=sgqlc.types.ArgDict((
        ('user_id', sgqlc.types.Arg(String, graphql_name='userId', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    issue_description_update_from_front = sgqlc.types.Field(sgqlc.types.non_null(IssuePayload), graphql_name='issueDescriptionUpdateFromFront', args=sgqlc.types.ArgDict((
        ('description', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='description', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    update_issue_summary = sgqlc.types.Field(sgqlc.types.non_null(IssuePayload), graphql_name='updateIssueSummary', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    issue_relation_create = sgqlc.types.Field(sgqlc.types.non_null(IssueRelationPayload), graphql_name='issueRelationCreate', args=sgqlc.types.ArgDict((
        ('override_created_at', sgqlc.types.Arg(DateTime, graphql_name='overrideCreatedAt', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IssueRelationCreateInput), graphql_name='input', default=None)),
))
    )
    issue_relation_update = sgqlc.types.Field(sgqlc.types.non_null(IssueRelationPayload), graphql_name='issueRelationUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IssueRelationUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    issue_relation_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='issueRelationDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    issue_label_create = sgqlc.types.Field(sgqlc.types.non_null(IssueLabelPayload), graphql_name='issueLabelCreate', args=sgqlc.types.ArgDict((
        ('replace_team_labels', sgqlc.types.Arg(Boolean, graphql_name='replaceTeamLabels', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IssueLabelCreateInput), graphql_name='input', default=None)),
))
    )
    issue_label_update = sgqlc.types.Field(sgqlc.types.non_null(IssueLabelPayload), graphql_name='issueLabelUpdate', args=sgqlc.types.ArgDict((
        ('replace_team_labels', sgqlc.types.Arg(Boolean, graphql_name='replaceTeamLabels', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IssueLabelUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    issue_label_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='issueLabelDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    issue_import_create_github = sgqlc.types.Field(sgqlc.types.non_null(IssueImportPayload), graphql_name='issueImportCreateGithub', args=sgqlc.types.ArgDict((
        ('team_id', sgqlc.types.Arg(String, graphql_name='teamId', default=None)),
        ('team_name', sgqlc.types.Arg(String, graphql_name='teamName', default=None)),
        ('github_repo_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='githubRepoIds', default=None)),
        ('github_labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='githubLabels', default=None)),
        ('instant_process', sgqlc.types.Arg(Boolean, graphql_name='instantProcess', default=None)),
        ('include_closed_issues', sgqlc.types.Arg(Boolean, graphql_name='includeClosedIssues', default=None)),
))
    )
    issue_import_create_jira = sgqlc.types.Field(sgqlc.types.non_null(IssueImportPayload), graphql_name='issueImportCreateJira', args=sgqlc.types.ArgDict((
        ('team_id', sgqlc.types.Arg(String, graphql_name='teamId', default=None)),
        ('team_name', sgqlc.types.Arg(String, graphql_name='teamName', default=None)),
        ('jira_token', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='jiraToken', default=None)),
        ('jira_project', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='jiraProject', default=None)),
        ('jira_email', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='jiraEmail', default=None)),
        ('jira_hostname', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='jiraHostname', default=None)),
        ('jql', sgqlc.types.Arg(String, graphql_name='jql', default=None)),
        ('instant_process', sgqlc.types.Arg(Boolean, graphql_name='instantProcess', default=None)),
        ('include_closed_issues', sgqlc.types.Arg(Boolean, graphql_name='includeClosedIssues', default=None)),
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
))
    )
    issue_import_create_csvjira = sgqlc.types.Field(sgqlc.types.non_null(IssueImportPayload), graphql_name='issueImportCreateCSVJira', args=sgqlc.types.ArgDict((
        ('team_id', sgqlc.types.Arg(String, graphql_name='teamId', default=None)),
        ('team_name', sgqlc.types.Arg(String, graphql_name='teamName', default=None)),
        ('csv_url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='csvUrl', default=None)),
        ('jira_hostname', sgqlc.types.Arg(String, graphql_name='jiraHostname', default=None)),
        ('jira_token', sgqlc.types.Arg(String, graphql_name='jiraToken', default=None)),
        ('jira_email', sgqlc.types.Arg(String, graphql_name='jiraEmail', default=None)),
))
    )
    issue_import_create_clubhouse = sgqlc.types.Field(sgqlc.types.non_null(IssueImportPayload), graphql_name='issueImportCreateClubhouse', args=sgqlc.types.ArgDict((
        ('team_id', sgqlc.types.Arg(String, graphql_name='teamId', default=None)),
        ('team_name', sgqlc.types.Arg(String, graphql_name='teamName', default=None)),
        ('clubhouse_token', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='clubhouseToken', default=None)),
        ('clubhouse_group_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='clubhouseGroupName', default=None)),
        ('instant_process', sgqlc.types.Arg(Boolean, graphql_name='instantProcess', default=None)),
        ('include_closed_issues', sgqlc.types.Arg(Boolean, graphql_name='includeClosedIssues', default=None)),
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
))
    )
    issue_import_create_asana = sgqlc.types.Field(sgqlc.types.non_null(IssueImportPayload), graphql_name='issueImportCreateAsana', args=sgqlc.types.ArgDict((
        ('team_id', sgqlc.types.Arg(String, graphql_name='teamId', default=None)),
        ('team_name', sgqlc.types.Arg(String, graphql_name='teamName', default=None)),
        ('asana_token', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='asanaToken', default=None)),
        ('asana_team_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='asanaTeamName', default=None)),
        ('instant_process', sgqlc.types.Arg(Boolean, graphql_name='instantProcess', default=None)),
        ('include_closed_issues', sgqlc.types.Arg(Boolean, graphql_name='includeClosedIssues', default=None)),
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
))
    )
    issue_import_create_linear_v2 = sgqlc.types.Field(sgqlc.types.non_null(IssueImportPayload), graphql_name='issueImportCreateLinearV2', args=sgqlc.types.ArgDict((
        ('linear_source_organization_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='linearSourceOrganizationId', default=None)),
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
))
    )
    issue_import_delete = sgqlc.types.Field(sgqlc.types.non_null(IssueImportDeletePayload), graphql_name='issueImportDelete', args=sgqlc.types.ArgDict((
        ('issue_import_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='issueImportId', default=None)),
))
    )
    issue_import_process = sgqlc.types.Field(sgqlc.types.non_null(IssueImportPayload), graphql_name='issueImportProcess', args=sgqlc.types.ArgDict((
        ('mapping', sgqlc.types.Arg(sgqlc.types.non_null(JSONObject), graphql_name='mapping', default=None)),
        ('issue_import_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='issueImportId', default=None)),
))
    )
    issue_import_update = sgqlc.types.Field(sgqlc.types.non_null(IssueImportPayload), graphql_name='issueImportUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IssueImportUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    integrations_settings_create = sgqlc.types.Field(sgqlc.types.non_null(IntegrationsSettingsPayload), graphql_name='integrationsSettingsCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IntegrationsSettingsCreateInput), graphql_name='input', default=None)),
))
    )
    integrations_settings_update = sgqlc.types.Field(sgqlc.types.non_null(IntegrationsSettingsPayload), graphql_name='integrationsSettingsUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IntegrationsSettingsUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    integration_template_create = sgqlc.types.Field(sgqlc.types.non_null(IntegrationTemplatePayload), graphql_name='integrationTemplateCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IntegrationTemplateCreateInput), graphql_name='input', default=None)),
))
    )
    integration_template_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='integrationTemplateDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    integration_update = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IntegrationUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    integration_settings_update = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationSettingsUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IntegrationSettingsInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    integration_github_commit_create = sgqlc.types.Field(sgqlc.types.non_null(GitHubCommitIntegrationPayload), graphql_name='integrationGithubCommitCreate')
    integration_github_connect = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationGithubConnect', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
        ('installation_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='installationId', default=None)),
))
    )
    integration_github_import_connect = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationGithubImportConnect', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
        ('installation_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='installationId', default=None)),
))
    )
    integration_github_import_refresh = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationGithubImportRefresh', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    integration_git_hub_enterprise_server_connect = sgqlc.types.Field(sgqlc.types.non_null(GitHubEnterpriseServerPayload), graphql_name='integrationGitHubEnterpriseServerConnect', args=sgqlc.types.ArgDict((
        ('organization_name', sgqlc.types.Arg(String, graphql_name='organizationName', default=None)),
        ('github_url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='githubUrl', default=None)),
))
    )
    integration_gitlab_connect = sgqlc.types.Field(sgqlc.types.non_null(GitLabIntegrationCreatePayload), graphql_name='integrationGitlabConnect', args=sgqlc.types.ArgDict((
        ('gitlab_url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='gitlabUrl', default=None)),
        ('access_token', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='accessToken', default=None)),
))
    )
    airbyte_integration_connect = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='airbyteIntegrationConnect', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AirbyteConfigurationInput), graphql_name='input', default=None)),
))
    )
    integration_google_calendar_personal_connect = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationGoogleCalendarPersonalConnect', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    integration_launch_darkly_connect = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationLaunchDarklyConnect', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
        ('project_key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='projectKey', default=None)),
        ('environment', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='environment', default=None)),
))
    )
    integration_launch_darkly_personal_connect = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationLaunchDarklyPersonalConnect', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    jira_integration_connect = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='jiraIntegrationConnect', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(JiraConfigurationInput), graphql_name='input', default=None)),
))
    )
    integration_jira_update = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationJiraUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(JiraUpdateInput), graphql_name='input', default=None)),
))
    )
    integration_jira_personal = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationJiraPersonal', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(String, graphql_name='code', default=None)),
        ('access_token', sgqlc.types.Arg(String, graphql_name='accessToken', default=None)),
))
    )
    integration_git_hub_personal = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationGitHubPersonal', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    integration_intercom = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationIntercom', args=sgqlc.types.ArgDict((
        ('domain_url', sgqlc.types.Arg(String, graphql_name='domainUrl', default=None)),
        ('redirect_uri', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='redirectUri', default=None)),
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    integration_intercom_delete = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationIntercomDelete')
    integration_intercom_customer_data_attributes_refresh = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationIntercomCustomerDataAttributesRefresh')
    integration_intercom_settings_update = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationIntercomSettingsUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IntercomSettingsInput), graphql_name='input', default=None)),
))
    )
    integration_discord = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationDiscord', args=sgqlc.types.ArgDict((
        ('redirect_uri', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='redirectUri', default=None)),
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    integration_opsgenie_connect = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationOpsgenieConnect', args=sgqlc.types.ArgDict((
        ('api_key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='apiKey', default=None)),
))
    )
    integration_opsgenie_refresh_schedule_mappings = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationOpsgenieRefreshScheduleMappings')
    integration_pager_duty_connect = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationPagerDutyConnect', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
        ('redirect_uri', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='redirectUri', default=None)),
))
    )
    integration_pager_duty_refresh_schedule_mappings = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationPagerDutyRefreshScheduleMappings')
    update_integration_slack_scopes = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='updateIntegrationSlackScopes', args=sgqlc.types.ArgDict((
        ('integration_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='integrationId', default=None)),
        ('redirect_uri', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='redirectUri', default=None)),
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    integration_slack = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationSlack', args=sgqlc.types.ArgDict((
        ('should_use_v2_auth', sgqlc.types.Arg(Boolean, graphql_name='shouldUseV2Auth', default=None)),
        ('redirect_uri', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='redirectUri', default=None)),
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    integration_slack_asks = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationSlackAsks', args=sgqlc.types.ArgDict((
        ('redirect_uri', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='redirectUri', default=None)),
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    integration_slack_personal = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationSlackPersonal', args=sgqlc.types.ArgDict((
        ('redirect_uri', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='redirectUri', default=None)),
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    integration_asks_connect_channel = sgqlc.types.Field(sgqlc.types.non_null(AsksChannelConnectPayload), graphql_name='integrationAsksConnectChannel', args=sgqlc.types.ArgDict((
        ('redirect_uri', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='redirectUri', default=None)),
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    integration_slack_post = sgqlc.types.Field(sgqlc.types.non_null('SlackChannelConnectPayload'), graphql_name='integrationSlackPost', args=sgqlc.types.ArgDict((
        ('should_use_v2_auth', sgqlc.types.Arg(Boolean, graphql_name='shouldUseV2Auth', default=None)),
        ('redirect_uri', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='redirectUri', default=None)),
        ('team_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='teamId', default=None)),
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    integration_slack_project_post = sgqlc.types.Field(sgqlc.types.non_null('SlackChannelConnectPayload'), graphql_name='integrationSlackProjectPost', args=sgqlc.types.ArgDict((
        ('service', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='service', default=None)),
        ('redirect_uri', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='redirectUri', default=None)),
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='projectId', default=None)),
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    integration_slack_initiative_post = sgqlc.types.Field(sgqlc.types.non_null('SlackChannelConnectPayload'), graphql_name='integrationSlackInitiativePost', args=sgqlc.types.ArgDict((
        ('redirect_uri', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='redirectUri', default=None)),
        ('initiative_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='initiativeId', default=None)),
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    integration_slack_custom_view_notifications = sgqlc.types.Field(sgqlc.types.non_null('SlackChannelConnectPayload'), graphql_name='integrationSlackCustomViewNotifications', args=sgqlc.types.ArgDict((
        ('redirect_uri', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='redirectUri', default=None)),
        ('custom_view_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='customViewId', default=None)),
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    integration_slack_customer_channel_link = sgqlc.types.Field(sgqlc.types.non_null('SuccessPayload'), graphql_name='integrationSlackCustomerChannelLink', args=sgqlc.types.ArgDict((
        ('redirect_uri', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='redirectUri', default=None)),
        ('customer_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='customerId', default=None)),
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    integration_slack_org_project_updates_post = sgqlc.types.Field(sgqlc.types.non_null('SlackChannelConnectPayload'), graphql_name='integrationSlackOrgProjectUpdatesPost', args=sgqlc.types.ArgDict((
        ('redirect_uri', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='redirectUri', default=None)),
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    integration_slack_org_initiative_updates_post = sgqlc.types.Field(sgqlc.types.non_null('SlackChannelConnectPayload'), graphql_name='integrationSlackOrgInitiativeUpdatesPost', args=sgqlc.types.ArgDict((
        ('redirect_uri', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='redirectUri', default=None)),
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    integration_slack_import_emojis = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationSlackImportEmojis', args=sgqlc.types.ArgDict((
        ('redirect_uri', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='redirectUri', default=None)),
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    integration_figma = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationFigma', args=sgqlc.types.ArgDict((
        ('redirect_uri', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='redirectUri', default=None)),
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    integration_google_sheets = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationGoogleSheets', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    refresh_google_sheets_data = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='refreshGoogleSheetsData', args=sgqlc.types.ArgDict((
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    integration_sentry_connect = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationSentryConnect', args=sgqlc.types.ArgDict((
        ('organization_slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='organizationSlug', default=None)),
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
        ('installation_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='installationId', default=None)),
))
    )
    integration_front = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationFront', args=sgqlc.types.ArgDict((
        ('redirect_uri', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='redirectUri', default=None)),
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    integration_zendesk = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationZendesk', args=sgqlc.types.ArgDict((
        ('subdomain', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='subdomain', default=None)),
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
        ('scope', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='scope', default=None)),
        ('redirect_uri', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='redirectUri', default=None)),
))
    )
    integration_loom = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationLoom')
    integration_salesforce = sgqlc.types.Field(sgqlc.types.non_null(IntegrationPayload), graphql_name='integrationSalesforce', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
        ('subdomain', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='subdomain', default=None)),
        ('redirect_uri', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='redirectUri', default=None)),
))
    )
    integration_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='integrationDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    integration_archive = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='integrationArchive', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    integration_request = sgqlc.types.Field(sgqlc.types.non_null(IntegrationRequestPayload), graphql_name='integrationRequest', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IntegrationRequestInput), graphql_name='input', default=None)),
))
    )
    initiative_update_create = sgqlc.types.Field(sgqlc.types.non_null(InitiativeUpdatePayload), graphql_name='initiativeUpdateCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(InitiativeUpdateCreateInput), graphql_name='input', default=None)),
))
    )
    initiative_update_update = sgqlc.types.Field(sgqlc.types.non_null(InitiativeUpdatePayload), graphql_name='initiativeUpdateUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(InitiativeUpdateUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    initiative_update_archive = sgqlc.types.Field(sgqlc.types.non_null('InitiativeUpdateArchivePayload'), graphql_name='initiativeUpdateArchive', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    create_initiative_update_reminder = sgqlc.types.Field(sgqlc.types.non_null(InitiativeUpdateReminderPayload), graphql_name='createInitiativeUpdateReminder', args=sgqlc.types.ArgDict((
        ('user_id', sgqlc.types.Arg(String, graphql_name='userId', default=None)),
        ('initiative_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='initiativeId', default=None)),
))
    )
    initiative_update_unarchive = sgqlc.types.Field(sgqlc.types.non_null('InitiativeUpdateArchivePayload'), graphql_name='initiativeUpdateUnarchive', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    initiative_to_project_create = sgqlc.types.Field(sgqlc.types.non_null(InitiativeToProjectPayload), graphql_name='initiativeToProjectCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(InitiativeToProjectCreateInput), graphql_name='input', default=None)),
))
    )
    initiative_to_project_update = sgqlc.types.Field(sgqlc.types.non_null(InitiativeToProjectPayload), graphql_name='initiativeToProjectUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(InitiativeToProjectUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    initiative_to_project_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='initiativeToProjectDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    initiative_create = sgqlc.types.Field(sgqlc.types.non_null(InitiativePayload), graphql_name='initiativeCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(InitiativeCreateInput), graphql_name='input', default=None)),
))
    )
    initiative_update = sgqlc.types.Field(sgqlc.types.non_null(InitiativePayload), graphql_name='initiativeUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(InitiativeUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    initiative_archive = sgqlc.types.Field(sgqlc.types.non_null('InitiativeArchivePayload'), graphql_name='initiativeArchive', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    initiative_unarchive = sgqlc.types.Field(sgqlc.types.non_null('InitiativeArchivePayload'), graphql_name='initiativeUnarchive', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    initiative_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='initiativeDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    initiative_relation_create = sgqlc.types.Field(sgqlc.types.non_null(InitiativeRelationPayload), graphql_name='initiativeRelationCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(InitiativeRelationCreateInput), graphql_name='input', default=None)),
))
    )
    initiative_relation_update = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='initiativeRelationUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(InitiativeRelationUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    initiative_relation_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='initiativeRelationDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    git_automation_target_branch_create = sgqlc.types.Field(sgqlc.types.non_null(GitAutomationTargetBranchPayload), graphql_name='gitAutomationTargetBranchCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(GitAutomationTargetBranchCreateInput), graphql_name='input', default=None)),
))
    )
    git_automation_target_branch_update = sgqlc.types.Field(sgqlc.types.non_null(GitAutomationTargetBranchPayload), graphql_name='gitAutomationTargetBranchUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(GitAutomationTargetBranchUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    git_automation_target_branch_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='gitAutomationTargetBranchDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    git_automation_state_create = sgqlc.types.Field(sgqlc.types.non_null(GitAutomationStatePayload), graphql_name='gitAutomationStateCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(GitAutomationStateCreateInput), graphql_name='input', default=None)),
))
    )
    git_automation_state_update = sgqlc.types.Field(sgqlc.types.non_null(GitAutomationStatePayload), graphql_name='gitAutomationStateUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(GitAutomationStateUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    git_automation_state_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='gitAutomationStateDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    file_upload = sgqlc.types.Field(sgqlc.types.non_null('UploadPayload'), graphql_name='fileUpload', args=sgqlc.types.ArgDict((
        ('meta_data', sgqlc.types.Arg(JSON, graphql_name='metaData', default=None)),
        ('make_public', sgqlc.types.Arg(Boolean, graphql_name='makePublic', default=None)),
        ('size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='size', default=None)),
        ('content_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='contentType', default=None)),
        ('filename', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filename', default=None)),
))
    )
    import_file_upload = sgqlc.types.Field(sgqlc.types.non_null('UploadPayload'), graphql_name='importFileUpload', args=sgqlc.types.ArgDict((
        ('meta_data', sgqlc.types.Arg(JSON, graphql_name='metaData', default=None)),
        ('size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='size', default=None)),
        ('content_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='contentType', default=None)),
        ('filename', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filename', default=None)),
))
    )
    image_upload_from_url = sgqlc.types.Field(sgqlc.types.non_null(ImageUploadFromUrlPayload), graphql_name='imageUploadFromUrl', args=sgqlc.types.ArgDict((
        ('url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='url', default=None)),
))
    )
    favorite_create = sgqlc.types.Field(sgqlc.types.non_null(FavoritePayload), graphql_name='favoriteCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(FavoriteCreateInput), graphql_name='input', default=None)),
))
    )
    favorite_update = sgqlc.types.Field(sgqlc.types.non_null(FavoritePayload), graphql_name='favoriteUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(FavoriteUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    favorite_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='favoriteDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    entity_external_link_create = sgqlc.types.Field(sgqlc.types.non_null(EntityExternalLinkPayload), graphql_name='entityExternalLinkCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(EntityExternalLinkCreateInput), graphql_name='input', default=None)),
))
    )
    entity_external_link_update = sgqlc.types.Field(sgqlc.types.non_null(EntityExternalLinkPayload), graphql_name='entityExternalLinkUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(EntityExternalLinkUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    entity_external_link_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='entityExternalLinkDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    emoji_create = sgqlc.types.Field(sgqlc.types.non_null(EmojiPayload), graphql_name='emojiCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(EmojiCreateInput), graphql_name='input', default=None)),
))
    )
    emoji_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='emojiDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    email_unsubscribe = sgqlc.types.Field(sgqlc.types.non_null(EmailUnsubscribePayload), graphql_name='emailUnsubscribe', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(EmailUnsubscribeInput), graphql_name='input', default=None)),
))
    )
    email_intake_address_create = sgqlc.types.Field(sgqlc.types.non_null(EmailIntakeAddressPayload), graphql_name='emailIntakeAddressCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(EmailIntakeAddressCreateInput), graphql_name='input', default=None)),
))
    )
    email_intake_address_rotate = sgqlc.types.Field(sgqlc.types.non_null(EmailIntakeAddressPayload), graphql_name='emailIntakeAddressRotate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    email_intake_address_update = sgqlc.types.Field(sgqlc.types.non_null(EmailIntakeAddressPayload), graphql_name='emailIntakeAddressUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(EmailIntakeAddressUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    email_intake_address_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='emailIntakeAddressDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    document_create = sgqlc.types.Field(sgqlc.types.non_null(DocumentPayload), graphql_name='documentCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DocumentCreateInput), graphql_name='input', default=None)),
))
    )
    document_update = sgqlc.types.Field(sgqlc.types.non_null(DocumentPayload), graphql_name='documentUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DocumentUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    document_delete = sgqlc.types.Field(sgqlc.types.non_null('DocumentArchivePayload'), graphql_name='documentDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    document_unarchive = sgqlc.types.Field(sgqlc.types.non_null('DocumentArchivePayload'), graphql_name='documentUnarchive', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    cycle_create = sgqlc.types.Field(sgqlc.types.non_null(CyclePayload), graphql_name='cycleCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CycleCreateInput), graphql_name='input', default=None)),
))
    )
    cycle_update = sgqlc.types.Field(sgqlc.types.non_null(CyclePayload), graphql_name='cycleUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CycleUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    cycle_archive = sgqlc.types.Field(sgqlc.types.non_null('CycleArchivePayload'), graphql_name='cycleArchive', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    cycle_shift_all = sgqlc.types.Field(sgqlc.types.non_null(CyclePayload), graphql_name='cycleShiftAll', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CycleShiftAllInput), graphql_name='input', default=None)),
))
    )
    cycle_start_upcoming_cycle_today = sgqlc.types.Field(sgqlc.types.non_null(CyclePayload), graphql_name='cycleStartUpcomingCycleToday', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    customer_tier_create = sgqlc.types.Field(sgqlc.types.non_null(CustomerTierPayload), graphql_name='customerTierCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CustomerTierCreateInput), graphql_name='input', default=None)),
))
    )
    customer_tier_update = sgqlc.types.Field(sgqlc.types.non_null(CustomerTierPayload), graphql_name='customerTierUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CustomerTierUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    customer_tier_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='customerTierDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    customer_status_create = sgqlc.types.Field(sgqlc.types.non_null(CustomerStatusPayload), graphql_name='customerStatusCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CustomerStatusCreateInput), graphql_name='input', default=None)),
))
    )
    customer_status_update = sgqlc.types.Field(sgqlc.types.non_null(CustomerStatusPayload), graphql_name='customerStatusUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CustomerStatusUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    customer_status_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='customerStatusDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    customer_create = sgqlc.types.Field(sgqlc.types.non_null(CustomerPayload), graphql_name='customerCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CustomerCreateInput), graphql_name='input', default=None)),
))
    )
    customer_update = sgqlc.types.Field(sgqlc.types.non_null(CustomerPayload), graphql_name='customerUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CustomerUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    customer_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='customerDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    customer_merge = sgqlc.types.Field(sgqlc.types.non_null(CustomerPayload), graphql_name='customerMerge', args=sgqlc.types.ArgDict((
        ('source_customer_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='sourceCustomerId', default=None)),
        ('target_customer_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='targetCustomerId', default=None)),
))
    )
    customer_upsert = sgqlc.types.Field(sgqlc.types.non_null(CustomerPayload), graphql_name='customerUpsert', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CustomerUpsertInput), graphql_name='input', default=None)),
))
    )
    customer_need_create = sgqlc.types.Field(sgqlc.types.non_null(CustomerNeedPayload), graphql_name='customerNeedCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CustomerNeedCreateInput), graphql_name='input', default=None)),
))
    )
    customer_need_create_from_attachment = sgqlc.types.Field(sgqlc.types.non_null(CustomerNeedPayload), graphql_name='customerNeedCreateFromAttachment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CustomerNeedCreateFromAttachmentInput), graphql_name='input', default=None)),
))
    )
    customer_need_update = sgqlc.types.Field(sgqlc.types.non_null(CustomerNeedUpdatePayload), graphql_name='customerNeedUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CustomerNeedUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    customer_need_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='customerNeedDelete', args=sgqlc.types.ArgDict((
        ('keep_attachment', sgqlc.types.Arg(Boolean, graphql_name='keepAttachment', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    customer_need_archive = sgqlc.types.Field(sgqlc.types.non_null('CustomerNeedArchivePayload'), graphql_name='customerNeedArchive', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    customer_need_unarchive = sgqlc.types.Field(sgqlc.types.non_null('CustomerNeedArchivePayload'), graphql_name='customerNeedUnarchive', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    custom_view_create = sgqlc.types.Field(sgqlc.types.non_null(CustomViewPayload), graphql_name='customViewCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CustomViewCreateInput), graphql_name='input', default=None)),
))
    )
    custom_view_update = sgqlc.types.Field(sgqlc.types.non_null(CustomViewPayload), graphql_name='customViewUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CustomViewUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    custom_view_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='customViewDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    contact_create = sgqlc.types.Field(sgqlc.types.non_null(ContactPayload), graphql_name='contactCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ContactCreateInput), graphql_name='input', default=None)),
))
    )
    contact_sales_create = sgqlc.types.Field(sgqlc.types.non_null(ContactPayload), graphql_name='contactSalesCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ContactSalesCreateInput), graphql_name='input', default=None)),
))
    )
    comment_create = sgqlc.types.Field(sgqlc.types.non_null(CommentPayload), graphql_name='commentCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CommentCreateInput), graphql_name='input', default=None)),
))
    )
    comment_update = sgqlc.types.Field(sgqlc.types.non_null(CommentPayload), graphql_name='commentUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CommentUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    comment_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='commentDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    comment_resolve = sgqlc.types.Field(sgqlc.types.non_null(CommentPayload), graphql_name='commentResolve', args=sgqlc.types.ArgDict((
        ('resolving_comment_id', sgqlc.types.Arg(String, graphql_name='resolvingCommentId', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    comment_unresolve = sgqlc.types.Field(sgqlc.types.non_null(CommentPayload), graphql_name='commentUnresolve', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    email_user_account_auth_challenge = sgqlc.types.Field(sgqlc.types.non_null(EmailUserAccountAuthChallengeResponse), graphql_name='emailUserAccountAuthChallenge', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(EmailUserAccountAuthChallengeInput), graphql_name='input', default=None)),
))
    )
    email_token_user_account_auth = sgqlc.types.Field(sgqlc.types.non_null(AuthResolverResponse), graphql_name='emailTokenUserAccountAuth', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TokenUserAccountAuthInput), graphql_name='input', default=None)),
))
    )
    saml_token_user_account_auth = sgqlc.types.Field(sgqlc.types.non_null(AuthResolverResponse), graphql_name='samlTokenUserAccountAuth', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TokenUserAccountAuthInput), graphql_name='input', default=None)),
))
    )
    google_user_account_auth = sgqlc.types.Field(sgqlc.types.non_null(AuthResolverResponse), graphql_name='googleUserAccountAuth', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(GoogleUserAccountAuthInput), graphql_name='input', default=None)),
))
    )
    passkey_login_start = sgqlc.types.Field(sgqlc.types.non_null('PasskeyLoginStartResponse'), graphql_name='passkeyLoginStart', args=sgqlc.types.ArgDict((
        ('auth_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='authId', default=None)),
))
    )
    passkey_login_finish = sgqlc.types.Field(sgqlc.types.non_null(AuthResolverResponse), graphql_name='passkeyLoginFinish', args=sgqlc.types.ArgDict((
        ('response', sgqlc.types.Arg(sgqlc.types.non_null(JSONObject), graphql_name='response', default=None)),
        ('auth_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='authId', default=None)),
))
    )
    create_organization_from_onboarding = sgqlc.types.Field(sgqlc.types.non_null(CreateOrJoinOrganizationResponse), graphql_name='createOrganizationFromOnboarding', args=sgqlc.types.ArgDict((
        ('survey', sgqlc.types.Arg(OnboardingCustomerSurvey, graphql_name='survey', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateOrganizationInput), graphql_name='input', default=None)),
))
    )
    join_organization_from_onboarding = sgqlc.types.Field(sgqlc.types.non_null(CreateOrJoinOrganizationResponse), graphql_name='joinOrganizationFromOnboarding', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(JoinOrganizationInput), graphql_name='input', default=None)),
))
    )
    leave_organization = sgqlc.types.Field(sgqlc.types.non_null(CreateOrJoinOrganizationResponse), graphql_name='leaveOrganization', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='organizationId', default=None)),
))
    )
    logout = sgqlc.types.Field(sgqlc.types.non_null(LogoutResponse), graphql_name='logout', args=sgqlc.types.ArgDict((
        ('reason', sgqlc.types.Arg(String, graphql_name='reason', default=None)),
))
    )
    logout_session = sgqlc.types.Field(sgqlc.types.non_null(LogoutResponse), graphql_name='logoutSession', args=sgqlc.types.ArgDict((
        ('session_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='sessionId', default=None)),
))
    )
    logout_all_sessions = sgqlc.types.Field(sgqlc.types.non_null(LogoutResponse), graphql_name='logoutAllSessions', args=sgqlc.types.ArgDict((
        ('reason', sgqlc.types.Arg(String, graphql_name='reason', default=None)),
))
    )
    logout_other_sessions = sgqlc.types.Field(sgqlc.types.non_null(LogoutResponse), graphql_name='logoutOtherSessions', args=sgqlc.types.ArgDict((
        ('reason', sgqlc.types.Arg(String, graphql_name='reason', default=None)),
))
    )
    attachment_create = sgqlc.types.Field(sgqlc.types.non_null(AttachmentPayload), graphql_name='attachmentCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AttachmentCreateInput), graphql_name='input', default=None)),
))
    )
    attachment_update = sgqlc.types.Field(sgqlc.types.non_null(AttachmentPayload), graphql_name='attachmentUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AttachmentUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    attachment_link_url = sgqlc.types.Field(sgqlc.types.non_null(AttachmentPayload), graphql_name='attachmentLinkURL', args=sgqlc.types.ArgDict((
        ('create_as_user', sgqlc.types.Arg(String, graphql_name='createAsUser', default=None)),
        ('display_icon_url', sgqlc.types.Arg(String, graphql_name='displayIconUrl', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
        ('url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='url', default=None)),
        ('issue_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='issueId', default=None)),
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
))
    )
    attachment_link_git_lab_mr = sgqlc.types.Field(sgqlc.types.non_null(AttachmentPayload), graphql_name='attachmentLinkGitLabMR', args=sgqlc.types.ArgDict((
        ('create_as_user', sgqlc.types.Arg(String, graphql_name='createAsUser', default=None)),
        ('display_icon_url', sgqlc.types.Arg(String, graphql_name='displayIconUrl', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
        ('issue_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='issueId', default=None)),
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
        ('url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='url', default=None)),
        ('project_path_with_namespace', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='projectPathWithNamespace', default=None)),
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Float), graphql_name='number', default=None)),
))
    )
    attachment_link_git_hub_issue = sgqlc.types.Field(sgqlc.types.non_null(AttachmentPayload), graphql_name='attachmentLinkGitHubIssue', args=sgqlc.types.ArgDict((
        ('create_as_user', sgqlc.types.Arg(String, graphql_name='createAsUser', default=None)),
        ('display_icon_url', sgqlc.types.Arg(String, graphql_name='displayIconUrl', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
        ('issue_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='issueId', default=None)),
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
        ('url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='url', default=None)),
))
    )
    attachment_link_git_hub_pr = sgqlc.types.Field(sgqlc.types.non_null(AttachmentPayload), graphql_name='attachmentLinkGitHubPR', args=sgqlc.types.ArgDict((
        ('create_as_user', sgqlc.types.Arg(String, graphql_name='createAsUser', default=None)),
        ('display_icon_url', sgqlc.types.Arg(String, graphql_name='displayIconUrl', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
        ('issue_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='issueId', default=None)),
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
        ('url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='url', default=None)),
        ('link_kind', sgqlc.types.Arg(GitLinkKind, graphql_name='linkKind', default=None)),
))
    )
    attachment_link_zendesk = sgqlc.types.Field(sgqlc.types.non_null(AttachmentPayload), graphql_name='attachmentLinkZendesk', args=sgqlc.types.ArgDict((
        ('create_as_user', sgqlc.types.Arg(String, graphql_name='createAsUser', default=None)),
        ('display_icon_url', sgqlc.types.Arg(String, graphql_name='displayIconUrl', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
        ('ticket_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='ticketId', default=None)),
        ('issue_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='issueId', default=None)),
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
        ('url', sgqlc.types.Arg(String, graphql_name='url', default=None)),
))
    )
    attachment_link_discord = sgqlc.types.Field(sgqlc.types.non_null(AttachmentPayload), graphql_name='attachmentLinkDiscord', args=sgqlc.types.ArgDict((
        ('create_as_user', sgqlc.types.Arg(String, graphql_name='createAsUser', default=None)),
        ('display_icon_url', sgqlc.types.Arg(String, graphql_name='displayIconUrl', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
        ('issue_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='issueId', default=None)),
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
        ('channel_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='channelId', default=None)),
        ('message_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='messageId', default=None)),
        ('url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='url', default=None)),
))
    )
    attachment_sync_to_slack = sgqlc.types.Field(sgqlc.types.non_null(AttachmentPayload), graphql_name='attachmentSyncToSlack', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    attachment_link_slack = sgqlc.types.Field(sgqlc.types.non_null(AttachmentPayload), graphql_name='attachmentLinkSlack', args=sgqlc.types.ArgDict((
        ('create_as_user', sgqlc.types.Arg(String, graphql_name='createAsUser', default=None)),
        ('display_icon_url', sgqlc.types.Arg(String, graphql_name='displayIconUrl', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
        ('issue_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='issueId', default=None)),
        ('url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='url', default=None)),
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
        ('sync_to_comment_thread', sgqlc.types.Arg(Boolean, graphql_name='syncToCommentThread', default=None)),
))
    )
    attachment_link_front = sgqlc.types.Field(sgqlc.types.non_null(FrontAttachmentPayload), graphql_name='attachmentLinkFront', args=sgqlc.types.ArgDict((
        ('create_as_user', sgqlc.types.Arg(String, graphql_name='createAsUser', default=None)),
        ('display_icon_url', sgqlc.types.Arg(String, graphql_name='displayIconUrl', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
        ('conversation_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='conversationId', default=None)),
        ('issue_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='issueId', default=None)),
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
))
    )
    attachment_link_intercom = sgqlc.types.Field(sgqlc.types.non_null(AttachmentPayload), graphql_name='attachmentLinkIntercom', args=sgqlc.types.ArgDict((
        ('create_as_user', sgqlc.types.Arg(String, graphql_name='createAsUser', default=None)),
        ('display_icon_url', sgqlc.types.Arg(String, graphql_name='displayIconUrl', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
        ('conversation_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='conversationId', default=None)),
        ('part_id', sgqlc.types.Arg(String, graphql_name='partId', default=None)),
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
        ('issue_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='issueId', default=None)),
))
    )
    attachment_link_jira_issue = sgqlc.types.Field(sgqlc.types.non_null(AttachmentPayload), graphql_name='attachmentLinkJiraIssue', args=sgqlc.types.ArgDict((
        ('create_as_user', sgqlc.types.Arg(String, graphql_name='createAsUser', default=None)),
        ('display_icon_url', sgqlc.types.Arg(String, graphql_name='displayIconUrl', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
        ('issue_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='issueId', default=None)),
        ('jira_issue_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='jiraIssueId', default=None)),
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
        ('url', sgqlc.types.Arg(String, graphql_name='url', default=None)),
))
    )
    attachment_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='attachmentDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    api_key_create = sgqlc.types.Field(sgqlc.types.non_null(ApiKeyPayload), graphql_name='apiKeyCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ApiKeyCreateInput), graphql_name='input', default=None)),
))
    )
    api_key_delete = sgqlc.types.Field(sgqlc.types.non_null('DeletePayload'), graphql_name='apiKeyDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    api_key_update = sgqlc.types.Field(sgqlc.types.non_null(ApiKeyPayload), graphql_name='apiKeyUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ApiKeyUpdateInput), graphql_name='input', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )


class NotificationBatchActionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'notifications', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    notifications = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Notification))), graphql_name='notifications')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class NotificationCategoryPreferences(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('assignments', 'status_changes', 'comments_and_replies', 'mentions', 'reactions', 'subscriptions', 'document_changes', 'posts_and_updates', 'reminders', 'reviews', 'apps_and_integrations', 'system', 'triage', 'customers')
    assignments = sgqlc.types.Field(sgqlc.types.non_null('NotificationChannelPreferences'), graphql_name='assignments')
    status_changes = sgqlc.types.Field(sgqlc.types.non_null('NotificationChannelPreferences'), graphql_name='statusChanges')
    comments_and_replies = sgqlc.types.Field(sgqlc.types.non_null('NotificationChannelPreferences'), graphql_name='commentsAndReplies')
    mentions = sgqlc.types.Field(sgqlc.types.non_null('NotificationChannelPreferences'), graphql_name='mentions')
    reactions = sgqlc.types.Field(sgqlc.types.non_null('NotificationChannelPreferences'), graphql_name='reactions')
    subscriptions = sgqlc.types.Field(sgqlc.types.non_null('NotificationChannelPreferences'), graphql_name='subscriptions')
    document_changes = sgqlc.types.Field(sgqlc.types.non_null('NotificationChannelPreferences'), graphql_name='documentChanges')
    posts_and_updates = sgqlc.types.Field(sgqlc.types.non_null('NotificationChannelPreferences'), graphql_name='postsAndUpdates')
    reminders = sgqlc.types.Field(sgqlc.types.non_null('NotificationChannelPreferences'), graphql_name='reminders')
    reviews = sgqlc.types.Field(sgqlc.types.non_null('NotificationChannelPreferences'), graphql_name='reviews')
    apps_and_integrations = sgqlc.types.Field(sgqlc.types.non_null('NotificationChannelPreferences'), graphql_name='appsAndIntegrations')
    system = sgqlc.types.Field(sgqlc.types.non_null('NotificationChannelPreferences'), graphql_name='system')
    triage = sgqlc.types.Field(sgqlc.types.non_null('NotificationChannelPreferences'), graphql_name='triage')
    customers = sgqlc.types.Field(sgqlc.types.non_null('NotificationChannelPreferences'), graphql_name='customers')


class NotificationChannelPreferences(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('mobile', 'desktop', 'email', 'slack')
    mobile = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='mobile')
    desktop = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='desktop')
    email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='email')
    slack = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='slack')


class NotificationConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('NotificationEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Notification))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class NotificationDeliveryPreferences(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('mobile',)
    mobile = sgqlc.types.Field('NotificationDeliveryPreferencesChannel', graphql_name='mobile')


class NotificationDeliveryPreferencesChannel(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('notifications_disabled', 'schedule')
    notifications_disabled = sgqlc.types.Field(Boolean, graphql_name='notificationsDisabled')
    schedule = sgqlc.types.Field('NotificationDeliveryPreferencesSchedule', graphql_name='schedule')


class NotificationDeliveryPreferencesDay(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(String, graphql_name='start')
    end = sgqlc.types.Field(String, graphql_name='end')


class NotificationDeliveryPreferencesSchedule(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('disabled', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
    disabled = sgqlc.types.Field(Boolean, graphql_name='disabled')
    sunday = sgqlc.types.Field(sgqlc.types.non_null(NotificationDeliveryPreferencesDay), graphql_name='sunday')
    monday = sgqlc.types.Field(sgqlc.types.non_null(NotificationDeliveryPreferencesDay), graphql_name='monday')
    tuesday = sgqlc.types.Field(sgqlc.types.non_null(NotificationDeliveryPreferencesDay), graphql_name='tuesday')
    wednesday = sgqlc.types.Field(sgqlc.types.non_null(NotificationDeliveryPreferencesDay), graphql_name='wednesday')
    thursday = sgqlc.types.Field(sgqlc.types.non_null(NotificationDeliveryPreferencesDay), graphql_name='thursday')
    friday = sgqlc.types.Field(sgqlc.types.non_null(NotificationDeliveryPreferencesDay), graphql_name='friday')
    saturday = sgqlc.types.Field(sgqlc.types.non_null(NotificationDeliveryPreferencesDay), graphql_name='saturday')


class NotificationEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(Notification), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class NotificationPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'notification', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    notification = sgqlc.types.Field(sgqlc.types.non_null(Notification), graphql_name='notification')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class NotificationSubscriptionConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('NotificationSubscriptionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(NotificationSubscription))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class NotificationSubscriptionEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(NotificationSubscription), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class NotificationSubscriptionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'notification_subscription', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    notification_subscription = sgqlc.types.Field(sgqlc.types.non_null(NotificationSubscription), graphql_name='notificationSubscription')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class OrganizationAcceptedOrExpiredInviteDetailsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('status',)
    status = sgqlc.types.Field(sgqlc.types.non_null(OrganizationInviteStatus), graphql_name='status')


class OrganizationCancelDeletePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class OrganizationDeletePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class OrganizationDomainClaimPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('verification_string',)
    verification_string = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='verificationString')


class OrganizationDomainPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'organization_domain', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    organization_domain = sgqlc.types.Field(sgqlc.types.non_null('OrganizationDomain'), graphql_name='organizationDomain')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class OrganizationDomainSimplePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class OrganizationExistsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success', 'exists')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')
    exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='exists')


class OrganizationInviteConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('OrganizationInviteEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('OrganizationInvite'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class OrganizationInviteEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('OrganizationInvite'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class OrganizationInviteFullDetailsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('status', 'inviter', 'email', 'role', 'created_at', 'organization_name', 'organization_id', 'organization_logo_url', 'accepted', 'expired', 'allowed_auth_services')
    status = sgqlc.types.Field(sgqlc.types.non_null(OrganizationInviteStatus), graphql_name='status')
    inviter = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='inviter')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    role = sgqlc.types.Field(sgqlc.types.non_null(UserRoleType), graphql_name='role')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    organization_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='organizationName')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='organizationId')
    organization_logo_url = sgqlc.types.Field(String, graphql_name='organizationLogoUrl')
    accepted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='accepted')
    expired = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='expired')
    allowed_auth_services = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='allowedAuthServices')


class OrganizationInvitePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'organization_invite', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    organization_invite = sgqlc.types.Field(sgqlc.types.non_null('OrganizationInvite'), graphql_name='organizationInvite')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class OrganizationIpRestriction(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('range', 'type', 'description', 'enabled')
    range = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='range')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    description = sgqlc.types.Field(String, graphql_name='description')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')


class OrganizationMeta(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('region', 'allowed_auth_services')
    region = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='region')
    allowed_auth_services = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='allowedAuthServices')


class OrganizationPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'organization', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class OrganizationStartTrialPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class PageInfo(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('has_previous_page', 'has_next_page', 'start_cursor', 'end_cursor')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')


class PasskeyLoginStartResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success', 'options')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')
    options = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='options')


class ProjectConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Project'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class ProjectEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Project'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class ProjectFilterSuggestionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('filter', 'log_id')
    filter = sgqlc.types.Field(JSONObject, graphql_name='filter')
    log_id = sgqlc.types.Field(String, graphql_name='logId')


class ProjectHistoryConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectHistoryEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectHistory'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class ProjectHistoryEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('ProjectHistory'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class ProjectLabelConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectLabelEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectLabel'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class ProjectLabelEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('ProjectLabel'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class ProjectMilestoneConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectMilestoneEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectMilestone'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class ProjectMilestoneEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('ProjectMilestone'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class ProjectMilestoneMoveIssueToTeam(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('issue_id', 'team_id')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='issueId')
    team_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='teamId')


class ProjectMilestoneMovePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'project_milestone', 'success', 'previous_issue_team_ids', 'previous_project_team_ids')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    project_milestone = sgqlc.types.Field(sgqlc.types.non_null('ProjectMilestone'), graphql_name='projectMilestone')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')
    previous_issue_team_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProjectMilestoneMoveIssueToTeam)), graphql_name='previousIssueTeamIds')
    previous_project_team_ids = sgqlc.types.Field('ProjectMilestoneMoveProjectTeams', graphql_name='previousProjectTeamIds')


class ProjectMilestoneMoveProjectTeams(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('project_id', 'team_ids')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')
    team_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='teamIds')


class ProjectMilestonePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'project_milestone', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    project_milestone = sgqlc.types.Field(sgqlc.types.non_null('ProjectMilestone'), graphql_name='projectMilestone')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class ProjectPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'project', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    project = sgqlc.types.Field('Project', graphql_name='project')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class ProjectRelationConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectRelationEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectRelation'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class ProjectRelationEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('ProjectRelation'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class ProjectRelationPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'project_relation', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    project_relation = sgqlc.types.Field(sgqlc.types.non_null('ProjectRelation'), graphql_name='projectRelation')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class ProjectSearchPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'archive_payload', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectSearchResultEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectSearchResult'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    archive_payload = sgqlc.types.Field(sgqlc.types.non_null(ArchiveResponse), graphql_name='archivePayload')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='totalCount')


class ProjectSearchResultEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('ProjectSearchResult'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class ProjectStatusConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectStatusEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectStatus'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class ProjectStatusCountPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('count', 'private_count', 'archived_team_count')
    count = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='count')
    private_count = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='privateCount')
    archived_team_count = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='archivedTeamCount')


class ProjectStatusEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('ProjectStatus'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class ProjectStatusPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'status', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    status = sgqlc.types.Field(sgqlc.types.non_null('ProjectStatus'), graphql_name='status')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class ProjectUpdateConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectUpdateEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectUpdate'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class ProjectUpdateEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('ProjectUpdate'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class ProjectUpdatePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'project_update', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    project_update = sgqlc.types.Field(sgqlc.types.non_null('ProjectUpdate'), graphql_name='projectUpdate')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class ProjectUpdateReminderPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class PushSubscriptionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'entity', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    entity = sgqlc.types.Field(sgqlc.types.non_null('PushSubscription'), graphql_name='entity')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class PushSubscriptionTestPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class Query(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('workflow_states', 'workflow_state', 'webhooks', 'webhook', 'failures_for_oauth_webhooks', 'user_settings', 'users', 'user', 'viewer', 'triage_responsibilities', 'triage_responsibility', 'time_schedules', 'time_schedule', 'templates', 'template', 'templates_for_integration', 'teams', 'administrable_teams', 'team', 'team_memberships', 'team_membership', 'semantic_search', 'search_documents', 'search_projects', 'search_issues', 'roadmap_to_projects', 'roadmap_to_project', 'roadmaps', 'roadmap', 'rate_limit_status', 'push_subscription_test', 'project_updates', 'project_update', 'summarize_project_updates', 'project_statuses', 'project_status_project_count', 'project_status', 'projects', 'project', 'project_filter_suggestion', 'project_relations', 'project_relation', 'project_milestones', 'project_milestone', 'organization', 'organization_exists', 'archived_teams', 'organization_meta', 'organization_invites', 'organization_invite', 'organization_invite_details', 'organization_domain_claim_request', 'notification_subscriptions', 'notification_subscription', 'notifications', 'notifications_unread_count', 'notification', 'issues', 'issue', 'issue_search', 'issue_vcs_branch_search', 'issue_figma_file_key_search', 'issue_priority_values', 'issue_filter_suggestion', 'issue_relations', 'issue_relation', 'issue_labels', 'issue_label', 'issue_import_check_csv', 'issue_import_check_sync', 'issue_import_jql_check', 'integrations_settings', 'integration_templates', 'integration_template', 'integrations', 'integration', 'verify_git_hub_enterprise_server_installation', 'integration_has_scopes', 'initiative_updates', 'initiative_update', 'initiative_to_projects', 'initiative_to_project', 'initiatives', 'initiative', 'initiative_relations', 'initiative_relation', 'favorites', 'favorite', 'external_users', 'external_user', 'entity_external_link', 'emojis', 'emoji', 'documents', 'document', 'document_content_history', 'cycles', 'cycle', 'customer_tiers', 'customer_tier', 'customer_statuses', 'customer_status', 'customers', 'customer', 'customer_needs', 'customer_need', 'issue_title_suggestion_from_customer_request', 'custom_views', 'custom_view', 'custom_view_details_suggestion', 'custom_view_has_subscribers', 'comments', 'comment', 'available_users', 'authentication_sessions', 'sso_url_from_email', 'audit_entry_types', 'audit_entries', 'attachments', 'attachment', 'attachments_for_url', 'attachment_issue', 'attachment_sources', 'application_info', 'application_info_by_ids', 'application_info_with_memberships_by_ids', 'application_with_authorization', 'authorized_applications', 'workspace_authorized_applications', 'workspace_authorized_application', 'api_keys')
    workflow_states = sgqlc.types.Field(sgqlc.types.non_null('WorkflowStateConnection'), graphql_name='workflowStates', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(WorkflowStateFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    workflow_state = sgqlc.types.Field(sgqlc.types.non_null('WorkflowState'), graphql_name='workflowState', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    webhooks = sgqlc.types.Field(sgqlc.types.non_null('WebhookConnection'), graphql_name='webhooks', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    webhook = sgqlc.types.Field(sgqlc.types.non_null('Webhook'), graphql_name='webhook', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    failures_for_oauth_webhooks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WebhookFailureEvent'))), graphql_name='failuresForOauthWebhooks', args=sgqlc.types.ArgDict((
        ('oauth_client_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='oauthClientId', default=None)),
))
    )
    user_settings = sgqlc.types.Field(sgqlc.types.non_null('UserSettings'), graphql_name='userSettings')
    users = sgqlc.types.Field(sgqlc.types.non_null('UserConnection'), graphql_name='users', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(UserFilter, graphql_name='filter', default=None)),
        ('include_disabled', sgqlc.types.Arg(Boolean, graphql_name='includeDisabled', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    viewer = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='viewer')
    triage_responsibilities = sgqlc.types.Field(sgqlc.types.non_null('TriageResponsibilityConnection'), graphql_name='triageResponsibilities', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    triage_responsibility = sgqlc.types.Field(sgqlc.types.non_null('TriageResponsibility'), graphql_name='triageResponsibility', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    time_schedules = sgqlc.types.Field(sgqlc.types.non_null('TimeScheduleConnection'), graphql_name='timeSchedules', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    time_schedule = sgqlc.types.Field(sgqlc.types.non_null('TimeSchedule'), graphql_name='timeSchedule', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    templates = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Template'))), graphql_name='templates')
    template = sgqlc.types.Field(sgqlc.types.non_null('Template'), graphql_name='template', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    templates_for_integration = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Template'))), graphql_name='templatesForIntegration', args=sgqlc.types.ArgDict((
        ('integration_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='integrationType', default=None)),
))
    )
    teams = sgqlc.types.Field(sgqlc.types.non_null('TeamConnection'), graphql_name='teams', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(TeamFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    administrable_teams = sgqlc.types.Field(sgqlc.types.non_null('TeamConnection'), graphql_name='administrableTeams', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(TeamFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    team = sgqlc.types.Field(sgqlc.types.non_null('Team'), graphql_name='team', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    team_memberships = sgqlc.types.Field(sgqlc.types.non_null('TeamMembershipConnection'), graphql_name='teamMemberships', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    team_membership = sgqlc.types.Field(sgqlc.types.non_null('TeamMembership'), graphql_name='teamMembership', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    semantic_search = sgqlc.types.Field(sgqlc.types.non_null('SemanticSearchPayload'), graphql_name='semanticSearch', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='query', default=None)),
        ('types', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SemanticSearchResultType)), graphql_name='types', default=None)),
        ('max_results', sgqlc.types.Arg(Int, graphql_name='maxResults', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
))
    )
    search_documents = sgqlc.types.Field(sgqlc.types.non_null(DocumentSearchPayload), graphql_name='searchDocuments', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
        ('term', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='term', default=None)),
        ('include_comments', sgqlc.types.Arg(Boolean, graphql_name='includeComments', default=None)),
        ('team_id', sgqlc.types.Arg(String, graphql_name='teamId', default=None)),
))
    )
    search_projects = sgqlc.types.Field(sgqlc.types.non_null(ProjectSearchPayload), graphql_name='searchProjects', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
        ('term', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='term', default=None)),
        ('include_comments', sgqlc.types.Arg(Boolean, graphql_name='includeComments', default=None)),
        ('team_id', sgqlc.types.Arg(String, graphql_name='teamId', default=None)),
))
    )
    search_issues = sgqlc.types.Field(sgqlc.types.non_null(IssueSearchPayload), graphql_name='searchIssues', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(IssueFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
        ('term', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='term', default=None)),
        ('include_comments', sgqlc.types.Arg(Boolean, graphql_name='includeComments', default=None)),
        ('team_id', sgqlc.types.Arg(String, graphql_name='teamId', default=None)),
))
    )
    roadmap_to_projects = sgqlc.types.Field(sgqlc.types.non_null('RoadmapToProjectConnection'), graphql_name='roadmapToProjects', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    roadmap_to_project = sgqlc.types.Field(sgqlc.types.non_null('RoadmapToProject'), graphql_name='roadmapToProject', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    roadmaps = sgqlc.types.Field(sgqlc.types.non_null('RoadmapConnection'), graphql_name='roadmaps', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    roadmap = sgqlc.types.Field(sgqlc.types.non_null('Roadmap'), graphql_name='roadmap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    rate_limit_status = sgqlc.types.Field(sgqlc.types.non_null('RateLimitPayload'), graphql_name='rateLimitStatus')
    push_subscription_test = sgqlc.types.Field(sgqlc.types.non_null(PushSubscriptionTestPayload), graphql_name='pushSubscriptionTest', args=sgqlc.types.ArgDict((
        ('target_mobile', sgqlc.types.Arg(Boolean, graphql_name='targetMobile', default=False)),
        ('send_strategy', sgqlc.types.Arg(SendStrategy, graphql_name='sendStrategy', default='push')),
))
    )
    project_updates = sgqlc.types.Field(sgqlc.types.non_null(ProjectUpdateConnection), graphql_name='projectUpdates', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ProjectUpdateFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    project_update = sgqlc.types.Field(sgqlc.types.non_null('ProjectUpdate'), graphql_name='projectUpdate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    summarize_project_updates = sgqlc.types.Field(sgqlc.types.non_null('SummaryPayload'), graphql_name='summarizeProjectUpdates', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
))
    )
    project_statuses = sgqlc.types.Field(sgqlc.types.non_null(ProjectStatusConnection), graphql_name='projectStatuses', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    project_status_project_count = sgqlc.types.Field(sgqlc.types.non_null(ProjectStatusCountPayload), graphql_name='projectStatusProjectCount', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    project_status = sgqlc.types.Field(sgqlc.types.non_null('ProjectStatus'), graphql_name='projectStatus', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    projects = sgqlc.types.Field(sgqlc.types.non_null(ProjectConnection), graphql_name='projects', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ProjectFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    project = sgqlc.types.Field(sgqlc.types.non_null('Project'), graphql_name='project', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    project_filter_suggestion = sgqlc.types.Field(sgqlc.types.non_null(ProjectFilterSuggestionPayload), graphql_name='projectFilterSuggestion', args=sgqlc.types.ArgDict((
        ('prompt', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='prompt', default=None)),
))
    )
    project_relations = sgqlc.types.Field(sgqlc.types.non_null(ProjectRelationConnection), graphql_name='projectRelations', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    project_relation = sgqlc.types.Field(sgqlc.types.non_null('ProjectRelation'), graphql_name='projectRelation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    project_milestones = sgqlc.types.Field(sgqlc.types.non_null(ProjectMilestoneConnection), graphql_name='projectMilestones', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ProjectMilestoneFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    project_milestone = sgqlc.types.Field(sgqlc.types.non_null('ProjectMilestone'), graphql_name='projectMilestone', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    organization = sgqlc.types.Field(sgqlc.types.non_null('Organization'), graphql_name='organization')
    organization_exists = sgqlc.types.Field(sgqlc.types.non_null(OrganizationExistsPayload), graphql_name='organizationExists', args=sgqlc.types.ArgDict((
        ('url_key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='urlKey', default=None)),
))
    )
    archived_teams = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Team'))), graphql_name='archivedTeams')
    organization_meta = sgqlc.types.Field(OrganizationMeta, graphql_name='organizationMeta', args=sgqlc.types.ArgDict((
        ('url_key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='urlKey', default=None)),
))
    )
    organization_invites = sgqlc.types.Field(sgqlc.types.non_null(OrganizationInviteConnection), graphql_name='organizationInvites', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    organization_invite = sgqlc.types.Field(sgqlc.types.non_null('OrganizationInvite'), graphql_name='organizationInvite', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    organization_invite_details = sgqlc.types.Field(sgqlc.types.non_null('OrganizationInviteDetailsPayload'), graphql_name='organizationInviteDetails', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    organization_domain_claim_request = sgqlc.types.Field(sgqlc.types.non_null(OrganizationDomainClaimPayload), graphql_name='organizationDomainClaimRequest', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    notification_subscriptions = sgqlc.types.Field(sgqlc.types.non_null(NotificationSubscriptionConnection), graphql_name='notificationSubscriptions', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    notification_subscription = sgqlc.types.Field(sgqlc.types.non_null(NotificationSubscription), graphql_name='notificationSubscription', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    notifications = sgqlc.types.Field(sgqlc.types.non_null(NotificationConnection), graphql_name='notifications', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(NotificationFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    notifications_unread_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='notificationsUnreadCount')
    notification = sgqlc.types.Field(sgqlc.types.non_null(Notification), graphql_name='notification', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(IssueFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
        ('sort', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(IssueSortInput)), graphql_name='sort', default=None)),
))
    )
    issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='issue', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    issue_search = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issueSearch', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(IssueFilter, graphql_name='filter', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    issue_vcs_branch_search = sgqlc.types.Field('Issue', graphql_name='issueVcsBranchSearch', args=sgqlc.types.ArgDict((
        ('branch_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='branchName', default=None)),
))
    )
    issue_figma_file_key_search = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issueFigmaFileKeySearch', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
        ('file_key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='fileKey', default=None)),
))
    )
    issue_priority_values = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IssuePriorityValue))), graphql_name='issuePriorityValues')
    issue_filter_suggestion = sgqlc.types.Field(sgqlc.types.non_null(IssueFilterSuggestionPayload), graphql_name='issueFilterSuggestion', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(String, graphql_name='projectId', default=None)),
        ('prompt', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='prompt', default=None)),
))
    )
    issue_relations = sgqlc.types.Field(sgqlc.types.non_null(IssueRelationConnection), graphql_name='issueRelations', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    issue_relation = sgqlc.types.Field(sgqlc.types.non_null('IssueRelation'), graphql_name='issueRelation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    issue_labels = sgqlc.types.Field(sgqlc.types.non_null(IssueLabelConnection), graphql_name='issueLabels', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(IssueLabelFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    issue_label = sgqlc.types.Field(sgqlc.types.non_null('IssueLabel'), graphql_name='issueLabel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    issue_import_check_csv = sgqlc.types.Field(sgqlc.types.non_null(IssueImportCheckPayload), graphql_name='issueImportCheckCSV', args=sgqlc.types.ArgDict((
        ('csv_url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='csvUrl', default=None)),
        ('service', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='service', default=None)),
))
    )
    issue_import_check_sync = sgqlc.types.Field(sgqlc.types.non_null(IssueImportSyncCheckPayload), graphql_name='issueImportCheckSync', args=sgqlc.types.ArgDict((
        ('issue_import_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='issueImportId', default=None)),
))
    )
    issue_import_jql_check = sgqlc.types.Field(sgqlc.types.non_null(IssueImportJqlCheckPayload), graphql_name='issueImportJqlCheck', args=sgqlc.types.ArgDict((
        ('jira_hostname', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='jiraHostname', default=None)),
        ('jira_token', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='jiraToken', default=None)),
        ('jira_email', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='jiraEmail', default=None)),
        ('jira_project', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='jiraProject', default=None)),
        ('jql', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='jql', default=None)),
))
    )
    integrations_settings = sgqlc.types.Field(sgqlc.types.non_null('IntegrationsSettings'), graphql_name='integrationsSettings', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    integration_templates = sgqlc.types.Field(sgqlc.types.non_null(IntegrationTemplateConnection), graphql_name='integrationTemplates', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    integration_template = sgqlc.types.Field(sgqlc.types.non_null('IntegrationTemplate'), graphql_name='integrationTemplate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    integrations = sgqlc.types.Field(sgqlc.types.non_null(IntegrationConnection), graphql_name='integrations', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    integration = sgqlc.types.Field(sgqlc.types.non_null('Integration'), graphql_name='integration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    verify_git_hub_enterprise_server_installation = sgqlc.types.Field(sgqlc.types.non_null(GitHubEnterpriseServerInstallVerificationPayload), graphql_name='verifyGitHubEnterpriseServerInstallation')
    integration_has_scopes = sgqlc.types.Field(sgqlc.types.non_null(IntegrationHasScopesPayload), graphql_name='integrationHasScopes', args=sgqlc.types.ArgDict((
        ('scopes', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='scopes', default=None)),
        ('integration_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='integrationId', default=None)),
))
    )
    initiative_updates = sgqlc.types.Field(sgqlc.types.non_null(InitiativeUpdateConnection), graphql_name='initiativeUpdates', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(InitiativeUpdateFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    initiative_update = sgqlc.types.Field(sgqlc.types.non_null('InitiativeUpdate'), graphql_name='initiativeUpdate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    initiative_to_projects = sgqlc.types.Field(sgqlc.types.non_null(InitiativeToProjectConnection), graphql_name='initiativeToProjects', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    initiative_to_project = sgqlc.types.Field(sgqlc.types.non_null('InitiativeToProject'), graphql_name='initiativeToProject', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    initiatives = sgqlc.types.Field(sgqlc.types.non_null(InitiativeConnection), graphql_name='initiatives', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(InitiativeFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    initiative = sgqlc.types.Field(sgqlc.types.non_null('Initiative'), graphql_name='initiative', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    initiative_relations = sgqlc.types.Field(sgqlc.types.non_null(InitiativeRelationConnection), graphql_name='initiativeRelations', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    initiative_relation = sgqlc.types.Field(sgqlc.types.non_null('ProjectRelation'), graphql_name='initiativeRelation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    favorites = sgqlc.types.Field(sgqlc.types.non_null(FavoriteConnection), graphql_name='favorites', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    favorite = sgqlc.types.Field(sgqlc.types.non_null('Favorite'), graphql_name='favorite', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    external_users = sgqlc.types.Field(sgqlc.types.non_null(ExternalUserConnection), graphql_name='externalUsers', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    external_user = sgqlc.types.Field(sgqlc.types.non_null('ExternalUser'), graphql_name='externalUser', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    entity_external_link = sgqlc.types.Field(sgqlc.types.non_null('EntityExternalLink'), graphql_name='entityExternalLink', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    emojis = sgqlc.types.Field(sgqlc.types.non_null(EmojiConnection), graphql_name='emojis', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    emoji = sgqlc.types.Field(sgqlc.types.non_null('Emoji'), graphql_name='emoji', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    documents = sgqlc.types.Field(sgqlc.types.non_null(DocumentConnection), graphql_name='documents', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(DocumentFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    document = sgqlc.types.Field(sgqlc.types.non_null('Document'), graphql_name='document', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    document_content_history = sgqlc.types.Field(sgqlc.types.non_null(DocumentContentHistoryPayload), graphql_name='documentContentHistory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    cycles = sgqlc.types.Field(sgqlc.types.non_null(CycleConnection), graphql_name='cycles', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CycleFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    cycle = sgqlc.types.Field(sgqlc.types.non_null('Cycle'), graphql_name='cycle', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    customer_tiers = sgqlc.types.Field(sgqlc.types.non_null(CustomerTierConnection), graphql_name='customerTiers', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    customer_tier = sgqlc.types.Field(sgqlc.types.non_null('CustomerTier'), graphql_name='customerTier', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    customer_statuses = sgqlc.types.Field(sgqlc.types.non_null(CustomerStatusConnection), graphql_name='customerStatuses', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    customer_status = sgqlc.types.Field(sgqlc.types.non_null('CustomerStatus'), graphql_name='customerStatus', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    customers = sgqlc.types.Field(sgqlc.types.non_null(CustomerConnection), graphql_name='customers', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CustomerFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
        ('sorts', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CustomerSortInput)), graphql_name='sorts', default=None)),
))
    )
    customer = sgqlc.types.Field(sgqlc.types.non_null('Customer'), graphql_name='customer', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    customer_needs = sgqlc.types.Field(sgqlc.types.non_null(CustomerNeedConnection), graphql_name='customerNeeds', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CustomerNeedFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    customer_need = sgqlc.types.Field(sgqlc.types.non_null('CustomerNeed'), graphql_name='customerNeed', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
        ('hash', sgqlc.types.Arg(String, graphql_name='hash', default=None)),
))
    )
    issue_title_suggestion_from_customer_request = sgqlc.types.Field(sgqlc.types.non_null(IssueTitleSuggestionFromCustomerRequestPayload), graphql_name='issueTitleSuggestionFromCustomerRequest', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='request', default=None)),
))
    )
    custom_views = sgqlc.types.Field(sgqlc.types.non_null(CustomViewConnection), graphql_name='customViews', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    custom_view = sgqlc.types.Field(sgqlc.types.non_null('CustomView'), graphql_name='customView', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    custom_view_details_suggestion = sgqlc.types.Field(sgqlc.types.non_null(CustomViewSuggestionPayload), graphql_name='customViewDetailsSuggestion', args=sgqlc.types.ArgDict((
        ('model_name', sgqlc.types.Arg(String, graphql_name='modelName', default=None)),
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(JSONObject), graphql_name='filter', default=None)),
))
    )
    custom_view_has_subscribers = sgqlc.types.Field(sgqlc.types.non_null(CustomViewHasSubscribersPayload), graphql_name='customViewHasSubscribers', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    comments = sgqlc.types.Field(sgqlc.types.non_null(CommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CommentFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    comment = sgqlc.types.Field(sgqlc.types.non_null('Comment'), graphql_name='comment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
        ('hash', sgqlc.types.Arg(String, graphql_name='hash', default=None)),
))
    )
    available_users = sgqlc.types.Field(sgqlc.types.non_null(AuthResolverResponse), graphql_name='availableUsers')
    authentication_sessions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AuthenticationSessionResponse))), graphql_name='authenticationSessions')
    sso_url_from_email = sgqlc.types.Field(sgqlc.types.non_null('SsoUrlFromEmailResponse'), graphql_name='ssoUrlFromEmail', args=sgqlc.types.ArgDict((
        ('is_desktop', sgqlc.types.Arg(Boolean, graphql_name='isDesktop', default=None)),
        ('email', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='email', default=None)),
))
    )
    audit_entry_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AuditEntryType))), graphql_name='auditEntryTypes')
    audit_entries = sgqlc.types.Field(sgqlc.types.non_null(AuditEntryConnection), graphql_name='auditEntries', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(AuditEntryFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    attachments = sgqlc.types.Field(sgqlc.types.non_null(AttachmentConnection), graphql_name='attachments', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(AttachmentFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    attachment = sgqlc.types.Field(sgqlc.types.non_null('Attachment'), graphql_name='attachment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    attachments_for_url = sgqlc.types.Field(sgqlc.types.non_null(AttachmentConnection), graphql_name='attachmentsForURL', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
        ('url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='url', default=None)),
))
    )
    attachment_issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='attachmentIssue', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    attachment_sources = sgqlc.types.Field(sgqlc.types.non_null(AttachmentSourcesPayload), graphql_name='attachmentSources', args=sgqlc.types.ArgDict((
        ('team_id', sgqlc.types.Arg(String, graphql_name='teamId', default=None)),
))
    )
    application_info = sgqlc.types.Field(sgqlc.types.non_null(Application), graphql_name='applicationInfo', args=sgqlc.types.ArgDict((
        ('client_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='clientId', default=None)),
))
    )
    application_info_by_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Application))), graphql_name='applicationInfoByIds', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
))
    )
    application_info_with_memberships_by_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkspaceAuthorizedApplication'))), graphql_name='applicationInfoWithMembershipsByIds', args=sgqlc.types.ArgDict((
        ('client_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='clientIds', default=None)),
))
    )
    application_with_authorization = sgqlc.types.Field(sgqlc.types.non_null('UserAuthorizedApplication'), graphql_name='applicationWithAuthorization', args=sgqlc.types.ArgDict((
        ('redirect_uri', sgqlc.types.Arg(String, graphql_name='redirectUri', default=None)),
        ('actor', sgqlc.types.Arg(String, graphql_name='actor', default='user')),
        ('scope', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='scope', default=None)),
        ('client_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='clientId', default=None)),
))
    )
    authorized_applications = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AuthorizedApplication))), graphql_name='authorizedApplications')
    workspace_authorized_applications = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkspaceAuthorizedApplication'))), graphql_name='workspaceAuthorizedApplications')
    workspace_authorized_application = sgqlc.types.Field(sgqlc.types.non_null('WorkspaceAuthorizedApplicationWithMemberships'), graphql_name='workspaceAuthorizedApplication', args=sgqlc.types.ArgDict((
        ('client_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='clientId', default=None)),
))
    )
    api_keys = sgqlc.types.Field(sgqlc.types.non_null(ApiKeyConnection), graphql_name='apiKeys', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )


class RateLimitPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('identifier', 'kind', 'limits')
    identifier = sgqlc.types.Field(String, graphql_name='identifier')
    kind = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='kind')
    limits = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RateLimitResultPayload'))), graphql_name='limits')


class RateLimitResultPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('type', 'requested_amount', 'allowed_amount', 'period', 'remaining_amount', 'reset')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    requested_amount = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='requestedAmount')
    allowed_amount = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='allowedAmount')
    period = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='period')
    remaining_amount = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='remainingAmount')
    reset = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='reset')


class ReactionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'reaction', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    reaction = sgqlc.types.Field(sgqlc.types.non_null('Reaction'), graphql_name='reaction')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class RoadmapConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RoadmapEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Roadmap'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class RoadmapEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Roadmap'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class RoadmapPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'roadmap', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    roadmap = sgqlc.types.Field(sgqlc.types.non_null('Roadmap'), graphql_name='roadmap')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class RoadmapToProjectConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RoadmapToProjectEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RoadmapToProject'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class RoadmapToProjectEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('RoadmapToProject'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class RoadmapToProjectPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'roadmap_to_project', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    roadmap_to_project = sgqlc.types.Field(sgqlc.types.non_null('RoadmapToProject'), graphql_name='roadmapToProject')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class SemanticSearchPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('enabled', 'results')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    results = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SemanticSearchResult'))), graphql_name='results')


class SlackAsksTeamSettings(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'has_default_ask')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    has_default_ask = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasDefaultAsk')


class SlackChannelConnectPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'integration', 'success', 'add_bot', 'nudge_to_connect_main_slack_integration', 'nudge_to_update_main_slack_integration')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    integration = sgqlc.types.Field('Integration', graphql_name='integration')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')
    add_bot = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='addBot')
    nudge_to_connect_main_slack_integration = sgqlc.types.Field(Boolean, graphql_name='nudgeToConnectMainSlackIntegration')
    nudge_to_update_main_slack_integration = sgqlc.types.Field(Boolean, graphql_name='nudgeToUpdateMainSlackIntegration')


class SlackChannelNameMapping(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'is_private', 'is_shared', 'bot_added', 'teams', 'auto_create_on_message', 'auto_create_on_emoji', 'auto_create_on_bot_mention', 'auto_create_template_id', 'post_cancellation_updates', 'post_completion_updates', 'post_accepted_from_triage_updates', 'ai_titles')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    is_private = sgqlc.types.Field(Boolean, graphql_name='isPrivate')
    is_shared = sgqlc.types.Field(Boolean, graphql_name='isShared')
    bot_added = sgqlc.types.Field(Boolean, graphql_name='botAdded')
    teams = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SlackAsksTeamSettings))), graphql_name='teams')
    auto_create_on_message = sgqlc.types.Field(Boolean, graphql_name='autoCreateOnMessage')
    auto_create_on_emoji = sgqlc.types.Field(Boolean, graphql_name='autoCreateOnEmoji')
    auto_create_on_bot_mention = sgqlc.types.Field(Boolean, graphql_name='autoCreateOnBotMention')
    auto_create_template_id = sgqlc.types.Field(String, graphql_name='autoCreateTemplateId')
    post_cancellation_updates = sgqlc.types.Field(Boolean, graphql_name='postCancellationUpdates')
    post_completion_updates = sgqlc.types.Field(Boolean, graphql_name='postCompletionUpdates')
    post_accepted_from_triage_updates = sgqlc.types.Field(Boolean, graphql_name='postAcceptedFromTriageUpdates')
    ai_titles = sgqlc.types.Field(Boolean, graphql_name='aiTitles')


class SsoUrlFromEmailResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success', 'saml_sso_url')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')
    saml_sso_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='samlSsoUrl')


class SuccessPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class SummaryPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('summary',)
    summary = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='summary')


class SyncedExternalThread(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'type', 'sub_type', 'name', 'display_name', 'url', 'is_connected', 'is_personal_integration_connected', 'is_personal_integration_required')
    id = sgqlc.types.Field(ID, graphql_name='id')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    sub_type = sgqlc.types.Field(String, graphql_name='subType')
    name = sgqlc.types.Field(String, graphql_name='name')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    url = sgqlc.types.Field(String, graphql_name='url')
    is_connected = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isConnected')
    is_personal_integration_connected = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPersonalIntegrationConnected')
    is_personal_integration_required = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPersonalIntegrationRequired')


class TeamConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TeamEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Team'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class TeamEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Team'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class TeamMembershipConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TeamMembershipEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TeamMembership'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class TeamMembershipEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('TeamMembership'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class TeamMembershipPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'team_membership', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    team_membership = sgqlc.types.Field('TeamMembership', graphql_name='teamMembership')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class TeamPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'team', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    team = sgqlc.types.Field('Team', graphql_name='team')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class TemplateConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TemplateEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Template'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class TemplateEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Template'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class TemplatePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'template', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    template = sgqlc.types.Field(sgqlc.types.non_null('Template'), graphql_name='template')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class TimeScheduleConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TimeScheduleEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TimeSchedule'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class TimeScheduleEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('TimeSchedule'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class TimeScheduleEntry(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('starts_at', 'ends_at', 'user_id', 'user_email')
    starts_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startsAt')
    ends_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='endsAt')
    user_id = sgqlc.types.Field(String, graphql_name='userId')
    user_email = sgqlc.types.Field(String, graphql_name='userEmail')


class TimeSchedulePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'time_schedule', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    time_schedule = sgqlc.types.Field(sgqlc.types.non_null('TimeSchedule'), graphql_name='timeSchedule')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class TriageResponsibilityConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TriageResponsibilityEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TriageResponsibility'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class TriageResponsibilityEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('TriageResponsibility'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class TriageResponsibilityManualSelection(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('user_ids', 'assignment_index')
    user_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='userIds')
    assignment_index = sgqlc.types.Field(Int, graphql_name='assignmentIndex')


class TriageResponsibilityPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'triage_responsibility', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    triage_responsibility = sgqlc.types.Field(sgqlc.types.non_null('TriageResponsibility'), graphql_name='triageResponsibility')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class UploadFile(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('filename', 'content_type', 'size', 'upload_url', 'asset_url', 'meta_data', 'headers')
    filename = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='filename')
    content_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='contentType')
    size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='size')
    upload_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uploadUrl')
    asset_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='assetUrl')
    meta_data = sgqlc.types.Field(JSONObject, graphql_name='metaData')
    headers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UploadFileHeader'))), graphql_name='headers')


class UploadFileHeader(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('key', 'value')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class UploadPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'upload_file', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    upload_file = sgqlc.types.Field(UploadFile, graphql_name='uploadFile')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class UserAdminPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class UserAuthorizedApplication(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'client_id', 'name', 'description', 'developer', 'developer_url', 'image_url', 'is_authorized', 'created_by_linear', 'webhooks_enabled', 'app_user_authentication', 'approval_error_code')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    client_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    developer = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='developer')
    developer_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='developerUrl')
    image_url = sgqlc.types.Field(String, graphql_name='imageUrl')
    is_authorized = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAuthorized')
    created_by_linear = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createdByLinear')
    webhooks_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='webhooksEnabled')
    app_user_authentication = sgqlc.types.Field(AppUserAuthentication, graphql_name='appUserAuthentication')
    approval_error_code = sgqlc.types.Field(String, graphql_name='approvalErrorCode')


class UserConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class UserEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class UserPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'user', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    user = sgqlc.types.Field('User', graphql_name='user')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class UserSettingsFlagPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'flag', 'value', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    flag = sgqlc.types.Field(String, graphql_name='flag')
    value = sgqlc.types.Field(Int, graphql_name='value')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class UserSettingsFlagsResetPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class UserSettingsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'user_settings', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    user_settings = sgqlc.types.Field(sgqlc.types.non_null('UserSettings'), graphql_name='userSettings')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class ViewPreferencesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'view_preferences', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    view_preferences = sgqlc.types.Field(sgqlc.types.non_null('ViewPreferences'), graphql_name='viewPreferences')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class ViewPreferencesValues(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('view_ordering', 'issue_grouping', 'show_completed_issues')
    view_ordering = sgqlc.types.Field(String, graphql_name='viewOrdering')
    issue_grouping = sgqlc.types.Field(String, graphql_name='issueGrouping')
    show_completed_issues = sgqlc.types.Field(String, graphql_name='showCompletedIssues')


class WebhookConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WebhookEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Webhook'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class WebhookEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Webhook'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class WebhookFailureEvent(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'created_at', 'webhook', 'url', 'http_status', 'response_or_error', 'execution_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    webhook = sgqlc.types.Field(sgqlc.types.non_null('Webhook'), graphql_name='webhook')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    http_status = sgqlc.types.Field(Float, graphql_name='httpStatus')
    response_or_error = sgqlc.types.Field(String, graphql_name='responseOrError')
    execution_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='executionId')


class WebhookPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'webhook', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    webhook = sgqlc.types.Field(sgqlc.types.non_null('Webhook'), graphql_name='webhook')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class WorkflowStateConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkflowStateEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkflowState'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class WorkflowStateEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('WorkflowState'), graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class WorkflowStatePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('last_sync_id', 'workflow_state', 'success')
    last_sync_id = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lastSyncId')
    workflow_state = sgqlc.types.Field(sgqlc.types.non_null('WorkflowState'), graphql_name='workflowState')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class WorkspaceAuthorizedApplication(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'description', 'developer', 'developer_url', 'image_url', 'scope', 'app_id', 'client_id', 'webhooks_enabled', 'total_members', 'memberships')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    developer = sgqlc.types.Field(String, graphql_name='developer')
    developer_url = sgqlc.types.Field(String, graphql_name='developerUrl')
    image_url = sgqlc.types.Field(String, graphql_name='imageUrl')
    scope = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='scope')
    app_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='appId')
    client_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientId')
    webhooks_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='webhooksEnabled')
    total_members = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='totalMembers')
    memberships = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AuthMembership))), graphql_name='memberships')


class WorkspaceAuthorizedApplicationWithMemberships(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client', 'memberships')
    client = sgqlc.types.Field(sgqlc.types.non_null(AuthorizedApplication), graphql_name='client')
    memberships = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AuthMembership))), graphql_name='memberships')


class ApiKey(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'label', 'scope', 'requested_sync_groups', 'organization')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    scope = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='scope')
    requested_sync_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='requestedSyncGroups')
    organization = sgqlc.types.Field(sgqlc.types.non_null('Organization'), graphql_name='organization')


class Attachment(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'title', 'subtitle', 'url', 'creator', 'external_user_creator', 'metadata', 'source', 'source_type', 'group_by_source', 'original_issue', 'issue', 'body_data')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    subtitle = sgqlc.types.Field(String, graphql_name='subtitle')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    external_user_creator = sgqlc.types.Field('ExternalUser', graphql_name='externalUserCreator')
    metadata = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='metadata')
    source = sgqlc.types.Field(JSONObject, graphql_name='source')
    source_type = sgqlc.types.Field(String, graphql_name='sourceType')
    group_by_source = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='groupBySource')
    original_issue = sgqlc.types.Field('Issue', graphql_name='originalIssue')
    issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='issue')
    body_data = sgqlc.types.Field(String, graphql_name='bodyData')


class AuditEntry(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'type', 'organization', 'actor', 'actor_id', 'ip', 'country_code', 'metadata', 'request_information')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    actor = sgqlc.types.Field('User', graphql_name='actor')
    actor_id = sgqlc.types.Field(String, graphql_name='actorId')
    ip = sgqlc.types.Field(String, graphql_name='ip')
    country_code = sgqlc.types.Field(String, graphql_name='countryCode')
    metadata = sgqlc.types.Field(JSONObject, graphql_name='metadata')
    request_information = sgqlc.types.Field(JSONObject, graphql_name='requestInformation')


class Comment(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'body', 'issue', 'document_content', 'project_update', 'initiative_update', 'post', 'parent', 'resolving_user', 'resolved_at', 'resolving_comment', 'user', 'external_user', 'edited_at', 'body_data', 'quoted_text', 'reaction_data', 'thread_summary', 'url', 'children', 'bot_actor', 'external_thread', 'reactions', 'synced_with')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    issue = sgqlc.types.Field('Issue', graphql_name='issue')
    document_content = sgqlc.types.Field('DocumentContent', graphql_name='documentContent')
    project_update = sgqlc.types.Field('ProjectUpdate', graphql_name='projectUpdate')
    initiative_update = sgqlc.types.Field('InitiativeUpdate', graphql_name='initiativeUpdate')
    post = sgqlc.types.Field('Post', graphql_name='post')
    parent = sgqlc.types.Field('Comment', graphql_name='parent')
    resolving_user = sgqlc.types.Field('User', graphql_name='resolvingUser')
    resolved_at = sgqlc.types.Field(DateTime, graphql_name='resolvedAt')
    resolving_comment = sgqlc.types.Field('Comment', graphql_name='resolvingComment')
    user = sgqlc.types.Field('User', graphql_name='user')
    external_user = sgqlc.types.Field('ExternalUser', graphql_name='externalUser')
    edited_at = sgqlc.types.Field(DateTime, graphql_name='editedAt')
    body_data = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bodyData')
    quoted_text = sgqlc.types.Field(String, graphql_name='quotedText')
    reaction_data = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='reactionData')
    thread_summary = sgqlc.types.Field(JSONObject, graphql_name='threadSummary')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    children = sgqlc.types.Field(sgqlc.types.non_null(CommentConnection), graphql_name='children', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CommentFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    bot_actor = sgqlc.types.Field(ActorBot, graphql_name='botActor')
    external_thread = sgqlc.types.Field(SyncedExternalThread, graphql_name='externalThread')
    reactions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Reaction'))), graphql_name='reactions')
    synced_with = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ExternalEntityInfo)), graphql_name='syncedWith')


class CustomView(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'name', 'description', 'icon', 'color', 'organization', 'creator', 'owner', 'updated_by', 'filters', 'filter_data', 'project_filter_data', 'feed_item_filter_data', 'shared', 'slug_id', 'model_name', 'team', 'projects', 'issues', 'user_view_preferences', 'organization_view_preferences', 'view_preferences_values')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    icon = sgqlc.types.Field(String, graphql_name='icon')
    color = sgqlc.types.Field(String, graphql_name='color')
    organization = sgqlc.types.Field(sgqlc.types.non_null('Organization'), graphql_name='organization')
    creator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='creator')
    owner = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='owner')
    updated_by = sgqlc.types.Field('User', graphql_name='updatedBy')
    filters = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='filters')
    filter_data = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='filterData')
    project_filter_data = sgqlc.types.Field(JSONObject, graphql_name='projectFilterData')
    feed_item_filter_data = sgqlc.types.Field(JSONObject, graphql_name='feedItemFilterData')
    shared = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='shared')
    slug_id = sgqlc.types.Field(String, graphql_name='slugId')
    model_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='modelName')
    team = sgqlc.types.Field('Team', graphql_name='team')
    projects = sgqlc.types.Field(sgqlc.types.non_null(ProjectConnection), graphql_name='projects', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ProjectFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(IssueFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
        ('sort', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(IssueSortInput)), graphql_name='sort', default=None)),
))
    )
    user_view_preferences = sgqlc.types.Field('ViewPreferences', graphql_name='userViewPreferences')
    organization_view_preferences = sgqlc.types.Field('ViewPreferences', graphql_name='organizationViewPreferences')
    view_preferences_values = sgqlc.types.Field(ViewPreferencesValues, graphql_name='viewPreferencesValues')


class CustomViewNotificationSubscription(sgqlc.types.Type, NotificationSubscription, Entity, Node):
    __schema__ = schema
    __field_names__ = ('notification_subscription_types',)
    notification_subscription_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='notificationSubscriptionTypes')


class Customer(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'name', 'logo_url', 'domains', 'external_ids', 'slack_channel_id', 'owner', 'status', 'revenue', 'size', 'tier', 'approximate_need_count', 'slug_id', 'main_source_id', 'integration')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    logo_url = sgqlc.types.Field(String, graphql_name='logoUrl')
    domains = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='domains')
    external_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='externalIds')
    slack_channel_id = sgqlc.types.Field(String, graphql_name='slackChannelId')
    owner = sgqlc.types.Field('User', graphql_name='owner')
    status = sgqlc.types.Field(sgqlc.types.non_null('CustomerStatus'), graphql_name='status')
    revenue = sgqlc.types.Field(Float, graphql_name='revenue')
    size = sgqlc.types.Field(Float, graphql_name='size')
    tier = sgqlc.types.Field('CustomerTier', graphql_name='tier')
    approximate_need_count = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='approximateNeedCount')
    slug_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slugId')
    main_source_id = sgqlc.types.Field(String, graphql_name='mainSourceId')
    integration = sgqlc.types.Field('Integration', graphql_name='integration')


class CustomerNeed(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'customer', 'issue', 'project', 'comment', 'attachment', 'project_attachment', 'priority', 'body', 'body_data', 'creator', 'original_issue', 'url')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    customer = sgqlc.types.Field(Customer, graphql_name='customer')
    issue = sgqlc.types.Field('Issue', graphql_name='issue')
    project = sgqlc.types.Field('Project', graphql_name='project')
    comment = sgqlc.types.Field(Comment, graphql_name='comment')
    attachment = sgqlc.types.Field(Attachment, graphql_name='attachment')
    project_attachment = sgqlc.types.Field('ProjectAttachment', graphql_name='projectAttachment')
    priority = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='priority')
    body = sgqlc.types.Field(String, graphql_name='body')
    body_data = sgqlc.types.Field(String, graphql_name='bodyData')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    original_issue = sgqlc.types.Field('Issue', graphql_name='originalIssue')
    url = sgqlc.types.Field(String, graphql_name='url')


class CustomerNeedArchivePayload(sgqlc.types.Type, ArchivePayload):
    __schema__ = schema
    __field_names__ = ('entity',)
    entity = sgqlc.types.Field(CustomerNeed, graphql_name='entity')


class CustomerNeedNotification(sgqlc.types.Type, Notification, Entity, Node):
    __schema__ = schema
    __field_names__ = ('customer_need_id', 'related_issue', 'related_project')
    customer_need_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='customerNeedId')
    related_issue = sgqlc.types.Field('Issue', graphql_name='relatedIssue')
    related_project = sgqlc.types.Field('Project', graphql_name='relatedProject')


class CustomerNotificationSubscription(sgqlc.types.Type, NotificationSubscription, Entity, Node):
    __schema__ = schema
    __field_names__ = ('notification_subscription_types',)
    notification_subscription_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='notificationSubscriptionTypes')


class CustomerStatus(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'name', 'color', 'description', 'position', 'type')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='color')
    description = sgqlc.types.Field(String, graphql_name='description')
    position = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='position')
    type = sgqlc.types.Field(CustomerStatusType, graphql_name='type')


class CustomerTier(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'name', 'color', 'description', 'position', 'display_name')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='color')
    description = sgqlc.types.Field(String, graphql_name='description')
    position = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='position')
    display_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='displayName')


class Cycle(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'number', 'name', 'description', 'starts_at', 'ends_at', 'completed_at', 'auto_archived_at', 'issue_count_history', 'completed_issue_count_history', 'scope_history', 'completed_scope_history', 'in_progress_scope_history', 'team', 'progress_history', 'current_progress', 'inherited_from', 'issues', 'uncompleted_issues_upon_close', 'progress')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    number = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='number')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    starts_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startsAt')
    ends_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='endsAt')
    completed_at = sgqlc.types.Field(DateTime, graphql_name='completedAt')
    auto_archived_at = sgqlc.types.Field(DateTime, graphql_name='autoArchivedAt')
    issue_count_history = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Float))), graphql_name='issueCountHistory')
    completed_issue_count_history = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Float))), graphql_name='completedIssueCountHistory')
    scope_history = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Float))), graphql_name='scopeHistory')
    completed_scope_history = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Float))), graphql_name='completedScopeHistory')
    in_progress_scope_history = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Float))), graphql_name='inProgressScopeHistory')
    team = sgqlc.types.Field(sgqlc.types.non_null('Team'), graphql_name='team')
    progress_history = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='progressHistory')
    current_progress = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='currentProgress')
    inherited_from = sgqlc.types.Field('Cycle', graphql_name='inheritedFrom')
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(IssueFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    uncompleted_issues_upon_close = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='uncompletedIssuesUponClose', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(IssueFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    progress = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='progress')


class CycleArchivePayload(sgqlc.types.Type, ArchivePayload):
    __schema__ = schema
    __field_names__ = ('entity',)
    entity = sgqlc.types.Field(Cycle, graphql_name='entity')


class CycleNotificationSubscription(sgqlc.types.Type, NotificationSubscription, Entity, Node):
    __schema__ = schema
    __field_names__ = ('notification_subscription_types',)
    notification_subscription_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='notificationSubscriptionTypes')


class Dashboard(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'slug_id', 'name', 'description', 'icon', 'color', 'sort_order', 'shared', 'organization', 'creator', 'updated_by', 'owner', 'issue_filter', 'project_filter', 'widgets')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    slug_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slugId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    icon = sgqlc.types.Field(String, graphql_name='icon')
    color = sgqlc.types.Field(String, graphql_name='color')
    sort_order = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='sortOrder')
    shared = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='shared')
    organization = sgqlc.types.Field(sgqlc.types.non_null('Organization'), graphql_name='organization')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    updated_by = sgqlc.types.Field('User', graphql_name='updatedBy')
    owner = sgqlc.types.Field('User', graphql_name='owner')
    issue_filter = sgqlc.types.Field(JSONObject, graphql_name='issueFilter')
    project_filter = sgqlc.types.Field(JSONObject, graphql_name='projectFilter')
    widgets = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='widgets')


class DeletePayload(sgqlc.types.Type, ArchivePayload):
    __schema__ = schema
    __field_names__ = ('entity_id',)
    entity_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='entityId')


class Document(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'title', 'icon', 'color', 'creator', 'updated_by', 'project', 'initiative', 'team', 'slug_id', 'last_applied_template', 'hidden_at', 'trashed', 'sort_order', 'comments', 'content', 'content_state', 'document_content_id', 'url')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    icon = sgqlc.types.Field(String, graphql_name='icon')
    color = sgqlc.types.Field(String, graphql_name='color')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    updated_by = sgqlc.types.Field('User', graphql_name='updatedBy')
    project = sgqlc.types.Field('Project', graphql_name='project')
    initiative = sgqlc.types.Field('Initiative', graphql_name='initiative')
    team = sgqlc.types.Field('Team', graphql_name='team')
    slug_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slugId')
    last_applied_template = sgqlc.types.Field('Template', graphql_name='lastAppliedTemplate')
    hidden_at = sgqlc.types.Field(DateTime, graphql_name='hiddenAt')
    trashed = sgqlc.types.Field(Boolean, graphql_name='trashed')
    sort_order = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='sortOrder')
    comments = sgqlc.types.Field(sgqlc.types.non_null(CommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CommentFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    content = sgqlc.types.Field(String, graphql_name='content')
    content_state = sgqlc.types.Field(String, graphql_name='contentState')
    document_content_id = sgqlc.types.Field(String, graphql_name='documentContentId')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class DocumentArchivePayload(sgqlc.types.Type, ArchivePayload):
    __schema__ = schema
    __field_names__ = ('entity',)
    entity = sgqlc.types.Field(Document, graphql_name='entity')


class DocumentContent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'content', 'content_state', 'issue', 'project', 'initiative', 'project_milestone', 'document', 'meeting', 'restored_at')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    content = sgqlc.types.Field(String, graphql_name='content')
    content_state = sgqlc.types.Field(String, graphql_name='contentState')
    issue = sgqlc.types.Field('Issue', graphql_name='issue')
    project = sgqlc.types.Field('Project', graphql_name='project')
    initiative = sgqlc.types.Field('Initiative', graphql_name='initiative')
    project_milestone = sgqlc.types.Field('ProjectMilestone', graphql_name='projectMilestone')
    document = sgqlc.types.Field(Document, graphql_name='document')
    meeting = sgqlc.types.Field('Meeting', graphql_name='meeting')
    restored_at = sgqlc.types.Field(DateTime, graphql_name='restoredAt')


class DocumentNotification(sgqlc.types.Type, Notification, Entity, Node):
    __schema__ = schema
    __field_names__ = ('comment_id', 'parent_comment_id', 'reaction_emoji', 'document_id')
    comment_id = sgqlc.types.Field(String, graphql_name='commentId')
    parent_comment_id = sgqlc.types.Field(String, graphql_name='parentCommentId')
    reaction_emoji = sgqlc.types.Field(String, graphql_name='reactionEmoji')
    document_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='documentId')


class DocumentSearchResult(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'title', 'icon', 'color', 'creator', 'updated_by', 'project', 'initiative', 'team', 'slug_id', 'last_applied_template', 'hidden_at', 'trashed', 'sort_order', 'comments', 'content', 'content_state', 'document_content_id', 'url', 'metadata')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    icon = sgqlc.types.Field(String, graphql_name='icon')
    color = sgqlc.types.Field(String, graphql_name='color')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    updated_by = sgqlc.types.Field('User', graphql_name='updatedBy')
    project = sgqlc.types.Field('Project', graphql_name='project')
    initiative = sgqlc.types.Field('Initiative', graphql_name='initiative')
    team = sgqlc.types.Field('Team', graphql_name='team')
    slug_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slugId')
    last_applied_template = sgqlc.types.Field('Template', graphql_name='lastAppliedTemplate')
    hidden_at = sgqlc.types.Field(DateTime, graphql_name='hiddenAt')
    trashed = sgqlc.types.Field(Boolean, graphql_name='trashed')
    sort_order = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='sortOrder')
    comments = sgqlc.types.Field(sgqlc.types.non_null(CommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CommentFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    content = sgqlc.types.Field(String, graphql_name='content')
    content_state = sgqlc.types.Field(String, graphql_name='contentState')
    document_content_id = sgqlc.types.Field(String, graphql_name='documentContentId')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    metadata = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='metadata')


class Draft(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'body_data', 'data', 'is_autogenerated', 'was_local_draft', 'user', 'issue', 'project', 'project_update', 'initiative', 'initiative_update', 'post', 'parent_comment', 'customer_need')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    body_data = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='bodyData')
    data = sgqlc.types.Field(JSONObject, graphql_name='data')
    is_autogenerated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAutogenerated')
    was_local_draft = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='wasLocalDraft')
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')
    issue = sgqlc.types.Field('Issue', graphql_name='issue')
    project = sgqlc.types.Field('Project', graphql_name='project')
    project_update = sgqlc.types.Field('ProjectUpdate', graphql_name='projectUpdate')
    initiative = sgqlc.types.Field('Initiative', graphql_name='initiative')
    initiative_update = sgqlc.types.Field('InitiativeUpdate', graphql_name='initiativeUpdate')
    post = sgqlc.types.Field('Post', graphql_name='post')
    parent_comment = sgqlc.types.Field(Comment, graphql_name='parentComment')
    customer_need = sgqlc.types.Field(CustomerNeed, graphql_name='customerNeed')


class EmailIntakeAddress(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'address', 'enabled', 'replies_enabled', 'template', 'team', 'organization', 'creator', 'customer_requests_enabled')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='address')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    replies_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='repliesEnabled')
    template = sgqlc.types.Field('Template', graphql_name='template')
    team = sgqlc.types.Field('Team', graphql_name='team')
    organization = sgqlc.types.Field(sgqlc.types.non_null('Organization'), graphql_name='organization')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    customer_requests_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='customerRequestsEnabled')


class Emoji(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'name', 'url', 'source', 'creator', 'organization')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    source = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='source')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    organization = sgqlc.types.Field(sgqlc.types.non_null('Organization'), graphql_name='organization')


class EntityExternalLink(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'url', 'label', 'sort_order', 'creator', 'initiative')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    sort_order = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='sortOrder')
    creator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='creator')
    initiative = sgqlc.types.Field('Initiative', graphql_name='initiative')


class ExternalUser(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'name', 'display_name', 'email', 'avatar_url', 'organization', 'last_seen')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    display_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='displayName')
    email = sgqlc.types.Field(String, graphql_name='email')
    avatar_url = sgqlc.types.Field(String, graphql_name='avatarUrl')
    organization = sgqlc.types.Field(sgqlc.types.non_null('Organization'), graphql_name='organization')
    last_seen = sgqlc.types.Field(DateTime, graphql_name='lastSeen')


class Facet(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'sort_order', 'source_organization', 'source_team', 'source_project', 'source_initiative', 'source_feed_user', 'source_page', 'target_custom_view')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    sort_order = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='sortOrder')
    source_organization = sgqlc.types.Field('Organization', graphql_name='sourceOrganization')
    source_team = sgqlc.types.Field('Team', graphql_name='sourceTeam')
    source_project = sgqlc.types.Field('Project', graphql_name='sourceProject')
    source_initiative = sgqlc.types.Field('Initiative', graphql_name='sourceInitiative')
    source_feed_user = sgqlc.types.Field('User', graphql_name='sourceFeedUser')
    source_page = sgqlc.types.Field(FacetPageSource, graphql_name='sourcePage')
    target_custom_view = sgqlc.types.Field(CustomView, graphql_name='targetCustomView')


class Favorite(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'type', 'parent', 'folder_name', 'project_tab', 'predefined_view_type', 'initiative_tab', 'owner', 'sort_order', 'children', 'issue', 'project', 'facet', 'project_team', 'cycle', 'custom_view', 'predefined_view_team', 'document', 'roadmap', 'initiative', 'label', 'project_label', 'user', 'customer', 'dashboard', 'url', 'title', 'detail', 'color', 'icon')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    parent = sgqlc.types.Field('Favorite', graphql_name='parent')
    folder_name = sgqlc.types.Field(String, graphql_name='folderName')
    project_tab = sgqlc.types.Field(ProjectTab, graphql_name='projectTab')
    predefined_view_type = sgqlc.types.Field(String, graphql_name='predefinedViewType')
    initiative_tab = sgqlc.types.Field(InitiativeTab, graphql_name='initiativeTab')
    owner = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='owner')
    sort_order = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='sortOrder')
    children = sgqlc.types.Field(sgqlc.types.non_null(FavoriteConnection), graphql_name='children', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    issue = sgqlc.types.Field('Issue', graphql_name='issue')
    project = sgqlc.types.Field('Project', graphql_name='project')
    facet = sgqlc.types.Field(Facet, graphql_name='facet')
    project_team = sgqlc.types.Field('Team', graphql_name='projectTeam')
    cycle = sgqlc.types.Field(Cycle, graphql_name='cycle')
    custom_view = sgqlc.types.Field(CustomView, graphql_name='customView')
    predefined_view_team = sgqlc.types.Field('Team', graphql_name='predefinedViewTeam')
    document = sgqlc.types.Field(Document, graphql_name='document')
    roadmap = sgqlc.types.Field('Roadmap', graphql_name='roadmap')
    initiative = sgqlc.types.Field('Initiative', graphql_name='initiative')
    label = sgqlc.types.Field('IssueLabel', graphql_name='label')
    project_label = sgqlc.types.Field('ProjectLabel', graphql_name='projectLabel')
    user = sgqlc.types.Field('User', graphql_name='user')
    customer = sgqlc.types.Field(Customer, graphql_name='customer')
    dashboard = sgqlc.types.Field(Dashboard, graphql_name='dashboard')
    url = sgqlc.types.Field(String, graphql_name='url')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    detail = sgqlc.types.Field(String, graphql_name='detail')
    color = sgqlc.types.Field(String, graphql_name='color')
    icon = sgqlc.types.Field(String, graphql_name='icon')


class GitAutomationState(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'state', 'team', 'target_branch', 'event', 'branch_pattern')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    state = sgqlc.types.Field('WorkflowState', graphql_name='state')
    team = sgqlc.types.Field(sgqlc.types.non_null('Team'), graphql_name='team')
    target_branch = sgqlc.types.Field('GitAutomationTargetBranch', graphql_name='targetBranch')
    event = sgqlc.types.Field(sgqlc.types.non_null(GitAutomationStates), graphql_name='event')
    branch_pattern = sgqlc.types.Field(String, graphql_name='branchPattern')


class GitAutomationTargetBranch(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'team', 'branch_pattern', 'is_regex', 'automation_states')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    team = sgqlc.types.Field(sgqlc.types.non_null('Team'), graphql_name='team')
    branch_pattern = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='branchPattern')
    is_regex = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRegex')
    automation_states = sgqlc.types.Field(sgqlc.types.non_null(GitAutomationStateConnection), graphql_name='automationStates', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )


class Initiative(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'update_reminder_frequency_in_weeks', 'update_reminder_frequency', 'frequency_resolution', 'update_reminders_day', 'update_reminders_hour', 'name', 'description', 'organization', 'creator', 'owner', 'slug_id', 'sort_order', 'color', 'icon', 'trashed', 'facets', 'target_date', 'target_date_resolution', 'status', 'last_update', 'health', 'health_updated_at', 'started_at', 'completed_at', 'url', 'projects', 'links', 'integrations_settings', 'history', 'sub_initiatives', 'content')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    update_reminder_frequency_in_weeks = sgqlc.types.Field(Float, graphql_name='updateReminderFrequencyInWeeks')
    update_reminder_frequency = sgqlc.types.Field(Float, graphql_name='updateReminderFrequency')
    frequency_resolution = sgqlc.types.Field(sgqlc.types.non_null(FrequencyResolutionType), graphql_name='frequencyResolution')
    update_reminders_day = sgqlc.types.Field(Day, graphql_name='updateRemindersDay')
    update_reminders_hour = sgqlc.types.Field(Float, graphql_name='updateRemindersHour')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    organization = sgqlc.types.Field(sgqlc.types.non_null('Organization'), graphql_name='organization')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    owner = sgqlc.types.Field('User', graphql_name='owner')
    slug_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slugId')
    sort_order = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='sortOrder')
    color = sgqlc.types.Field(String, graphql_name='color')
    icon = sgqlc.types.Field(String, graphql_name='icon')
    trashed = sgqlc.types.Field(Boolean, graphql_name='trashed')
    facets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Facet))), graphql_name='facets')
    target_date = sgqlc.types.Field(TimelessDate, graphql_name='targetDate')
    target_date_resolution = sgqlc.types.Field(DateResolutionType, graphql_name='targetDateResolution')
    status = sgqlc.types.Field(sgqlc.types.non_null(InitiativeStatus), graphql_name='status')
    last_update = sgqlc.types.Field('InitiativeUpdate', graphql_name='lastUpdate')
    health = sgqlc.types.Field(InitiativeUpdateHealthType, graphql_name='health')
    health_updated_at = sgqlc.types.Field(DateTime, graphql_name='healthUpdatedAt')
    started_at = sgqlc.types.Field(DateTime, graphql_name='startedAt')
    completed_at = sgqlc.types.Field(DateTime, graphql_name='completedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    projects = sgqlc.types.Field(sgqlc.types.non_null(ProjectConnection), graphql_name='projects', args=sgqlc.types.ArgDict((
        ('include_sub_initiatives', sgqlc.types.Arg(Boolean, graphql_name='includeSubInitiatives', default=None)),
        ('filter', sgqlc.types.Arg(ProjectFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    links = sgqlc.types.Field(sgqlc.types.non_null(EntityExternalLinkConnection), graphql_name='links', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    integrations_settings = sgqlc.types.Field('IntegrationsSettings', graphql_name='integrationsSettings')
    history = sgqlc.types.Field(sgqlc.types.non_null(InitiativeHistoryConnection), graphql_name='history', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    sub_initiatives = sgqlc.types.Field(sgqlc.types.non_null(InitiativeConnection), graphql_name='subInitiatives', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(InitiativeFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    content = sgqlc.types.Field(String, graphql_name='content')


class InitiativeArchivePayload(sgqlc.types.Type, ArchivePayload):
    __schema__ = schema
    __field_names__ = ('entity',)
    entity = sgqlc.types.Field(Initiative, graphql_name='entity')


class InitiativeHistory(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'entries', 'initiative')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    entries = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='entries')
    initiative = sgqlc.types.Field(sgqlc.types.non_null(Initiative), graphql_name='initiative')


class InitiativeNotification(sgqlc.types.Type, Notification, Entity, Node):
    __schema__ = schema
    __field_names__ = ('comment_id', 'parent_comment_id', 'reaction_emoji', 'initiative_id', 'initiative_update_id')
    comment_id = sgqlc.types.Field(String, graphql_name='commentId')
    parent_comment_id = sgqlc.types.Field(String, graphql_name='parentCommentId')
    reaction_emoji = sgqlc.types.Field(String, graphql_name='reactionEmoji')
    initiative_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='initiativeId')
    initiative_update_id = sgqlc.types.Field(String, graphql_name='initiativeUpdateId')


class InitiativeNotificationSubscription(sgqlc.types.Type, NotificationSubscription, Entity, Node):
    __schema__ = schema
    __field_names__ = ('notification_subscription_types',)
    notification_subscription_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='notificationSubscriptionTypes')


class InitiativeRelation(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'initiative', 'related_initiative', 'user', 'sort_order')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    initiative = sgqlc.types.Field(sgqlc.types.non_null(Initiative), graphql_name='initiative')
    related_initiative = sgqlc.types.Field(sgqlc.types.non_null(Initiative), graphql_name='relatedInitiative')
    user = sgqlc.types.Field('User', graphql_name='user')
    sort_order = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='sortOrder')


class InitiativeToProject(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'project', 'initiative', 'sort_order')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    project = sgqlc.types.Field(sgqlc.types.non_null('Project'), graphql_name='project')
    initiative = sgqlc.types.Field(sgqlc.types.non_null(Initiative), graphql_name='initiative')
    sort_order = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sortOrder')


class InitiativeUpdate(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'body', 'edited_at', 'reaction_data', 'body_data', 'slug_id', 'initiative', 'user', 'health', 'info_snapshot', 'is_diff_hidden', 'url', 'is_stale', 'diff', 'diff_markdown', 'reactions', 'comments')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    edited_at = sgqlc.types.Field(DateTime, graphql_name='editedAt')
    reaction_data = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='reactionData')
    body_data = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bodyData')
    slug_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slugId')
    initiative = sgqlc.types.Field(sgqlc.types.non_null(Initiative), graphql_name='initiative')
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')
    health = sgqlc.types.Field(sgqlc.types.non_null(InitiativeUpdateHealthType), graphql_name='health')
    info_snapshot = sgqlc.types.Field(JSONObject, graphql_name='infoSnapshot')
    is_diff_hidden = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDiffHidden')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    is_stale = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isStale')
    diff = sgqlc.types.Field(JSONObject, graphql_name='diff')
    diff_markdown = sgqlc.types.Field(String, graphql_name='diffMarkdown')
    reactions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Reaction'))), graphql_name='reactions')
    comments = sgqlc.types.Field(sgqlc.types.non_null(CommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CommentFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )


class InitiativeUpdateArchivePayload(sgqlc.types.Type, ArchivePayload):
    __schema__ = schema
    __field_names__ = ('entity',)
    entity = sgqlc.types.Field(InitiativeUpdate, graphql_name='entity')


class Integration(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'service', 'organization', 'team', 'creator')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    service = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='service')
    organization = sgqlc.types.Field(sgqlc.types.non_null('Organization'), graphql_name='organization')
    team = sgqlc.types.Field('Team', graphql_name='team')
    creator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='creator')


class IntegrationTemplate(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'template', 'integration', 'foreign_entity_id')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    template = sgqlc.types.Field(sgqlc.types.non_null('Template'), graphql_name='template')
    integration = sgqlc.types.Field(sgqlc.types.non_null(Integration), graphql_name='integration')
    foreign_entity_id = sgqlc.types.Field(String, graphql_name='foreignEntityId')


class IntegrationsSettings(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'context_view_type', 'slack_issue_created', 'slack_issue_new_comment', 'slack_issue_status_changed_done', 'slack_issue_added_to_view', 'slack_issue_status_changed_all', 'slack_project_update_created', 'slack_project_update_created_to_team', 'slack_project_update_created_to_workspace', 'slack_initiative_update_created', 'slack_issue_added_to_triage', 'slack_issue_sla_high_risk', 'slack_issue_sla_breached', 'team', 'project', 'initiative')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    context_view_type = sgqlc.types.Field(ContextViewType, graphql_name='contextViewType')
    slack_issue_created = sgqlc.types.Field(Boolean, graphql_name='slackIssueCreated')
    slack_issue_new_comment = sgqlc.types.Field(Boolean, graphql_name='slackIssueNewComment')
    slack_issue_status_changed_done = sgqlc.types.Field(Boolean, graphql_name='slackIssueStatusChangedDone')
    slack_issue_added_to_view = sgqlc.types.Field(Boolean, graphql_name='slackIssueAddedToView')
    slack_issue_status_changed_all = sgqlc.types.Field(Boolean, graphql_name='slackIssueStatusChangedAll')
    slack_project_update_created = sgqlc.types.Field(Boolean, graphql_name='slackProjectUpdateCreated')
    slack_project_update_created_to_team = sgqlc.types.Field(Boolean, graphql_name='slackProjectUpdateCreatedToTeam')
    slack_project_update_created_to_workspace = sgqlc.types.Field(Boolean, graphql_name='slackProjectUpdateCreatedToWorkspace')
    slack_initiative_update_created = sgqlc.types.Field(Boolean, graphql_name='slackInitiativeUpdateCreated')
    slack_issue_added_to_triage = sgqlc.types.Field(Boolean, graphql_name='slackIssueAddedToTriage')
    slack_issue_sla_high_risk = sgqlc.types.Field(Boolean, graphql_name='slackIssueSlaHighRisk')
    slack_issue_sla_breached = sgqlc.types.Field(Boolean, graphql_name='slackIssueSlaBreached')
    team = sgqlc.types.Field('Team', graphql_name='team')
    project = sgqlc.types.Field('Project', graphql_name='project')
    initiative = sgqlc.types.Field(Initiative, graphql_name='initiative')


class Issue(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'number', 'title', 'priority', 'estimate', 'board_order', 'sort_order', 'priority_sort_order', 'started_at', 'completed_at', 'started_triage_at', 'triaged_at', 'canceled_at', 'auto_closed_at', 'auto_archived_at', 'due_date', 'sla_started_at', 'sla_medium_risk_at', 'sla_high_risk_at', 'sla_breaches_at', 'sla_type', 'added_to_project_at', 'added_to_cycle_at', 'added_to_team_at', 'trashed', 'snoozed_until_at', 'suggestions_generated_at', 'activity_summary', 'document_content', 'label_ids', 'team', 'cycle', 'project', 'project_milestone', 'last_applied_template', 'recurring_issue_template', 'previous_identifiers', 'creator', 'external_user_creator', 'assignee', 'snoozed_by', 'state', 'sub_issue_sort_order', 'reaction_data', 'priority_label', 'source_comment', 'integration_source_type', 'bot_actor', 'favorite', 'identifier', 'url', 'branch_name', 'customer_ticket_count', 'subscribers', 'parent', 'children', 'comments', 'history', 'labels', 'relations', 'inverse_relations', 'attachments', 'former_attachments', 'description', 'description_state', 'reactions', 'needs', 'former_needs', 'synced_with', 'suggestions', 'incoming_suggestions')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    number = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='number')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    priority = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='priority')
    estimate = sgqlc.types.Field(Float, graphql_name='estimate')
    board_order = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='boardOrder')
    sort_order = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='sortOrder')
    priority_sort_order = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='prioritySortOrder')
    started_at = sgqlc.types.Field(DateTime, graphql_name='startedAt')
    completed_at = sgqlc.types.Field(DateTime, graphql_name='completedAt')
    started_triage_at = sgqlc.types.Field(DateTime, graphql_name='startedTriageAt')
    triaged_at = sgqlc.types.Field(DateTime, graphql_name='triagedAt')
    canceled_at = sgqlc.types.Field(DateTime, graphql_name='canceledAt')
    auto_closed_at = sgqlc.types.Field(DateTime, graphql_name='autoClosedAt')
    auto_archived_at = sgqlc.types.Field(DateTime, graphql_name='autoArchivedAt')
    due_date = sgqlc.types.Field(TimelessDate, graphql_name='dueDate')
    sla_started_at = sgqlc.types.Field(DateTime, graphql_name='slaStartedAt')
    sla_medium_risk_at = sgqlc.types.Field(DateTime, graphql_name='slaMediumRiskAt')
    sla_high_risk_at = sgqlc.types.Field(DateTime, graphql_name='slaHighRiskAt')
    sla_breaches_at = sgqlc.types.Field(DateTime, graphql_name='slaBreachesAt')
    sla_type = sgqlc.types.Field(String, graphql_name='slaType')
    added_to_project_at = sgqlc.types.Field(DateTime, graphql_name='addedToProjectAt')
    added_to_cycle_at = sgqlc.types.Field(DateTime, graphql_name='addedToCycleAt')
    added_to_team_at = sgqlc.types.Field(DateTime, graphql_name='addedToTeamAt')
    trashed = sgqlc.types.Field(Boolean, graphql_name='trashed')
    snoozed_until_at = sgqlc.types.Field(DateTime, graphql_name='snoozedUntilAt')
    suggestions_generated_at = sgqlc.types.Field(DateTime, graphql_name='suggestionsGeneratedAt')
    activity_summary = sgqlc.types.Field(JSONObject, graphql_name='activitySummary')
    document_content = sgqlc.types.Field(DocumentContent, graphql_name='documentContent')
    label_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='labelIds')
    team = sgqlc.types.Field(sgqlc.types.non_null('Team'), graphql_name='team')
    cycle = sgqlc.types.Field(Cycle, graphql_name='cycle')
    project = sgqlc.types.Field('Project', graphql_name='project')
    project_milestone = sgqlc.types.Field('ProjectMilestone', graphql_name='projectMilestone')
    last_applied_template = sgqlc.types.Field('Template', graphql_name='lastAppliedTemplate')
    recurring_issue_template = sgqlc.types.Field('Template', graphql_name='recurringIssueTemplate')
    previous_identifiers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='previousIdentifiers')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    external_user_creator = sgqlc.types.Field(ExternalUser, graphql_name='externalUserCreator')
    assignee = sgqlc.types.Field('User', graphql_name='assignee')
    snoozed_by = sgqlc.types.Field('User', graphql_name='snoozedBy')
    state = sgqlc.types.Field(sgqlc.types.non_null('WorkflowState'), graphql_name='state')
    sub_issue_sort_order = sgqlc.types.Field(Float, graphql_name='subIssueSortOrder')
    reaction_data = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='reactionData')
    priority_label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='priorityLabel')
    source_comment = sgqlc.types.Field(Comment, graphql_name='sourceComment')
    integration_source_type = sgqlc.types.Field(IntegrationService, graphql_name='integrationSourceType')
    bot_actor = sgqlc.types.Field(ActorBot, graphql_name='botActor')
    favorite = sgqlc.types.Field(Favorite, graphql_name='favorite')
    identifier = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='identifier')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    branch_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='branchName')
    customer_ticket_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='customerTicketCount')
    subscribers = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='subscribers', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(UserFilter, graphql_name='filter', default=None)),
        ('include_disabled', sgqlc.types.Arg(Boolean, graphql_name='includeDisabled', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    parent = sgqlc.types.Field('Issue', graphql_name='parent')
    children = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='children', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(IssueFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    comments = sgqlc.types.Field(sgqlc.types.non_null(CommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CommentFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    history = sgqlc.types.Field(sgqlc.types.non_null(IssueHistoryConnection), graphql_name='history', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    labels = sgqlc.types.Field(sgqlc.types.non_null(IssueLabelConnection), graphql_name='labels', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(IssueLabelFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    relations = sgqlc.types.Field(sgqlc.types.non_null(IssueRelationConnection), graphql_name='relations', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    inverse_relations = sgqlc.types.Field(sgqlc.types.non_null(IssueRelationConnection), graphql_name='inverseRelations', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    attachments = sgqlc.types.Field(sgqlc.types.non_null(AttachmentConnection), graphql_name='attachments', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(AttachmentFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    former_attachments = sgqlc.types.Field(sgqlc.types.non_null(AttachmentConnection), graphql_name='formerAttachments', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(AttachmentFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    description = sgqlc.types.Field(String, graphql_name='description')
    description_state = sgqlc.types.Field(String, graphql_name='descriptionState')
    reactions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Reaction'))), graphql_name='reactions')
    needs = sgqlc.types.Field(sgqlc.types.non_null(CustomerNeedConnection), graphql_name='needs', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CustomerNeedFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    former_needs = sgqlc.types.Field(sgqlc.types.non_null(CustomerNeedConnection), graphql_name='formerNeeds', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CustomerNeedFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    synced_with = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ExternalEntityInfo)), graphql_name='syncedWith')
    suggestions = sgqlc.types.Field(sgqlc.types.non_null(IssueSuggestionConnection), graphql_name='suggestions', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    incoming_suggestions = sgqlc.types.Field(sgqlc.types.non_null(IssueSuggestionConnection), graphql_name='incomingSuggestions', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )


class IssueArchivePayload(sgqlc.types.Type, ArchivePayload):
    __schema__ = schema
    __field_names__ = ('entity',)
    entity = sgqlc.types.Field(Issue, graphql_name='entity')


class IssueDraft(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'title', 'description', 'priority', 'estimate', 'due_date', 'label_ids', 'team_id', 'cycle_id', 'project_id', 'project_milestone_id', 'creator', 'assignee_id', 'state_id', 'parent', 'parent_id', 'source_comment_id', 'parent_issue', 'parent_issue_id', 'sub_issue_sort_order', 'priority_label', 'description_data', 'attachments', 'needs', 'schedule')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')
    priority = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='priority')
    estimate = sgqlc.types.Field(Float, graphql_name='estimate')
    due_date = sgqlc.types.Field(TimelessDate, graphql_name='dueDate')
    label_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='labelIds')
    team_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='teamId')
    cycle_id = sgqlc.types.Field(String, graphql_name='cycleId')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    project_milestone_id = sgqlc.types.Field(String, graphql_name='projectMilestoneId')
    creator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='creator')
    assignee_id = sgqlc.types.Field(String, graphql_name='assigneeId')
    state_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='stateId')
    parent = sgqlc.types.Field('IssueDraft', graphql_name='parent')
    parent_id = sgqlc.types.Field(String, graphql_name='parentId')
    source_comment_id = sgqlc.types.Field(String, graphql_name='sourceCommentId')
    parent_issue = sgqlc.types.Field(Issue, graphql_name='parentIssue')
    parent_issue_id = sgqlc.types.Field(String, graphql_name='parentIssueId')
    sub_issue_sort_order = sgqlc.types.Field(Float, graphql_name='subIssueSortOrder')
    priority_label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='priorityLabel')
    description_data = sgqlc.types.Field(JSON, graphql_name='descriptionData')
    attachments = sgqlc.types.Field(JSONObject, graphql_name='attachments')
    needs = sgqlc.types.Field(JSONObject, graphql_name='needs')
    schedule = sgqlc.types.Field(JSONObject, graphql_name='schedule')


class IssueHistory(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'issue', 'actor_id', 'updated_description', 'from_title', 'to_title', 'from_assignee_id', 'to_assignee_id', 'from_priority', 'to_priority', 'from_team_id', 'to_team_id', 'from_parent_id', 'to_parent_id', 'from_state_id', 'to_state_id', 'from_cycle_id', 'to_cycle_id', 'to_converted_project_id', 'from_project_id', 'to_project_id', 'from_estimate', 'to_estimate', 'archived', 'trashed', 'attachment_id', 'added_label_ids', 'removed_label_ids', 'relation_changes', 'auto_closed', 'auto_archived', 'from_due_date', 'to_due_date', 'customer_need_id', 'changes', 'actor', 'actors', 'description_updated_by', 'from_assignee', 'to_assignee', 'from_cycle', 'to_cycle', 'to_converted_project', 'from_project', 'to_project', 'from_state', 'to_state', 'from_team', 'to_team', 'from_parent', 'to_parent', 'attachment', 'issue_import', 'triage_responsibility_notified_users', 'bot_actor', 'added_labels', 'removed_labels')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='issue')
    actor_id = sgqlc.types.Field(String, graphql_name='actorId')
    updated_description = sgqlc.types.Field(Boolean, graphql_name='updatedDescription')
    from_title = sgqlc.types.Field(String, graphql_name='fromTitle')
    to_title = sgqlc.types.Field(String, graphql_name='toTitle')
    from_assignee_id = sgqlc.types.Field(String, graphql_name='fromAssigneeId')
    to_assignee_id = sgqlc.types.Field(String, graphql_name='toAssigneeId')
    from_priority = sgqlc.types.Field(Float, graphql_name='fromPriority')
    to_priority = sgqlc.types.Field(Float, graphql_name='toPriority')
    from_team_id = sgqlc.types.Field(String, graphql_name='fromTeamId')
    to_team_id = sgqlc.types.Field(String, graphql_name='toTeamId')
    from_parent_id = sgqlc.types.Field(String, graphql_name='fromParentId')
    to_parent_id = sgqlc.types.Field(String, graphql_name='toParentId')
    from_state_id = sgqlc.types.Field(String, graphql_name='fromStateId')
    to_state_id = sgqlc.types.Field(String, graphql_name='toStateId')
    from_cycle_id = sgqlc.types.Field(String, graphql_name='fromCycleId')
    to_cycle_id = sgqlc.types.Field(String, graphql_name='toCycleId')
    to_converted_project_id = sgqlc.types.Field(String, graphql_name='toConvertedProjectId')
    from_project_id = sgqlc.types.Field(String, graphql_name='fromProjectId')
    to_project_id = sgqlc.types.Field(String, graphql_name='toProjectId')
    from_estimate = sgqlc.types.Field(Float, graphql_name='fromEstimate')
    to_estimate = sgqlc.types.Field(Float, graphql_name='toEstimate')
    archived = sgqlc.types.Field(Boolean, graphql_name='archived')
    trashed = sgqlc.types.Field(Boolean, graphql_name='trashed')
    attachment_id = sgqlc.types.Field(String, graphql_name='attachmentId')
    added_label_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='addedLabelIds')
    removed_label_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='removedLabelIds')
    relation_changes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IssueRelationHistoryPayload)), graphql_name='relationChanges')
    auto_closed = sgqlc.types.Field(Boolean, graphql_name='autoClosed')
    auto_archived = sgqlc.types.Field(Boolean, graphql_name='autoArchived')
    from_due_date = sgqlc.types.Field(TimelessDate, graphql_name='fromDueDate')
    to_due_date = sgqlc.types.Field(TimelessDate, graphql_name='toDueDate')
    customer_need_id = sgqlc.types.Field(String, graphql_name='customerNeedId')
    changes = sgqlc.types.Field(JSONObject, graphql_name='changes')
    actor = sgqlc.types.Field('User', graphql_name='actor')
    actors = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='actors')
    description_updated_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='descriptionUpdatedBy')
    from_assignee = sgqlc.types.Field('User', graphql_name='fromAssignee')
    to_assignee = sgqlc.types.Field('User', graphql_name='toAssignee')
    from_cycle = sgqlc.types.Field(Cycle, graphql_name='fromCycle')
    to_cycle = sgqlc.types.Field(Cycle, graphql_name='toCycle')
    to_converted_project = sgqlc.types.Field('Project', graphql_name='toConvertedProject')
    from_project = sgqlc.types.Field('Project', graphql_name='fromProject')
    to_project = sgqlc.types.Field('Project', graphql_name='toProject')
    from_state = sgqlc.types.Field('WorkflowState', graphql_name='fromState')
    to_state = sgqlc.types.Field('WorkflowState', graphql_name='toState')
    from_team = sgqlc.types.Field('Team', graphql_name='fromTeam')
    to_team = sgqlc.types.Field('Team', graphql_name='toTeam')
    from_parent = sgqlc.types.Field(Issue, graphql_name='fromParent')
    to_parent = sgqlc.types.Field(Issue, graphql_name='toParent')
    attachment = sgqlc.types.Field(Attachment, graphql_name='attachment')
    issue_import = sgqlc.types.Field('IssueImport', graphql_name='issueImport')
    triage_responsibility_notified_users = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='triageResponsibilityNotifiedUsers')
    bot_actor = sgqlc.types.Field(ActorBot, graphql_name='botActor')
    added_labels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IssueLabel')), graphql_name='addedLabels')
    removed_labels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IssueLabel')), graphql_name='removedLabels')


class IssueImport(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'team_name', 'creator_id', 'service', 'status', 'mapping', 'error', 'progress', 'csv_file_url', 'error_metadata', 'service_metadata', 'display_name')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    team_name = sgqlc.types.Field(String, graphql_name='teamName')
    creator_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='creatorId')
    service = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='service')
    status = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='status')
    mapping = sgqlc.types.Field(JSONObject, graphql_name='mapping')
    error = sgqlc.types.Field(String, graphql_name='error')
    progress = sgqlc.types.Field(Float, graphql_name='progress')
    csv_file_url = sgqlc.types.Field(String, graphql_name='csvFileUrl')
    error_metadata = sgqlc.types.Field(JSONObject, graphql_name='errorMetadata')
    service_metadata = sgqlc.types.Field(JSONObject, graphql_name='serviceMetadata')
    display_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='displayName')


class IssueLabel(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'name', 'description', 'color', 'is_group', 'organization', 'team', 'creator', 'parent', 'inherited_from', 'issues', 'children')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='color')
    is_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isGroup')
    organization = sgqlc.types.Field(sgqlc.types.non_null('Organization'), graphql_name='organization')
    team = sgqlc.types.Field('Team', graphql_name='team')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    parent = sgqlc.types.Field('IssueLabel', graphql_name='parent')
    inherited_from = sgqlc.types.Field('IssueLabel', graphql_name='inheritedFrom')
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(IssueFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    children = sgqlc.types.Field(sgqlc.types.non_null(IssueLabelConnection), graphql_name='children', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(IssueLabelFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )


class IssueNotification(sgqlc.types.Type, Notification, Entity, Node):
    __schema__ = schema
    __field_names__ = ('comment_id', 'parent_comment_id', 'reaction_emoji', 'issue_id', 'issue', 'comment', 'parent_comment', 'team', 'subscriptions')
    comment_id = sgqlc.types.Field(String, graphql_name='commentId')
    parent_comment_id = sgqlc.types.Field(String, graphql_name='parentCommentId')
    reaction_emoji = sgqlc.types.Field(String, graphql_name='reactionEmoji')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='issueId')
    issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='issue')
    comment = sgqlc.types.Field(Comment, graphql_name='comment')
    parent_comment = sgqlc.types.Field(Comment, graphql_name='parentComment')
    team = sgqlc.types.Field(sgqlc.types.non_null('Team'), graphql_name='team')
    subscriptions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(NotificationSubscription)), graphql_name='subscriptions')


class IssueRelation(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'type', 'issue', 'related_issue')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='issue')
    related_issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='relatedIssue')


class IssueSearchResult(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'number', 'title', 'priority', 'estimate', 'board_order', 'sort_order', 'priority_sort_order', 'started_at', 'completed_at', 'started_triage_at', 'triaged_at', 'canceled_at', 'auto_closed_at', 'auto_archived_at', 'due_date', 'sla_started_at', 'sla_medium_risk_at', 'sla_high_risk_at', 'sla_breaches_at', 'sla_type', 'added_to_project_at', 'added_to_cycle_at', 'added_to_team_at', 'trashed', 'snoozed_until_at', 'suggestions_generated_at', 'activity_summary', 'document_content', 'label_ids', 'team', 'cycle', 'project', 'project_milestone', 'last_applied_template', 'recurring_issue_template', 'previous_identifiers', 'creator', 'external_user_creator', 'assignee', 'snoozed_by', 'state', 'sub_issue_sort_order', 'reaction_data', 'priority_label', 'source_comment', 'integration_source_type', 'bot_actor', 'favorite', 'identifier', 'url', 'branch_name', 'customer_ticket_count', 'subscribers', 'parent', 'children', 'comments', 'history', 'labels', 'relations', 'inverse_relations', 'attachments', 'former_attachments', 'description', 'description_state', 'reactions', 'needs', 'former_needs', 'synced_with', 'suggestions', 'incoming_suggestions', 'metadata')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    number = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='number')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    priority = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='priority')
    estimate = sgqlc.types.Field(Float, graphql_name='estimate')
    board_order = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='boardOrder')
    sort_order = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='sortOrder')
    priority_sort_order = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='prioritySortOrder')
    started_at = sgqlc.types.Field(DateTime, graphql_name='startedAt')
    completed_at = sgqlc.types.Field(DateTime, graphql_name='completedAt')
    started_triage_at = sgqlc.types.Field(DateTime, graphql_name='startedTriageAt')
    triaged_at = sgqlc.types.Field(DateTime, graphql_name='triagedAt')
    canceled_at = sgqlc.types.Field(DateTime, graphql_name='canceledAt')
    auto_closed_at = sgqlc.types.Field(DateTime, graphql_name='autoClosedAt')
    auto_archived_at = sgqlc.types.Field(DateTime, graphql_name='autoArchivedAt')
    due_date = sgqlc.types.Field(TimelessDate, graphql_name='dueDate')
    sla_started_at = sgqlc.types.Field(DateTime, graphql_name='slaStartedAt')
    sla_medium_risk_at = sgqlc.types.Field(DateTime, graphql_name='slaMediumRiskAt')
    sla_high_risk_at = sgqlc.types.Field(DateTime, graphql_name='slaHighRiskAt')
    sla_breaches_at = sgqlc.types.Field(DateTime, graphql_name='slaBreachesAt')
    sla_type = sgqlc.types.Field(String, graphql_name='slaType')
    added_to_project_at = sgqlc.types.Field(DateTime, graphql_name='addedToProjectAt')
    added_to_cycle_at = sgqlc.types.Field(DateTime, graphql_name='addedToCycleAt')
    added_to_team_at = sgqlc.types.Field(DateTime, graphql_name='addedToTeamAt')
    trashed = sgqlc.types.Field(Boolean, graphql_name='trashed')
    snoozed_until_at = sgqlc.types.Field(DateTime, graphql_name='snoozedUntilAt')
    suggestions_generated_at = sgqlc.types.Field(DateTime, graphql_name='suggestionsGeneratedAt')
    activity_summary = sgqlc.types.Field(JSONObject, graphql_name='activitySummary')
    document_content = sgqlc.types.Field(DocumentContent, graphql_name='documentContent')
    label_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='labelIds')
    team = sgqlc.types.Field(sgqlc.types.non_null('Team'), graphql_name='team')
    cycle = sgqlc.types.Field(Cycle, graphql_name='cycle')
    project = sgqlc.types.Field('Project', graphql_name='project')
    project_milestone = sgqlc.types.Field('ProjectMilestone', graphql_name='projectMilestone')
    last_applied_template = sgqlc.types.Field('Template', graphql_name='lastAppliedTemplate')
    recurring_issue_template = sgqlc.types.Field('Template', graphql_name='recurringIssueTemplate')
    previous_identifiers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='previousIdentifiers')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    external_user_creator = sgqlc.types.Field(ExternalUser, graphql_name='externalUserCreator')
    assignee = sgqlc.types.Field('User', graphql_name='assignee')
    snoozed_by = sgqlc.types.Field('User', graphql_name='snoozedBy')
    state = sgqlc.types.Field(sgqlc.types.non_null('WorkflowState'), graphql_name='state')
    sub_issue_sort_order = sgqlc.types.Field(Float, graphql_name='subIssueSortOrder')
    reaction_data = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='reactionData')
    priority_label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='priorityLabel')
    source_comment = sgqlc.types.Field(Comment, graphql_name='sourceComment')
    integration_source_type = sgqlc.types.Field(IntegrationService, graphql_name='integrationSourceType')
    bot_actor = sgqlc.types.Field(ActorBot, graphql_name='botActor')
    favorite = sgqlc.types.Field(Favorite, graphql_name='favorite')
    identifier = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='identifier')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    branch_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='branchName')
    customer_ticket_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='customerTicketCount')
    subscribers = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='subscribers', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(UserFilter, graphql_name='filter', default=None)),
        ('include_disabled', sgqlc.types.Arg(Boolean, graphql_name='includeDisabled', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    parent = sgqlc.types.Field(Issue, graphql_name='parent')
    children = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='children', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(IssueFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    comments = sgqlc.types.Field(sgqlc.types.non_null(CommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CommentFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    history = sgqlc.types.Field(sgqlc.types.non_null(IssueHistoryConnection), graphql_name='history', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    labels = sgqlc.types.Field(sgqlc.types.non_null(IssueLabelConnection), graphql_name='labels', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(IssueLabelFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    relations = sgqlc.types.Field(sgqlc.types.non_null(IssueRelationConnection), graphql_name='relations', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    inverse_relations = sgqlc.types.Field(sgqlc.types.non_null(IssueRelationConnection), graphql_name='inverseRelations', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    attachments = sgqlc.types.Field(sgqlc.types.non_null(AttachmentConnection), graphql_name='attachments', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(AttachmentFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    former_attachments = sgqlc.types.Field(sgqlc.types.non_null(AttachmentConnection), graphql_name='formerAttachments', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(AttachmentFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    description = sgqlc.types.Field(String, graphql_name='description')
    description_state = sgqlc.types.Field(String, graphql_name='descriptionState')
    reactions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Reaction'))), graphql_name='reactions')
    needs = sgqlc.types.Field(sgqlc.types.non_null(CustomerNeedConnection), graphql_name='needs', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CustomerNeedFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    former_needs = sgqlc.types.Field(sgqlc.types.non_null(CustomerNeedConnection), graphql_name='formerNeeds', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CustomerNeedFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    synced_with = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ExternalEntityInfo)), graphql_name='syncedWith')
    suggestions = sgqlc.types.Field(sgqlc.types.non_null(IssueSuggestionConnection), graphql_name='suggestions', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    incoming_suggestions = sgqlc.types.Field(sgqlc.types.non_null(IssueSuggestionConnection), graphql_name='incomingSuggestions', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    metadata = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='metadata')


class IssueSuggestion(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'issue', 'issue_id', 'type', 'state', 'state_changed_at', 'metadata', 'suggested_issue', 'suggested_issue_id', 'suggested_team', 'suggested_project', 'suggested_user', 'suggested_user_id', 'suggested_label', 'suggested_label_id')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='issue')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='issueId')
    type = sgqlc.types.Field(sgqlc.types.non_null(IssueSuggestionType), graphql_name='type')
    state = sgqlc.types.Field(sgqlc.types.non_null(IssueSuggestionState), graphql_name='state')
    state_changed_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='stateChangedAt')
    metadata = sgqlc.types.Field(IssueSuggestionMetadata, graphql_name='metadata')
    suggested_issue = sgqlc.types.Field(Issue, graphql_name='suggestedIssue')
    suggested_issue_id = sgqlc.types.Field(String, graphql_name='suggestedIssueId')
    suggested_team = sgqlc.types.Field('Team', graphql_name='suggestedTeam')
    suggested_project = sgqlc.types.Field('Project', graphql_name='suggestedProject')
    suggested_user = sgqlc.types.Field('User', graphql_name='suggestedUser')
    suggested_user_id = sgqlc.types.Field(String, graphql_name='suggestedUserId')
    suggested_label = sgqlc.types.Field(IssueLabel, graphql_name='suggestedLabel')
    suggested_label_id = sgqlc.types.Field(String, graphql_name='suggestedLabelId')


class LabelNotificationSubscription(sgqlc.types.Type, NotificationSubscription, Entity, Node):
    __schema__ = schema
    __field_names__ = ('notification_subscription_types',)
    notification_subscription_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='notificationSubscriptionTypes')


class Meeting(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'title', 'location', 'meeting_link', 'recording_link', 'icon', 'color', 'creator', 'updated_by', 'project', 'initiative', 'starts_at', 'ends_at', 'hidden_at', 'trashed', 'sort_order')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    location = sgqlc.types.Field(String, graphql_name='location')
    meeting_link = sgqlc.types.Field(String, graphql_name='meetingLink')
    recording_link = sgqlc.types.Field(String, graphql_name='recordingLink')
    icon = sgqlc.types.Field(String, graphql_name='icon')
    color = sgqlc.types.Field(String, graphql_name='color')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    updated_by = sgqlc.types.Field('User', graphql_name='updatedBy')
    project = sgqlc.types.Field('Project', graphql_name='project')
    initiative = sgqlc.types.Field(Initiative, graphql_name='initiative')
    starts_at = sgqlc.types.Field(DateTime, graphql_name='startsAt')
    ends_at = sgqlc.types.Field(DateTime, graphql_name='endsAt')
    hidden_at = sgqlc.types.Field(DateTime, graphql_name='hiddenAt')
    trashed = sgqlc.types.Field(Boolean, graphql_name='trashed')
    sort_order = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='sortOrder')


class NotificationArchivePayload(sgqlc.types.Type, ArchivePayload):
    __schema__ = schema
    __field_names__ = ('entity',)
    entity = sgqlc.types.Field(Notification, graphql_name='entity')


class OauthClientApproval(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'oauth_client_id', 'requester_id', 'responder_id', 'status', 'scopes', 'request_reason', 'deny_reason')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    oauth_client_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='oauthClientId')
    requester_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='requesterId')
    responder_id = sgqlc.types.Field(String, graphql_name='responderId')
    status = sgqlc.types.Field(sgqlc.types.non_null(OAuthClientApprovalStatus), graphql_name='status')
    scopes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='scopes')
    request_reason = sgqlc.types.Field(String, graphql_name='requestReason')
    deny_reason = sgqlc.types.Field(String, graphql_name='denyReason')


class OauthClientApprovalNotification(sgqlc.types.Type, Notification, Entity, Node):
    __schema__ = schema
    __field_names__ = ('oauth_client_approval_id', 'oauth_client_approval')
    oauth_client_approval_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='oauthClientApprovalId')
    oauth_client_approval = sgqlc.types.Field(sgqlc.types.non_null(OauthClientApproval), graphql_name='oauthClientApproval')


class Organization(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'name', 'url_key', 'logo_url', 'period_upload_volume', 'facets', 'git_branch_format', 'git_linkback_messages_enabled', 'git_public_linkback_messages_enabled', 'roadmap_enabled', 'project_update_reminder_frequency_in_weeks', 'project_update_reminders_day', 'project_update_reminders_hour', 'initiative_update_reminder_frequency_in_weeks', 'initiative_update_reminders_day', 'initiative_update_reminders_hour', 'fiscal_year_start_month', 'working_days', 'saml_enabled', 'saml_settings', 'scim_enabled', 'scim_settings', 'allowed_auth_services', 'ip_restrictions', 'deletion_requested_at', 'trial_ends_at', 'previous_url_keys', 'allow_members_to_invite', 'restrict_team_creation_to_admins', 'restrict_label_management_to_admins', 'theme_settings', 'release_channel', 'customers_configuration', 'default_feed_summary_schedule', 'feed_enabled', 'sla_day_count', 'project_updates_reminder_frequency', 'users', 'teams', 'project_statuses', 'integrations', 'subscription', 'user_count', 'created_issue_count', 'templates', 'labels', 'project_labels', 'customer_count', 'customers_enabled')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url_key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='urlKey')
    logo_url = sgqlc.types.Field(String, graphql_name='logoUrl')
    period_upload_volume = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='periodUploadVolume')
    facets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Facet))), graphql_name='facets')
    git_branch_format = sgqlc.types.Field(String, graphql_name='gitBranchFormat')
    git_linkback_messages_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='gitLinkbackMessagesEnabled')
    git_public_linkback_messages_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='gitPublicLinkbackMessagesEnabled')
    roadmap_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='roadmapEnabled')
    project_update_reminder_frequency_in_weeks = sgqlc.types.Field(Float, graphql_name='projectUpdateReminderFrequencyInWeeks')
    project_update_reminders_day = sgqlc.types.Field(sgqlc.types.non_null(Day), graphql_name='projectUpdateRemindersDay')
    project_update_reminders_hour = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='projectUpdateRemindersHour')
    initiative_update_reminder_frequency_in_weeks = sgqlc.types.Field(Float, graphql_name='initiativeUpdateReminderFrequencyInWeeks')
    initiative_update_reminders_day = sgqlc.types.Field(sgqlc.types.non_null(Day), graphql_name='initiativeUpdateRemindersDay')
    initiative_update_reminders_hour = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='initiativeUpdateRemindersHour')
    fiscal_year_start_month = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='fiscalYearStartMonth')
    working_days = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Float))), graphql_name='workingDays')
    saml_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='samlEnabled')
    saml_settings = sgqlc.types.Field(JSONObject, graphql_name='samlSettings')
    scim_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='scimEnabled')
    scim_settings = sgqlc.types.Field(JSONObject, graphql_name='scimSettings')
    allowed_auth_services = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='allowedAuthServices')
    ip_restrictions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(OrganizationIpRestriction)), graphql_name='ipRestrictions')
    deletion_requested_at = sgqlc.types.Field(DateTime, graphql_name='deletionRequestedAt')
    trial_ends_at = sgqlc.types.Field(DateTime, graphql_name='trialEndsAt')
    previous_url_keys = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='previousUrlKeys')
    allow_members_to_invite = sgqlc.types.Field(Boolean, graphql_name='allowMembersToInvite')
    restrict_team_creation_to_admins = sgqlc.types.Field(Boolean, graphql_name='restrictTeamCreationToAdmins')
    restrict_label_management_to_admins = sgqlc.types.Field(Boolean, graphql_name='restrictLabelManagementToAdmins')
    theme_settings = sgqlc.types.Field(JSONObject, graphql_name='themeSettings')
    release_channel = sgqlc.types.Field(sgqlc.types.non_null(ReleaseChannel), graphql_name='releaseChannel')
    customers_configuration = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='customersConfiguration')
    default_feed_summary_schedule = sgqlc.types.Field(FeedSummarySchedule, graphql_name='defaultFeedSummarySchedule')
    feed_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='feedEnabled')
    sla_day_count = sgqlc.types.Field(sgqlc.types.non_null(SLADayCountType), graphql_name='slaDayCount')
    project_updates_reminder_frequency = sgqlc.types.Field(sgqlc.types.non_null(ProjectUpdateReminderFrequency), graphql_name='projectUpdatesReminderFrequency')
    users = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='users', args=sgqlc.types.ArgDict((
        ('include_disabled', sgqlc.types.Arg(Boolean, graphql_name='includeDisabled', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    teams = sgqlc.types.Field(sgqlc.types.non_null(TeamConnection), graphql_name='teams', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(TeamFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    project_statuses = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectStatus'))), graphql_name='projectStatuses')
    integrations = sgqlc.types.Field(sgqlc.types.non_null(IntegrationConnection), graphql_name='integrations', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    subscription = sgqlc.types.Field('PaidSubscription', graphql_name='subscription')
    user_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='userCount')
    created_issue_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createdIssueCount')
    templates = sgqlc.types.Field(sgqlc.types.non_null(TemplateConnection), graphql_name='templates', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(NullableTemplateFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    labels = sgqlc.types.Field(sgqlc.types.non_null(IssueLabelConnection), graphql_name='labels', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(IssueLabelFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    project_labels = sgqlc.types.Field(sgqlc.types.non_null(ProjectLabelConnection), graphql_name='projectLabels', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ProjectLabelFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    customer_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='customerCount')
    customers_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='customersEnabled')


class OrganizationDomain(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'name', 'verified', 'verification_email', 'creator', 'auth_type', 'claimed', 'disable_organization_creation')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    verified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='verified')
    verification_email = sgqlc.types.Field(String, graphql_name='verificationEmail')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    auth_type = sgqlc.types.Field(sgqlc.types.non_null(OrganizationDomainAuthType), graphql_name='authType')
    claimed = sgqlc.types.Field(Boolean, graphql_name='claimed')
    disable_organization_creation = sgqlc.types.Field(Boolean, graphql_name='disableOrganizationCreation')


class OrganizationInvite(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'email', 'role', 'external', 'accepted_at', 'expires_at', 'metadata', 'inviter', 'invitee', 'organization')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    role = sgqlc.types.Field(sgqlc.types.non_null(UserRoleType), graphql_name='role')
    external = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='external')
    accepted_at = sgqlc.types.Field(DateTime, graphql_name='acceptedAt')
    expires_at = sgqlc.types.Field(DateTime, graphql_name='expiresAt')
    metadata = sgqlc.types.Field(JSONObject, graphql_name='metadata')
    inviter = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='inviter')
    invitee = sgqlc.types.Field('User', graphql_name='invitee')
    organization = sgqlc.types.Field(sgqlc.types.non_null(Organization), graphql_name='organization')


class PaidSubscription(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'type', 'seats', 'seats_minimum', 'seats_maximum', 'creator', 'organization', 'collection_method', 'canceled_at', 'cancel_at', 'pending_change_type', 'next_billing_at')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    seats = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='seats')
    seats_minimum = sgqlc.types.Field(Float, graphql_name='seatsMinimum')
    seats_maximum = sgqlc.types.Field(Float, graphql_name='seatsMaximum')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    organization = sgqlc.types.Field(sgqlc.types.non_null(Organization), graphql_name='organization')
    collection_method = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='collectionMethod')
    canceled_at = sgqlc.types.Field(DateTime, graphql_name='canceledAt')
    cancel_at = sgqlc.types.Field(DateTime, graphql_name='cancelAt')
    pending_change_type = sgqlc.types.Field(String, graphql_name='pendingChangeType')
    next_billing_at = sgqlc.types.Field(DateTime, graphql_name='nextBillingAt')


class Post(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'body', 'body_data', 'written_summary_data', 'audio_summary', 'title', 'slug_id', 'creator', 'edited_at', 'reaction_data', 'ttl_url', 'user', 'team', 'type', 'eval_log_id', 'feed_summary_schedule_at_create')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    body_data = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bodyData')
    written_summary_data = sgqlc.types.Field(JSONObject, graphql_name='writtenSummaryData')
    audio_summary = sgqlc.types.Field(String, graphql_name='audioSummary')
    title = sgqlc.types.Field(String, graphql_name='title')
    slug_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slugId')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    edited_at = sgqlc.types.Field(DateTime, graphql_name='editedAt')
    reaction_data = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='reactionData')
    ttl_url = sgqlc.types.Field(String, graphql_name='ttlUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    team = sgqlc.types.Field('Team', graphql_name='team')
    type = sgqlc.types.Field(PostType, graphql_name='type')
    eval_log_id = sgqlc.types.Field(String, graphql_name='evalLogId')
    feed_summary_schedule_at_create = sgqlc.types.Field(FeedSummarySchedule, graphql_name='feedSummaryScheduleAtCreate')


class PostNotification(sgqlc.types.Type, Notification, Entity, Node):
    __schema__ = schema
    __field_names__ = ('comment_id', 'parent_comment_id', 'reaction_emoji', 'post_id')
    comment_id = sgqlc.types.Field(String, graphql_name='commentId')
    parent_comment_id = sgqlc.types.Field(String, graphql_name='parentCommentId')
    reaction_emoji = sgqlc.types.Field(String, graphql_name='reactionEmoji')
    post_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='postId')


class Project(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'update_reminder_frequency_in_weeks', 'update_reminder_frequency', 'frequency_resolution', 'update_reminders_day', 'update_reminders_hour', 'name', 'description', 'document_content', 'slug_id', 'icon', 'color', 'status', 'creator', 'lead', 'facets', 'project_update_reminders_paused_until_at', 'start_date', 'start_date_resolution', 'target_date', 'target_date_resolution', 'started_at', 'completed_at', 'canceled_at', 'auto_archived_at', 'trashed', 'sort_order', 'priority_sort_order', 'converted_from_issue', 'last_applied_template', 'priority', 'last_update', 'health', 'health_updated_at', 'issue_count_history', 'completed_issue_count_history', 'scope_history', 'completed_scope_history', 'in_progress_scope_history', 'progress_history', 'current_progress', 'slack_new_issue', 'slack_issue_comments', 'slack_issue_statuses', 'label_ids', 'favorite', 'url', 'initiatives', 'teams', 'members', 'project_updates', 'documents', 'project_milestones', 'issues', 'external_links', 'history', 'labels', 'progress', 'scope', 'integrations_settings', 'content', 'content_state', 'comments', 'relations', 'inverse_relations', 'needs', 'state', 'priority_label')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    update_reminder_frequency_in_weeks = sgqlc.types.Field(Float, graphql_name='updateReminderFrequencyInWeeks')
    update_reminder_frequency = sgqlc.types.Field(Float, graphql_name='updateReminderFrequency')
    frequency_resolution = sgqlc.types.Field(sgqlc.types.non_null(FrequencyResolutionType), graphql_name='frequencyResolution')
    update_reminders_day = sgqlc.types.Field(Day, graphql_name='updateRemindersDay')
    update_reminders_hour = sgqlc.types.Field(Float, graphql_name='updateRemindersHour')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    document_content = sgqlc.types.Field(DocumentContent, graphql_name='documentContent')
    slug_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slugId')
    icon = sgqlc.types.Field(String, graphql_name='icon')
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='color')
    status = sgqlc.types.Field(sgqlc.types.non_null('ProjectStatus'), graphql_name='status')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    lead = sgqlc.types.Field('User', graphql_name='lead')
    facets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Facet))), graphql_name='facets')
    project_update_reminders_paused_until_at = sgqlc.types.Field(DateTime, graphql_name='projectUpdateRemindersPausedUntilAt')
    start_date = sgqlc.types.Field(TimelessDate, graphql_name='startDate')
    start_date_resolution = sgqlc.types.Field(DateResolutionType, graphql_name='startDateResolution')
    target_date = sgqlc.types.Field(TimelessDate, graphql_name='targetDate')
    target_date_resolution = sgqlc.types.Field(DateResolutionType, graphql_name='targetDateResolution')
    started_at = sgqlc.types.Field(DateTime, graphql_name='startedAt')
    completed_at = sgqlc.types.Field(DateTime, graphql_name='completedAt')
    canceled_at = sgqlc.types.Field(DateTime, graphql_name='canceledAt')
    auto_archived_at = sgqlc.types.Field(DateTime, graphql_name='autoArchivedAt')
    trashed = sgqlc.types.Field(Boolean, graphql_name='trashed')
    sort_order = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='sortOrder')
    priority_sort_order = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='prioritySortOrder')
    converted_from_issue = sgqlc.types.Field(Issue, graphql_name='convertedFromIssue')
    last_applied_template = sgqlc.types.Field('Template', graphql_name='lastAppliedTemplate')
    priority = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='priority')
    last_update = sgqlc.types.Field('ProjectUpdate', graphql_name='lastUpdate')
    health = sgqlc.types.Field(ProjectUpdateHealthType, graphql_name='health')
    health_updated_at = sgqlc.types.Field(DateTime, graphql_name='healthUpdatedAt')
    issue_count_history = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Float))), graphql_name='issueCountHistory')
    completed_issue_count_history = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Float))), graphql_name='completedIssueCountHistory')
    scope_history = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Float))), graphql_name='scopeHistory')
    completed_scope_history = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Float))), graphql_name='completedScopeHistory')
    in_progress_scope_history = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Float))), graphql_name='inProgressScopeHistory')
    progress_history = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='progressHistory')
    current_progress = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='currentProgress')
    slack_new_issue = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='slackNewIssue')
    slack_issue_comments = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='slackIssueComments')
    slack_issue_statuses = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='slackIssueStatuses')
    label_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='labelIds')
    favorite = sgqlc.types.Field(Favorite, graphql_name='favorite')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    initiatives = sgqlc.types.Field(sgqlc.types.non_null(InitiativeConnection), graphql_name='initiatives', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    teams = sgqlc.types.Field(sgqlc.types.non_null(TeamConnection), graphql_name='teams', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(TeamFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    members = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='members', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(UserFilter, graphql_name='filter', default=None)),
        ('include_disabled', sgqlc.types.Arg(Boolean, graphql_name='includeDisabled', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    project_updates = sgqlc.types.Field(sgqlc.types.non_null(ProjectUpdateConnection), graphql_name='projectUpdates', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    documents = sgqlc.types.Field(sgqlc.types.non_null(DocumentConnection), graphql_name='documents', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(DocumentFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    project_milestones = sgqlc.types.Field(sgqlc.types.non_null(ProjectMilestoneConnection), graphql_name='projectMilestones', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ProjectMilestoneFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(IssueFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    external_links = sgqlc.types.Field(sgqlc.types.non_null(EntityExternalLinkConnection), graphql_name='externalLinks', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    history = sgqlc.types.Field(sgqlc.types.non_null(ProjectHistoryConnection), graphql_name='history', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    labels = sgqlc.types.Field(sgqlc.types.non_null(ProjectLabelConnection), graphql_name='labels', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ProjectLabelFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    progress = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='progress')
    scope = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='scope')
    integrations_settings = sgqlc.types.Field(IntegrationsSettings, graphql_name='integrationsSettings')
    content = sgqlc.types.Field(String, graphql_name='content')
    content_state = sgqlc.types.Field(String, graphql_name='contentState')
    comments = sgqlc.types.Field(sgqlc.types.non_null(CommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CommentFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    relations = sgqlc.types.Field(sgqlc.types.non_null(ProjectRelationConnection), graphql_name='relations', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    inverse_relations = sgqlc.types.Field(sgqlc.types.non_null(ProjectRelationConnection), graphql_name='inverseRelations', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    needs = sgqlc.types.Field(sgqlc.types.non_null(CustomerNeedConnection), graphql_name='needs', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CustomerNeedFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    state = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='state')
    priority_label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='priorityLabel')


class ProjectArchivePayload(sgqlc.types.Type, ArchivePayload):
    __schema__ = schema
    __field_names__ = ('entity',)
    entity = sgqlc.types.Field(Project, graphql_name='entity')


class ProjectAttachment(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'title', 'subtitle', 'url', 'creator', 'metadata', 'source', 'source_type')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    subtitle = sgqlc.types.Field(String, graphql_name='subtitle')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    metadata = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='metadata')
    source = sgqlc.types.Field(JSONObject, graphql_name='source')
    source_type = sgqlc.types.Field(String, graphql_name='sourceType')


class ProjectHistory(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'entries', 'project')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    entries = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='entries')
    project = sgqlc.types.Field(sgqlc.types.non_null(Project), graphql_name='project')


class ProjectLabel(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'name', 'description', 'color', 'is_group', 'organization', 'creator', 'parent')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='color')
    is_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isGroup')
    organization = sgqlc.types.Field(sgqlc.types.non_null(Organization), graphql_name='organization')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    parent = sgqlc.types.Field('ProjectLabel', graphql_name='parent')


class ProjectMilestone(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'name', 'document_content', 'target_date', 'project', 'progress_history', 'current_progress', 'sort_order', 'description', 'status', 'progress', 'description_state', 'issues')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    document_content = sgqlc.types.Field(DocumentContent, graphql_name='documentContent')
    target_date = sgqlc.types.Field(TimelessDate, graphql_name='targetDate')
    project = sgqlc.types.Field(sgqlc.types.non_null(Project), graphql_name='project')
    progress_history = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='progressHistory')
    current_progress = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='currentProgress')
    sort_order = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='sortOrder')
    description = sgqlc.types.Field(String, graphql_name='description')
    status = sgqlc.types.Field(sgqlc.types.non_null(ProjectMilestoneStatus), graphql_name='status')
    progress = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='progress')
    description_state = sgqlc.types.Field(String, graphql_name='descriptionState')
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(IssueFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )


class ProjectNotification(sgqlc.types.Type, Notification, Entity, Node):
    __schema__ = schema
    __field_names__ = ('comment_id', 'parent_comment_id', 'reaction_emoji', 'project_id', 'project_milestone_id', 'project_update_id', 'project', 'initiative', 'document', 'project_update', 'initiative_update', 'comment', 'parent_comment')
    comment_id = sgqlc.types.Field(String, graphql_name='commentId')
    parent_comment_id = sgqlc.types.Field(String, graphql_name='parentCommentId')
    reaction_emoji = sgqlc.types.Field(String, graphql_name='reactionEmoji')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')
    project_milestone_id = sgqlc.types.Field(String, graphql_name='projectMilestoneId')
    project_update_id = sgqlc.types.Field(String, graphql_name='projectUpdateId')
    project = sgqlc.types.Field(sgqlc.types.non_null(Project), graphql_name='project')
    initiative = sgqlc.types.Field(Initiative, graphql_name='initiative')
    document = sgqlc.types.Field(Document, graphql_name='document')
    project_update = sgqlc.types.Field('ProjectUpdate', graphql_name='projectUpdate')
    initiative_update = sgqlc.types.Field(InitiativeUpdate, graphql_name='initiativeUpdate')
    comment = sgqlc.types.Field(Comment, graphql_name='comment')
    parent_comment = sgqlc.types.Field(Comment, graphql_name='parentComment')


class ProjectNotificationSubscription(sgqlc.types.Type, NotificationSubscription, Entity, Node):
    __schema__ = schema
    __field_names__ = ('notification_subscription_types',)
    notification_subscription_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='notificationSubscriptionTypes')


class ProjectRelation(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'type', 'project', 'project_milestone', 'anchor_type', 'related_project', 'related_project_milestone', 'related_anchor_type', 'user')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    project = sgqlc.types.Field(sgqlc.types.non_null(Project), graphql_name='project')
    project_milestone = sgqlc.types.Field(ProjectMilestone, graphql_name='projectMilestone')
    anchor_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='anchorType')
    related_project = sgqlc.types.Field(sgqlc.types.non_null(Project), graphql_name='relatedProject')
    related_project_milestone = sgqlc.types.Field(ProjectMilestone, graphql_name='relatedProjectMilestone')
    related_anchor_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='relatedAnchorType')
    user = sgqlc.types.Field('User', graphql_name='user')


class ProjectSearchResult(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'update_reminder_frequency_in_weeks', 'update_reminder_frequency', 'frequency_resolution', 'update_reminders_day', 'update_reminders_hour', 'name', 'description', 'document_content', 'slug_id', 'icon', 'color', 'status', 'creator', 'lead', 'facets', 'project_update_reminders_paused_until_at', 'start_date', 'start_date_resolution', 'target_date', 'target_date_resolution', 'started_at', 'completed_at', 'canceled_at', 'auto_archived_at', 'trashed', 'sort_order', 'priority_sort_order', 'converted_from_issue', 'last_applied_template', 'priority', 'last_update', 'health', 'health_updated_at', 'issue_count_history', 'completed_issue_count_history', 'scope_history', 'completed_scope_history', 'in_progress_scope_history', 'progress_history', 'current_progress', 'slack_new_issue', 'slack_issue_comments', 'slack_issue_statuses', 'label_ids', 'favorite', 'url', 'initiatives', 'teams', 'members', 'project_updates', 'documents', 'project_milestones', 'issues', 'external_links', 'history', 'labels', 'progress', 'scope', 'integrations_settings', 'content', 'content_state', 'comments', 'relations', 'inverse_relations', 'needs', 'state', 'priority_label', 'metadata')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    update_reminder_frequency_in_weeks = sgqlc.types.Field(Float, graphql_name='updateReminderFrequencyInWeeks')
    update_reminder_frequency = sgqlc.types.Field(Float, graphql_name='updateReminderFrequency')
    frequency_resolution = sgqlc.types.Field(sgqlc.types.non_null(FrequencyResolutionType), graphql_name='frequencyResolution')
    update_reminders_day = sgqlc.types.Field(Day, graphql_name='updateRemindersDay')
    update_reminders_hour = sgqlc.types.Field(Float, graphql_name='updateRemindersHour')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    document_content = sgqlc.types.Field(DocumentContent, graphql_name='documentContent')
    slug_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slugId')
    icon = sgqlc.types.Field(String, graphql_name='icon')
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='color')
    status = sgqlc.types.Field(sgqlc.types.non_null('ProjectStatus'), graphql_name='status')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    lead = sgqlc.types.Field('User', graphql_name='lead')
    facets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Facet))), graphql_name='facets')
    project_update_reminders_paused_until_at = sgqlc.types.Field(DateTime, graphql_name='projectUpdateRemindersPausedUntilAt')
    start_date = sgqlc.types.Field(TimelessDate, graphql_name='startDate')
    start_date_resolution = sgqlc.types.Field(DateResolutionType, graphql_name='startDateResolution')
    target_date = sgqlc.types.Field(TimelessDate, graphql_name='targetDate')
    target_date_resolution = sgqlc.types.Field(DateResolutionType, graphql_name='targetDateResolution')
    started_at = sgqlc.types.Field(DateTime, graphql_name='startedAt')
    completed_at = sgqlc.types.Field(DateTime, graphql_name='completedAt')
    canceled_at = sgqlc.types.Field(DateTime, graphql_name='canceledAt')
    auto_archived_at = sgqlc.types.Field(DateTime, graphql_name='autoArchivedAt')
    trashed = sgqlc.types.Field(Boolean, graphql_name='trashed')
    sort_order = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='sortOrder')
    priority_sort_order = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='prioritySortOrder')
    converted_from_issue = sgqlc.types.Field(Issue, graphql_name='convertedFromIssue')
    last_applied_template = sgqlc.types.Field('Template', graphql_name='lastAppliedTemplate')
    priority = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='priority')
    last_update = sgqlc.types.Field('ProjectUpdate', graphql_name='lastUpdate')
    health = sgqlc.types.Field(ProjectUpdateHealthType, graphql_name='health')
    health_updated_at = sgqlc.types.Field(DateTime, graphql_name='healthUpdatedAt')
    issue_count_history = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Float))), graphql_name='issueCountHistory')
    completed_issue_count_history = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Float))), graphql_name='completedIssueCountHistory')
    scope_history = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Float))), graphql_name='scopeHistory')
    completed_scope_history = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Float))), graphql_name='completedScopeHistory')
    in_progress_scope_history = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Float))), graphql_name='inProgressScopeHistory')
    progress_history = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='progressHistory')
    current_progress = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='currentProgress')
    slack_new_issue = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='slackNewIssue')
    slack_issue_comments = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='slackIssueComments')
    slack_issue_statuses = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='slackIssueStatuses')
    label_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='labelIds')
    favorite = sgqlc.types.Field(Favorite, graphql_name='favorite')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    initiatives = sgqlc.types.Field(sgqlc.types.non_null(InitiativeConnection), graphql_name='initiatives', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    teams = sgqlc.types.Field(sgqlc.types.non_null(TeamConnection), graphql_name='teams', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(TeamFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    members = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='members', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(UserFilter, graphql_name='filter', default=None)),
        ('include_disabled', sgqlc.types.Arg(Boolean, graphql_name='includeDisabled', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    project_updates = sgqlc.types.Field(sgqlc.types.non_null(ProjectUpdateConnection), graphql_name='projectUpdates', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    documents = sgqlc.types.Field(sgqlc.types.non_null(DocumentConnection), graphql_name='documents', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(DocumentFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    project_milestones = sgqlc.types.Field(sgqlc.types.non_null(ProjectMilestoneConnection), graphql_name='projectMilestones', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ProjectMilestoneFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(IssueFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    external_links = sgqlc.types.Field(sgqlc.types.non_null(EntityExternalLinkConnection), graphql_name='externalLinks', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    history = sgqlc.types.Field(sgqlc.types.non_null(ProjectHistoryConnection), graphql_name='history', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    labels = sgqlc.types.Field(sgqlc.types.non_null(ProjectLabelConnection), graphql_name='labels', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ProjectLabelFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    progress = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='progress')
    scope = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='scope')
    integrations_settings = sgqlc.types.Field(IntegrationsSettings, graphql_name='integrationsSettings')
    content = sgqlc.types.Field(String, graphql_name='content')
    content_state = sgqlc.types.Field(String, graphql_name='contentState')
    comments = sgqlc.types.Field(sgqlc.types.non_null(CommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CommentFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    relations = sgqlc.types.Field(sgqlc.types.non_null(ProjectRelationConnection), graphql_name='relations', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    inverse_relations = sgqlc.types.Field(sgqlc.types.non_null(ProjectRelationConnection), graphql_name='inverseRelations', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    needs = sgqlc.types.Field(sgqlc.types.non_null(CustomerNeedConnection), graphql_name='needs', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CustomerNeedFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    state = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='state')
    priority_label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='priorityLabel')
    metadata = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='metadata')


class ProjectStatus(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'name', 'color', 'description', 'position', 'type', 'indefinite')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='color')
    description = sgqlc.types.Field(String, graphql_name='description')
    position = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='position')
    type = sgqlc.types.Field(sgqlc.types.non_null(ProjectStatusType), graphql_name='type')
    indefinite = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='indefinite')


class ProjectStatusArchivePayload(sgqlc.types.Type, ArchivePayload):
    __schema__ = schema
    __field_names__ = ('entity',)
    entity = sgqlc.types.Field(ProjectStatus, graphql_name='entity')


class ProjectUpdate(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'body', 'edited_at', 'reaction_data', 'body_data', 'slug_id', 'project', 'health', 'user', 'info_snapshot', 'is_diff_hidden', 'url', 'is_stale', 'diff', 'diff_markdown', 'reactions', 'comments')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    edited_at = sgqlc.types.Field(DateTime, graphql_name='editedAt')
    reaction_data = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='reactionData')
    body_data = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bodyData')
    slug_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slugId')
    project = sgqlc.types.Field(sgqlc.types.non_null(Project), graphql_name='project')
    health = sgqlc.types.Field(sgqlc.types.non_null(ProjectUpdateHealthType), graphql_name='health')
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')
    info_snapshot = sgqlc.types.Field(JSONObject, graphql_name='infoSnapshot')
    is_diff_hidden = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDiffHidden')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    is_stale = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isStale')
    diff = sgqlc.types.Field(JSONObject, graphql_name='diff')
    diff_markdown = sgqlc.types.Field(String, graphql_name='diffMarkdown')
    reactions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Reaction'))), graphql_name='reactions')
    comments = sgqlc.types.Field(sgqlc.types.non_null(CommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CommentFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )


class ProjectUpdateArchivePayload(sgqlc.types.Type, ArchivePayload):
    __schema__ = schema
    __field_names__ = ('entity',)
    entity = sgqlc.types.Field(ProjectUpdate, graphql_name='entity')


class PullRequest(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'title', 'number', 'source_branch', 'target_branch', 'url', 'status')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    number = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='number')
    source_branch = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sourceBranch')
    target_branch = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='targetBranch')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    status = sgqlc.types.Field(sgqlc.types.non_null(PullRequestStatus), graphql_name='status')


class PullRequestNotification(sgqlc.types.Type, Notification, Entity, Node):
    __schema__ = schema
    __field_names__ = ('comment_id', 'parent_comment_id', 'reaction_emoji', 'pull_request_id', 'pull_request')
    comment_id = sgqlc.types.Field(String, graphql_name='commentId')
    parent_comment_id = sgqlc.types.Field(String, graphql_name='parentCommentId')
    reaction_emoji = sgqlc.types.Field(String, graphql_name='reactionEmoji')
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pullRequestId')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')


class PushSubscription(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')


class Reaction(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'emoji', 'issue', 'comment', 'project_update', 'initiative_update', 'post', 'user', 'external_user')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    emoji = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='emoji')
    issue = sgqlc.types.Field(Issue, graphql_name='issue')
    comment = sgqlc.types.Field(Comment, graphql_name='comment')
    project_update = sgqlc.types.Field(ProjectUpdate, graphql_name='projectUpdate')
    initiative_update = sgqlc.types.Field(InitiativeUpdate, graphql_name='initiativeUpdate')
    post = sgqlc.types.Field(Post, graphql_name='post')
    user = sgqlc.types.Field('User', graphql_name='user')
    external_user = sgqlc.types.Field(ExternalUser, graphql_name='externalUser')


class Roadmap(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'name', 'description', 'organization', 'creator', 'owner', 'slug_id', 'sort_order', 'color', 'projects', 'url')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    organization = sgqlc.types.Field(sgqlc.types.non_null(Organization), graphql_name='organization')
    creator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='creator')
    owner = sgqlc.types.Field('User', graphql_name='owner')
    slug_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slugId')
    sort_order = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='sortOrder')
    color = sgqlc.types.Field(String, graphql_name='color')
    projects = sgqlc.types.Field(sgqlc.types.non_null(ProjectConnection), graphql_name='projects', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ProjectFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class RoadmapArchivePayload(sgqlc.types.Type, ArchivePayload):
    __schema__ = schema
    __field_names__ = ('entity',)
    entity = sgqlc.types.Field(Roadmap, graphql_name='entity')


class RoadmapToProject(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'project', 'roadmap', 'sort_order')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    project = sgqlc.types.Field(sgqlc.types.non_null(Project), graphql_name='project')
    roadmap = sgqlc.types.Field(sgqlc.types.non_null(Roadmap), graphql_name='roadmap')
    sort_order = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sortOrder')


class SemanticSearchResult(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('type', 'issue', 'project', 'initiative', 'document')
    type = sgqlc.types.Field(sgqlc.types.non_null(SemanticSearchResultType), graphql_name='type')
    issue = sgqlc.types.Field(Issue, graphql_name='issue')
    project = sgqlc.types.Field(Project, graphql_name='project')
    initiative = sgqlc.types.Field(Initiative, graphql_name='initiative')
    document = sgqlc.types.Field(Document, graphql_name='document')


class Team(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'name', 'key', 'description', 'icon', 'color', 'organization', 'parent', 'children', 'cycles_enabled', 'cycle_start_day', 'cycle_duration', 'cycle_cooldown_time', 'cycle_issue_auto_assign_started', 'cycle_issue_auto_assign_completed', 'cycle_lock_to_active', 'upcoming_cycle_count', 'timezone', 'invite_hash', 'inherit_workflow_statuses', 'inherit_issue_estimation', 'issue_estimation_type', 'issue_ordering_no_priority_first', 'issue_estimation_allow_zero', 'set_issue_sort_order_on_state_change', 'issue_estimation_extended', 'default_issue_estimate', 'triage_enabled', 'require_priority_to_leave_triage', 'default_issue_state', 'default_template_for_members', 'default_template_for_members_id', 'default_template_for_non_members', 'default_template_for_non_members_id', 'default_project_template', 'triage_issue_state', 'private', 'facets', 'posts', 'scim_managed', 'scim_group_name', 'progress_history', 'current_progress', 'draft_workflow_state', 'start_workflow_state', 'review_workflow_state', 'mergeable_workflow_state', 'merge_workflow_state', 'group_issue_history', 'ai_thread_summaries_enabled', 'slack_new_issue', 'slack_issue_comments', 'slack_issue_statuses', 'auto_close_period', 'auto_close_state_id', 'auto_archive_period', 'auto_close_parent_issues', 'auto_close_child_issues', 'marked_as_duplicate_workflow_state', 'join_by_default', 'cycle_calender_url', 'display_name', 'issues', 'issue_count', 'cycles', 'active_cycle', 'triage_responsibility', 'members', 'membership', 'memberships', 'projects', 'states', 'git_automation_states', 'templates', 'labels', 'webhooks', 'integrations_settings', 'issue_sort_order_default_to_bottom')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    description = sgqlc.types.Field(String, graphql_name='description')
    icon = sgqlc.types.Field(String, graphql_name='icon')
    color = sgqlc.types.Field(String, graphql_name='color')
    organization = sgqlc.types.Field(sgqlc.types.non_null(Organization), graphql_name='organization')
    parent = sgqlc.types.Field('Team', graphql_name='parent')
    children = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Team'))), graphql_name='children')
    cycles_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='cyclesEnabled')
    cycle_start_day = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='cycleStartDay')
    cycle_duration = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='cycleDuration')
    cycle_cooldown_time = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='cycleCooldownTime')
    cycle_issue_auto_assign_started = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='cycleIssueAutoAssignStarted')
    cycle_issue_auto_assign_completed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='cycleIssueAutoAssignCompleted')
    cycle_lock_to_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='cycleLockToActive')
    upcoming_cycle_count = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='upcomingCycleCount')
    timezone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='timezone')
    invite_hash = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='inviteHash')
    inherit_workflow_statuses = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='inheritWorkflowStatuses')
    inherit_issue_estimation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='inheritIssueEstimation')
    issue_estimation_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='issueEstimationType')
    issue_ordering_no_priority_first = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='issueOrderingNoPriorityFirst')
    issue_estimation_allow_zero = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='issueEstimationAllowZero')
    set_issue_sort_order_on_state_change = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='setIssueSortOrderOnStateChange')
    issue_estimation_extended = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='issueEstimationExtended')
    default_issue_estimate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='defaultIssueEstimate')
    triage_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='triageEnabled')
    require_priority_to_leave_triage = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requirePriorityToLeaveTriage')
    default_issue_state = sgqlc.types.Field('WorkflowState', graphql_name='defaultIssueState')
    default_template_for_members = sgqlc.types.Field('Template', graphql_name='defaultTemplateForMembers')
    default_template_for_members_id = sgqlc.types.Field(String, graphql_name='defaultTemplateForMembersId')
    default_template_for_non_members = sgqlc.types.Field('Template', graphql_name='defaultTemplateForNonMembers')
    default_template_for_non_members_id = sgqlc.types.Field(String, graphql_name='defaultTemplateForNonMembersId')
    default_project_template = sgqlc.types.Field('Template', graphql_name='defaultProjectTemplate')
    triage_issue_state = sgqlc.types.Field('WorkflowState', graphql_name='triageIssueState')
    private = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='private')
    facets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Facet))), graphql_name='facets')
    posts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Post))), graphql_name='posts')
    scim_managed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='scimManaged')
    scim_group_name = sgqlc.types.Field(String, graphql_name='scimGroupName')
    progress_history = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='progressHistory')
    current_progress = sgqlc.types.Field(sgqlc.types.non_null(JSONObject), graphql_name='currentProgress')
    draft_workflow_state = sgqlc.types.Field('WorkflowState', graphql_name='draftWorkflowState')
    start_workflow_state = sgqlc.types.Field('WorkflowState', graphql_name='startWorkflowState')
    review_workflow_state = sgqlc.types.Field('WorkflowState', graphql_name='reviewWorkflowState')
    mergeable_workflow_state = sgqlc.types.Field('WorkflowState', graphql_name='mergeableWorkflowState')
    merge_workflow_state = sgqlc.types.Field('WorkflowState', graphql_name='mergeWorkflowState')
    group_issue_history = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='groupIssueHistory')
    ai_thread_summaries_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='aiThreadSummariesEnabled')
    slack_new_issue = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='slackNewIssue')
    slack_issue_comments = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='slackIssueComments')
    slack_issue_statuses = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='slackIssueStatuses')
    auto_close_period = sgqlc.types.Field(Float, graphql_name='autoClosePeriod')
    auto_close_state_id = sgqlc.types.Field(String, graphql_name='autoCloseStateId')
    auto_archive_period = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='autoArchivePeriod')
    auto_close_parent_issues = sgqlc.types.Field(Boolean, graphql_name='autoCloseParentIssues')
    auto_close_child_issues = sgqlc.types.Field(Boolean, graphql_name='autoCloseChildIssues')
    marked_as_duplicate_workflow_state = sgqlc.types.Field('WorkflowState', graphql_name='markedAsDuplicateWorkflowState')
    join_by_default = sgqlc.types.Field(Boolean, graphql_name='joinByDefault')
    cycle_calender_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cycleCalenderUrl')
    display_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='displayName')
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('include_sub_teams', sgqlc.types.Arg(Boolean, graphql_name='includeSubTeams', default=False)),
        ('filter', sgqlc.types.Arg(IssueFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    issue_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='issueCount', args=sgqlc.types.ArgDict((
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=False)),
))
    )
    cycles = sgqlc.types.Field(sgqlc.types.non_null(CycleConnection), graphql_name='cycles', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CycleFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    active_cycle = sgqlc.types.Field(Cycle, graphql_name='activeCycle')
    triage_responsibility = sgqlc.types.Field('TriageResponsibility', graphql_name='triageResponsibility')
    members = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='members', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(UserFilter, graphql_name='filter', default=None)),
        ('include_disabled', sgqlc.types.Arg(Boolean, graphql_name='includeDisabled', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    membership = sgqlc.types.Field('TeamMembership', graphql_name='membership', args=sgqlc.types.ArgDict((
        ('user_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='userId', default=None)),
))
    )
    memberships = sgqlc.types.Field(sgqlc.types.non_null(TeamMembershipConnection), graphql_name='memberships', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    projects = sgqlc.types.Field(sgqlc.types.non_null(ProjectConnection), graphql_name='projects', args=sgqlc.types.ArgDict((
        ('include_sub_teams', sgqlc.types.Arg(Boolean, graphql_name='includeSubTeams', default=False)),
        ('filter', sgqlc.types.Arg(ProjectFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    states = sgqlc.types.Field(sgqlc.types.non_null(WorkflowStateConnection), graphql_name='states', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(WorkflowStateFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    git_automation_states = sgqlc.types.Field(sgqlc.types.non_null(GitAutomationStateConnection), graphql_name='gitAutomationStates', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    templates = sgqlc.types.Field(sgqlc.types.non_null(TemplateConnection), graphql_name='templates', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(NullableTemplateFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    labels = sgqlc.types.Field(sgqlc.types.non_null(IssueLabelConnection), graphql_name='labels', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(IssueLabelFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    webhooks = sgqlc.types.Field(sgqlc.types.non_null(WebhookConnection), graphql_name='webhooks', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    integrations_settings = sgqlc.types.Field(IntegrationsSettings, graphql_name='integrationsSettings')
    issue_sort_order_default_to_bottom = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='issueSortOrderDefaultToBottom')


class TeamArchivePayload(sgqlc.types.Type, ArchivePayload):
    __schema__ = schema
    __field_names__ = ('entity',)
    entity = sgqlc.types.Field(Team, graphql_name='entity')


class TeamMembership(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'user', 'team', 'owner', 'sort_order')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')
    team = sgqlc.types.Field(sgqlc.types.non_null(Team), graphql_name='team')
    owner = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='owner')
    sort_order = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='sortOrder')


class TeamNotificationSubscription(sgqlc.types.Type, NotificationSubscription, Entity, Node):
    __schema__ = schema
    __field_names__ = ('notification_subscription_types',)
    notification_subscription_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='notificationSubscriptionTypes')


class Template(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'type', 'name', 'description', 'template_data', 'sort_order', 'organization', 'team', 'creator', 'last_updated_by', 'inherited_from')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    template_data = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='templateData')
    sort_order = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='sortOrder')
    organization = sgqlc.types.Field(sgqlc.types.non_null(Organization), graphql_name='organization')
    team = sgqlc.types.Field(Team, graphql_name='team')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    last_updated_by = sgqlc.types.Field('User', graphql_name='lastUpdatedBy')
    inherited_from = sgqlc.types.Field('Template', graphql_name='inheritedFrom')


class TimeSchedule(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'name', 'entries', 'external_id', 'external_url', 'organization', 'integration')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    entries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TimeScheduleEntry)), graphql_name='entries')
    external_id = sgqlc.types.Field(String, graphql_name='externalId')
    external_url = sgqlc.types.Field(String, graphql_name='externalUrl')
    organization = sgqlc.types.Field(sgqlc.types.non_null(Organization), graphql_name='organization')
    integration = sgqlc.types.Field(Integration, graphql_name='integration')


class TriageResponsibility(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'action', 'manual_selection', 'team', 'time_schedule', 'current_user')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    action = sgqlc.types.Field(sgqlc.types.non_null(TriageResponsibilityAction), graphql_name='action')
    manual_selection = sgqlc.types.Field(TriageResponsibilityManualSelection, graphql_name='manualSelection')
    team = sgqlc.types.Field(sgqlc.types.non_null(Team), graphql_name='team')
    time_schedule = sgqlc.types.Field(TimeSchedule, graphql_name='timeSchedule')
    current_user = sgqlc.types.Field('User', graphql_name='currentUser')


class User(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'name', 'display_name', 'email', 'avatar_url', 'disable_reason', 'calendar_hash', 'description', 'status_emoji', 'status_label', 'status_until_at', 'timezone', 'organization', 'last_seen', 'initials', 'avatar_background_color', 'guest', 'app', 'active', 'issue_drafts', 'drafts', 'url', 'assigned_issues', 'created_issues', 'created_issue_count', 'teams', 'team_memberships', 'is_me', 'admin', 'invite_hash', 'git_hub_user_id')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    display_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='displayName')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    avatar_url = sgqlc.types.Field(String, graphql_name='avatarUrl')
    disable_reason = sgqlc.types.Field(String, graphql_name='disableReason')
    calendar_hash = sgqlc.types.Field(String, graphql_name='calendarHash')
    description = sgqlc.types.Field(String, graphql_name='description')
    status_emoji = sgqlc.types.Field(String, graphql_name='statusEmoji')
    status_label = sgqlc.types.Field(String, graphql_name='statusLabel')
    status_until_at = sgqlc.types.Field(DateTime, graphql_name='statusUntilAt')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    organization = sgqlc.types.Field(sgqlc.types.non_null(Organization), graphql_name='organization')
    last_seen = sgqlc.types.Field(DateTime, graphql_name='lastSeen')
    initials = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='initials')
    avatar_background_color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='avatarBackgroundColor')
    guest = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='guest')
    app = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='app')
    active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='active')
    issue_drafts = sgqlc.types.Field(sgqlc.types.non_null(IssueDraftConnection), graphql_name='issueDrafts', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    drafts = sgqlc.types.Field(sgqlc.types.non_null(DraftConnection), graphql_name='drafts', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    assigned_issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='assignedIssues', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(IssueFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    created_issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='createdIssues', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(IssueFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    created_issue_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createdIssueCount')
    teams = sgqlc.types.Field(sgqlc.types.non_null(TeamConnection), graphql_name='teams', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(TeamFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    team_memberships = sgqlc.types.Field(sgqlc.types.non_null(TeamMembershipConnection), graphql_name='teamMemberships', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )
    is_me = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMe')
    admin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='admin')
    invite_hash = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='inviteHash')
    git_hub_user_id = sgqlc.types.Field(String, graphql_name='gitHubUserId')


class UserNotificationSubscription(sgqlc.types.Type, NotificationSubscription, Entity, Node):
    __schema__ = schema
    __field_names__ = ('notification_subscription_types',)
    notification_subscription_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='notificationSubscriptionTypes')


class UserSettings(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'notification_delivery_preferences', 'unsubscribed_from', 'user', 'calendar_hash', 'subscribed_to_changelog', 'subscribed_to_dpa', 'subscribed_to_invite_accepted', 'subscribed_to_privacy_legal_updates', 'show_full_user_names', 'auto_assign_to_self', 'notification_category_preferences', 'notification_channel_preferences')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    notification_delivery_preferences = sgqlc.types.Field(sgqlc.types.non_null(NotificationDeliveryPreferences), graphql_name='notificationDeliveryPreferences')
    unsubscribed_from = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='unsubscribedFrom')
    user = sgqlc.types.Field(sgqlc.types.non_null(User), graphql_name='user')
    calendar_hash = sgqlc.types.Field(String, graphql_name='calendarHash')
    subscribed_to_changelog = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='subscribedToChangelog')
    subscribed_to_dpa = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='subscribedToDPA')
    subscribed_to_invite_accepted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='subscribedToInviteAccepted')
    subscribed_to_privacy_legal_updates = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='subscribedToPrivacyLegalUpdates')
    show_full_user_names = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='showFullUserNames')
    auto_assign_to_self = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='autoAssignToSelf')
    notification_category_preferences = sgqlc.types.Field(sgqlc.types.non_null(NotificationCategoryPreferences), graphql_name='notificationCategoryPreferences')
    notification_channel_preferences = sgqlc.types.Field(sgqlc.types.non_null(NotificationChannelPreferences), graphql_name='notificationChannelPreferences')


class ViewPreferences(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'type', 'view_type', 'preferences')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    view_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='viewType')
    preferences = sgqlc.types.Field(sgqlc.types.non_null(ViewPreferencesValues), graphql_name='preferences')


class Webhook(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'label', 'url', 'enabled', 'team', 'team_ids', 'all_public_teams', 'creator', 'secret', 'resource_types', 'failures')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    label = sgqlc.types.Field(String, graphql_name='label')
    url = sgqlc.types.Field(String, graphql_name='url')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    team = sgqlc.types.Field(Team, graphql_name='team')
    team_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='teamIds')
    all_public_teams = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='allPublicTeams')
    creator = sgqlc.types.Field(User, graphql_name='creator')
    secret = sgqlc.types.Field(String, graphql_name='secret')
    resource_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='resourceTypes')
    failures = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(WebhookFailureEvent))), graphql_name='failures')


class WorkflowState(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'updated_at', 'archived_at', 'name', 'color', 'description', 'position', 'type', 'team', 'inherited_from', 'issues')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='color')
    description = sgqlc.types.Field(String, graphql_name='description')
    position = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='position')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    team = sgqlc.types.Field(sgqlc.types.non_null(Team), graphql_name='team')
    inherited_from = sgqlc.types.Field('WorkflowState', graphql_name='inheritedFrom')
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(IssueFilter, graphql_name='filter', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=None)),
        ('order_by', sgqlc.types.Arg(PaginationOrderBy, graphql_name='orderBy', default=None)),
))
    )


class WorkflowStateArchivePayload(sgqlc.types.Type, ArchivePayload):
    __schema__ = schema
    __field_names__ = ('entity',)
    entity = sgqlc.types.Field(WorkflowState, graphql_name='entity')



########################################################################
# Unions
########################################################################
class ExternalEntityInfoMetadata(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (ExternalEntityInfoGithubMetadata, ExternalEntityInfoJiraMetadata, ExternalEntitySlackMetadata)


class OrganizationInviteDetailsPayload(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (OrganizationInviteFullDetailsPayload, OrganizationAcceptedOrExpiredInviteDetailsPayload)



########################################################################
# Schema Entry Points
########################################################################
schema.query_type = Query
schema.mutation_type = Mutation
schema.subscription_type = None

