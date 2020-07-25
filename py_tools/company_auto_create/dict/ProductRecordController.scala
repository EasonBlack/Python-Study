

@Singleton
class ProductRecordController @Inject()(cacheApi: SyncCacheApi, productRecordService: ProductRecordService,
                                     hqFeatureHelper: HqFeatureHelper, authAction: AuthAction)
                                    (implicit exec: ExecutionContext) extends BaseController {


  def view = Action { request =>
    Ok(views.html.productRecord(request.authToken, request.queryString + ("tag" -> ""),
      hqFeatureHelper.get(request.authToken.body.hqId)))
  }

  def searchProductRecord = Action.async { request =>
    val hqId = request.authToken.body.hqId;
    productRecordService.searchProductRecord(hqId).map(result => dataResult(Json.toJson(result)))
  }

  def saveProductRecord = Action.async(parse.json) { request =>
    request.body.validate[ProductRecord].fold(
      errors => Future.successful(jsonInvalidResult(request, errors)),
      m => {
        productRecordService.saveProductRecord(m).map(id => dataResult(JsNumber(id)))
      }
    )
  }

  def updateProductRecord = Action.async(parse.json) { request =>
    request.body.validate[ProductRecord].fold(
      errors => Future.successful(jsonInvalidResult(request, errors)),
      m => {
        productRecordService.updateProductRecord(m).map(_ => emptyResult)
      }
    )
  }

  override def Action = authAction()
}