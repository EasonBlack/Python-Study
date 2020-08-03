

@Singleton
class BranchKdsController @Inject()(cacheApi: SyncCacheApi, branchKdsService: BranchKdsService,
                                     hqFeatureHelper: HqFeatureHelper, authAction: AuthAction)
                                    (implicit exec: ExecutionContext) extends BaseController {


  def view = Action { request =>
    Ok(views.html.branchKds(request.authToken, request.queryString + ("tag" -> ""),
      hqFeatureHelper.get(request.authToken.body.hqId)))
  }

  def searchBranchKds = Action.async { request =>
    val hqId = request.authToken.body.hqId;
    branchKdsService.searchBranchKds(hqId).map(result => dataResult(Json.toJson(result)))
  }

  def findBranchKdsById(id: Long) = Action.async {request =>
    val hqId = request.authToken.body.hqId
    branchKdsService.findBranchKdsById(hqId, id).map { result =>
      dataResult(Json.toJson(result))
    }
  }

  def saveBranchKds = Action.async(parse.json) { request =>
    request.body.validate[BranchKds].fold(
      errors => Future.successful(jsonInvalidResult(request, errors)),
      m => {
        branchKdsService.saveBranchKds(m).map(id => dataResult(JsNumber(id)))
      }
    )
  }

  def updateBranchKds = Action.async(parse.json) { request =>
    request.body.validate[BranchKds].fold(
      errors => Future.successful(jsonInvalidResult(request, errors)),
      m => {
        branchKdsService.updateBranchKds(m).map(_ => emptyResult)
      }
    )
  }

  override def Action = authAction()
}